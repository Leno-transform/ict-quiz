"""Append the two new sources, preserving legacy IDs and reviewed provenance."""
import copy
import json
import re
import zipfile
from collections import Counter
from pathlib import Path
from urllib.parse import quote

from import_questions import normalize

ROOT=Path(__file__).resolve().parents[1]
NAMES={'legacy':'原题库','word1508':'数通 / DCN / 安全','wlan943':'WLAN 扫描题库'}
TYPE_NAMES={'single':'单选','multiple':'多选','judge':'判断','fill':'填空'}

def read(path):return json.loads(path.read_text(encoding='utf-8-sig'))
def write(path,value):path.write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')

def topic(q):
    text=q['stem']
    if re.search('无线考点|WLAN|CAPWAP|SSID|802\\.11|射频|天线|无线|Wi-Fi',text,re.I):return 'WLAN 与无线'
    if re.search('DCN|CloudFabric|VXLAN|EVPN|OpenStack|数据中心|Spine|Leaf|Fabric|容器|Ansible',text,re.I):return '数据中心与自动化'
    if re.search('安全考点|防火墙|IPSec|SSL|加密|病毒|攻击|安全|证据',text,re.I):return '网络安全'
    if re.search('OSPF|BGP|IS-IS|MPLS|路由|Router',text,re.I):return '路由与广域网'
    if re.search('VLAN|STP|交换|以太网|LACP|MAC',text,re.I):return '交换与以太网'
    if re.search('IPv6|IPv4|子网|IP地址|ARP|ICMP',text,re.I):return 'IP 与地址规划'
    if re.search('TCP|UDP|HTTP|FTP|DHCP|DNS|SNMP|Telnet|NETCONF|Python',text,re.I):return '网络协议与运维'
    return '网络基础与综合'

def identity(q):
    return normalize(q['stem'])+'|'+('|'.join(sorted(normalize(v) for v in q['options'].values())) if q['type']!='fill' else '<fill>')

def reference(q):
    item={'bank_id':q['bank_id'],'bank_name':NAMES[q['bank_id']],'number':q['source_number'],'document':q['document']}
    if q.get('page'):item['page']=q['page']
    return item

def main():
    payload=read(ROOT/'data/questions.json')
    additions=read(ROOT/'data/additional_source_questions.json')
    decisions={}
    for bank,files in [('word1508',['new_word_a.json','new_word_b.json']),('wlan943',['new_pdf_a.json','new_pdf_b.json','new_pdf_c.json','new_pdf_manual.json'])]:
        for filename in files:
            path=ROOT/'review'/filename
            if not path.exists():
                if filename=='new_pdf_manual.json':continue
                raise ValueError(f'缺少新增题审核记录：{filename}')
            for row in read(path):decisions[(bank,row['source_number'])]=row
    cleaning=read(ROOT/'exports/题库清理明细.json')
    removed=[{**r,'bank_id':'legacy','source_number':r['id'],'source_name':NAMES['legacy']} for r in cleaning['removed']]
    corrections=[{**r,'bank_id':'legacy','source_number':r['id'],'source_name':NAMES['legacy']} for r in cleaning['corrections']]
    old_ids={q['id'] for q in payload['questions']}
    for q in payload['questions']:
        q['bank_ids']=['legacy'];q['source_refs']=[{'bank_id':'legacy','bank_name':NAMES['legacy'],'number':q['id'],'document':'ICT网络赛道知识题库(1).docx'}]
        q['explanation_origin']='原题库已审核解析'
    kept=payload['questions'];seen={identity(q):q for q in kept}
    explanations_added=0;provided_explanations=0
    for raw in additions['questions']:
        q=copy.deepcopy(raw);bank=q['bank_id'];number=q['source_number'];review=decisions.get((bank,number),{})
        q['id']=(10000 if bank=='word1508' else 20000)+number
        q['original_answer']=copy.deepcopy(q['answer'])
        original_explanation=q.get('explanation','').strip()
        changes={}
        for field in ('stem','options','answer'):
            if f'corrected_{field}' in review:
                replacement=review[f'corrected_{field}']
                if q[field]!=replacement:changes[field]={'before':q[field],'after':replacement}
                q[field]=replacement
        q['type']=review.get('corrected_type',q['type'])
        q['stem']=re.sub(r'【[^】]*(?:考点|背答案)[^】]*】','',q['stem']).strip()
        q['topic']=review.get('topic') or topic(raw)
        q['image']=review.get('image',q.get('image'))
        q['explanation']=review.get('explanation') or original_explanation
        q['explanation_origin']='补写解析' if not original_explanation else '校正解析' if review.get('explanation') else '原文自带解析'
        q['sources']=list(dict.fromkeys(review.get('sources') or ['https://github.com/Leno-transform/ict-quiz/blob/main/'+quote(q['document'])]))
        if q['type']=='fill':
            if isinstance(q['answer'],str):q['answer']=[q['answer'].strip()]
        else:
            if isinstance(q['answer'],list):q['answer']=''.join(q['answer'])
            q['answer']=q['answer'].replace(' ','').upper()
            normalized={k:normalize(v) for k,v in q['options'].items()}
            if set(normalized.values()) in ({'true','false'},{'正确','错误'}):
                q['type']='judge';q['options']={k:'正确' if v in ('true','正确') else '错误' for k,v in normalized.items()}
            elif q['type']!='judge':q['type']='multiple' if len(q['answer'])>1 else 'single'
        reasons=[]
        if review.get('action')=='exclude':reasons.append(review.get('reason') or '审核认为条件不足或答案不可靠')
        if q.get('extraction_error'):reasons.append(q['extraction_error'])
        if not q['stem'] or q['type']!='fill' and (len(q['options'])<2 or any(not v.strip() for v in q['options'].values())):reasons.append('题干或选项残缺')
        if q['type']!='fill' and (not re.fullmatch('[A-H]+',q['answer']) or not set(q['answer'])<=set(q['options'])):reasons.append('答案缺失或不能对应选项')
        if q['type']=='fill' and (not q['answer'] or any(not v for v in q['answer'])):reasons.append('填空答案缺失')
        if re.search('如图|图所示|下图|图示|如表',q['stem']) and not q['image']:reasons.append('原文缺少必需图示，无法可靠恢复')
        ref=reference(q)
        if reasons:
            removed.append({'id':q['id'],'bank_id':bank,'source_name':NAMES[bank],'source_number':number,'page':q.get('page'),'category':'invalid','reason':'；'.join(dict.fromkeys(reasons)),'stem':q['stem']})
            continue
        if not q['explanation'] or q['explanation'].strip().lower() in ('nan','none','null'):
            raise ValueError(f'{bank} #{number} 缺少真正的解析，拒绝发布。')
        if not original_explanation:explanations_added+=1
        else:provided_explanations+=1
        q['bank_ids']=[bank];q['source_refs']=[ref]
        key=identity(q)
        if key in seen:
            winner=seen[key]
            if bank not in winner['bank_ids']:winner['bank_ids'].append(bank)
            winner['source_refs'].append(ref)
            incoming_values=sorted(normalize(q['options'][a]) for a in q['answer']) if q['type']!='fill' else q['answer']
            kept_values=sorted(normalize(winner['options'][a]) for a in winner['answer']) if winner['type']!='fill' else winner['answer']
            record={'id':q['id'],'bank_id':bank,'source_name':NAMES[bank],'source_number':number,'page':q.get('page'),'category':'duplicate','reason':f'题干与选项归一化后相同，合并至保留题 {winner["id"]}','duplicate_of':winner['id'],'stem':q['stem']}
            if incoming_values!=kept_values:
                record['answer_conflict']={'retained_answer':winner['answer'],'incoming_answer':q['answer'],'retained_answer_text':kept_values,'incoming_answer_text':incoming_values}
                record['reason']+='；来源答案存在冲突，已单独记录以供核对'
            removed.append(record)
            continue
        q={k:q[k] for k in ('id','stem','options','answer','original_answer','type','topic','image','explanation','explanation_origin','sources','bank_ids','source_refs')}
        if changes or review.get('action')=='correct':
            corrections.append({'id':q['id'],'bank_id':bank,'source_name':NAMES[bank],'source_number':number,'changes':changes,'reason':review.get('reason',''),'explanation':q['explanation'],'sources':q['sources'],'verification_note':review.get('verification_note','')})
        seen[key]=q;kept.append(q)
    assert old_ids<={q['id'] for q in kept},'不能移除原有可用题目'
    summary={**payload['summary'],'source_count':payload['summary']['source_count']+len(additions['questions']),'kept_count':len(kept),
             'duplicate_count':sum(r['category']=='duplicate' for r in removed),'invalid_count':sum(r['category']=='invalid' for r in removed),
             'answer_correction_count':sum('answer' in r['changes'] for r in corrections),'text_correction_count':sum('stem' in r['changes'] or 'options' in r['changes'] for r in corrections),
             'image_count':sum(bool(q['image']) for q in kept),'types':dict(Counter(q['type'] for q in kept)),
             'new_source_count':len(additions['questions']),'explanations_added':explanations_added,'provided_explanations':provided_explanations}
    assert summary['source_count']==summary['kept_count']+summary['duplicate_count']+summary['invalid_count']
    banks=[{'id':bank,'name':name,'question_count':sum(bank in q['bank_ids'] for q in kept),'source_count':payload['summary']['source_count'] if bank=='legacy' else next(x['count'] for x in additions['sources'] if x['bank_id']==bank)} for bank,name in NAMES.items()]
    payload={**payload,'summary':summary,'banks':banks,'questions':kept}
    write(ROOT/'data/questions.json',payload);write(ROOT/'exports/题库及解析.json',payload)
    write(ROOT/'exports/题库清理明细.json',{'summary':summary,'sources':additions['sources'],'banks':banks,'removed':removed,'corrections':corrections})
    markdown=['# ICT 网络赛道题库与解析','',f'共核对 {summary["source_count"]} 道来源题目，合并清理后保留 {len(kept)} 道。原题库题号保持不变，新增题注明来源及原题号。','',
              '相同题目只保留一份，来源信息均保留；厂家相关题以题目适用版本为准。原文自带解析与新增补写解析分别标记。','']
    images=ROOT/'exports/图片';images.mkdir(exist_ok=True)
    for q in kept:
        refs='；'.join(f'{r["bank_name"]} #{r["number"]}'+(f'（PDF 第 {r["page"]} 页）' if r.get('page') else '') for r in q['source_refs'])
        markdown += [f'## {refs} · {TYPE_NAMES[q["type"]]} · {q["topic"]}','',q['stem'],'']
        if q['image']:
            source=ROOT/'web'/q['image']['src'].lstrip('/');(images/source.name).write_bytes(source.read_bytes())
            markdown += [f'![{q["image"]["alt"]}](图片/{source.name})','',q['image']['caption'],'']
        markdown += [f'- **{key}.** {value}' for key,value in q['options'].items()]
        markdown += ['',f'**答案：** {"、".join(q["answer"])}','',f'**解析：** {q["explanation"]}','',f'解析来源：{q["explanation_origin"]}','',
                     '参考：'+'；'.join(f'[资料 {i+1}]({url})' for i,url in enumerate(q['sources'])),'']
    (ROOT/'exports/题库及解析.md').write_text('\n'.join(markdown),encoding='utf-8')
    report=['# ICT 题库合并、清理与解析补全报告','',f'来源共 {summary["source_count"]} 道；保留 {len(kept)} 道；合并重复 {summary["duplicate_count"]} 道；剔除残缺或存疑 {summary["invalid_count"]} 道。','',
            f'本次新增来源 {summary["new_source_count"]} 道。对可导入的新题补写解析 {explanations_added} 道（含之后合并为重复题的条目）；已有解析按原文保留或在审核记录中校正。','',
            '扫描PDF已离线识别；配图从原扫描裁切，不根据题意虚构。原文含重复截图或额外未编号讲义的，按原编号题目拆分。文字归一化去重保留不同条件的题；原544道题的ID保持不变，个人数据库不重建。','',
            '新增Word中原文自带的解析并不等于独立核验；已纠正明确矛盾并补齐nan占位，型号/版本相关的资料限制在审核备注中记录。','',
            '## 来源统计','','| 题库 | 来源题目 | 去重后含该来源的题目 |','| --- | ---: | ---: |']
    report += [f'| {b["name"]} | {b["source_count"]} | {b["question_count"]} |' for b in banks]
    report += ['','同一保留题可以关联多个来源，因此右列不能简单相加。','','## 剔除与合并明细','','| 来源 | 原题号 | 分类 | 原因 |','| --- | ---: | --- | --- |']
    report += [f'| {r["source_name"]} | {r["source_number"]} | {"重复" if r["category"]=="duplicate" else "残缺或存疑"} | {r["reason"].replace("|","／")} |' for r in removed]
    report += ['','## 修复与补写记录','']
    for item in corrections:
        report += [f'### {item["source_name"]} #{item["source_number"]}','',item.get('reason','') or '原题库审核修正','',item['explanation'],'']
        if item.get('changes'):report += ['变更：'+json.dumps(item['changes'],ensure_ascii=False),'']
        if item.get('verification_note'):report += ['核验范围：'+item['verification_note'],'']
    (ROOT/'exports/题库清理报告.md').write_text('\n'.join(report),encoding='utf-8')
    with zipfile.ZipFile(ROOT/'exports/题库资料.zip','w',zipfile.ZIP_DEFLATED) as archive:
        for path in sorted((ROOT/'exports').rglob('*')):
            if path.is_file() and path.suffix!='.zip':archive.write(path,path.relative_to(ROOT/'exports'))
    print(json.dumps(summary,ensure_ascii=False))

if __name__=='__main__':
    raise SystemExit('请运行 scripts/build_bank.py；它会先重建原题库，再调用此合并步骤。')

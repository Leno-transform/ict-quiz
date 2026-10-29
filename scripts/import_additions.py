"""Import the new DOCX and the reviewed OCR transcription of the supplied PDF."""
import hashlib
import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
WORD='网络赛道1500题-数通DCN安全.docx'
PDF='网络赛道943题-wlan部分.pdf'
NS={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

def word_questions():
    with zipfile.ZipFile(ROOT/WORD) as archive:
        xml=ET.fromstring(archive.read('word/document.xml'))
    lines=[''.join(t.text or '' for t in p.findall('.//w:t',NS)).strip() for p in xml.findall('.//w:body//w:p',NS)]
    output=[];current=None;kind=''
    for text in lines:
        if text in ('单选题','多选题','判断题','填空题'):
            kind={'单选题':'single','多选题':'multiple','判断题':'judge','填空题':'fill'}[text];continue
        match=re.match(r'^(\d+)\.\s*(.*)',text)
        if match:
            if current:output.append(current)
            current={'source_number':int(match[1]),'type':kind,'stem':match[2],'raw_options':[],'answer':'','explanation':''}
        elif current and text.startswith('正确答案:'):current['answer']=text.split(':',1)[1].strip()
        elif current and text.startswith('解析:'):current['explanation']=text.split(':',1)[1].strip()
        elif current and text:current['raw_options'].append(text)
    if current:output.append(current)
    for q in output:
        raw='\n'.join(q.pop('raw_options'));marks=[]
        for match in re.finditer(r'([A-H])[.．、]',raw):
            # Only consume consecutive option labels; OSPF、 is not option F.
            if ord(match[1])==ord('A')+len(marks):marks.append(match)
        q['options']={m[1]:raw[m.end():marks[i+1].start() if i+1<len(marks) else len(raw)].strip() for i,m in enumerate(marks)}
        q['bank_id']='word1508';q['document']=WORD
        if q['explanation'].lower() in ('nan','none','null','无','暂无'):q['explanation']=''
    return output

def main():
    frozen=ROOT/'data'/'wlan_source.json'
    if not frozen.exists():raise ValueError('缺少扫描PDF的已核对文字转录 data/wlan_source.json。')
    pdf=json.loads(frozen.read_text(encoding='utf-8'))
    if (ROOT/PDF).exists() and hashlib.sha256((ROOT/PDF).read_bytes()).hexdigest()!=pdf['document_sha256']:
        raise ValueError('扫描PDF与已核对转录的文件指纹不符。')
    word=word_questions()
    if len({q['source_number'] for q in word})!=len(word) or len({q['source_number'] for q in pdf['questions']})!=len(pdf['questions']):
        raise ValueError('同一来源出现重复题号，拒绝导入。')
    sources=[{'bank_id':'word1508','document':WORD,'count':len(word),'sha256':hashlib.sha256((ROOT/WORD).read_bytes()).hexdigest()},
             {'bank_id':'wlan943','document':PDF,'count':len(pdf['questions']),'sha256':pdf['document_sha256']}]
    questions=word+[{**q,'bank_id':'wlan943','document':PDF} for q in pdf['questions']]
    (ROOT/'data'/'additional_source_questions.json').write_text(json.dumps({'sources':sources,'questions':questions},ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'new_sources':sources,'missing_explanations':sum(not q.get('explanation') for q in questions)},ensure_ascii=False))

if __name__=='__main__':main()

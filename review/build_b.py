import json,re
from pathlib import Path
root=Path(__file__).parent
questions=json.loads((root/'questions_b.json').read_text(encoding='utf-8-sig'))
S={
'ospf':'https://www.rfc-editor.org/rfc/rfc2328',
'ospfh':'https://info.support.huawei.com/enterprise/zh/doc/EDOC1100334536/c1083833',
'ospfc':'https://support.huawei.com/enterprise/zh/doc/EDOC1100352131/753f0155',
'ospf3':'https://www.rfc-editor.org/rfc/rfc5340',
'ip':'https://www.rfc-editor.org/rfc/rfc791',
'ipv6':'https://www.rfc-editor.org/rfc/rfc8200',
'addr6':'https://www.rfc-editor.org/rfc/rfc4291',
'nd':'https://www.rfc-editor.org/rfc/rfc4861',
'dhcp':'https://www.rfc-editor.org/rfc/rfc2131',
'vrrp':'https://www.rfc-editor.org/rfc/rfc5798',
'mpls':'https://www.rfc-editor.org/rfc/rfc3031',
'label':'https://www.rfc-editor.org/rfc/rfc3032',
'ldp':'https://www.rfc-editor.org/rfc/rfc5036',
'vpn':'https://www.rfc-editor.org/rfc/rfc4364',
'sr':'https://www.rfc-editor.org/rfc/rfc8402',
'arp':'https://www.rfc-editor.org/rfc/rfc826',
'eth':'https://www.iana.org/assignments/ieee-802-numbers/ieee-802-numbers.xhtml',
'tcp':'https://www.rfc-editor.org/rfc/rfc9293',
'udp':'https://www.rfc-editor.org/rfc/rfc768',
'ppp':'https://www.rfc-editor.org/rfc/rfc1661',
'pppoe':'https://www.rfc-editor.org/rfc/rfc2516',
'telnet':'https://www.rfc-editor.org/rfc/rfc854',
'telpy':'https://docs.python.org/3.12/library/telnetlib.html',
'py':'https://docs.python.org/3/tutorial/introduction.html',
'snmp':'https://www.rfc-editor.org/rfc/rfc3411',
'snmpops':'https://www.rfc-editor.org/rfc/rfc3416',
'snmpsec':'https://www.rfc-editor.org/rfc/rfc3414',
'acl':'https://info.support.huawei.com/info-finder/encyclopedia/zh/detail?action=queryEntityDetail&keyword=ACL',
'aclm':'https://support.huawei.com/enterprise/zh/doc/EDOC1100276741/73a9b1a0/acl-fundamentals',
'aclorder':'https://info.support.huawei.com/hedex/api/pages/EDOC1100362944/AZN04029/05/resources/vrp/dc_vrp_acl4_cfg_0041.html',
'lacp':'https://support.huawei.com/enterprise/zh/doc/EDOC1100459514/b1d8b5a3',
'trunk':'https://info.support.huawei.com/info-finder/encyclopedia/zh/Eth-trunk.html',
'trunklim':'https://info.support.huawei.com/enterprise/zh/doc/EDOC1100459514/4c4a3551',
'stp':'https://support.huawei.com/enterprise/en/doc/EDOC1100466171/c9a6630d/stp-rstp-mstp-configuration',
'wlan':'https://info.support.huawei.com/info-finder/encyclopedia/zh/detail?action=queryEntityDetail&keyword=WiFi',
'apon':'https://info.support.huawei.com/hedex/api/pages/EDOC1100210440/AZK0901G/09/resources/dc/dc_fd_wlan_basic_0007.html',
'apadd':'https://info.support.huawei.com/hedex/api/pages/EDOC1100331917/AZM1014P/05/resources/dc/dc_cfg_wlan_basic_0018.html',
'apup':'https://info.support.huawei.com/hedex/api/pages/EDOC1100331917/AZM1014P/05/resources/dc/dc_cfg_wlan_basic_0049.html',
'apmode':'https://support.huawei.com/enterprise/en/doc/EDOC1100081212/1f32f097/ap-mode-switching---overview-examples-and-troubleshooting',
'login':'https://info.support.huawei.com/hedex/api/pages/EDOC1000053358/YEF0907R/25/resources/en-us_task_0133027518.html',
'keys':'https://support.huawei.com/enterprise/en/doc/EDOC1100410538/36ae01a3/using-command-line-shortcut-keys',
'static':'https://support.huawei.com/enterprise/zh/doc/EDOC1100333406/ac7caed7/ip-route-static',
'pre':'https://info.support.huawei.com/hedex/api/pages/EDOC1100277650/AZM1016J/03/resources/vrp/feature_0003992083.html',
'qos':'https://info.support.huawei.com/hedex/api/pages/EDOC1100331207/FZM1012J/06/resources/zh-cn_topic_0000001312646813.html',
'wred':'https://info.support.huawei.com/enterprise/zh/doc/EDOC1100466177/ad9bd63c',
'nfv':'https://nfvwiki.etsi.org/index.php?title=NFV_FAQ',
'as':'https://info.support.huawei.com/hedex/api/pages/EDOC1100149311/AZJ0713J/18/resources/admin/sec_admin_aspf_0037.html',
'natserver':'https://info.support.huawei.com/hedex/api/pages/EDOC1100149308/AEJ0713J/18/resources/admin/sec_admin_nat_0091-c80.html',
'es':'https://enterprise.huawei.com/ucmf/groups/entpublic/documents/enterprise_webasset/hw_193007.pdf'
}
rows={}
def load(block):
 for line in block.strip().splitlines():
  fields=line.split('|'); id=int(fields[0]); topic,src,explanation=fields[1:4]
  rows[id]=dict(id=id,explanation=explanation,topic=topic,status='keep',reason='',corrected_answer=fields[4] if len(fields)>4 and fields[4] else None,corrected_stem=None,corrected_options=None,sources=[S[x] for x in src.split(',')])
load('''
265|OSPF|ospf3|OSPFv3 为 IPv6 定义了邻居发现与链路状态路由机制，OSPFv2 主要用于 IPv4。
268|DHCP|dhcp|客户端尚未获得地址时，DHCPDISCOVER 的源 IP 为 0.0.0.0，目的 IP 通常为 255.255.255.255。
270|以太网交换|eth|普通二层交换机依据 MAC 地址学习和转发以太网帧，因此工作在数据链路层。
272|VRRP|vrrp|手工配置的普通 VRRP 优先级为 1–254；255 留给虚拟 IP 的地址拥有者，0 用于通知退出 Master。
273|QoS|wred|WRED 在队列尚未填满时按概率提前丢包，从而缓解拥塞并避免 TCP 流同时减速。
274|MPLS|mpls|MPLS 标签具有本地意义，入标签与出标签由相邻节点分别分配，数值可能恰好相同。
275|MPLS|mpls|出标签由下游节点分配；不同下一跳使用独立标签空间，数值可能相同。|C
281|VLAN|eth|基于 MAC 地址划分 VLAN 随终端身份分组，终端移动到其他端口后仍可归入原 VLAN。
282|OSPF|ospfc|这里问的是路由协议 preference，华为 OSPF 内部路由默认值为 10；接口 DR 选举优先级默认值另为 1。
284|路由基础|pre|路由条目用目的网段与掩码定位目标，并记录协议、开销、下一跳和出接口等转发依据。
285|路由基础|static|/22 精确覆盖这四个 /24，/21 覆盖更大范围，默认路由 /0 同样能匹配；/23 无法覆盖四段。|BCD
286|链路聚合|lacp|LACP 主动端先比较系统优先级，数值小者优先；相等时比较设备 MAC 地址，较小者优先。
287|VLAN|eth|VLAN 1 是默认 VLAN，不能删除；普通可配置 VLAN 的编号范围为 1–4094。
290|WLAN|apon|CAPWAP 用 Echo 检测控制隧道，用 Keepalive 检测数据隧道；DPD 与 Hello 不属于这两类探测。
291|IPv6|ipv6|IPv6 定义分片、目的选项和逐跳选项等扩展首部；VLAN 标记属于二层帧结构。
292|SDN|snmp|南向接口负责控制器与设备交互，SNMP 用于管理，NETCONF 用于配置，OpenFlow/PCEP 用于转发或路径控制。
293|ACL|acl|华为基本 ACL 编号为 2000–2999，高级 ACL 为 3000–3999，二层 ACL 为 4000–4999。
294|设备管理|keys|Ctrl+Z 可从配置视图直接返回用户视图，因此从系统视图返回用户视图也是其适用情形。
295|OSPF|ospf|OSPF Area ID 是 32 位值，骨干区域固定为 0.0.0.0；并不要求所有网络都在骨干区域中。
296|以太网交换|eth|HUB 共享冲突域和广播域；二层交换机隔离端口冲突域，但同一 VLAN 的端口仍共享广播域。
297|生成树|stp|根桥按最小 Bridge ID 选举，Bridge ID 包括桥优先级与 MAC 地址，与 IP 地址和接口带宽无关。
298|生成树|stp|经典 STP 有 Disabled、Blocking、Listening、Learning、Forwarding 五种状态；Discarding 属于 RSTP 状态名。
302|生成树|stp|STP 选举比较桥 ID、根路径开销和端口 ID；Forward Delay 是状态过渡计时器，并非选举参数。
303|OSPF|ospfh|OSPF 的四类常见网络类型为广播、NBMA、点到点和点到多点；广播与 NBMA 才选举 DR/BDR。
304|IPv6|nd,dhcp|IPv6 可手工配置，也可通过 SLAAC 无状态自动配置或 DHCPv6 获取地址，自动配置不止一种方式。
305|WLAN|apmode|Fat AP 可独立提供 WLAN，Fit AP 由 AC 管理，Cloud AP 由云平台管理；具体模式还取决于设备型号。
306|OSPF|ospfc|Router ID 可手工指定；自动选择时优先采用最大的 Loopback 地址，否则选其他接口中最大的地址。
308|链路聚合|trunk|链路聚合把多条物理链路组成逻辑链路，可增加总带宽、分担流量并提供链路备份，不直接提供安全控制。|ACD
309|VLAN|ip|VLANIF 是三层逻辑接口，配置 IP 地址和子网掩码后才能确定其所属网段并进行三层通信。
310|以太网交换|eth|0x8100 表示帧带有 802.1Q VLAN 标记，后续协议仍可承载 ARP 或包含 TCP、UDP、ICMP 的 IP 报文。
311|NAT|static|默认路由把未知目的流量送往互联网出口，NAT 把私网地址转换为可在公网通信的地址。
312|DHCP|dhcp|DHCP 集中下发地址与 DNS 等参数，并利用租约回收和复用地址，减少手工配置及地址冲突。|ACD
313|IPv6|nd|RS 是主机请求路由器通告，RA 是路由器发布前缀等信息的通告；题目问错误描述，所以选择 B、D。|BD
314|静态路由|static|255.255.255.255 是 /32 主机路由，目的地址为 10.0.2.2，下一跳为 10.0.12.2，preference 为 20。
316|AAA|login|VTY 使用 AAA 后可按用户名验证；在 AAA 中建立各管理员账号，并分别设置密码和权限级别。
317|网络基础|eth|家庭和公司办公网络通常覆盖有限区域，属于 LAN；互联网和广域网络跨越更大的地域范围。
318|生成树|stp|Forwarding 端口既学习源 MAC 又转发业务；是否发送配置 BPDU 还取决于端口角色，不能仅由转发状态断定。
339|链路聚合|trunk|聚合链路的总可用带宽与活动成员数量及成员带宽有关；单条流通常只落在一个成员端口上。
340|路由基础|static|默认路由为 0.0.0.0/0，作为没有更长前缀匹配时的兜底；既可静态配置也可由动态协议学习。
341|生成树|stp|RSTP 将经典 STP 状态归并为 Discarding、Learning 和 Forwarding，Listening 不再独立存在。
343|生成树|stp|经典 STP 从 Listening 到 Learning、再到 Forwarding，通常各等待一个 Forward Delay，以降低临时环路风险。
345|SNMP|snmpsec,snmpops|SNMPv3 的 USM 可提供认证和加密；SNMPv2c 仍用团体字，增加了 GetBulk 和 Inform 等操作。
348|网络基础|eth|视频、网页、邮件和即时聊天都要通过网络在不同设备间传送数据，都是通信网络的应用。
349|路由基础|pre|华为路由 preference 数值越小越优先，同协议通常优选较小 cost；直连路由默认 preference 为 0。
350|堆叠集群|trunk|堆叠把多台交换机作为逻辑设备管理，可扩展端口并支持跨设备聚合，但不会消除所有通信故障。
351|SNMP|snmp|管理站通过 Agent 访问被管设备的信息，MIB 定义管理对象及其结构，四者共同构成管理体系。
352|OSPF|ospfc|silent-interface 使该接口停止收发 OSPF 协议报文，邻居关系无法继续维持并最终失效。
353|静态路由|static|华为静态路由 preference 的可配置范围为 1–255、默认 60；0 不属于可配置的普通静态路由优先级。
355|WLAN|apadd|AC 可按 AP 的 MAC 地址、序列号 SN 验证其身份，也可配置不认证；普通 AP 接入认证没有 Password 选项。
356|WLAN|wlan|802.11b 和 802.11g 只使用 2.4 GHz；802.11a 使用 5 GHz，802.11n 可使用 2.4 GHz 和 5 GHz。
359|OSPF|ospf|相邻接口的 Area ID 与 Dead Interval 必须一致；Router ID 应不同，DR 优先级可以不同。
362|VLAN|ip|VLANIF 上的 IPv4 地址和掩码共同描述接口网段；无需手工配置 MAC 地址来启用三层地址。
363|WLAN|apon|Keepalive 用于 CAPWAP 数据隧道保活，Echo Request/Response 用于控制隧道的连通性检测。
365|设备管理|keys|上方向键和 Ctrl+P 都读取上一条历史命令；左方向键移动光标，Ctrl+U 清除当前行。
366|网络基础|ip|封装为数据添加各层控制信息，解封装逐层处理这些信息，使不同层协议协同完成端到端通信。
367|OSPF|ospf|骨干区域是 Area 0，区域号为 32 位值；Loopback 配置不是创建 OSPF 区域的必备前提。
369|WLAN|wlan|802.11n 与 802.11ax 都支持 2.4 GHz 和 5 GHz；802.11g 仅 2.4 GHz，802.11ac 使用 5 GHz。
370|SDN|snmp|控制器可用 SNMP 采集管理信息、NETCONF 下发配置，或通过 OpenFlow/PCEP 控制转发及路径。
371|网络基础|snmp|数据平面负责转发报文，控制平面计算路由等状态，管理平面负责配置、监控和维护。
376|IPv6|nd|主机发送 RS 请求路由器信息，路由器发送 RA 通告地址前缀、默认路由和相关参数。
378|Segment Routing|sr|SR 用源路由描述分段路径，支持集中和分布控制，并可扩展 IGP；SR-MPLS 仍需要标签转发表。
382|OSPF|ospfh|广播和 NBMA 网络选举 DR/BDR 来减少邻接关系；点到点和点到多点网络无需这项选举。
383|WLAN|wlan|802.11n 即 Wi-Fi 4，支持 2.4 GHz 与 5 GHz，不使用 2.5 GHz 或 6 GHz。
384|OSPF|ospfh|广播、NBMA、点到点和点到多点是 OSPF 的标准网络类型，不同类型的邻接建立方式有所区别。
386|DHCP|dhcp|首次分配通常经过 Discover、Offer、Request、ACK；协议没有 DHCP ROLLOVER 报文。
388|OSPF|ospfh|同一区域的链路状态信息最终同步一致；各路由器以自己为 SPF 根节点，计算出的下一跳和路由表通常不同。
389|动态路由|ospfh|OSPF 和 BGP 通过协议交换信息学习路由；Direct 来自接口网段，Static 来自管理员配置。
390|OSPF|ospf|Hello 用来发现邻居并周期维持关系，也携带 DR/BDR 等参数；LSDB 摘要和 LSA 更新由其他报文完成。
391|路由基础|ip|普通路由器按目的 IP 查路由表，主要连接不同网段；按源 IP 转发需要额外的策略路由机制。
394|链路聚合|lacp|LACP 先比较系统优先级，较小者成为主动端；仅在相等时才比较设备 MAC，不能无条件按 MAC 选举。
395|MPLS|label|每个 MPLS 标签头都有一位 S：S=1 表示栈底、后面没有其他标签；S=0 表示后面仍有标签。|AB
397|DHCP|dhcp|地址池耗尽或 DHCP 无法通信会导致分配失败；另一个 DHCP 服务器也可能抢先应答，Windows 回退地址常在 169.254/16。
399|IPv6|addr6|IPv6 有单播、组播和任播，取消了广播地址；原本需要广播的用途通常由组播实现。
400|设备管理|keys|Ctrl+P 与上方向键均可回看上一条历史命令；Ctrl+U 用于删除当前输入行。
401|WLAN|apon|企业集中管理 WLAN 通常用 AC 管理 AP，PoE 交换机同时给 AP 提供有线连接和供电。
402|WLAN|apon|CAPWAP 控制隧道用 Echo 检测连通性，数据隧道用 Keepalive 保活，分别使用 UDP 5246 和 5247。
403|OSPF|ospf|同一多访问网段中，DROther 仅与 DR/BDR 建立完全邻接，减少邻接数量和重复的 LSA 交换。
404|VLAN|eth|0x8100 是 802.1Q Tag 的类型标识；Trunk 和配置为 tagged 的 Hybrid 端口可发送带 VLAN 标记的帧。
405|ACL|aclm,aclorder|ACL 按配置的匹配顺序逐条检查，命中后停止；未命中是“不匹配”，业务模块决定最终放行或丢弃。|ABCD
406|WLAN|wlan|802.11a 工作在 5 GHz，802.11n 与 802.11ax 支持 5 GHz；802.11g 仅支持 2.4 GHz。
407|Segment Routing|sr|SR 用分段列表表达源路由路径，可结合控制器或分布协议工作；SR-MPLS 并非无需标签表的纯 IP 转发。
409|链路聚合|lacp|LACP 主动端由系统优先级和设备 MAC 地址共同决定；接口优先级和接口号用于成员链路选择。
412|传输协议|tcp,udp|传统 FTP 和 HTTP/1.1、HTTP/2 基于 TCP，TFTP 使用 UDP，Ping 使用 ICMP；HTTP/3 则基于 QUIC/UDP。
413|WLAN|apadd|AC 添加 AP 的三种方式是离线导入、自动发现及手工确认未认证列表，在线添加不是独立方式。
414|WLAN|apup|华为 AC 管理 Fit AP 的升级方式包括 AC、FTP 和 SFTP，TFTP 不在这里所列的在线升级模式中。
415|SNMP|snmp|NMS 管理站与 Agent 通信，Agent 暴露被管对象；MIB 为这些对象定义名称、结构和数据类型。
416|IPv6|addr6|任播将相同地址配置给多个接口，路由把流量送到其中最近的节点，可支持冗余及分担，地址格式与单播相同。
418|设备管理|login|VRP 软件文件可通过设备的 FTP 客户端、FTP 服务器或 TFTP 客户端传输；TFTP 服务器角色并非这些设备的通用升级方式。
419|设备管理|login|Telnet 是远程命令行入口，Console 与支持的 Mini USB 是本地入口；FTP 主要传文件而非交互配置。
420|设备管理|static|清除下次启动配置后需重启，并在重启提示时不保存当前配置，设备才会按无已保存配置的状态启动。
421|堆叠集群|trunk|多台设备组成一台逻辑设备可扩展端口、统一管理并支持跨设备聚合，配合冗余机制可降低单点故障影响。
422|VLAN|eth|单臂路由在一条物理链路上承载多个 VLAN，交换机使用 Trunk，路由器使用各 VLAN 对应的子接口。
423|生成树|stp|经典 STP 为避免暂时环路，Listening→Learning 和 Learning→Forwarding 两次过渡各使用 Forward Delay。
424|IPv4子网|ip|255.255.224.0 是 /19，150.25.0.0/19 的广播地址为 150.25.31.255；C、D 位于主机范围内。
425|OSPF|ospfh|OSPF 可按区域组织网络，拓扑变化触发链路状态更新；SPF 依据链路 cost，而非单纯跳数。
426|OSPF|ospf|DD 报文携带 LSA 头部摘要而非完整内容，LSA 类型、Link State ID 和通告者等头字段共同标识 LSA。
428|OSPF|ospfc|Router ID 用于唯一标识路由器，可手工配置或自动选择，不强制等于接口地址，同一区域不能重复。
429|IPv4|ip|IPv4 的 TTL 占 8 位，值域为 0–255；路由器转发时减 1，耗尽则丢弃，防止报文在环路中无限传播。|ABCD
431|IPv6|ipv6|IPv6 扩展首部包含分片、目的选项和逐跳选项；VLAN 头属于以太网二层封装。
432|OSPF|ospfh|DROther 在广播网段与 DR、BDR 建立 Full 邻接，借助它们交换链路状态；与其他 DROther 保持 2-Way。
433|IPv4分片|ip|Identification 标识原始数据报，Fragment Offset 指明位置，Flags 包含 DF/MF 控制位；TTL 不决定分片位置。
434|路由基础|static|默认路由的前缀为 /0，匹配所有目的地址，但仅在无更长匹配时采用；路由表并非必须包含它。
435|链路聚合|trunk|常用链路聚合模式为手工负载分担与 LACP，后者通过协议协商活动成员和备份链路。
437|PPPoE|pppoe|PPPoE 先在 Discovery 阶段发现接入集中器并获得 Session ID，再在 Session 阶段传送 PPP 报文。
438|OSPF|ospfh|OSPF 支持 Broadcast、NBMA、Point-to-Point 与 Point-to-Multipoint，网络类型影响 Hello 和邻接处理。
439|MAC地址|eth|主机源 MAC 应为单播；首字节最低位为 1 的 01 和 03 开头地址属于组播，不能作为普通网卡单播地址。|BD
441|网络基础|ip|封装与解封装逐层添加或读取控制信息，实现不同协议功能并支撑网络互通；不会以缩短报文为目的。|BC
442|路由基础|static,ospfh|路由条目的三种基本来源为直连接口、手工静态配置和动态路由协议；聚合是整理前缀的方式。|ABC
443|ACL|acl|高级 ACL 可匹配源/目的 IP、协议及 TCP/UDP 端口；用户名属于用户 ACL 范畴，源 MAC 属于二层 ACL。|ABD
444|OSPF|ospf|Area ID 的取值覆盖 32 位空间，骨干区固定为 0；其他区域可宣告自己的网络，无需先创建 Loopback。
445|OSPF|ospf|ExStart 协商 DD 主从关系与初始序列号，Exchange 交换 DD 摘要，LSDB 同步完成后达到 Full。|BCD
446|AAA|login|只有某一管理员不能登录时，应检查其账号是否删除或禁用；全局关闭 Telnet 会同时影响其他管理员。
448|OSPF|ospfc|手工 Router ID 优先；自动选取时优先最大 Loopback 地址，否则最大其他接口地址，VLANIF 也可成为候选。
449|OSPF|ospfc|进入 OSPF 进程视图后，area 0 与 area 0.0.0.0 都表示骨干区并进入其区域视图。
450|PPP|ppp|PPP 用 LCP 建立和管理链路，可选认证验证身份，并用 NCP 配置网络层协议；PPPoE 是承载 PPP 的封装方式。
451|IPv6|ipv6,ip|IPv4 与 IPv6 首部都含版本、源地址和目的地址；IPv6 使用 Next Header，IPv4 相应字段名为 Protocol。
454|BFD|ospfc|BFD 快速检测转发路径故障，可与 VRRP、OSPF、BGP 或静态路由联动，使对应模块及时切换或撤销路径。
461|静态路由|static|/32 路由仅匹配 10.0.2.2，下一跳 10.0.12.2 用于转送该报文，preference 20 是路由优先级。
462|LDP|ldp|Hello 发现标签分发邻居，Initialization 协商会话参数，KeepAlive 维持会话；标签映射不是会话建立的结束条件。|ABC
463|LDP|ldp|LDP 会话类消息包括 Initialization 与 KeepAlive，分别协商会话参数和监测连接；标签请求及释放属于标签类消息。
464|LDP|ldp|自由标签保留保存全部邻居提供的映射，耗费更多资源，但下一跳改变时可能直接使用已保存标签，缩短收敛。
465|MPLS|mpls|以太网和 PPP 使用帧模式 MPLS，ATM 使用信元模式；不同承载把标签放在不同链路封装位置。
466|MPLS|label|MPLS 标签头固定 4 字节，位于链路层与网络层之间；标签栈按后进先出，先处理最外侧栈顶标签。
467|NFV|nfv|NFV 将网络功能软件化并运行在共享通用平台上，有利于降低专用设备成本及加快服务部署，不要求软件统一版本。
468|QoS|wred|PQ 优先调度低时延关键业务，WFQ 按权重分享剩余带宽；灵活分类由流分类机制负责，并非队列组合本身。
470|QoS|qos|简单流分类通常依据 DSCP、802.1p 等已有优先级，复杂流分类结合地址、协议和端口等多种报文特征。
473|QoS|wred|拥塞造成队列积压，使可用吞吐、时延和抖动恶化；网络传输距离不因拥塞而改变。
474|DHCP|dhcp|DHCP 可下发 IP 地址以及网关、DNS 等选项，客户端操作系统名称不是地址配置参数。
477|VLAN|eth|默认 VLAN 1 预先存在且不可删除，交换端口缺省归属该 VLAN，无需先手工创建。
480|防火墙|as,natserver|ASPF 的动态 Server-map 可放行相关数据连接并会老化；连接建立后的报文依靠会话表，NAT Server 也会生成映射。
482|MPLS|mpls|Ingress 从 IP 路由/FEC 找到 NHLFE，得到下一跳及标签动作并执行 Push；ILM 主要处理已带入标签的报文。
483|MPLS|mpls|Ingress 对未带标签的 IP 报文查询 FTN/FEC 对应的 NHLFE，再压入出标签；不能把入口查询写为 ILM。|D
491|防火墙|as|状态检测先查会话表，未匹配进入首包流程；已匹配按会话处理，启用严格 TCP 状态检查时通常以 SYN 建立连接。
492|QoS|wred|低于 35 不丢包，超过 40 丢弃；区间内概率随平均队长增长，50% 是最大概率，不是全区间固定概率。|ABC
497|链路聚合|trunk|多条物理链路汇合提供更高总带宽，按流散列分担负载，并在部分链路故障时通过剩余成员继续转发。
498|RADIUS|login|authentication 与 accounting 分别指定 200.0.12.1 的认证、计费服务，RADIUS 在认证应答中同时携带授权属性；未配置源 IP。
499|NAT|static|私网主机访问公网通常需要默认路由指向出口，再用 NAT 将私网源地址转换为公网地址。
500|AAA|login|AAA 为每位管理员分配独立身份与权限；需配置本地用户名、密码及权限级别，并让 VTY 使用 AAA。
502|QoS|wred|提高瓶颈链路容量可承载更多流量，降低拥塞和排队导致的丢包、时延及抖动，但不能保证所有时延都下降。
507|LDP|ldp|下游自主方式无需先收到请求便通告标签；有序控制从出口或已有下游映射的节点开始，沿上游逐步建立绑定。
509|信息安全|snmpsec|机密性防止未授权读取，完整性防止未授权篡改，可用性保证服务可访问，三者构成 CIA 基本目标。
510|IPv6|nd,dhcp|IPv6 不限于手工配置，支持 SLAAC 无状态配置与 DHCPv6 等自动配置方式。
512|MPLS VPN|vpn|VPN 路由先在 CE/PE 交换，再由 VRF 导入 MP-BGP，远端 PE 将其导入 VRF；公网标签分配属于传输隧道建立。|ACD
514|QoS|wred|RED/WRED 是主动丢弃机制，FIFO 与 WFQ 是排队调度方式，不是拥塞避免的随机丢弃策略。
517|MPLS VPN|vpn|RD 与 IPv4 前缀组成 VPNv4 地址来区分重叠网段；路由导入导出由 RT 控制，RD 不是发布控制策略。
518|NFV|nfv|NFVI 的物理基础为计算、存储和网络资源，服务器、存储及网络设备分别提供这些能力；空调是机房配套设施。
521|ACL|aclorder,acl|高级 ACL 能匹配端口范围，同一 ACL 可用于多个接口；规则编号可自定，也能在入方向应用并匹配 IP 协议号。
523|生成树|stp|STP 与 RSTP 都按 Bridge ID 选根桥，先比较桥优先级，再比较 MAC 地址；STP 并非只比较优先级。
524|IPv4|ip|普通路由转发保留端到端目的 IP，修改链路层封装并递减 TTL；目的地址转换属于另外配置的 NAT 操作。
525|生成树|stp|RSTP 边缘端口原本假定连接终端；收到 BPDU 表明对端可能是桥，便按非边缘端口参与生成树计算。
527|生成树|stp|二层环路会让广播帧反复复制转发，形成广播风暴；生成树通过阻塞冗余路径来消除活动拓扑中的环路。
528|Telnet|telnet|Telnet 基于可靠有序的 TCP 字节流，默认服务端口为 TCP 23。
''')
S.update({
'vlan':'https://info.support.huawei.com/info-finder/encyclopedia/zh/VLAN.html',
'switch':'https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BA%A4%E6%8D%A2%E6%9C%BA.html',
'macvlan':'https://support.huawei.com/enterprise/zh/doc/EDOC1100365027/2580a0e4/Interface%20Types.htm',
'stpd':'https://info.support.huawei.com/enterprise/zh/doc/EDOC1100457495/e66d44a3',
'wac':'https://info.support.huawei.com/info-finder/encyclopedia/zh/detail?action=queryEntityDetail&keyword=WAC',
'radius':'https://www.rfc-editor.org/rfc/rfc2865',
'netconf':'https://www.rfc-editor.org/rfc/rfc6241',
'snoop':'https://info.support.huawei.com/info-finder/encyclopedia/zh/DHCP%20Snooping.html',
'dhcpc':'https://info.support.huawei.com/hedex/api/pages/EDOC1100331917/AZM1014P/05/resources/dc/dc_cfg_dhcp_1019.html',
'mirror':'https://info.support.huawei.com/info-finder/encyclopedia/zh/%E9%95%9C%E5%83%8F.html',
'dhcpstats':'https://info.support.huawei.com/hedex/api/pages/EDOC1000053358/YEF0907R/25/resources/en-us_cliref_0133022555.html',
'dhcpcommands':'https://info.support.huawei.com/hedex/api/pages/EDOC1100331435/AEM10132/04/resources/dc/dhcp_configuration_commands.html'
})
load('''
271|WLAN|wac|AC 集中管理 Fit AP，常放在汇聚层或旁挂部署；Fat AP 可独立工作，AP 通常仍有有线上联接口。
283|设备管理|login|Telnet 提供远程命令行，Console 和受支持的 Mini USB 提供本地控制台；FTP 的主要用途是文件传输。
288|ACL|acl|二层 ACL 按源 MAC、二层协议和 VLAN 等帧信息匹配；源 IPv4 地址是三层匹配条件。
300|RADIUS|radius|认证及计费服务器均设为 200.0.12.1；RADIUS 认证应答也承载授权属性，NAS-IP 属性本身不决定 IP 报文源地址。
301|以太网交换|arp,eth|0x0806 表示 Ethernet II 中承载 ARP，请求可以使用广播目的 MAC；源 MAC 必须是单播地址。
357|WLAN|wac|Fit AP 由 AC 集中控制，Fat AP 通常独立提供接入；因此 C 把两者职责写反，只有 D 描述正确。|D
361|链路聚合|lacp|LACPDU 包含系统 MAC、系统优先级、端口优先级及端口号；接口描述文字不参与协议交换。|B
377|虚拟化|nfv|虚拟机在同一硬件上分区运行并相互隔离，其状态可封装为文件；共享进程地址空间不是虚拟机的封装特征。|ABD
380|网络编程|netconf|NETCONF 和 RESTCONF 是设备配置访问协议，XML、JSON 是数据编码格式；题目问非接口，故选 B、C。|BC
387|WLAN|wlan|AP 周期发送 Beacon，被动扫描可读取 SSID；主动扫描时 AP 通过 Probe Response 回应，Probe Request 由终端发出。|AC
392|以太网交换|arp,eth|EtherType 0x0806 标识 ARP，属于 Ethernet II；ARP 请求目的 MAC 可为广播地址，源 MAC 不能为广播。
393|生成树|stpd|根端口先比较到根桥的路径开销，再按 BPDU 优先级向量及端口 ID 破同分；端口 ID 包含优先级和端口号。
396|ACL|acl|source-mac、l2-protocol 和 vlan-id 都匹配二层信息；source 192.168.1.1 则匹配三层源 IP。|BCD
410|VLAN|vlan|可用 VLAN ID 为 1–4094，VLAN 1 为不可删除的默认 VLAN；4096 已超出有效范围，所以只能选 B、C。|BC
417|Python|py|Python 注释以 # 开头，缩进决定代码块，大小写敏感的输出函数是 print()，不是 Print()。|BCD
440|ACL|acl|常见 ACL 分为基本、高级、二层和用户 ACL，分别面向源 IP、IP/端口、MAC 等二层字段及用户组。
456|DHCP|dhcpc|先全局开启 DHCP，再按所选方式启用全局或接口地址池并配置地址范围；Option 82 是中继附加信息而非必配。
457|DHCP安全|snoop|DHCP Snooping 校验服务器来源及绑定信息，可防伪造服务器、CHADDR 地址耗尽及部分 IP/MAC 欺骗，不能替代 TCP 标志攻击防护。
459|DHCP安全|snoop|DHCP 广播易被伪造服务器响应，CHADDR 身份也可伪造；假 IP/MAC 映射可用于中间人攻击，响应时间长并非根本原因。
460|SNMP网管|snmp|设备与网管需互通并配置一致的 SNMP 参数，设备还需把 Trap 发往正确网管地址，网管才能识别并管理告警。
475|端口镜像|mirror|端口镜像可分别复制入方向、出方向或双向报文；“被丢弃报文”不是这里定义的普通端口镜像方向。
489|AAA|login|其他管理员仍能登录说明全局 Telnet 服务可用，应检查该用户是否删除或禁用，权限 0 本身并不禁止登录。
501|DHCP|dhcpstats,dhcpcommands|display dhcp statistics 及 relay/server statistics 用于统计 DHCP 报文；原选项 statics 应为 statistics。
513|MPLS VPN|vpn|路由传递涉及 CE/PE 交换、VRF 导入 MP-BGP 和远端导回 VRF；公网标签分配建立传输路径，不属于 VPN 路由传递。|ACD
515|WLAN|apadd|华为添加 AP 的方式为自动发现、离线导入和手工确认未认证列表；“在线添加”不是独立方式。|BCD
''')

# Exact repeated blocks preserve each original ID; the parent performs final deduplication.
duplicates={319:299,320:300,321:301,322:302,323:303,324:304,325:305,326:306,327:307,328:308,329:309,330:310,331:311,332:312,333:313,334:314,335:315,336:316,337:317,338:318}

excluded={
266:('QoS','qos','单选题中 A、B、C 均描述可用的 QoS 标记，无法形成唯一正确答案。'),
267:('Python','telpy','代码选项残缺，weite、b\\ 和调用对象不一致使多个选项同时错误，无法唯一判分。'),
269:('路由基础','static','引用两条路由表项却未给出网段及掩码，无法比较最长前缀。'),
276:('eSight','es','未标明 eSight 版本，当前可访问的一手资料不足以逐项确认该版本的四级告警名。'),
277:('LDP','ldp','单选题 A 正确，而 D 的“可以一致”也成立；同时多个 OCR 残词使原题无法形成唯一答案。'),
278:('防火墙','as','区域名称 TrustD/localp/Jntrust 破损，未明确使用的区域优先级，不能可靠恢复全部选项。'),
279:('RADIUS','radius','是否必须计费取决于业务需求，计费服务器也可能为可选项；单选条件不足。'),
280:('MPLS VPN','vpn','题干接口 G0/0/0、G0/0/1 与选项 B 的 G0/0/1、G0/0/2 不一致，存在多个错误描述。'),
289:('WLAN','apup','AP 升级模式取决于型号和版本，官方当前文档列 AC/FTP/SFTP，题目未限定版本却把 TFTP 也选入。'),
299:('设备管理','login','是否支持 none 不认证随 VRP 版本和插件变化，题目没有限定环境，无法确认固定答案 AB。'),
307:('OSPF','ospf','选项 A 缺少 Router ID 比较方向，且默认均参与选举的 C 与答案冲突，无法无猜测恢复。'),
315:('FTP','login','题干“根目录为”后缺少目录值，无法判断选项 A 中的路径是否符合要求。'),
342:('MAC地址表','switch','选项 B 拼接了两句话及另一选项内容，原本关于用户数的条件不完整。'),
344:('Segment Routing','sr','A、B、C 三个选项完全相同，原选项内容丢失，不能恢复原题。'),
346:('NFV','nfv','NVFM/Birtualised 等标识破损，VIM 管理资源与实现虚拟化职责混用，不能可靠恢复原定义。'),
347:('链路聚合','trunklim','选项 D“物理编导”不可恢复，且成员数量/介质限制随模式与设备变化，未限定环境。'),
354:('VLAN','vlan','没有题目所引用的端口配置或拓扑，无法判断 PVID、标签或连通性。'),
358:('ARP','arp','题干没有说明“报文格式”属于哪个协议，不能凭选项推断成 ARP 后判分。'),
360:('ICMP','arp','Ping 的核心协议是 ICMP，ARP 是否需要取决于 IPv4、缓存和下一跳；题目未给出场景，CD 非普遍结论。'),
364:('链路聚合','trunklim','光电口混合和不同速率成员限制取决于产品版本；题目无环境限制，答案还遗漏正确的不能嵌套。'),
368:('WLAN','apon','三层发现可用 DHCP、DNS 或手工指定，广播通常限本广播域；“推荐”缺乏环境条件，原 AC 答案错误但不能唯一确定建议组合。'),
372:('设备管理','login','题干引用的版本输出缺失，不能判断 VRP 版本、运行时间或主控板状态。'),
373:('WLAN','wac','FIA AP 不是明确的 AP 模式名称，无法判断原文是 FIT 还是 FAT；不能通过答案猜改术语。'),
374:('WLAN认证','radius','RADIUS 是后台认证协议，MAC/802.1X/Portal 是终端接入认证方式；分类层级混合，缺少明确问法。'),
375:('WLAN安全','wlan','WPA 未限定版本，WEP 可用开放或共享密钥认证；缺少设备及安全策略条件，不能固定为全部支持。'),
379:('静态路由','static','目的前缀需地址与掩码，下一跳和出接口不是任何场景都必须同时填写；条件不足而答案把三者均列必需。'),
381:('传输协议','tcp','知名端口范围应为 0–1023，TCP 关闭也可合并为三段；UDP 没有序列号，原答案 AC 不可靠且问法过于绝对。'),
385:('OSPF','ospf','Attempt 是否稳定与 NBMA 场景有关，“稳定状态”未定义且未限定网络类型。'),
398:('WLAN安全','wlan','WPA28021 选项不可准确还原，且 WEP 认证模式未限定，不能无猜测判定全部正确。'),
408:('链路聚合','trunklim','CE 电口术语破损，介质与速率混合受型号/版本影响，原题未限定设备。'),
411:('ACL','acl','匹配规则正文缺失，只有 rule 5，A 地址“10045”也不完整，无法进行通配符计算。'),
427:('IPv4分类','ip','127/8 具有 A 类格式但保留用于环回；未区分分类格式和可分配 A 类主机地址，答案存在口径歧义。'),
430:('WLAN','wlan','“2.4GHz两个字段”缺失另一个频段或词语，无法确认原题问单频还是双频。'),
436:('IPv6','addr6','题干组值 39A 与选项的 839A 不同，不能确定该恢复哪一边，不能靠选项答案反推地址。'),
447:('OpenFlow','netconf','原答案 CD 但 C“只能一张流表”错误，题干混入未限定版本的定长/变长断言，缺乏匹配的 OpenFlow 版本条件。'),
452:('IPv6','nd','SLAAC 获取前缀使用 RS/RA，但完整配置还包含以 NS/NA 做重复地址检测；问法未限定获取前缀阶段。'),
453:('准入控制','radius','Agile Controller 版本未给出，现有可访问一手资料不能确认全部 SACG/Portal 等组合。'),
455:('DHCP中继','dhcpc','服务器组并非所有 VRP DHCP Relay 配置方式都必须，题目未限定旧版组式配置。'),
458:('DHCP','dhcp','冲突地址是否以及如何恢复取决于实现和探测结果，选项 D 条件残缺，不能把所有冲突地址均视作可分配。'),
469:('VRRP','vrrp','IP-link 联动受产品与版本限制，未指定设备，不能确认四种机制全部支持。'),
471:('防火墙','as','分片报文过滤能力与匹配字段及实现相关，题干“检测过速”破损，原答案漏首片但未给出可判定规则。'),
472:('eSight','es','未指定 eSight 版本，当前一手资料不足以确认这四个历史告警筛选字段。'),
476:('DHCP中继','dhcpc','引用的交换机配置完全缺失，无法确认 VLANIF、服务器组名称及中继动作。'),
478:('防火墙','as','安全策略匹配报文长度或应用的能力依型号与版本变化，未指定产品，一手资料不足以完整核对选项。'),
479:('防火墙','as','题干问接口工作模式但选项混入整机路由/透明模式，缺少具体防火墙型号和明确层级。'),
481:('DHCP','dhcpc','全局地址池服务仍有接口使能和中继条件，A“所有端口”过于绝对，原答案 AB 不能普遍成立。'),
484:('DHCP','dhcp','没有 DHCP RENEW 报文类型，续租使用 DHCPREQUEST；其余选项把 renew 与释放混淆，无法提供完整正确组合。'),
485:('VRRP','vrrp','选项 A“当 slave 收到 master2 发送报文时”缺失结论，无法恢复；优先级 0 也会先缩短超时而非无条件立即切换。'),
486:('MAC地址表','switch','选项 B 把 MAC 表数量和重启丢失拼成一句，条件与结论混杂，无法原样可靠判分。'),
487:('网络可靠性','trunk','A 与 B 重复且“可用性网络”问法残缺，原答案选择故障只能人工恢复，与高可用含义不符。'),
488:('QoS','wred','题干问时延抖动，选项却为业务中断、管理和设备利用率，明显属于另一题，不能恢复。'),
490:('eSight','es','NP 地址不是明确发现方式，可能丢失“IP 网段”等内容，不能根据答案反推修复。'),
493:('QoS','wred','各流量速率、端口总带宽与 WFQ 权重全部缺失，不能计算调度结果。'),
494:('QoS','wred','选项 B“传验过程”不可准确恢复，收发处理与队列均可能丢包，原 ABC 缺乏判定边界。'),
495:('QoS','qos','QoS 优先级标记与地址改写概念混用，设备对 MAC/IP 改写支持也依特性与型号，未给出明确条件。'),
496:('QoS','qos','是否能按包长复杂分类取决于设备和匹配扩展能力，未限定环境，不能普遍判定 D 错误。'),
503:('防火墙','as,natserver','选项 C 拼接了 D，ASPF 名称也破损，不能恢复完整选项后唯一判分。'),
504:('MPLS','mpls','命令 ingiess/out-lable 与入接口 LSR 等多处残缺，无法不猜测恢复具体配置题。'),
505:('终端安全','nfv','Agile Controller 产品版本未给出，选项多处 OCR 异常，缺少能逐项确认的一手资料。'),
506:('终端安全','nfv','版本和 MC 管理能力未明确，选项“一键完全修复”等绝对断言无可验证条件。'),
508:('信息安全','snmpsec','题干“体系时000三者”有关键缺词，人员/管理/技术组合无法仅凭选项恢复原问法。'),
511:('eSight','es','物理拓扑与业务关系混用，未给版本，现有官方资料只支持布局和状态展示，无法确认所有描述。'),
516:('eSight','es','未给 eSight 版本，当前一手资料不足以确认子网嵌套及其资源管理选项。'),
519:('OSPF','ospf','A DR 与 DR 的表述不明确，B 缺少 Router ID 比较方向，关键描述残缺。'),
520:('NFV','nfv','VAR 不是明确的产品场景名称，无法确认原题是否 vAR 及对应虚拟化功能集合。'),
522:('网络规划','nfv','题目属于厂商课程的需求归纳，未给背景，一手资料不足以判定哪些是必选新需求。'),
526:('生成树','stpd','根桥端口在普通点到点拓扑常为指定端口，但同一共享网段的冗余端口可有其他角色，“所有”未限定拓扑。')
}
for id,(topic,src,reason) in excluded.items():
 rows[id]=dict(id=id,explanation='已剔除：'+reason,topic=topic,status='exclude',reason=reason,corrected_answer=None,corrected_stem=None,corrected_options=None,sources=[S[x] for x in src.split(',')])
for dst,src in duplicates.items():
 rows[dst]={**rows[src], 'id':dst,'duplicate_of':src}

# OCR repairs whose intended tokens are unambiguous.
Q={q['id']:q for q in questions}
repairs={271:{'A':'无线控制器 AC 一般位于网络汇聚层，提供高速、安全、可靠的 WLAN 业务'},288:{'A':'rule 20 permit source-mac 0230-0405-0607','B':'rule 10 permit l2-protocol arp','C':'rule 25 permit source 192.168.1.1 0.0.0.0','D':'rule 15 permit vlan-id 100'},392:{'A':'此数据帧的目的 MAC 地址有可能是 FFFF-FFFF-FFFF','B':'此数据帧为 Ethernet II 帧','C':'此数据帧的源 MAC 地址一定不是 FFFF-FFFF-FFFF','D':'此数据帧为 IEEE 802.3 帧'},396:{'B':'rule 10 permit l2-protocol arp'},440:{'A':'基本 ACL'},457:{'A':'防御改变 CHADDR 值的地址耗尽攻击'},501:{'A':'display dhcp statistics','B':'display dhcp relay statistics','C':'display dhcp server statistics','D':'display dhcp'}}
for id,change in repairs.items(): rows[id]['corrected_options']={**Q[id]['options'],**change}
rows[281]['corrected_stem']='主机经常移动位置时，使用哪种 VLAN 划分方式最合适？'
rows[380]['corrected_options']={**Q[380]['options'],'A':'RESTCONF'}
for id in (301,321):
 rows[id]['corrected_stem']='如果以太网数据帧 Length/Type=0x0806，下列说法正确的是？'
 rows[id]['corrected_options']={**Q[id]['options'],'D':'此数据帧为 Ethernet II 帧'}
rows[341]['corrected_options']={**Q[341]['options'],'B':'Forwarding','D':'Learning'}
rows[432]['corrected_options']={**Q[432]['options'],'A':'BDR'}
rows[450]['corrected_stem']='PPP 协议由以下哪些协议组成？'
rows[514]['corrected_options']={**Q[514]['options'],'B':'RED'}
rows[498]['reason']='依据题干中完整 RADIUS 配置核对；待主代理补绘配置截图。'
rows[498]['sources']=[S['radius']]

for id in [270,296,317,348]:rows[id]['sources']=[S['switch']]
rows[281]['sources']=[S['macvlan']]
for id in [287,309,310,329,330,362,404,422,477]:rows[id]['sources']=[S['vlan']]
for id in [297,298,302,318,322,338,341,343,423,523,525,527]:rows[id]['sources']=[S['stpd']]

# Final audit: retain complete literal configuration rather than guessing missing tokens.
for id,reason in {
483:'选项 B 把 ILM 写成提供出标签及操作的表，正确应为 NHLFE；其余选项也混淆 FTN/ILM，疑似配置题 OCR 丢失，无法恢复完整原题。',
465:'选项 D“已经解怠了 MPLS Header”含关键不可恢复残词，无法可靠判断完整描述。',
502:'增加带宽可缓解拥塞，但是否增加控制协议可用带宽依调度策略，“意味着更小时延抖动”也不是无条件保证，选项缺少条件。'
}.items():
 rows[id].update(status='exclude',reason=reason,explanation='已剔除：'+reason,corrected_answer=None,corrected_stem=None,corrected_options=None)
rows[407]['corrected_options']={**Q[407]['options'],'A':'SR（Segment Routing）采用 IP 转发，不需要额外维护另一张标签转发表。','D':'采用源路由技术，提供网络和上层应用快速交互的能力。'}
rows[407]['corrected_stem']='通过 SR（Segment Routing）可以简易定义一条显式路径，网络中的节点维护分段路由信息。Segment Routing 具有如下哪些特点？'
rows[378]['corrected_stem']='通过 SR 可简易定义一条显式路径，网络中的节点维护 Segment Routing 信息。下列哪些是 Segment Routing 的特点？'
rows[378]['corrected_options']={**Q[378]['options'],'A':'通过对现有协议（例如 IGP）进行扩展，使现有网络能够平滑迁移。','D':'同时支持控制器的集中控制与转发器的分布控制，在两者之间提供平衡。'}
for id in (300,320):
 rows[id]['corrected_stem']='路由器 RADIUS 配置如下，下列说法正确的是？\nRADIUS-server template Huawei\nRADIUS-server shared-key cipher Huawei\nRADIUS-server authentication 200.0.12.1 1812\nRADIUS-server accounting 200.0.12.1 1813\nRADIUS-attribute nas-ip 200.0.12.2'
rows[515]['duplicate_of']=413
rows[509]['sources']=['https://www.nccoe.nist.gov/publication/1800-26/VolA/index.html']
for r in rows.values():
 r['sources']=['https://datatracker.ietf.org/doc/html/rfc4364' if u==S['vpn'] else u for u in r['sources']]

fixes={'inte et':'Internet','Ethe et':'Ethernet','Frowarding':'Forwarding','frowarding':'Forwarding','Froward':'Forward','Lea ing':'Learning','lea ing':'Learning','无状态主动配置':'无状态自动配置','多种方式主动配置':'多种方式自动配置','DHCPV6的形状':'DHCPv6 的方式','Mulit-Access':'Multi-Access','riouter id':'router ID','CAWAP':'CAPWAP','keeplive':'Keepalive','Furst Out':'First Out','Lasth Fiust Out':'Last In First Out','未了区分':'为了区分','协议类型有哪些':'网络类型有哪些','协议支持以下哪些协议类型':'协议支持以下哪些网络类型'}
for id,r in rows.items():
 if r['status']!='keep':continue
 originalstem=r['corrected_stem'] or Q[id]['stem']
 fixedstem=originalstem
 for old,new in fixes.items():fixedstem=fixedstem.replace(old,new)
 if fixedstem!=originalstem:r['corrected_stem']=fixedstem
 opts=dict(r['corrected_options'] or Q[id]['options'])
 fixed=dict(opts)
 for letter,value in opts.items():
  for old,new in fixes.items():value=value.replace(old,new)
  fixed[letter]=value
 if fixed!=opts:r['corrected_options']=fixed

missing=sorted(set(Q)-set(rows))
assert not missing,missing
for r in rows.values():
 assert r['explanation'] and r['topic']
 if r['corrected_answer']:assert all(a in (r['corrected_options'] or Q[r['id']]['options']) for a in r['corrected_answer'])
(root/'review_b.json').write_text(json.dumps([rows[id] for id in sorted(rows)],ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'total':len(rows),'keep':sum(r['status']=='keep' for r in rows.values()),'exclude':sum(r['status']=='exclude' for r in rows.values()),'corrected_answers':sum(bool(r['corrected_answer']) for r in rows.values())},ensure_ascii=False))

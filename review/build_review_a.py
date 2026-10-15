import json
from pathlib import Path

ROOT = Path(__file__).parent
questions = json.loads((ROOT / 'questions_a.json').read_text(encoding='utf-8-sig'))
reviews = {}
sources = {
 '路由基础': 'https://info.support.huawei.com/info-finder/encyclopedia/en/detail?action=queryEntityDetail&keyword=IP+routing',
 '静态路由': 'https://support.huawei.com/enterprise/zh/doc/EDOC1100333406/ac7caed7/ip-route-static',
 'OSPF': 'https://www.rfc-editor.org/rfc/rfc2328.html',
 'STP/RSTP': 'https://info.support.huawei.com/enterprise/zh/doc/EDOC1100457495/e66d44a3',
 'VLAN': 'https://info.support.huawei.com/hedex/api/pages/EDOC1100331440/AZM10131/04/resources/dc/dc_cfg_vlan_1005.html',
 '以太网交换': 'https://info.support.huawei.com/hedex/api/pages/EDOC1000053358/YEF0907R/25/resources/en-us_concept_0141563763.html',
 '链路聚合': 'https://info.support.huawei.com/info-finder/encyclopedia/en/LACP.html',
 'IPv4': 'https://www.rfc-editor.org/rfc/rfc791.html',
 'IPv6': 'https://www.rfc-editor.org/rfc/rfc4291.html',
 'IPv6报文': 'https://www.rfc-editor.org/rfc/rfc8200.html',
 'DHCP': 'https://www.rfc-editor.org/rfc/rfc2131.html',
 'PPP': 'https://www.rfc-editor.org/rfc/rfc1661.html',
 'PPPoE': 'https://www.rfc-editor.org/rfc/rfc2516.html',
 'FTP': 'https://www.rfc-editor.org/rfc/rfc959.html',
 'SNMP': 'https://www.rfc-editor.org/rfc/rfc1157.html',
 'ARP': 'https://www.rfc-editor.org/rfc/rfc826.html',
 'NAT': 'https://www.rfc-editor.org/rfc/rfc3022.html',
 'MPLS': 'https://www.rfc-editor.org/rfc/rfc3032.html',
 'Segment Routing': 'https://www.rfc-editor.org/rfc/rfc8402.html',
 'CAPWAP': 'https://www.rfc-editor.org/rfc/rfc5415.html',
 'AP上线': 'https://info.support.huawei.com/hedex/api/pages/EDOC1100210440/AZK0901G/09/resources/dc/dc_fd_wlan_basic_0007.html',
 'Python Telnet': 'https://docs.python.org/3.12/library/telnetlib.html',
 'VRP权限': 'https://info.support.huawei.com/hedex/api/pages/EDOC1000053358/YEF0907R/25/resources/en-us_cliref_0133032600.html',
}

def add_rows(data):
 for line in data.strip().splitlines():
  if not line.strip(): continue
  parts=line.split('|')
  i=int(parts[0]); topic=parts[1]; expl=parts[2]
  status='keep'; reason=''; ans=None
  if len(parts)>3 and parts[3]:
   if parts[3].startswith('!'): status='exclude'; reason=parts[3][1:]
   else: ans=parts[3]
  reviews[i]=dict(id=i, explanation=expl,topic=topic,status=status,reason=reason,corrected_answer=ans,corrected_stem=None,corrected_options=None,sources=[sources[topic]] if topic in sources else [])

add_rows('''
1|路由基础|路由器在网络层按目的 IP 转发报文，默认不转发二层广播，因此能隔离广播域。
2|VRP命令|Unrecognized command 表示当前位置的关键字无法识别；命令缺少参数通常提示 Incomplete command。
3|OSPF|广播型接口的默认 Hello 间隔为 10 秒，Dead 间隔通常为其 4 倍。
4|IPv4|缺少主机掩码、目标地址与网关所在位置，无法判断目标是否同网段及是否发包。|!依赖缺失拓扑图和地址条件，无法唯一判分
5|OSPF|2-Way 只表示双向邻居关系；达到 Full 才表示链路状态数据库同步完成、邻接关系建立。|D
6|VRP命令|接口的物理、协议和管理状态需依据实际显示信息判断，题目未提供该信息。|!原文缺少接口状态截图
7|静态路由|备用路由配置更大的 preference 值，使其优先级低于主路由，主路由失效后再参与转发。
8|OSPF|Hello 报文周期性发现邻居并维护其存活状态，也用于检查建立邻居所需的参数。
9|OSPF|OSPF 按路径上接口开销之和选择最短路径，缺少各链路开销无法计算。|!缺少拓扑图与链路开销
10|STP/RSTP|RSTP 将端口状态归并为 Discarding、Learning、Forwarding；Blocking 是传统 STP 的状态名。
11|VLAN|802.1Q 的 VLAN 标签中 VID 占 12 bit，可编码 4096 个值；0 和 4095 保留。|C
12|以太网交换|目的 MAC 未在地址表中时，交换机会在同 VLAN 内除入端口外的可转发端口泛洪，并学习源 MAC。
13|VLAN|VLANIF 是 VLAN 对应的三层逻辑接口，可以配置 IP 地址并作为该 VLAN 的网关。
14|VLAN|interface vlanif 加 VLAN 编号用于创建或进入相应 VLAN 的三层接口视图。
15|STP/RSTP|RSTP 的三种端口状态分别是丢弃、学习和转发；丢弃状态不学习 MAC，也不转发用户帧。
16|ACL|通配符 0.0.0.255 匹配 192.168.2.0/24，0.0.0.0 精确匹配目的主机 172.16.10.2。
17|NAT|对外提供 HTTP 服务通常需要将公网地址和 TCP 端口映射至内网服务器，但本题配置选项缺失。|!缺少拓扑、地址、配置选项，选项仅为字母
18|NAT|动态 NAPT 自动建立地址和端口转换表，通常无需逐个手工指定私网端口与公网端口的对应关系。
19|DHCP|客户端初始广播不能跨路由器，中继把请求送到其他网段的 DHCP 服务器，并用 giaddr 标识客户端网段。
20|CAPWAP|CAPWAP 使用 Image Data Request / Response 传输镜像相关数据，AP 可据此完成软件镜像下载。
21|PPPoE|PPPoE 会话由 Session-ID 与通信双方的以太网 MAC 地址共同标识，不以 IP 地址区分。|C
22|PPP|PPP 提供点到点链路上的封装与链路控制，属于 OSI 数据链路层协议。
23|IPv6|链路本地地址的标准格式包含 64 bit 接口标识，前 64 bit 由前缀和零位组成。
24|Python Telnet|close() 会关闭 Telnet 连接，不能用来等待命令回显；读取回显应使用 read_until() 等方法。
25|静态路由|静态路由由管理员配置，无须路由协议交换更新；路径变化时通常需要人工修改或配合检测机制。
26|静态路由|display ip routing-table protocol static 按协议来源筛选，只显示静态路由。
27|VRP命令|VRP ping 的 -a 参数指定 Echo Request 使用的源 IP 地址。
28|OSPF|LSAck 对收到的 LSA 进行确认，配合超时重传保证链路状态信息可靠泛洪。
29|OSPF|LSR 按 LSA 的类型、标识和通告路由器，请求邻居发送本地缺少或更新的 LSA。
30|STP/RSTP|根桥选择最小 Bridge ID，先比较桥优先级，再比较 MAC；4096 小于其余选项的 32768。
31|链路聚合|选定主动端设备后，活动端口先按端口优先级排序；值相同再比较端口号，均为较小者优先。
32|VLAN|Hybrid 可按 VLAN 分别设置 tagged 或 untagged，发送属于 untagged 列表的帧时去除标签。
33|VLAN|空格列举 10 和 20 只创建两个 VLAN；10 to 20 是包含两端的连续区间，共 11 个。
34|ACL|华为编号型二层 ACL 使用 4000–4999，主要按 MAC 地址和以太网类型等二层字段匹配。
35|ACL|高级 ACL 的编号范围为 3000–3999，可按源/目的 IP、协议以及 TCP/UDP 端口等条件匹配。
36|DNS|DNS 将域名解析为地址等资源记录，客户端可用易记的名字访问网络服务。
37|HTTP|HTTP 同样能传输文件内容，题目没有明确“专门用于文件传输”的限定，单选分类不严谨。|!HTTP 可传输文件，题干缺少排他性限定
38|WLAN|Wi-Fi 6 引入 OFDMA 等机制提高容量并降低拥塞时延，TWT 有助于终端节电，更高耗电并非其优势。
39|AP上线|AP 发现 AC 后先建立 CAPWAP 控制连接，随后才进行镜像检查、配置获取和业务运行。
40|Segment Routing|Segment Routing 将转发路径表达为段的有序列表，由源节点施加段列表，属于源路由思想。
41|PPP|链路建立阶段由 LCP 协商 MRU、认证方式等链路参数；NCP 在之后配置网络层协议。|B
42|IPv4|TTL 为 8 bit，路由器转发时递减；归零后丢弃报文，避免数据包在环路中无限转发。
43|IPv6报文|IPv6 基本首部固定为 40 字节；扩展首部与负载不计入这个长度。
44|IPv6报文|Hop Limit 在每次经过路由器时递减，作用对应 IPv4 的 TTL。
45|SNMP|管理站通常在 UDP 162 端口接收 Trap；UDP 161 则用于代理接收常规管理请求。
46|IPv6|MAC 中间插入 FFFE，并翻转首字节的 U/L 位：00→02，得到 02E0:FCFF:FEEF:0FEC。
47|OSPF|OSPF 视图下 display this 和 display current-configuration 都可以查看配置，前者只显示当前视图。|!单选题存在 A、B 两个正确选项
48|VRP命令|FTP 用于传输配置文件等文件，不能像 Console 或 Telnet 那样提供命令行交互配置会话。
49|路由基础|路由器在网络层读取目的 IP 并选择下一跳；普通二层交换机则按 MAC 地址转发帧。
50|OSPF|在 VRP 中配置 OSPF 通常既要创建进程，也要配置区域；Router ID 可自动选取。|!单选题 B、C 均为配置步骤，无法唯一判分
51|IPv4|/30 留下 2 bit 主机位，地址块为 .0–.3，主机位全 1 的 .3 为广播地址。
52|SNMP|Trap 是代理主动发送的异步告警，不要求管理站先发出查询请求。
53|以太网交换|首字节 01 的最低有效位为 1，表示组地址，因此该 MAC 是组播而非单播地址。
54|PPPoE|PPPoE 定义发现和会话两个主要阶段，PADT 可终结会话；“数据转发阶段”不是独立阶段名称。
55|AAA|authentication-mode 选择认证方法；authorization-mode 选择授权方法，二者职责不同。
56|WLAN|Wi-Fi 6 对应 IEEE 802.11ax；IEEE 802.11ac 对应 Wi-Fi 5。
57|IPv6|IPv6 地址由 8 组、每组 16 bit 构成，总长度为 128 bit。
58|VRP命令|在系统视图中执行 sysname Huawei，设备名称及命令行提示符随之改变。
59|ACL|高级 ACL 可以检查 TCP/UDP 源、目的端口；基本 ACL 主要检查源 IP 地址。
60|静态路由|默认路由前缀为 0.0.0.0/0，在系统视图配置，并指定有效下一跳 192.168.1.1。
61|IPv4|平均分为 8 个 /27 子网应使用 255.255.255.224；/28 虽可容纳 14 台主机，却会划出 16 个子网。|!“平均分配 8 个”与选项冲突，缺少 /27 正确选项
62|IPv4|20 台主机需要至少 /27 的 30 个可用地址；选项 C、D 却完全相同，无法唯一判分。|!C、D 选项重复且均正确
63|VLAN|Access 出口面向普通终端，发送本 VLAN 的帧时去除 802.1Q 标签。
64|STP/RSTP|RSTP 保留 Learning 与 Forwarding，并用 Discarding 合并传统 STP 的非转发状态。
65|VLAN|VLANIF 的链路状态依赖所属 VLAN 至少一个成员接口 Up；只有创建 VLAN 和配置 IP 不够。
66|以太网交换|普通二层交换机按 MAC 转发帧，不执行 IP 路由，因此不需要修改三层 TTL 等字段。
67|ACL|编号型二层 ACL 主要匹配 MAC、VLAN、以太网类型等二层信息，区别于 IP ACL。
68|DHCP|客户端发送 DHCPDISCOVER 发现可用服务器，服务器再用 DHCPOFFER 提供候选配置。
69|CAPWAP|CAPWAP 使用 UDP 并分别承载控制和数据；在集中转发模式下，AP 将用户报文封装后交给 AC。
70|AP上线|Huawei IPv4 AP 可从 DHCP Option 43 的厂商信息获取 AC 地址，然后发送单播发现请求。
71|MPLS|MPLS 标签的 TC 字段占 3 bit，可编码 2³=8 个值，用于服务类别标记。
72|SNMP|Trap 的接收端是管理站 UDP 162；代理 UDP 161 主要接收 Get、Set 等管理请求。|C
73|IPv6报文|IPv6 新增 20 bit Flow Label，用来标识报文所属流；IPv4 基本首部没有对应字段。
74|IPv6|Router Advertisement 是 ICMPv6 邻居发现报文，携带前缀等参数以支持无状态地址配置。
75|IPv6|2001::12:1 属于全球单播地址范围；FE80::/10 是链路本地，FF00::/8 是组播。
76|MPLS|一个 MPLS 标签栈条目占 4 字节，双层标签增加 2×4=8 字节。
77|OSPF|OSPF 有 Hello、DD、LSR、LSU、LSAck 五类报文，分别承担发现、同步、请求、更新和确认。
78|OSPF|display ospf peer 显示邻居及状态，便于检查是否到达预期的 2-Way 或 Full。
79|静态路由|华为静态路由默认 preference 为 60，取值为 1–255；题中关于 0 的两项均有问题。|!单选题 A、C 均错误
80|路由基础|默认 preference 为 Direct 0、OSPF 内部路由 10、Static 60、RIP 100；数值越小越优先。
81|VLAN|Access 端口将所属 VLAN 的帧以 untagged 形式发送，普通终端不需要处理 VLAN 标签。
82|STP/RSTP|桥优先级相同时比较整个 MAC 数值；00-E0-DC 小于 00-E0-FC，因此交换机 4 成为根桥。|B
83|STP/RSTP|RSTP 通过边缘端口、P/A 与快速根端口切换加快收敛，但在某些场景仍会使用 Forward Delay。
84|NAT|Easy IP 用出口接口的当前公网地址进行端口复用，适合只有一个且可能变化的公网地址。
85|ACL|高级 ACL 匹配 IP、协议、端口和时间范围等条件；物理接口通常是应用 ACL 的位置。
86|NAT|10.0.0.1 属于私有地址，访问 IPv4 公网通常需要 NAT 将源地址转换为可路由的公网地址。
87|FTP|FTP 控制连接使用 TCP 21，命令与响应在控制连接上传输，文件内容走数据连接。
88|FTP|一次典型 FTP 文件传输使用一条控制 TCP 连接和一条数据 TCP 连接，共两条。|B
89|WLAN|无线 STA 完成认证后通过 Association Request/Response 建立关联，协商接入所需参数。
90|VRP命令|display cpu-usage 查看 CPU 使用情况，可用于判断设备处理负载。
91|IPv6|FE80::/10 是链路本地单播前缀，此地址用于同一链路通信，不由路由器跨链路转发。
92|园区网络|先规划需求、地址、拓扑和设备，再实施部署，随后进入运维与优化阶段。
93|IPv4|IPv4 总长度包含首部和数据；有效载荷为 1500−20=1480 字节。
94|路由基础|NextHop 表示转发给哪个下一跳设备，通常是邻居接口地址，而不是本路由器的接口地址。
95|OSPF|VRP 执行 ospf 而未指定 process-id 时，默认进入进程 1；进程号只在本机区分实例。
96|OSPF|OSPF 直接封装在 IP 中，IPv4 Protocol 字段为 89，不使用 TCP 或 UDP 端口。
97|OSPF|LSAck 对 LSU 携带的 LSA 进行确认，发送方据此取消对应重传。
98|VRP权限|command-privilege 修改指定视图中某条命令的权限，本例把用户视图 save 命令设置为 3 级。|D
99|STP/RSTP|默认路径开销按链路带宽确定，带宽越高开销越低，因而更容易被选入到根桥的路径。
100|VLAN|终端通常不携带 VLAN 标签，Access 端口把其流量归入一个 VLAN，并以 untagged 方式发送。
''')

add_rows('''
101|WLAN|SSID 是无线网络的名称；BSSID 标识某个 BSS，通常对应 AP 无线接口或 VAP 的 MAC 地址。
102|静态路由|静态路由不交换动态拓扑信息，普通配置不能自动计算故障后的替代路径。
103|静态路由|华为 VRP 静态路由默认 preference 为 60，数值越小优先级越高。
104|OSPF|ExStart 阶段确定 DD 交换的主从关系和初始序列号，Router ID 较大的一方为主。
105|以太网交换|普通以太网交换机在数据链路层根据 MAC 地址转发帧，并学习源 MAC 与端口对应关系。
106|链路聚合|LACP 模式两端交换 LACPDU，所有活动接口也参与负载分担；C、D 都描述了该模式。|!单选题 C、D 均正确，C 含可辨识 OCR 错误
107|STP/RSTP|传统 STP 的 Forward Delay 默认 15 秒，Listening 与 Learning 各经历一次该延时。
108|STP/RSTP|RSTP BPDU 的协议版本为 2，BPDU Type 为 0x02；传统配置 BPDU 的 Type 为 0x00。
109|VRP命令|设备名称属于系统级配置，需进入 System-view 后执行 sysname。
110|WLAN|country-code 设置监管国家/地区，决定设备允许使用的信道和发射功率等参数。
111|PPP|LCP 的 Magic-Number 用于识别环回等异常；收到与自身相同的魔术字可能表明链路环回。
112|STP/RSTP|RSTP 在二层冗余拓扑中选择无环转发树，并使部分端口不转发用户流量。
113|Python Telnet|read_very_lazy() 不执行阻塞 I/O；read_eager() 和 read_very_eager() 通常也不阻塞，但 IAC 序列处理中可阻塞。|!“非阻塞”限定不清且多方法符合，无法唯一判分
114|UDP|UDP 自身不提供确认和重传；应用若需要可靠性，应在应用层实现相应机制。
115|VRP命令|VRP 是 Versatile Routing Platform 的缩写，即华为通用路由平台。
116|路由基础|网络层提供逻辑地址与路由转发，负责把分组从源网络送往目的网络。
117|ARP|在以太网中 ARP 直接封装为 EtherType 0x0806 的帧，用来查询同链路 IPv4 地址对应的 MAC。
118|IPv4|IPv4 首部最大 60 字节，固定部分为 20 字节，因而选项及填充最多占 40 字节。
119|路由基础|路由表记录目的前缀、下一跳、出接口等三层信息；MAC 对应关系通常存在 ARP 或 MAC 表中。
120|OSPF|ASBR 负责引入其他路由来源，ABR 负责连接多个区域；路由器可为 ASBR 而不同时是 ABR。
121|IPv4|/12 表示前 12 位为 1：首字节为 255，第二字节为 11110000₂=240。
122|以太网交换|静态 MAC 表项由管理员配置，不按动态 MAC 的老化计时器自动删除。
123|VLAN|802.1Q 增加 4 字节标签，其中 TPID 占 2 字节，TCI 占 2 字节；这不是整帧长度。
124|Segment Routing|邻接段表示特定节点的一条邻接链路，Adj-SID 可由节点动态分配，不能说必须手工配置。
125|PPPoE|display pppoe-client session summary 汇总显示 PPPoE 客户端会话状态，便于确认是否建立成功。
126|CAPWAP|直接转发时用户流量由 AP 转发，不必绕经 AC；AC 仍负责控制和统一管理。
127|IPv4|/28 有 16 个地址，除网络和广播地址后有 14 个主机地址；已占用一个，还能增加 13 台。
128|OSPF|DD 携带 LSA 首部摘要描述本地数据库，邻居据此发现缺少或旧的 LSA。
129|IPv4|10.1.1.1 位于 RFC 1918 的 10.0.0.0/8 私有范围，公网不直接路由这些地址。
130|MPLS|常见以太网 MPLS 封装把标签栈放在二层帧头与 IP 首部之间，而不是网络层与传输层之间。
131|STP/RSTP|RSTP 只有 Discarding、Learning、Forwarding 三种端口状态。
132|以太网交换|交换机收到帧后，用源 MAC、入端口和 VLAN 学习表项，再根据目的 MAC 选择转发出口。
133|STP/RSTP|Forward Delay 用于传统 STP 的 Listening、Learning 迁移，给拓扑信息传播和 MAC 学习留时间。|!全部选项均不正确，C 所述 Blocking/Disabled 迁移不符
134|STP/RSTP|根桥按完整 Bridge ID 选举；Bridge ID 由桥优先级等字段和 MAC 地址组成。
135|WLAN|BSS 是基本服务集，表示单个 AP 提供服务的基本覆盖区域；BSSID 则是这个 BSS 的标识符。
136|DHCP|初始客户端尚无服务器地址，DHCPDISCOVER 通常以 255.255.255.255 有限广播寻找服务器。
137|AAA|AAA 依次是 Authentication、Authorization、Accounting，对应身份认证、权限授权和使用记录。
138|RADIUS|Access-Reject 表示服务器拒绝认证，Access-Accept 则表示认证通过。
139|STP/RSTP|RSTP 的非转发状态统一称为 Discarding，没有名为 Blocking 的独立状态。
140|STP/RSTP|RSTP 将传统 STP 的 Disabled、Blocking、Listening 归并为 Discarding，总计三种状态。
141|VLAN|基于 MAC 的 VLAN 分配跟随终端身份，主机更换交换机端口后仍可归入相同 VLAN。
142|ICMP|中间路由器发回 ICMP Time Exceeded，其源 IP 标识该跳设备，Tracert 据此显示路径。
143|IPv4|传统 D 类地址范围 224.0.0.0/4 用于组播，不分配为普通主机的单播地址。
144|IPv4|26 台主机至少需要 5 bit 主机位，2⁵−2=30；因此选 /27，即 255.255.255.224。
145|VRP命令|华为 VRP 在系统视图使用 sysname Huawei 修改设备名称。
146|ARP|以太网 IPv4 通常用 ARP 解析地址；PPP 点到点链路不需要 Ethernet MAC 解析，不能推广到所有链路协议。
147|IPv4|传统点到点互联常用 /30，提供两个可用主机地址；双方支持 RFC 3021 时也可使用 /31。
148|MPLS|MPLS 标签栈通常位于二层帧头之后、网络层报文之前，而非 IP 与 TCP/UDP 之间。
149|VRP命令|Incomplete command 表示已识别命令，但还缺少执行所需的关键字或参数。
150|IPv4|IPv4 IHL 占 4 bit 且以 4 字节为单位，首部长度为 20–60 字节，64 字节超出上限。
151|ICMP|ping 使用 ICMP Echo；在以太网且缺少 ARP 缓存时也可能使用 ARP 解析下一跳 MAC。|!题干“可能使用”使 B、C 均正确，单选类型有误
152|VLAN|端口型 VLAN 绑定交换机端口；终端搬到另一个端口后，需要确保新端口也被配置到目标 VLAN。
153|STP/RSTP|Forwarding 端口转发用户流量、学习 MAC，也继续处理 BPDU 来维护生成树。
154|以太网交换|未知单播一般在同 VLAN 中泛洪；已知目的在入端口时过滤，否则向目的端口转发。
155|ACL|华为基本 ACL 编号范围为 2000–2999，主要用于基于源 IP 的分类与过滤。
156|ACL|ACL 默认步长为 5，使自动编号间保留空隙，便于后续插入规则。
157|FTP|路由器 A 接受一条 Telnet TCP 连接，又作为 FTP 客户端建立控制与数据连接，总计 3 条。
158|DHCP|初始客户端尚未获得 IPv4 地址，发送 DHCPDISCOVER 时源地址使用 0.0.0.0。
159|DHCP|若服务器未另行指定，T1 默认为租期的 50%，客户端开始向原服务器发送续租请求。
160|WLAN|SSID 表示无线网络名称；同一网络可由多个 AP 使用相同 SSID 提供覆盖。
161|IPv6|FE80::/10 标识链路本地单播地址，适用于邻居发现等本链路通信。
162|链路聚合|手工模式无 LACP 协商，所有活动接口都参与转发；同时不使用 LACP 模式的活动链路上限设置。|!单选题 A、B 均正确
163|WLAN|BSS 表示单个 AP 的基本服务区域；BSSID 是该 BSS 的标识符，不能将两者当作同一概念。|B
164|WLAN|华为 AC 使用 country-code 配置国家/地区码，设备据此遵守信道与功率监管要求。
165|WLAN|主动扫描时 STA 发送 Probe Request 查询无线网络，AP 通过 Probe Response 返回 SSID 等信息。
166|SNMP|SetRequest 用于修改管理对象，而 GetRequest、GetNextRequest 也都是管理操作；题干没有限定“修改”。|!“完成管理”含读取与设置，多选项成立
167|IPv4|200.200.200.200/30 的网络地址为 .200，可用地址为 .201、.202；本题主机地址本身无效。|!题干主机地址是网络地址且无有效同网段选项
168|SNMP|常见 SNMP 基于 UDP 传输，查询常用 161 端口，通知常用 162 端口。
169|SDN|典型 SDN 分为应用层、控制层与基础设施/设备层；芯片属于设备内部组成。
170|FTP|固件是二进制文件，应使用 Image/Binary 模式，避免 ASCII 模式转换换行而破坏文件。
171|Segment Routing|Prefix-SID 的分配涉及节点实现与管理策略，标准不将所有 IGP 自动分配一律判为错误。|!缺少特定产品及分配机制限定，B、D 无法可靠排他判断
172|SNMP|SNMPv3 的 USM 可提供认证与隐私保护，使用 authPriv 时加密报文内容。
173|路由基础|Cost 可反映跳数、带宽或时延等路径指标；Sysname 仅是设备名称，不是链路性能指标。
174|以太网交换|MAC 表按 MAC、VLAN 与出端口记录二层转发位置；IP 与 MAC 的映射属于 ARP 表。
175|STP/RSTP|P/A 握手前会同步下游端口，将可能成环的非边缘指定端口置于非转发状态，再允许新链路快速转发。
176|VLAN|所属 VLAN 至少有一个处于 Up 的物理成员接口，VLANIF 才具备正常链路状态条件。
177|STP/RSTP|Alternate 端口提供到根桥的备用路径，根端口失效后最优 Alternate 可快速接替根端口。
178|UDP|UDP 不保证报文交付与顺序；需要可靠性的应用必须自行实现确认、重传等逻辑。|D
179|VRP权限|配置级对应默认命令级别 2，可配置业务；文件系统等基本系统管理通常需要管理级 3。
180|ICMP|华为 VRP 的 tracert 通常发送逐步增加 TTL 的 UDP 探测报文，所以 IPv4 Protocol 为 17。
181|路由基础|华为直连路由 preference 为 0，比 OSPF 10、静态 60、RIP 100 更优先。
182|OSPF|OSPF 泛洪链路状态信息并维护 LSDB，通过 SPF 算法计算路径，属于链路状态协议。
183|OSPF|OSPF 直接运行在 IP 上，协议号为 89，不依赖 TCP 或 UDP。
184|IPv4|145.4.2.55/26 是有效单播主机地址；237 属组播、127 属回环，.112/30 是网络地址。
185|链路聚合|按流散列把同一流映射到相同成员链路，避免逐包分担造成的报文乱序。
186|以太网交换|未打标签的标准 Ethernet II 帧通常为 64–1518 字节，包含 MAC 首部和 FCS，不包含前导码。
187|STP/RSTP|STP 选择无环的逻辑转发树，阻塞部分冗余链路，同时保留故障后的替代路径。
188|VLAN|0x8100 是常见 802.1Q 标签的 TPID，表示其后存在 VLAN 控制信息。
189|VRP权限|认证通过仅说明允许登录；用户等级过低时，仍无权执行配置接口 IP 的命令。
190|AP上线|AP 与 AC 不同网段时可通过 DHCP Option 43 获取 AC 地址，以单播方式跨三层发现 AC。
191|WLAN|AP 周期性发送 Beacon，广播 SSID、能力和时间等信息，供 STA 被动扫描。
192|WLAN|一个物理 AP 可创建多个 VAP，分别绑定 SSID 和安全策略，为不同用户提供不同服务。
193|Python|Python 的运行性能取决于解释器和任务，不能笼统判定所有 Python 程序都“运行效率高”。|!主观性能表述且未限定解释器或比较基准，单选判据不严谨
194|OSPF|未手工指定且没有 Loopback 时，VRP 通常从有效物理接口地址中选取最大 IPv4 地址作为 Router ID。
195|OSPF|LSU 携带一个或多个完整 LSA，向邻居同步和泛洪链路状态信息。
196|STP/RSTP|华为可配置的桥优先级以 4096 为步长，0、4096、8192 合法，2048 不合法。|D
197|STP/RSTP|P/A 通过同步下游端口建立无环条件后再快速转发，快速收敛不依赖盲目缩短等待时间。
198|以太网交换|区分静态与动态 MAC 项必须查看表项类型；题目缺表格，且 D 选项只剩地址。|!MAC 表缺失且选项残缺
199|STP/RSTP|指定端口由网段两端到根桥的路径开销、桥 ID 等信息决定，缺少拓扑不能判断。|!缺少拓扑图和生成树参数
200|以太网交换|MAC 与端口的映射取决于帧从哪个端口到达，必须知道实际连接关系。|!缺少主机与交换机连接拓扑
201|OSPF|Router ID 自动选择需比较 Loopback 与其他接口地址，题中未给接口列表。|!缺少接口地址及类型列表
202|ACL|规则匹配源 192.168.1.0/24、目的 172.16.10.1 且 TCP 目的端口为 21 的报文。
203|VLAN|Hybrid 发送时是否剥离标签取决于 tagged/untagged 配置，题目未提供端口配置。|!缺少交换机端口配置，无法判断各 VLAN 标签行为
204|VRP命令|命令不明确、参数错误、关键字不存在与命令不完整对应不同提示，必须看到实际错误消息。|!缺少题干引用的错误提示内容
205|IPv4|IPv4 基本首部没有 Sequence Number；序列号通常用于 TCP 等协议，TTL 则是 IPv4 字段。|C
206|IPv4|Telnet 使用 TCP，IPv4 Protocol 记录传输层协议号 6；Telnet 的服务端口 23 是另一字段。|B
207|VLAN|802.1Q PCP/Priority 占 3 bit，可表示 0–7 八个优先级值。|A
208|FTP|二进制模式按原字节传输固件，避免文本模式修改换行或字符编码。
209|PPP认证|PAP 认证失败时返回 Authenticate-Nak；成功返回 Authenticate-Ack。
210|以太网交换|交换机主要提供局域网终端接入与二层帧转发，网络出口通常由路由器或防火墙承担。
211|VRP权限|默认配置级可运行各业务配置命令；操作文件系统通常属于管理级权限。
212|OSPF|广播网中的两个 DROther 不建立完整邻接，互相停留在 2-Way 属于正常现象。
213|静态路由|静态路由通常需要目的前缀及下一跳或出接口；B、C、D 均可属于其基本参数。|!单选题多个基本参数选项成立
214|VLAN|port trunk allow-pass vlan all 允许所有 VLAN 通过此 Trunk；PVID 决定相应帧的标签处理。
''')

add_rows('''
215|以太网交换|MAC 地址表保存 MAC、VLAN 与端口的映射，不记录主机的 IP 地址。
216|AAA|用户名没有域后缀时使用默认域，但管理员与普通接入用户的默认域不同，必须明确接入类型。|!未说明管理登录或普通接入，无法确定 default 或 default_admin
217|IPv6|IPv6 组播前缀为 FF00::/8，所以 FF02 开头的是链路范围组播；FE80 是链路本地单播。|D
218|IPv6报文|Traffic Class 为 8 bit，可携带 DSCP/ECN，支持报文分类与 QoS 处理。
219|园区网络|小型园区一般覆盖范围有限、用户较少、层次与业务需求简单；覆盖广不是其典型特点。
220|STP/RSTP|桥优先级越小越优先；数值相同时继续比较 MAC 地址，选最小 Bridge ID 为根桥。
221|AAA|authentication-mode none 关闭该认证检查，因此不要求输入用户名和密码；这会降低访问保护。
222|WLAN|802.11g 工作在 2.4 GHz；802.11n 可使用 2.4/5 GHz，802.11ac 使用 5 GHz。
223|WLAN|802.11g 仅工作于 2.4 GHz，802.11a 使用 5 GHz，而 n、ax 支持多个频段。
224|CAPWAP|Image Data Request 是 CAPWAP 镜像传输请求，AP 通过相关交换获取所需软件镜像。
225|VRP命令|display startup 可显示本次与下次启动文件，但题目未提供实际显示内容。|!缺少题干引用的 startup 输出，B/C 无法核对
226|DHCP|DHCPDISCOVER 由客户端发出以寻找服务器，随后服务器以 DHCPOFFER 返回候选地址。
227|DHCP|默认 T1 为租期 50%，T2 为 87.5%；收到 NAK 要停止用旧地址，租约到期也必须停止使用。|!A、B、D 均基本正确，C“会一直发送”不成立且题干为单选
228|DHCP|DHCPv4 使用 UDP，服务器端口为 67、客户端端口为 68；其报文再封装于 IP。
229|QoS|AF、EF、CS 是不同转发行为类别，实际队列优先级由策略决定；AF11 的丢弃优先级低于 AF12。|!CS 不统一表示最高优先级，缺少配置前提且选项 OCR 残缺
230|IPv4/IPv6|IPv4 地址为 32 bit，IPv6 地址为 128 bit；题干只写“IP”无法排除两种解释。|!缺少 IP 版本关键条件
231|LDP|基本发现通过链路 Hello 自动发现直连 LDP 邻居；扩展发现用定向 Hello 支持非直连邻居。
232|网络成本|OPEX 是 Operational Expenditure，指持续运营支出；CAPEX 才是资本性投入。
233|QoS|RED 是随机早期检测，提前随机丢包以缓解队列拥塞；题中“FED”含义不明且正确范围不确定。|!技术名词疑似 OCR 且单选范围不可靠，不能无依据补写
234|NAT|NAPT 可让多台主机共用公网地址，通过源端口建立不同会话映射，地址数不必等于主机数。
235|SDN|SDN 将控制与转发分离，以逻辑集中控制器管理网络，并通过开放接口支持编程。
236|SDN|ONF 推动以控制与转发分离、OpenFlow 为核心的 SDN 架构；OpenFlow 是控制器与转发设备的接口。
237|静态路由|protocol static 按静态协议来源过滤路由表，区别于完整路由表或统计摘要。
238|VRP命令|NetStream 用于流量统计与导出，不提供登录会话；Telnet、SSH、Web 才是管理接入方式。
239|CAPWAP|CAPWAP 标准化 AC 与无线终结点间的控制与数据通信，FIT AP 通过它受 AC 管理。
240|STP/RSTP|根桥产生携带 TC 标志的配置 BPDU，非根桥沿指定端口向下游传播，根端口负责从上游接收。
241|VXLAN|题目要求排列 VXLAN 通信步骤，但缺少完整选项与有效答案，不能作为独立题判分。|!题干被错误拆分，答案与选项缺失
242|VXLAN|这一行只是上一道题的步骤 1，不是具有题干、选项和答案的完整题目。|!原题步骤被拆成独立题，答案及选项缺失
243|VXLAN|这一行只是上一道题的步骤 2，缺少独立问题及可判分选项。|!原题步骤被拆成独立题，答案及选项缺失
244|VXLAN|“本地进行单播应答”是过程片段，不能脱离原问题成为刷题题目。|!原题步骤被拆成独立题，答案及选项缺失
245|VXLAN|这一行描述目标 VTEP 封装与转发的步骤，缺少完整题目结构。|!原题步骤被拆成独立题，答案及选项缺失
246|VXLAN|这一行是源 VTEP 收到应答后的过程片段，没有独立可判分问题。|!原题步骤被拆成独立题，答案及选项缺失
247|VXLAN|本行只保留步骤 6 与排序选项，前五步不在题干中；不能将缺失步骤顺序当作可直接判分的题。|!依赖前面被拆分的题干，当前独立题残缺
248|SDN|传统网络设备往往各自配置、厂家命令有差异，跨设备部署和调整路径需要较多人工操作。
249|PPP|NCP 完成后进入正常网络通信；Terminate 是终止阶段，PPP 标准要求全双工链路。|!B、E 均错误，单选题无唯一答案
250|ACL|高级 ACL 编号为 3000–3999，可匹配 IP 协议、源目的地址及传输层端口。
251|OSPF|ABR 连接不同区域，ASBR 导入外部路由；ASBR 并不必须处于区域边界。
252|静态路由|给备用静态路由设置更大的 preference，优先使用主路由，主路由失效后切到备用。
253|VRP命令|修改设备名需进入系统视图，再执行 sysname；用户视图主要用于查询和诊断。
254|STP/RSTP|Bridge ID 先比桥优先级，4096 比 32768 小，因此无需再比较 MAC 就能确定根桥。
255|路由基础|路由器根据 IP 目的地址执行跨网络转发，对应 OSI 网络层。
256|Python Telnet|Telnet 构造函数接收 host、port、timeout，不接收用户名密码；题目各项的地址与参数也不正确。|!所有选项均不合法，且设备地址与选项不符
257|VLAN|基于 MAC 的 VLAN 识别终端网卡地址，不依赖其接入端口，适合经常更换办公位置的用户。|B
258|VRRP|preempt-mode timer delay 设置 VRRP 抢占等待时间，防止设备刚恢复就立即抢占引发震荡。
259|DHCP|华为题库所对应的 VRP DHCP 服务器默认租约通常为 1 天，即 24 小时；这不是 DHCP 标准固定值。
260|防火墙|华为防火墙默认安全策略通常为 deny，未匹配到允许规则的跨域流量被拒绝。
261|IPv4|Telnet 使用 TCP，因此 IPv4 Protocol 为 6；23 是 TCP 服务端口号，不能填入 Protocol。|C
262|IPv4|/28 有 14 个可用主机地址，已分配一个，还可增加 13 台主机。|C
263|AP上线|华为 AP 可广播发现同网段 AC，也可静态指定或通过 DHCP Option 获取 AC 地址；组播不是列出的发现方式。|C
264|VLAN|Access 端口发送帧时去掉本 VLAN 的标签；Trunk 可发送 tagged 帧，也可发送 PVID 对应的 untagged 帧。
''')

sources.update({
 'ACL': 'https://info.support.huawei.com/info-finder/encyclopedia/en/ACL.html',
 'WLAN': 'https://info.support.huawei.com/info-finder/encyclopedia/en/SSID.html',
 'DNS': 'https://www.rfc-editor.org/rfc/rfc1034.html',
 'UDP': 'https://www.rfc-editor.org/rfc/rfc768.html',
 'ICMP': 'https://www.rfc-editor.org/rfc/rfc792.html',
 'RADIUS': 'https://www.rfc-editor.org/rfc/rfc2865.html',
 'PPP认证': 'https://www.rfc-editor.org/rfc/rfc1334.html',
 'SDN': 'https://opennetworking.org/sdn-definition/',
 'LDP': 'https://www.rfc-editor.org/info/rfc5036/',
 'VRRP': 'https://info.support.huawei.com/hedex/api/pages/EDOC1100331435/AEM10132/05/resources/dc/dc_cfg_vrrp_0047.html',
})
for r in reviews.values():
 if not r['sources'] and r['topic'] in sources: r['sources']=[sources[r['topic']]]

def source_for(ids, url):
 for i in ids: reviews[i]['sources']=[url]

source_for([2,149], 'https://info.support.huawei.com/hedex/api/pages/EDOC1100277644/AEM10221/04/resources/software/nev8r10_vrpv8r16/user/galaxy/vrp_cli_cfg_0008.html')
source_for([58,109,145,253], 'https://info.support.huawei.com/hedex/api/pages/EDOC1000053358/YEF0907R/25/resources/en-us_cliref_0133022893.html')
source_for([32,63,81,100,214,264], 'https://info.support.huawei.com/hedex/api/pages/EDOC1100331435/AEM10132/04/resources/dc/dc_cfg_vlan_1007.html')
source_for([13,14], 'https://info.support.huawei.com/hedex/api/pages/EDOC1000053358/YEF0907R/25/resources/en-us_cliref_0133018324.html')
source_for([38,56], 'https://info.support.huawei.com/info-finder/encyclopedia/en/detail?action=queryEntityDetail&keyword=WiFi+6')
source_for([135,163], 'https://info.support.huawei.com/info-finder/encyclopedia/en/SSID.html')
source_for([98], 'https://info.support.huawei.com/hedex/api/pages/EDOC1100331435/AEM10132/04/resources/dc/dc_cfg_cli_0029.html')
source_for([156], 'https://info.support.huawei.com/hedex/api/pages/EDOC1100334321/AEM1020X/05/resources/dc/dc_fd_ACL_0007.html')
source_for([141,152,257], 'https://support.huawei.com/enterprise/zh/doc/EDOC1100365027/2580a0e4/Interface%20Types.htm')
source_for([196], 'https://info.support.huawei.com/hedex/api/pages/EDOC1100334321/AEM1020X/05/resources/dc/stp_priority.html')
source_for([206,261], 'https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml')
source_for([259], 'https://info.support.huawei.com/enterprise/en/doc/EDOC1100424954/ceacf129/network-interconnection')
source_for([172], 'https://www.rfc-editor.org/rfc/rfc3414.html')
source_for([55,137,221], 'https://info.support.huawei.com/enterprise/zh/doc/EDOC1100410648/330af205')
source_for([48], 'https://www.rfc-editor.org/rfc/rfc959.html')
source_for([90], 'https://info.support.huawei.com/network/ptmngsys/Web/tsrev_s/en/content/s/13_edesk_ping_packet_loss/edesk_ping_packet_loss_edesk008.html')
source_for([238], 'https://info.support.huawei.com/info-finder/encyclopedia/zh/NetStream.html')
source_for([260], 'https://info.support.huawei.com/hedex/api/pages/EDOC1100149308/AEJ0713J/18/resources/admin/sec_admin_secpolicy_0007.html')
source_for([232], 'https://www.ibm.com/docs/en/apptio-gov/benchmarking/saas?topic=started-appendix-glossary-acronyms')
source_for([95], 'https://info.support.huawei.com/hedex/api/pages/EDOC1100331435/AEM10132/05/resources/dc/dc_cfg_ospf_0005.html')
source_for([78], 'https://info.support.huawei.com/hedex/api/pages/EDOC1100277650/AZM1016J/03/resources/log/yunshan/ospfNbrStateChange_ospfNbrStateChange_Active_2.html')
source_for([125], 'https://info.support.huawei.com/network/ptmngsys/Web/tsrev_ar/en/content/ar/13_edesk_pppoe_cannot_dialup_to_the_internet/edesk_pppoe_cannot_dialup_to_the_internet_edesk001.html')
source_for([26,237], 'https://info.support.huawei.com/enterprise/en/doc/EDOC1100335692/c1ebaf03/basic-ip-routing-configuration')
source_for([180], 'https://info.support.huawei.com/hedex/api/pages/EDOC1100363264/AEN0403J/06/resources/command/yunshan/TRACERT%28DGNIP4OM%29.html')
source_for([222,223], 'https://info.support.huawei.com/network/ptmngsys/Web/tsrev_wlan/en/content/wlan/03_edesk_sta_display_rate_is_slow/edesk_sta_display_rate_is_slow_edesk002.html')
source_for([110,164], 'https://info.support.huawei.com/enterprise/zh/doc/EDOC1100112395/fc9e2b56')
source_for([27], 'https://support.huawei.com/enterprise/en/doc/EDOC1100352661/fda60ef2/verifying-the-network-connectivity-and-reachability')
source_for([115], 'https://info.support.huawei.com/network/ptmngsys/Web/tsrev_wlan/cn/content/wlan/10_edesk_web_login_failure/edesk_web_login_failure_edesk002.html')
source_for([33], 'https://info.support.huawei.com/hedex/api/pages/EDOC1100277650/AZM1016J/04/resources/command/yunshan/BATCHCREATEVLAN%28VLANOM%29.html')
source_for([194], 'https://info.support.huawei.com/info-finder/encyclopedia/en/OSPF.html')
source_for([186], 'https://support.huawei.com/enterprise/zh/doc/EDOC1100412642/461ce9f6')
source_for([89,165,191], 'https://info.support.huawei.com/hedex/api/pages/EDOC1100210440/AZK0901G/09/resources/dc/dc_fd_wlan_basic_0008.html')
source_for([65,176], 'https://info.support.huawei.com/info-finder/encyclopedia/zh/detail?action=queryEntityDetail&keyword=Super+VLAN')
reviews[65]['source_notes']='官方 Super VLAN 描述通过与普通 VLAN 对照说明普通 VLANIF 依赖自身成员物理接口 Up；精确“至少一个”条件另见华为旧版 Command Reference。'
reviews[176]['source_notes']=reviews[65]['source_notes']

stems = {
 11:'IEEE 802.1Q 定义的 VLAN 帧标签中，VLAN ID 总共有多少 bit？',
 43:'IPv6 基本报文头长度为多少 Byte？',
 65:'网络管理员在三层交换机上创建了 VLAN 10，并在该 VLAN 的虚拟接口下配置了 IP 地址。使用 display ip interface brief 查看接口状态，发现 VLANIF10 处于 Down 状态。应通过怎样的操作使 VLANIF10 恢复正常？',
 79:'下列关于华为设备中静态路由的说法错误的是？',
 81:'Access 端口发送数据帧时如何处理？',
 84:'一个公司有 50 个私有 IP 地址，使用 NAT 接入公网，但仅有一个且不固定的公网地址，哪种 NAT 转换方式符合需求？',
 86:'下面选项中，能使一台 IP 地址为 10.0.0.1 的主机访问 Internet 的必要技术是？',
 89:'完成链路认证后，STA 会继续发起关联协商，具体通过以下哪项报文实现？',
 95:'VRP 支持 OSPF 多进程，如果启用 OSPF 时不指定进程号，默认使用的进程号是？',
 114:'UDP 是面向无连接的，必须依靠什么来保障应用所需的传输可靠性？',
 116:'关于 OSI 参考模型中网络层的功能，描述正确的是？',
 123:'IEEE 802.1Q 定义的 VLAN 标签总长度为多少字节？',
 153:'运行 STP 协议的设备端口处于 Forwarding 状态，下列说法正确的是？',
 164:'AC 配置国家码的命令是？',
 177:'RSTP 协议中，当根端口失效时，哪种端口可快速转换为新的根端口并进入转发状态？',
 197:'RSTP 使用 P/A 机制加快端口转到 Forwarding 状态，但没有出现临时环路的原因是什么？',
 214:'命令 port trunk allow-pass vlan all 有什么作用？',
 232:'OPEX 的定义是？',
 236:'SDN 主张采用分层开放架构，倡导、定义集中式架构和 OpenFlow 的是哪一个技术流派？',
 240:'标准 STP 模式下，非根交换机的哪个端口向下游传播根桥产生的 TC 置为 1 的配置 BPDU？',
}
for i,s in stems.items(): reviews[i]['corrected_stem']=s

def option_fix(i, changes):
 opts=dict(questions[i-1]['options']); opts.update(changes); reviews[i]['corrected_options']=opts

for i in [10,64,139]:
 opts=dict(questions[i-1]['options'])
 opts={k:v.replace('Lea ing','Learning').replace('Frowarding','Forwarding') for k,v in opts.items()}
 reviews[i]['corrected_options']=opts
option_fix(20, {'C':'Image Data Request'})
option_fix(24, {'A':'可以使用 telnet.write(b"display current-configuration\\n") 向设备输入查看当前配置的命令', 'B':'使用 telnetlib.Telnet(host) 连接到 Telnet 服务器'})
option_fix(48, {'B':'通过 FTP 对路由器进行交互式配置'})
option_fix(65, {'A':'在 VLANIF10 接口下使用 undo shutdown', 'B':'将一个状态为 Up 的物理接口加入 VLAN 10', 'C':'将任意物理接口加入 VLAN 10', 'D':'将一个状态为 Up 且必须为 Trunk 类型的接口加入 VLAN 10'})
option_fix(117, {'B':'ARP 协议基于 Ethernet 封装'})
option_fix(154, {'A':'如果目的 MAC 对应的端口与入端口相同，则交换机执行丢弃操作', 'B':'如果查不到目的 MAC 地址，则交换机在同 VLAN 的其他可转发端口泛洪', 'C':'如果目的 MAC 对应的端口不是入端口，则交换机从对应端口转发'})
option_fix(164, {'A':'province-code', 'B':'country-code', 'C':'state-code', 'D':'nation-code'})
option_fix(177, {'A':'Forwarding 端口', 'B':'Alternate 端口'})
option_fix(222, {'C':'802.11ac wave 1', 'D':'802.11ac wave 2'})
option_fix(223, {'C':'802.11ax', 'D':'802.11a'})
option_fix(224, {'A':'VRP System Request', 'C':'Image Data Request', 'D':'Image Package Request'})
option_fix(235, {'A':'转控分离、集中控制、开放接口', 'D':'转控分离、集中控制、封闭接口'})
option_fix(237, {'A':'display ip routing-table statistics', 'C':'display ip routing-table'})

reviews[12]['reason']='需按题干重绘交换机未知单播泛洪示意图；重绘不补造具体原拓扑'
reviews[157]['reason']='需按完整题干重绘 Telnet 与 FTP 连接示意图；文字条件足够判断'
reviews[24]['explanation'] += '该题适用于 Python 3.12 及更早版本，telnetlib 已从 Python 3.13 移除。'

# 严格保留原题边界：不补原文缺掉的动作、不改题意以迁就选项。
for i,reason in {
 123:'题干问整帧长度而选项仅能对应标签长度，题意与选项不匹配',
 154:'C 选项缺少具体执行动作，无法恢复原选项',
 197:'题干 OCR 大段重复且 A/B 完全相同，题目质量不足',
 214:'A 选项缺少结论，未提供完整可比较选项',
}.items():
 reviews[i].update(status='exclude',reason=reason,corrected_stem=None,corrected_options=None)
reviews[95]['source_notes']='本轮官方搜索返回完整操作正文并明确默认进程号为 1；直接打开页面返回 403。'


# 原始重复标记仅提供候选；最终由主程序统一归一化和去重。
for q in questions:
 for reason in q.get('initial_exclusion_reasons',[]):
  if reason.startswith('与原题 ') and reason.endswith(' 重复'):
   reviews[q['id']]['duplicate_of']=int(reason.split()[1])

if __name__ == '__main__':
 assert set(reviews)==set(range(1,265))
 assert all(r['explanation'] and r['status'] in ['keep','exclude'] for r in reviews.values())
 (ROOT/'review_a.json').write_text(json.dumps(list(reviews.values()),ensure_ascii=False,indent=2),encoding='utf-8')

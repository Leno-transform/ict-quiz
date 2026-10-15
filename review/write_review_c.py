import json
from pathlib import Path

ROOT=Path(__file__).parent
sources={
'wifi':'https://www-file.huawei.com/-/media/corporate/pdf/ilab/cloud_vr_oriented_bearer_network_white_paper_en_v2.pdf',
'wlan':'https://info.support.huawei.com/enterprise/zh/doc/EDOC1100112395/fc9e2b56',
'stp':'https://info.support.huawei.com/enterprise/zh/doc/EDOC1100457495/e66d44a3',
'stpp':'https://info.support.huawei.com/info-finder/encyclopedia/zh/detail?action=queryEntityDetail&keyword=STP%E7%8E%AF%E8%B7%AF%E4%BF%9D%E6%8A%A4',
'vlan':'https://info.support.huawei.com/hedex/api/pages/EDOC1100331435/AEM10132/04/resources/dc/dc_cfg_vlan_1007.html',
'vlantype':'https://info.support.huawei.com/hedex/api/pages/EDOC1100277650/AZM1016J/03/resources/command/yunshan/PORTLINKTYPE%28VLANOM%29.html',
'ospf':'https://www.rfc-editor.org/rfc/rfc2328',
'ospfh':'https://info.support.huawei.com/enterprise/zh/doc/EDOC1100334536/c1083833',
'ospfi':'https://info.support.huawei.com/hedex/api/pages/EDOC1100210440/AZK0901G/09/resources/dc/import-route_ospf.html',
'bgp':'https://datatracker.ietf.org/doc/html/rfc4271',
'bgph':'https://info.support.huawei.com/info-finder/encyclopedia/zh/BGP.html',
'bgpa':'https://info.support.huawei.com/hedex/api/pages/EDOC1100149308/AEJ0713J/18/resources/admin/sec_admin_router_bgp_0029.html',
'bgpselect':'https://info.support.huawei.com/hedex/api/pages/EDOC1000053358/YEF0907R/25/resources/en-us_concept_0133025584.html',
'ip':'https://www.rfc-editor.org/rfc/rfc791',
'ip6':'https://www.rfc-editor.org/rfc/rfc8200',
'ip6addr':'https://datatracker.ietf.org/doc/html/rfc4291',
'dad':'https://datatracker.ietf.org/doc/html/rfc4862',
'nd':'https://www.rfc-editor.org/rfc/rfc4861',
'snmp':'https://www.rfc-editor.org/rfc/rfc1157',
'snmph':'https://info.support.huawei.com/hedex/api/pages/EDOC1000053358/YEF0907R/25/resources/en-us_concept_0133040780.html',
'dhcp':'https://www.rfc-editor.org/rfc/rfc2132',
'dhcp6':'https://www.rfc-editor.org/rfc/rfc8415',
'capwap':'https://www.rfc-editor.org/rfc/rfc5415',
'vrrp':'https://www.rfc-editor.org/rfc/rfc5798',
'bfd':'https://www.rfc-editor.org/rfc/rfc5880',
'isis':'https://info.support.huawei.com/info-finder/encyclopedia/zh/IS-IS.html',
'nat':'https://www.rfc-editor.org/rfc/rfc3022',
'igmp':'https://www.rfc-editor.org/rfc/rfc3376',
'igmph':'https://info.support.huawei.com/hedex/api/pages/EDOC1100334321/AEM1020X/05/resources/dc/dc_fd_igmp_1005.html',
'igmp2':'https://www.rfc-editor.org/rfc/rfc2236',
'snoop':'https://info.support.huawei.com/enterprise/zh/doc/EDOC1000178145/992007f',
'pim':'https://info.support.huawei.com/info-finder/encyclopedia/zh/PIM.html',
'ssh':'https://www.rfc-editor.org/rfc/rfc4253',
'vxlan':'https://www.rfc-editor.org/rfc/rfc7348',
'mpls':'https://www.rfc-editor.org/rfc/rfc3032',
'qos':'https://www.rfc-editor.org/rfc/rfc2474',
'policy':'https://info.support.huawei.com/hedex/api/pages/EDOC1100277650/AZM1016J/05/resources/vrp/dc_vrp_route-policy_cfg_0001.html',
'policycmd':'https://info.support.huawei.com/enterprise/en/doc/EDOC1100420140/26892fde/routing-policy-configuration-commands',
'traffic':'https://info.support.huawei.com/info-finder/encyclopedia/zh/detail?action=queryEntityDetail&keyword=%E6%B5%81%E7%AD%96%E7%95%A5',
'stack':'https://info.support.huawei.com/info-finder/encyclopedia/zh/%E5%A0%86%E5%8F%A0.html',
'stackjoin':'https://info.support.huawei.com/hedex/api/pages/EDOC1000053358/YEF0907R/25/resources/en-us_concept_0133037414.html',
'vlanpool':'https://info.support.huawei.com/hedex/api/pages/EDOC1100413634/FEN1022J/01/resources/en-us_topic_0000001719655008.html',
'python':'https://docs.python.org/zh-cn/3.12/library/telnetlib.html',
}

# 每行都是人工逐题编写的审核结果；等号只复用语义相同题目的解析。
data='''
529|无线网络|wifi|802.11ac 的 VHT 物理层工作在 5 GHz 频段；双频 AP 的 2.4 GHz 无线通常使用其他 802.11 标准。
530|无线网络|wlan|STA 可被动接收 Beacon，也可主动发送 Probe Request 并接收 Probe Response 来发现网络。
531|网络管理|snmp|SNMP Agent 可主动发送 Trap 通知故障或事件，无需等待管理站轮询。
532|网络基础|ip|IPv4 的 Protocol=6 表示 TCP；传统 HTTP/HTTPS 使用 TCP，但 HTTP/3 使用 UDP，题干未限定版本。
533|设备管理|vrp|save 保存当前运行配置到配置文件，系统时间使用 clock 等命令设置。
534|设备管理|tracert|tracert 逐步增大探测报文的 TTL，借助各跳返回的信息显示到目的地的转发路径。
535|OSPF|ospf|Full 表示邻接两端的链路状态数据库已经完成同步；数据库交换发生在此状态之前。
536|网络基础|vlan|路由器隔离二层广播，普通三层接口连接的网络属于不同广播域。
537|OSPF|ospf|不同接口可以加入不同区域；连接多个区域的路由器可作为 ABR。
538|路由基础|ospf|动态路由通过邻居检测和路由信息更新感知拓扑变化，并重新计算可达路径。
539|网络编程|python|read_very_eager() 读取当前可用数据，通常不等待新数据；IAC 序列处理是例外，必要的等待可用 time.sleep() 实现。
540|生成树|stp|端口被管理关闭或链路失效后即可进入 Disabled，不必依次经过学习和转发状态。
541|IPv6|ip6addr|IPv6 可省略组内前导零，并用一次 :: 压缩连续全零组；本地址没有这两类可压缩内容。
542|以太网交换|mac|二层交换机学习收到帧的源 MAC 与入端口，再按目的 MAC 查表决定转发端口。
543|访问控制|acl|配置顺序下命中首条规则后停止匹配，因此应先放更具体的条件，避免被范围较大的规则遮蔽。
544|访问控制|acl|ACL 只给出匹配结果，最终动作由调用模块决定；例如路由过滤中的 deny 表示不接受路由，并非丢弃一个数据报文。
545|无线安全|wlansecurity|TKIP 可用于 WPA，也曾被 WPA2 的兼容配置支持，因此并非 WPA2-PSK 独有。
546|无线网络|capwap|CAPWAP 控制通道使用 UDP 5246，数据通道使用 UDP 5247，两者端口不同。
547|网络管理|snmp|SNMPv1 定义 GetRequest、GetNextRequest、GetResponse、SetRequest 和 Trap 五种 PDU。
548|=547
549|网络管理|snmph|MIB 描述被管理对象，Agent 维护设备相关的管理信息，NMS 通过对象标识 OID 访问它，并非只存在于 NMS。
550|网络编程|python|read_all() 持续读取到 EOF；如果连接不关闭且未到达 EOF，调用会保持阻塞。
551|网络基础|arp|ARP 在本地链路上解析 IPv4 地址对应的 MAC；目的主机在远端时，主机解析的是下一跳网关的 MAC。
552|设备管理|startup|startup saved-configuration 用来指定下次启动加载的配置文件，save 则负责保存当前配置。
553|=535
554|IPv4|ip|以太网类型 0x0800 表示 IPv4；IHL 以 4 字节为单位，取值 5–15，首部长度为 20–60 字节。
555|VLAN|vlanif|同一路由实例的普通 VLANIF 接口不能配置重复 IP；不同 VPN 实例允许地址重叠，题干遗漏作用范围。
556|IPv4|private|192.168.1.2 是私有地址，不能在公网直接路由；可通过 NAT 或应用代理等方式访问互联网，不能说一定使用 NAT。
557|访问控制|acl|二层 ACL 主要匹配 MAC、以太网类型和 VLAN 等二层字段；源、目的 IP 通常由基本或高级 ACL 匹配。
558|无线网络|wifi6|Wi-Fi 6 是基于 IEEE 802.11ax 的代际名称，关键改进包括 OFDMA 和更高效的多用户传输。
559|无线网络|channel|2.4 GHz 相邻信道中心频率通常只相差 5 MHz，而信道宽度更大，因此多个信道相互重叠。
560|无线网络|fitap|Fit AP 的常规集中管理模式依赖 AC 下发配置和管理；可独立完成管理的是 Fat AP 模式。
561|网络管理|snmp|SNMP 的 Get 类操作读取对象，SetRequest 修改可写对象，因此不只支持查看状态。
562|设备管理|idle|idle-timeout 可在 Console、VTY 等用户界面配置，登录超时并不限于 VTY。
563|链路聚合|trunk|Eth-Trunk 的散列选路由各端独立执行；两端可使用不同负载分担字段，不影响聚合链路成立。
564|生成树|stp|Discarding 状态既不转发用户数据，也不学习源 MAC；进入 Learning 后才学习 MAC。
565|无线网络|country|国家码对应当地无线监管规则，决定允许使用的信道、频段以及发射功率上限。
566|生成树|stp|根桥始发的配置 BPDU 的 Message Age 为 0，下游桥转发时增加该值以限制陈旧信息传播。
567|SDN|sdn|控制与转发分离是 SDN 的核心架构特征之一；题干使用“起源”“本质”作价值判断，缺少明确技术定义。
568|设备管理|vrp|pwd 显示当前工作目录路径，dir 列出目录中的文件和子目录，两者用途不同。
569|OSPF|ospf|Router ID 是 32 位路由器标识，可手工指定，无需与任何实际接口 IP 相同。
570|路由基础|staticroute|静态路由可通过 preference 参数设置优先级；缺省值不代表禁止修改。
571|路由基础|preference|华为普通 OSPF 路由默认优先级常为 10，外部路由默认不同，且优先级可配置，不能由协议名称断言固定值。
572|OSPF|ospf|224.0.0.6 是 AllDRouters 组播地址，广播网络上的 DR 和 BDR 都监听它。
573|VLAN|vlanid|VID=0 表示优先级标签而非普通 VLAN，用户可创建的普通 VLAN ID 为 1–4094。
574|VLAN|vlan|对 Access、Trunk、Hybrid 的普通接收处理会按 PVID 为无标签帧分类；是否丢弃还取决于允许 VLAN，题干未限定端口模式。
575|生成树|stpp|未配置 BPDU 保护时，边缘端口收到 BPDU 后转为非边缘端口，参与生成树计算。
576|VLAN|vlantype|Hybrid 允许多个 VLAN，并可分别设置哪些 VLAN 发出时携带标签，因而既适用于终端连接，也适用于设备互联。
577|SDN|sdn|业务编排负责把服务意图转换为资源部署；OpenStack 涵盖计算、网络等多个组件，不能在未定义架构层次时只归入一个层。
578|路由基础|iprouter|路由器依最长前缀匹配查找可达路由；没有匹配项和默认路由时无法转发，通常丢弃并可能返回 ICMP 不可达。
579|IPv4|iprouter|普通 IPv4 子网中主机位全为 1 是定向广播地址，不可分配为普通主机地址。
580|网络编程|python|telnetlib 曾是 Python 标准库的 Telnet 客户端模块，但从 Python 3.13 起已移除；判断必须限定 Python 版本。
581|VLAN|vlan|普通 Trunk 与 Hybrid 接收时都按 PVID 处理无标签帧，并检查带标签帧的 VLAN 是否允许；主要区别在发送时的标签处理。
582|生成树|stp|Alternate 和 Backup 通常不转发用户数据，但仍处理 BPDU，以便监测拓扑和作为备用路径。
583|访问控制|acl|config 指按规则编号的配置顺序匹配，auto 指按深度优先原则自动排序；原句关键谓语“是”可明确修复。
584|生成树|stp|根桥到自身的根路径开销是 0，但原句在“是”之后缺失数值，无法保留为完整判断题。
585|NAT|nat|NAPT 使用地址加传输层端口映射区分会话；ICMP 查询可使用标识符，单靠 IP 协议号不能区分不同用户。
586|设备管理|vty|user-interface maximum-vty 设置可用 VTY 用户界面总数，从而限制 Telnet/SSH 等远程连接容量。
587|无线网络|apmode|支持的 AP 可在 Fat、Fit 或云模式间切换，具体能力取决于型号和软件版本，不能说都不允许切换。
588|网络基础|topology|树形拓扑由分层星形结构组成，便于扩展；上层节点汇聚更多下层分支，故障影响范围通常更大。
589|IPv6|dhcp6dns|DHCPv6 可通过选项提供递归 DNS 服务器地址；无状态 DHCPv6 也可只分发此类参数而不分配地址。
590|IPv6|dad|DAD 向待检测地址发送 NS；收到相关 NA 或冲突 NS 表示地址可能重复，检查通过后才能正常使用地址。
591|网络虚拟化|nfv|NFV 把网络功能从专用硬件中解耦为软件实例，可在通用服务器上部署和管理。
592|IPv4|ip|/25 留下 7 位主机位；192.168.1.0/25 的广播地址为 192.168.1.127，但原文网段开头已缺失。
593|VLAN|vlan|华为 VLAN 处理模型中，交换机按 VLAN 分类并进行内部转发；原句开头损坏，无法确定被判断的限定条件。
594|无线网络|fitap|AP 上线时会检查版本，仅在需要升级等条件下下载软件；版本匹配时无需每次重新下载。
595|生成树|stp|传统 STP 在默认计时器下依次等待 Listening 和 Learning，各 15 秒，再进入 Forwarding，共至少 30 秒。
596|网络管理|snmph|设备可能支持 SNMPv1、v2c、v3，但默认启用哪些版本取决于具体软件版本；“默认存在所有版本”含义不明确。
597|DHCP|dhcp|DHCP 的 DNS 服务器选项可携带多个 IPv4 地址，长度为 4 字节的整数倍，并非只能提供一个。
598|IPv6|ip6addr|IPv6 环回地址是 ::1/128，用于本机通信，不能作为链路上转发的源或目的地址。
599|OSPF|ospf|各区域维护本区域的拓扑 LSDB；骨干区域收到其他区域的摘要路由，不等于掌握其他区域的完整拓扑。
600|IPv6|ip6|IPv6 基本首部固定为 40 字节；可变的扩展首部位于基本首部之后。
601|以太网交换|mac|已知单播仍要检查出入端口、VLAN 和端口状态；若查到的出口就是入口等情况，应过滤而非一定转发。
602|生成树|stp|STP/RSTP 支持互操作，RSTP 端口检测到传统 STP 后会迁移到兼容模式，并非简单丢弃对方所有 BPDU。
603|VLAN|vlanid|VLAN ID 4095 被保留，普通 VLAN 为 1–4094；华为缺省 VLAN 1 不能删除。
604|路由基础|staticroute|PPP 是点到点链路，出口对端唯一，因此静态路由可使用出接口或下一跳描述路径。
605|无线网络|capwapsource|capwap source interface 或 capwap source ip-address 可指定 AC 建立 CAPWAP 通道时使用的本地源。
606|无线网络|ssid|一个射频可承载多个 VAP，各 VAP 可对应不同 SSID；上限依 AP 型号而定。
607|网络规划|dhcpdesign|服务器提供稳定服务，通常使用静态地址或 DHCP 地址保留，便于客户端定位和统一管理。
608|IPv6|rdnss|SLAAC 负责生成地址，DNS 可由 RA 的 RDNSS 选项或无状态 DHCPv6 提供，因此并非无法获取 DNS。
609|网络管理|snmptransport|常用 SNMP 使用 UDP，管理请求一般发往 161，通知一般发往 162；题干所说 TCP 不是通常传输方式。
610|IPv4|ip|广播地址由网络前缀和全 1 主机位共同确定；只给 192.168.1.0 而未给掩码，不能确定广播地址。
611|AAA|aaa|认证、授权、计费方案和服务器模板是配置资源；在用户所属域下引用后，才用于该域的用户接入流程。
612|VLAN|vlanid|802.1Q 的 VID 只有 12 位，普通 VLAN ID 最大 4094；4096 超出字段范围。
613|AAA|radius|RADIUS 常用于集中式 AAA，其中 Access 类报文处理认证授权，Accounting 报文处理计费记录。
614|NAT|nat|ICMP 查询报文虽无 TCP/UDP 端口，但有标识符，NAPT 可转换标识符以区分并还原不同主机的查询。
615|生成树|stp|Alternate 备份根端口，Backup 备份同一网段上的指定端口，故 Backup 不能承担根端口的替代角色。
616|链路聚合|stack|堆叠或集群把多台物理设备组成一个逻辑设备，可把不同成员上的端口加入同一 Eth-Trunk。
617|=569
618|网络基础|arp|同一子网内的主机可直接 ARP 解析并通信，通常只有访问其他子网时才需要默认网关。
619|无线网络|apmode|Fat AP 自带无线接入、认证及配置管理能力，能独立工作；Fit AP 的集中管理依赖 AC。
620|链路聚合|stack|链路聚合提供成员链路冗余，堆叠提供成员设备冗余，两者结合可降低单链路或单设备故障影响。
621|=562
622|VLAN|vlanbatch|vlan batch 支持一次创建多个指定编号或范围内的 VLAN，减少逐个进入 VLAN 视图的操作。
623|设备管理|vty|华为规范命令是 user-interface maximum-vty；题干的 max-vty 并非该完整命令，来源中的名称不够可靠。
624|无线网络|wlanlayer|WLAN 二层组网描述 AP 与 AC 的管理网络二层可达关系；STA 网关位置不决定 AP 与 AC 的组网类型。
625|无线安全|wlansecurity|WEP 使用 RC4 密钥流机制，TKIP 属于 WPA 等安全机制，并非 WEP 的加密方式。
626|设备冗余|stack|支持 iStack 的型号可把多台设备组成统一的逻辑交换机，具体最大成员数由产品能力决定。
627|AAA|aaa|NAS 按域选用认证、授权、计费方案；用户被映射到某个域后，使用该域的策略和服务器配置。
628|网络基础|pstn|传统固定电话通过公共交换电话网络传递语音，属于通信网络的一种应用。
629|网络规划|vlandesign|按业务划分 VLAN 可隔离广播和不同业务流量，并便于分别配置访问控制和服务质量策略。
630|=539
631|无线安全|wlansecurity|TKIP 可用于 WPA-PSK 和曾经的 WPA2 兼容配置，不应把它限定为单一 PSK 策略。
632|生成树|stp|STP 通过选举根桥并阻塞部分冗余路径形成无环拓扑，避免广播风暴和 MAC 地址表震荡。
633|=529
634|=579
635|路由基础|preference|华为直连路由的优先级为 0，数值越小优先级越高，直连路径因此优于常见动态和静态路由。
636|=556
637|=606
638|=583
639|=530
640|=594
641|访问控制|acl|config 按规则编号匹配；auto 按匹配条件的精确程度自动排序，即深度优先顺序。
642|设备管理|vrp|mkdir 创建指定目录；在当前目录执行 mkdir test 会创建名称为 test 的子目录。
643|传输层|tcp|TCP 建连通常使用三次握手，正常关闭通常使用四个报文；可靠传输还依赖确认、序号、重传等机制。
644|OSPF|ospf|2-Way 只说明双向 Hello 通信建立，LSDB 同步要经过 ExStart、Exchange、Loading 等阶段后达到 Full。
645|OSPF|ospfh|修改 Router ID 通常不会直接替换正在运行的 OSPF 标识，需要重启相应进程后生效。
646|=569
647|生成树|stppriority|华为 STP 桥优先级缺省为 32768；桥 ID 比较时先比较优先级，再比较 MAC 地址。
648|VLAN|vlan|Trunk 发出 PVID 对应 VLAN 的帧时通常去标签，其他允许 VLAN 的帧保留标签。
649|无线网络|apmode|Fat AP 可独立工作，Fit AP 常规模式依赖 AC；仅写“AP”未限定模式，无法统一判定。
650|无线网络|capwap|CAPWAP 控制通道传输配置、状态等管理消息；用户数据封装使用数据通道。
651|MPLS|mpls|MPLS 标签栈放在二层帧头之后、网络层报文之前，常被称作二层与三层之间的封装。
652|=609
653|=547
654|网络管理|snmp|被管理设备运行 SNMP Agent，处理 NMS 的查询和设置，并可生成通知报文。
655|路由基础|preference|优先级用于比较不同路由来源，但不同协议的 cost 含义不同，不能无条件跨协议比较；原句缺少适用条件。
656|VLAN|vlan|Trunk 通常按 PVID 决定是否去标签，Hybrid 按 tagged/untagged 配置决定，不能对所有端口一概而论。
657|NAT|nat|传统静态 NAT 固定映射一个内部 IP 与一个外部 IP；端口复用属于 NAPT 等不同转换形式。
658|生成树|stp|二层环路还需要实际存在闭环链路；本身是树形拓扑的网络，即使不运行 STP 也不会必然出现环路。
659|故障检测|bfd|BFD 是标准化的通用转发路径故障检测协议，不要求双方设备来自某个特殊厂商。
660|故障检测|bfd|BFD 使用较短的周期性控制报文和检测倍数，可把故障检测时间缩短到毫秒级，具体取决于配置和设备能力。
661|故障检测|bfd|BFD 独立检测两端转发路径是否可用，可服务于多种路由协议，不依赖某一种路由协议自身的 Hello 机制。
662|故障检测|bfd|BFD 负责快速检测并报告故障；流量倒换通常由路由协议、FRR 等收到故障通知后执行。
663|=529
664|服务质量|qos|IPv4 原 ToS 字段现解释为 DS 字段，前 6 位是 DSCP，后 2 位用于 ECN。
665|网络虚拟化|nfv|NFV 强调把网络功能软件化并与专用硬件解耦；原句“以特殊化的方式”含义损坏，无法据此判断。
666|网关冗余|vrrp|VRRPv2 与 VRRPv3 的报文和认证机制不同：v3 删除了认证字段，笼统说“VRRP 不支持认证”缺少版本条件。
667|网络虚拟化|vxlan|VXLAN 使用 MAC-in-UDP，将原始二层以太网帧封装进 VXLAN、UDP 和外层 IP，而非 MAC-in-TCP。
668|网络基础|bandwidth|端到端可用吞吐受瓶颈链路容量约束；还会受到协议开销、拥塞和设备性能等因素影响。
669|=644
670|网络基础|delay|端到端时延包含处理、排队、传输及传播时延，不能只统计前两项。
671|生成树|stp|在普通点到点树形连接中根桥端口为指定端口；共享网段上的冗余接口可能为 Backup，且关闭端口不参与，原句过于绝对。
672|=549
673|=626
674|以太网交换|staticmac|静态 MAC 表项由管理员配置；保存配置后重启可恢复，而动态学习表项通常需要重新学习。
675|网络管理|mirror|本地流镜像把匹配流量复制到本机观察端口，远程流镜像通过网络传送至远端监控设备。
676|故障检测|bfd|路由协议的 Hello 检测通常较慢；BFD 可独立加速转发故障检测，不能因已有 Hello 就断言无需 BFD。
677|传输层|protocol|IPv4 的 Protocol 字段中 UDP 的协议号为 17，TCP 才是 6。
678|无线网络|apip|AP 在 IPv4 管理网络中可手工配置静态 IP，也可通过 DHCP 获取管理地址。
679|AAA|authorization|若配置授权方式回退，例如远程授权后跟本地授权，远程服务器无响应时可按配置转用本地；这不是所有设备自动保证的行为。
680|=620
681|IS-IS|isiscost|华为 IS-IS 引入路由时默认 cost 通常为 0，可显式指定；16 不是其默认引入开销。
682|BGP|bgp|AS_PATH 属于公认必遵属性，用来记录经过的 AS 并检测环路，不属于可选过渡属性。
683|OSPF|ospf|DD 交换阶段通过 Router ID 选主从，较大的 Router ID 为主，负责控制 DD 序号。
684|无线网络|vlanpool|HASH 按 STA MAC 的哈希结果选 VLAN，可能发生不均匀分配；even 算法才侧重轮流均衡分配。
685|DHCP|dhcprelay|DHCP Relay 在客户端网段接收请求并转发给服务器，携带中继信息帮助服务器选择正确地址池。
686|网关冗余|vrrp|VRRP 优先级相同的竞选者比较主 IP 地址，地址较大者优先成为 Master。
687|网关冗余|vrrp|虚拟 IP 可与某台成员接口的真实 IP 相同，该设备称地址拥有者，其 VRRP 优先级为 255。
688|网络安全|firewall|发送给防火墙自身接口 IP 的流量终止于设备本机处理，区别于穿越防火墙转发的流量。
689|组播|snoop|IGMP Snooping 监听成员报告并建立二层组播转发表，只向有成员的端口复制数据，减少无关端口的带宽浪费。
690|组播|igmph|SSM Mapping 为不携带源地址的旧版成员报告补充源信息，IGMPv1 和 IGMPv2 主机都可借此接入 SSM。
691|设备冗余|stackjoin|断电设备连接后上电加入现有堆叠属于堆叠加入；已上电运行的系统再连接通常称堆叠合并，原文“上电之后”不能明确区分流程。
692|设备冗余|css|CSS 第一代可通过主控板上的集群卡互联，CSS2 支持交换网板上的集群连接；不能把主控板集群卡限定方式归为 CSS2。
693|服务质量|traffic|MQC 可在接口、VLAN 等支持的视图应用，不只用于三层接口；PBR 的具体应用范围也依设备能力而定。
694|OSPF|ospfi|import-route limit 设置一个 OSPF 进程能引入的最大外部路由数量，正是限制引入规模的命令。
695|OSPF|ospf|Stub 不接收 4、5 类 LSA，ABR 向其中发布 3 类默认路由，使区域仍能访问 AS 外部目的地。
696|OSPF|asbrsummary|asbr-summary 汇总外部路由；带 not-advertise 时，指定范围的外部路由不向外通告。
697|IS-IS|isishello|IS-IS 通过邻居通告的保持时间管理邻接，Hello 发送间隔不必相同；建立邻接还需满足区域、级别等条件。
698|OSPF|ospfpriority|华为接口 DR 优先级缺省为 1，范围 0–255；值 0 表示不参与 DR/BDR 选举。
699|OSPF|ospf|DR/BDR 选举非抢占，已有 DR 不会仅因后来出现更高优先级设备就被替换。
700|以太网交换|switcharch|框式交换机转发依具体架构和报文出入口而异，可能在同一板内完成；题干“上行/下行接口板”未定义且省略交换网环节。
701|网络管理|nce|iMaster NCE-Campus 使用 NETCONF 管理受支持的华为设备，并可通过 SNMP 获取第三方设备管理信息，能力依型号而定。
702|网络安全|firewall|Untrust 是接口所属安全域；Local 代表防火墙设备本身，任何到设备自身的报文仍按 Local 方向处理。
703|组播|igmpproxy|IGMP Proxy 在下游收到成员报告后维护组成员状态，并向上游报告加入，而不是向成员接入侧发送报告。
704|组播|multicastmac|IPv4 组播 MAC 前缀为 01:00:5e，只映射组播 IP 的低 23 位；其余 5 位被舍弃，所以最多 32 个组地址共享同一 MAC。
705|组播|igmp|IGMPv3 保留一般组查询和特定组查询，并增加组与源特定查询，以管理指定源的接收状态。
706|组播|igmph|独立的 IGMP 查询器选举机制由 IGMPv2 引入；IGMPv1 依赖其他组播路由机制确定查询器。
707|OSPF|ospffilter|链路状态协议的 filter-policy import 过滤的是安装到本地路由表的结果，不阻断区域内正常 LSA 泛洪。
708|BGP|bgpa|华为手动聚合比自动聚合具有更高优先级，并可更细致地控制聚合路由属性和明细发布。
709|BGP|bgp|通过 import-route 重分发注入的 BGP 路由，其 Origin 通常为 Incomplete；network 注入的通常为 IGP。
710|BGP|bgp|BGP 使用 TCP 179 建立可靠的对等体会话，UDP 并非其邻居传输协议。
711|无线网络|acpriority|双链路热备的 AC 选举中优先级数值越小越优先，不要与无线报文的 QoS 优先级混淆。
712|接入认证|portal|MAC 优先的 Portal 认证会缓存成功用户的 MAC 认证关系，在缓存有效期内再次接入可免于重复 Portal 登录。
713|OSPF|ospf|ASBR 的条件是引入 AS 外部路由，它可位于支持外部路由的非骨干区域，并不必须在区域 0。
714|OSPF|nssa|NSSA 不接收外部 4、5 类 LSA，本地外部路由使用 7 类 LSA；原句“会将 LSA 泛洪给其他区域”丢失了关键类别。
715|IPv6|icmp6|ICMPv6 类型值小于 128 表示差错报文，128 及以上表示信息报文，例如回显请求和邻居发现消息。
716|IPv6|dad|SLAAC 的第一步即可自动构造链路本地地址，并通过 DAD 检查重复；不必等路由器分配一个全局前缀。
717|组播|pim|SPT 以组播源为根，使接收者沿最短路径接收流量；RPT 则以汇聚点 RP 为根。
718|BGP|bgprouterid|显式在 BGP 进程配置 Router ID 时采用该值，未配置才使用系统路由管理选择的标识。
719|BGP|bgp|收到 OPEN 后将本地与对端的 Hold Time 取较小值；0 表示不使用 Hold/Keepalive 定时机制。
720|BGP|bgprefresh|支持动态策略更新的华为 VRP 可在出方向策略改变后重新计算并发送更新，无需一概要求手工重置邻居。
721|OSPF|ospf|DR/BDR 选举还取决于接口优先级；所有接口优先级为 0 时不会选出 DR，因此不是只由设备数量决定。
722|OSPF|bandwidthref|bandwidth-reference 设置 OSPF 计算接口 cost 的参考带宽，华为命令的单位为 Mbit/s。
723|OSPF|ospfcost|默认 cost 通常按参考带宽除以接口带宽计算；也可使用 ospf cost 手工配置，不是只能自动计算。
724|路由基础|recursion|递归路由的下一跳可为非直连地址，设备继续查路由解析其实际可达出口，因此不一定同网段。
725|BGP|bgpselect|LOCAL_PREF 越大越优先，用于 AS 内部选择向外发送流量的出口。
726|网络虚拟化|evpn|EVPN 可携带 MAC/IP 与 IP 前缀路由，既支持二层延伸，也支持三层互联，并非仅能提供二层 VPN。
727|BGP|connectinterface|使用 Loopback 等稳定地址建立一对逻辑 BGP 对等体时，应通过 connect-interface 指定源接口，避免各物理链路使用不同源地址。
728|OSPF|ospf|广播/NBMA 网络中 DROther 通常只与 DR/BDR 建立 Full 邻接，DROther 之间维持 2-Way，以减少数据库同步数量。
729|无线网络|nativeac|随板 AC 把无线控制功能集成在支持的交换机中，可统一承载有线交换和无线接入管理。
730|网关冗余|vrrp|新 Master 会发送免费 ARP，帮助主机更新 ARP 缓存并使交换机学习虚拟 MAC 的位置，促进流量切换。
731|路由策略|policycmd|route-policy 按节点匹配路由并可修改 BGP 属性；未命中任何节点的路由默认不通过该策略。
732|组播|pim|RPF 检查报文是否从到源或 RP 的正确上游接口到达，错误接口的报文被丢弃，从而防止重复转发和环路。
733|生成树|stp|RSTP 使用 BPDU Type=2 的 RST BPDU，拓扑变化由其中的 TC 标志承载，不再单独使用 TCN BPDU。
734|BGP|bgp|会话建立时先交换可发布的初始路由，之后主要通过增量 UPDATE 通告新增、变化或撤销的路由。
735|OSPF|ospfauth|接口认证配置优先于区域认证，允许接口覆盖所在区域的默认认证方式。
736|OSPF|ospf|DR Priority=0 表示不参与 DR/BDR 选举，并不是以最低候选优先级参与。
737|OSPF|ospf|区域内 SPF 主要使用 1 类 Router LSA 和 2 类 Network LSA；3 类 Summary LSA 描述区域间网络，不参与本区域拓扑建树。
738|生成树|stp|MSTP 在域内为每个 MSTI 分别计算生成树，把不同 VLAN 映射到不同实例后可实现链路负载分担。
739|BGP|bgpa|自动聚合需要显式配置 summary automatic；默认不对引入路由进行自动聚合。
740|BGP|bgph|BGP 可通过 network 精确注入已有路由，也可通过 import-route 引入其他协议或直连、静态路由。
741|网络安全|stateful|状态防火墙首先按策略处理新流，允许后创建会话；后续匹配会话的报文可按状态和会话信息快速处理。
742|路由策略|policy|PBR 直接依据报文条件选择转发路径，作用于转发平面；路由策略过滤或修改路由信息，作用于控制平面。
743|OSPF|ospfh|同一设备的多个 OSPF 进程分别维护邻居和 LSDB；需要通过路由引入才能在独立进程间交换路由。
744|OSPF|ospf|OSPF 区域间路由经骨干区域传递，ABR 必须在逻辑上连接骨干；必要时可通过虚链路满足该连接要求。
745|无线网络|hsb|HSB 使用心跳检测主备备份通道状态；业务备份报文的重传不等于专门的通道保活检测。
746|故障检测|bfd|快速检测可缩短故障发现时间并触发倒换，但不能单独保证业务绝不中断；原句“不/部中断”存在歧义。
747|组播|multicastroute|组播路由表提供协议状态，实际报文由组播转发表指导；不同资料中的 (*,G) 路由/转发表用语不同，题干缺少表类型定义。
748|路由基础|preference|同一目的前缀来自不同协议时，路由优先级决定更可信的来源；华为数值越小越优先。
749|OSPF|ospf|OSPFv2 不只有 MD5，标准还定义空认证和简单口令认证，后续标准也扩展了密码学认证方式。
750|生成树|stpp|普通边缘端口收到 BPDU 后变为非边缘端口；只有启用相应 BPDU 保护等功能时才进入 error-down。
751|网关冗余|vrrp|VRRP 虚拟路由器可包含一个或多个虚拟 IP，并有虚拟 MAC；原题“只能拥有虚拟IP地址”缺少数量或排他范围。
752|无线网络|hsb|HSB 备份需要主备配置与运行状态一致；原句“主AC首先之后”损坏，且所述操作依产品版本，无法可靠复原流程。
753|组播|igmp|IGMP 在 IPv4 主机与直连组播路由器之间报告和查询成员关系，帮助路由器判断哪些网段需要组播流。
754|网络安全|ssh|AES、DES 属于对称加密算法，非对称算法用于密钥交换或身份验证；SSH 的消息认证机制用于检验完整性。
755|服务质量|traffic|traffic-filter 可直接调用 ACL 过滤，MQC 将分类与行为绑定成流策略，并能在设备支持的更多视图应用。
756|网络安全|ddos|DDoS 由分布式来源共同耗尽目标带宽、连接表或处理资源，使正常用户无法获得服务。
757|网关冗余|vrrppreempt|华为 AR 的普通 VRRP 缺省启用抢占：更高优先级设备恢复后可按抢占配置接替 Master。
758|OSPF|ospf3id|华为 OSPFv3 需要配置 32 位 Router ID，不能直接从 128 位 IPv6 接口地址自动生成该标识。
759|IS-IS|isis|Level-1 邻接只在相同区域内形成；跨区域连通使用 Level-2 邻接和 Level-1-2 路由器。
760|路由基础|recursion|转发表 FIB 指导的是数据报文转发，“数据库”与网络转发对象不符，无法判断原题是否把“数据包”误识别为此词。
761|无线网络|dualac|双链路热备时 AP 同时与主、备 AC 建立 CAPWAP 连接，使主 AC 失效后可快速切换控制器。
762|BGP|bgpprocess|华为 VRP 的普通 BGP 配置只允许一个 BGP 进程，VPN 等隔离由该进程内的实例/地址族处理；不能推广到所有厂商实现。
763|访问控制|acl|ACL 定义匹配规则，但必须被流量过滤、路由过滤等业务调用，具体匹配结果才会产生业务效果。
764|BGP|bgpselect|在满足 MED 比较条件时，较小的 MED 更优，用于表达进入某个 AS 的较优入口。
765|=740
766|=694
767|=743
768|OSPF|ospf|DR/BDR 同时监听 AllSPFRouters 的 224.0.0.5 和 AllDRouters 的 224.0.0.6。
769|=615
770|=564
771|BGP|bgprefresh|支持 Route Refresh 时，VRP 的入方向策略变化可自动请求对端重发路由以重新过滤；需对端具备相应能力。
772|=724
773|=537
774|OSPF|nssa|NSSA 不接收用于描述外部 ASBR 的 4 类 LSA；本地外部路由通过 7 类 LSA 表达，并由 ABR 转换为 5 类发布到其他区域。
775|OSPF|ospf|Stub 及 Totally Stub 都不允许 5 类 AS External LSA，使用 ABR 注入的默认路由访问外部网络。
776|BGP|bgp|BGP 可通过 OPEN/NOTIFICATION 反复尝试版本，双方有共同版本时选择最高共同支持版本。
777|=725
778|BGP|bgp|Active 状态的 TCP 失败会按重试事件回到 Active/Connect 等状态继续尝试；不是所有失败都无条件回 Idle。
779|路由策略|policy|route-policy 可同时过滤和设置属性，但部分协议的引入命令也可直接设置 cost、type 等并配合其他过滤工具，“只能”过于绝对。
780|故障检测|bfd|BFD 状态机通过 Down、Init、Up 的状态交互确认两端状态，建立与拆除都采用三步确认机制，区别于 TCP 握手。
781|=711
782|BGP|filterpolicy|华为 BGP 的 filter-policy 可在地址族范围统一应用，也可针对特定 peer 或 peer-group 应用，控制收发路由。
783|=600
784|故障检测|bfddiscriminator|静态 BFD 会话的标识符不能简单被新值直接覆盖；通常需要撤销原会话或相应绑定后重新配置。
785|OSPF|ospf|广播或 NBMA 网络的两个 DROther 通常保持 2-Way；它们各自与 DR/BDR 建立 Full 邻接。
786|服务质量|traffic|流策略可在受支持接口的入方向或出方向应用，具体行为有方向限制，并非只能在出口调用。
787|IS-IS|isis|缺省 Level-1 路由器经 ATT 信息生成指向 Level-1-2 的默认路由；Level-2 明细进入 Level-1 需要配置路由渗透。
788|网关冗余|vrrp|Master 对虚拟 IP 的 ARP 请求返回虚拟 MAC，而非接口物理 MAC，使切换 Master 后网关 MAC 保持稳定。
789|网络虚拟化|vrfinterface|接口绑定 VPN/VRF 与子接口能力取决于具体设备和绑定层级；缺少型号与配置条件，不能断言所有物理接口都不能再划分。
790|网络管理|cloudcampus|CloudCampus 业务随行基于用户或安全组统一控制策略，支持用户在不同接入位置获得一致的权限。
791|生成树|stp|RSTP 把非边缘端口迁移到 Forwarding 视为拓扑变化，并通过带 TC 标志的 BPDU 通知其他桥更新 MAC 学习信息。
792|路由策略|policycmd|route-policy 按节点号顺序检查，匹配一个节点后即停止，因此不同节点是“或”；单节点内不同属性的条件通常为“与”。
'''

reviews={}
for line in data.strip().splitlines():
    fields=line.split('|')
    i=int(fields[0])
    if fields[1].startswith('='):
        reviews[i]=dict(reviews[int(fields[1][1:])],id=i)
    else:
        reviews[i]={'id':i,'topic':fields[1],'source_keys':fields[2].split(','),'explanation':fields[3]}

sources.update(json.loads((ROOT/'sources_c.json').read_text(encoding='utf-8')))
aliases={'staticmac':'mac','authorization':'aaa','ospfcost':'bandwidthref','ospffilter':'ospfh','ospfauth':'ospfh','nssa':'ospfh','asbrsummary':'ospfh','vlandesign':'vlan','staticroute':'preference'}
for key,target in aliases.items():
    sources[key]=sources[target]
sources['vrp_dir']=sources['dir']
sources['vrp_mkdir']='https://info.support.huawei.com/hedex/api/pages/EDOC1100331440/AZM10131/04/resources/dc/mkdir_user_view.html'
sources['vrrppreempt']='https://www.rfc-editor.org/rfc/rfc5798'
sources['stscan']='https://info.support.huawei.com/hedex/api/pages/EDOC1100210440/AZK0901G/09/resources/dc/dc_fd_wlan_basic_0008.html'
sources['bfddiscriminator']='https://info.support.huawei.com/enterprise/en/doc/EDOC1100325913/e72e182d/bfd-configuration-commands'
sources['bfddiscriminator2']='https://support.huawei.com/enterprise/en/doc/EDOC1100306155/81d122bb/bfd-configuration-commands'
sources['firewall']='https://info.support.huawei.com/hedex/api/pages/EDOC1100149311/AZJ0713J/17/resources/admin/sec_admin_hotstandby_0062.html'

excluded={
532:'未限定 HTTP 版本；HTTP/3 使用 UDP，原题把所有 Web 访问概括为 TCP。',
555:'未限定路由实例；不同 VPN 实例可使用重复 IP，原答案无法通用。',
567:'对 SDN 起源和本质的判断缺少明确可验证定义。',
574:'未限定端口模式，普通 VLAN 接收处理与特殊端口模式不能一概而论。',
577:'未提供采用的 SDN 分层架构，OpenStack 组件范围也未限定。',
580:'Python 3.13 已移除 telnetlib，题目缺少 Python 版本。',
584:'题干在“根路径开销一定是”之后截断，缺少被判断的数值。',
592:'题干网段为 168.1.0/25，不是完整 IPv4 地址，无法确认缺失部分。',
593:'题干开头“他、”损坏且原答案与常规 VLAN 模型冲突，无法确认原命题。',
596:'默认启用协议版本与“支持协议版本”混淆，未注明 VRP 软件版本。',
623:'命令 max-vty 名称损坏，无法确认是否是合法缩写；与完整 maximum-vty 题重复语义。',
631:'wpai-psk 安全策略名称损坏，无法确认是 WPA、WPA2 或其他原文。',
645:'Router ID 变更后是否自动重启并生效存在 VRP 版本差异，题目未限定。',
649:'未说明 AP 是 Fat 还是 Fit，不同模式答案相反。',
655:'未限定 cost 比较是否在同一协议内，不同协议 cost 不可直接通用比较。',
665:'“以特殊化的方式”破坏 NFV 关键定义，无法确认原文。',
666:'VRRP 认证机制随 v2/v3 和设备实现变化，题目没有版本条件。',
671:'根桥所有端口都是指定端口的强断言未排除共享网段冗余端口和关闭端口。',
691:'“上电之后加入”不能区分断电连接后上电加入与已运行系统的合并。',
700:'“上行/下行接口板”未定义，忽略同板转发与具体硬件架构条件。',
701:'当前官方资料只证实云管 NETCONF 与传统 SNMP，未直接确认本题第三方设备管理范围。',
703:'“接入设备”上下游指代不明确，官方将 Proxy 的上游也称接入设备，原答案无法可靠判断。',
711:'未取得直接支持该数值比较规则的官方正文，暂不凭原答案保留。',
714:'“会将 LSA 泛洪给其他区域”缺少 LSA 类别，无法恢复关键判断条件。',
718:'未取得直接说明这两个视图的 Router ID 优先关系的官方正文。',
720:'未限定 VRP 版本，未直接核实默认出方向策略更新是否自动发送。',
727:'只说明多物理链路而未限定使用 Loopback 连接，必须使用某命令的条件不充分。',
746:'“业务部中断”文字损坏；快速检测本身不能保证业务绝不中断。',
747:'未明确协议路由表或硬件转发表；官方资料中“指导”措辞不统一。',
751:'“只能拥有虚拟IP地址”缺少数量或排他范围，题意不完整。',
752:'“主AC首先之后”损坏，且准确重启备份流程缺少型号版本依据。',
758:'未取得直接说明华为 OSPFv3 自动选取规则的对应版本文档，不泛用 OSPFv2 规则。',
760:'“数据库的转发”与网络报文对象不符，修为数据包会改变判断答案，故不猜修复。',
762:'只写路由器而未限定厂商/平台，多个 BGP 进程支持能力并非通用协议限制。',
771:'未限定 VRP 版本及对端 Route Refresh 能力，默认自动刷新的强断言未直接证实。',
781:'同 711，缺少直接官方依据核实数值比较规则。',
784:'S7700 文档不允许直接修改，而 S310 文档允许，题目缺少设备型号和版本。',
789:'VRF 绑定与子接口限制依设备平台及绑定层级，缺少必要条件。',
790:'官方材料支持业务随行，但本题图形化配置与具体接入能力范围未直接核实。',
619:'“无线定义”关键功能名称损坏，无法明确判断原文对应的接入功能。',
785:'“在A网络中”缺失网络类型，不能自行猜补为广播或 NBMA 网络。',
}

corrections={529:'A',550:'A',556:'B',636:'B',653:'A',663:'A',677:'B',716:'A',717:'A',745:'A',776:'A',786:'B',787:'B',791:'A'}
stem_fixes={
529:'IEEE 802.11ac 标准只支持 5 GHz 频段。',
539:'telnetlib 中 Telnet.read_very_eager() 的作用是非阻塞地读取可用数据，通常需要和 time 模块一起使用。',
541:'IPv6 地址 2001:ABEF:224E:FFE2:BCC0:CD00:DDBE:8D58 不能简写。',
547:'SNMPv1 定义了 5 种协议操作。',548:'SNMPv1 定义了 5 种协议操作。',
550:'telnetlib 中 Telnet.read_all() 的作用是读取所有数据直到 EOF；如果连接没有到达 EOF，则会一直阻塞。',
552:'VRP 界面下，使用 startup saved-configuration backup.cfg 配置下次启动时使用 backup.cfg 文件。',
556:'主机使用 IP 地址 192.168.1.2 访问 Internet 一定要经过 NAT。',
559:'2.4 GHz 频段中的 14 个可用信道不存在信道重叠。',
579:'广播地址是网络地址中主机位全部置为 1 的一种特殊地址，它也可以作为主机地址使用。',
582:'RSTP 中 Alternate 端口和 Backup 端口均无法转发用户流量，也不可以接收、处理、发送 BPDU。',
583:'config 模式是华为设备上缺省的 ACL 匹配顺序。',
586:'user-interface maximum-vty 命令可以配置允许同时通过 Telnet 登录设备的 VTY 用户界面数量。',
590:'IPv6 协议使用 NS 和 NA 报文进行重复地址检测（DAD）。',
595:'缺省情况下，传统 STP 协议中的端口由 Disabled 转换为 Forwarding 状态至少需要 30 秒。',
598:'::1/128 是 IPv6 环回地址。',
619:'Fat AP 无需 AC 即可独立完成无线接入、无线认证和业务数据转发等工作。',
620:'园区可以通过链路聚合和堆叠提高网络可靠性。',
630:'telnetlib 中 Telnet.read_very_eager() 的作用是非阻塞地读取可用数据，通常需要和 time 模块一起使用。',
634:'广播地址是网络地址中主机位全部置为 1 的一种特殊地址，它也可以作为主机地址使用。',
638:'config 模式是华为设备上缺省的 ACL 匹配顺序。',
651:'MPLS 标签头封装在报文的数据链路层头部和网络层头部之间。',
668:'带宽决定数据传输的速率，而且传输路径的最大带宽由路径上的最小链路带宽决定。',
676:'路由协议通过 Hello 报文可以检测到故障，所以不需要 BFD。',
683:'当两个路由器通过 DD 报文交换数据库信息时，首先形成一个主从关系，Router ID 大的一定为主。',
693:'MQC 与 PBR 一样，只能在设备的三层接口下调用。',
694:'import-route limit 命令不能限制一个 OSPF 进程内可以引入的最大外部路由数量。',
695:'OSPF Stub 区域的 ABR 不向 Stub 区域泛洪 5 类和 4 类 LSA，而向 Stub 区域通告一条 3 类默认 LSA，指导数据包到达 AS 外部目的地。',
697:'运行 IS-IS 的两台路由器，只有 IIH 发送时间间隔相同才可以建立邻接关系。',
699:'在 OSPF 广播或者 NBMA 网络类型中，DR Priority 大的设备不一定会成为 DR。',
705:'IGMPv3 不仅支持 IGMPv1 的普遍组查询和 IGMPv2 的特定组查询，还支持指定源/组查询。',
713:'OSPF 的 AS 边界路由器可以是内部路由器，也可以是 ABR，但是必须属于骨干区域。',
728:'在广播或 NBMA 网络中，并非所有邻居之间都会建立邻接关系。',
730:'在 VRRP 中，设备成为 Master 后会立即发送免费 ARP，刷新下游设备的 ARP/MAC 表项，把用户流量引到该设备。',
731:'路由策略工具 route-policy 能够基于预定义条件过滤路由并设置 BGP 属性，常用于 BGP Peer 策略及路由生成时期；缺省情况下未匹配的路由被拒绝通过 route-policy。',
733:'不同于 STP，RSTP 的 BPDU Type 只有一种，其值为 2，没有 TCN BPDU。',
742:'策略路由和路由策略都能影响数据包转发，但方式不同：策略路由基于转发平面，路由策略基于控制平面，为路由协议和路由表服务。',
743:'OSPF 支持多进程，同一台路由器上可以运行多个独立的 OSPF 进程；不同进程之间的路由交互相当于不同路由协议之间的路由交互。',
744:'为了避免区域间环路，OSPF 不允许直接在两个非骨干区域之间发布区域间路由，区域间路由必须经过骨干区域，因此 ABR 必须连接到骨干区域。',
745:'可以通过发送 HSB 主备服务报文和重传等机制，防止主备 AC 间的 HSB 备份通道中断且无法感知的情况。',
750:'RSTP 边缘端口无需等待 Forward Delay，可直接进入 Forwarding；如果收到 BPDU，则边缘端口会被直接关闭并进入 error-down 状态。',
754:'SSH 使用非对称加密算法 AES、DES 实现数据传输安全，使用 HMAC 保证数据完整性。',
755:'实现流量过滤可以使用 traffic-filter，也可以使用 MQC；相比 traffic-filter，MQC 可在更多视图内调用。',
766:'import-route limit 命令不能限制一个 OSPF 进程内可以引入的最大外部路由数量。',
767:'OSPF 支持多进程，同一台路由器上可以运行多个独立的 OSPF 进程；不同进程之间的路由交互相当于不同路由协议之间的路由交互。',
777:'LOCAL_PREF 属性用于判断流量离开 AS 的最佳路由；通过不同 IBGP 对等体得到目的地址相同但下一跳不同的路由时，优先选择 LOCAL_PREF 较高的路由。',
779:'一种路由协议引入其他路由协议时，若只引入满足条件的部分路由并设置其属性，则只能使用 route-policy 工具。',
782:'在 BGP 中，Filter-Policy 可在 BGP 下全局部署，也可针对对等体部署。',
785:'在广播网络中，两台 DROther 不建立邻接关系，它们的状态维持在 2-Way。',
791:'非边缘端口迁移到 Forwarding 状态是 RSTP 检测拓扑变化的标准之一。',
792:'一个 route-policy 下可以有多个节点，不同节点用节点号标识，节点之间是“或”的关系。',
}

# 覆盖几处审核中发现的版本差异及官方正文中的细节。
reviews[745]['explanation']='HSB 服务定期发送并重传服务报文；超过重传间隔与次数仍未收到对端报文时，上报异常并重建通道。'
reviews[784]['explanation']='旧版 S7700 静态会话要求删除后重建标识符，新版 S310 可直接修改；缺少平台信息时不能统一判分。'
reviews[784]['source_keys']=['bfddiscriminator','bfddiscriminator2']
reviews[703]['explanation']='IGMP Proxy 汇聚下游成员信息并向上游报告；华为资料把该上游也称“接入设备”，原题上下游指代不明确。'
reviews[645]['explanation']='Router ID 变更需要进程采用新标识；部分 VRP 版本会自动重启进程，另一些配置需手工重启，不能跨版本统一判断。'
reviews[539]['explanation']='read_very_eager() 通常读取当前可用数据而不等待新数据；处理 IAC 序列时可能短暂阻塞，发送命令后可按需要先等待回显。'
reviews[630]['explanation']=reviews[539]['explanation']
for i in (530,639): reviews[i]['source_keys']=['stscan']
reviews[568]['source_keys']=['vrp','vrp_dir']
reviews[642]['source_keys']=['vrp_mkdir']
reviews[679]['source_keys']=['authorization']
reviews[757]['explanation']='VRRP 标准的抢占默认开启；更高优先级设备恢复后，可按抢占延时配置接替 Master。'
reviews[675]['source_keys']=['mirror']
reviews[652]['explanation']='常用 SNMP 使用 UDP，管理请求一般发往 UDP 161，Trap/Inform 通知一般发往 UDP 162。'
reviews[553]['explanation']='OSPF 在 Exchange、Loading 阶段同步 LSDB，数据库同步完成后才进入 Full，题干把先后顺序颠倒了。'
# 保留原题条件，只修明显字词；不通过改写设备视图或加入新条件配答案。
stem_fixes.pop(586,None)
stem_fixes[695]='OSPF Stub 区域的 ABR 不向 Stub 区域泛洪第五类和第四类 LSA，向 Stub 区域通告一条默认 LSA，指导数据包到达 AS 外部目的地。'
stem_fixes[730]='在 VRRP 中，当设备状态变为 Master 后，会立即发送免费 ARP，刷新下游设备的 MAC 表项，从而把用户流量引到此设备。'

questions=json.loads((ROOT/'questions_c.json').read_text(encoding='utf-8-sig'))
assert set(reviews)==set(q['id'] for q in questions)
result=[]
for q in questions:
    i=q['id']; r=reviews[i]
    r['status']='exclude' if i in excluded else 'keep'
    r['reason']=excluded.get(i,'')
    r['corrected_answer']=corrections.get(i) if i not in excluded else None
    r['corrected_stem']=stem_fixes.get(i) if i not in excluded else None
    r['corrected_options']=None
    r['sources']=list(dict.fromkeys(sources[k] for k in r.pop('source_keys') if k in sources))
    if r['status']=='keep':
        assert r['sources'], (i,'未提供来源')
    result.append(r)
(ROOT/'review_c.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'total':len(result),'keep':sum(r['status']=='keep' for r in result),'exclude':sum(r['status']=='exclude' for r in result),'corrected_answers':{r['id']:r['corrected_answer'] for r in result if r['corrected_answer']},'stem_fixes':sum(r['corrected_stem'] is not None for r in result)},ensure_ascii=False))

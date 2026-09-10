# ICT 网络赛道题库 · 生成与剔除报告

- 源文件：资料库/ICT网络赛道知识题库(1).docx
- 原文档题目总数：792（编号 1–792，连续）
- 保留入库：644 题（单选 227 / 判断 236 / 多选 181）
- 剔除：148 题

## 剔除原因统计

| 代码 | 含义 | 命中题数 | 题号 |
| --- | --- | --- | --- |
| H1 | 题干依赖配图，原 docx 不含图片，无法作答 | 9 | 4, 6, 9, 12, 17, 157, 199, 200, 498 |
| H1b | 题干引用了仅存在于原图中的配置/输出内容，无法作答 | 2 | 204, 354 |
| H2 | 无有效答案 / 选项不足 2 项 / 答案字母不存在 | 6 | 241, 242, 243, 244, 245, 246 |
| H3 | 选项标记丢失，选项内容互相串行 | 1 | 503 |
| H4 | 两个选项内容完全相同 | 4 | 62, 167, 197, 344 |
| H6 | 与另一题题干完全重复（保留质量更好的一道） | 46 | 131, 139, 224, 226, 237, 250, 251, 254, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 344, 362, 370, 373, 402, 431, 486, 513, 515, 519, 548, 575, 617, 646, 671, 672, 673, 769 |
| S1 | 含已核对的缺损术语/错字（转换损坏） | 96 | 10, 17, 24, 64, 65, 84, 86, 114, 115, 117, 129, 133, 139, 149, 164, 175, 177, 180, 186, 197, 214, 224, 227, 229, 232, 233, 236, 237, 253, 267, 269, 277, 278, 280, 288, 300, 301, 303, 306, 311, 314, 318, 320, 321, 323, 326, 331, 334, 338, 341, 343, 345, 346, 349, 363, 392, 400, 423, 433, 448, 457, 465, 466, 484, 498, 499, 503, 504, 509, 541, 547, 548, 550, 552, 556, 582, 595, 596, 611, 631, 651, 655, 693, 694, 699, 713, 720, 750, 755, 766, 768, 771, 777, 782, 790, 791 |

> 一道题可能同时命中多条原因，故各原因题数之和大于剔除题数。

## 数据处理说明

1. 多选题的 `answer` 为下标数组（如 `[1,2,3]`），单选/判断题为单个数字下标。
2. 源文档没有解析，故入库题目的 `explanation` 统一为空字符串，App 中会显示"（本题未提供解析）"。
3. 转换造成的断行已自动拼接（如 `访问inte` + `et的必要技术是` → `访问inteet的必要技术是`）。
4. **已知局限**：源文档是低质量转换产物，除上表已检出的模式外，中文层面的缺字（如"为了免区域间"缺"避"）无法可靠自动检出，本报告不声称已完全清除文字问题。

## 被剔除题目明细（可据此回填或修正后重新导入）

### 原第 4 题

- 剔除原因：**H1** 题干依赖配图，而原 docx 不含任何图片
- 原答案：A
- 题干：如图所示的网络,主机A没有配置网关,主机B存在网关的ARP缓存,在主机A 使用命令ping 11.0.12.1,下列说法正确的是
  - A．不会有任何数据包从主机A出
  - B．主机A发出的数据帧的目的MAC地址是MAC-c
  - C．主机A 发出的数据帧的目的MAC地址是MAC-B
  - D．主机A发出的数据包的目的IP地址为11.0.12.1

### 原第 6 题

- 剔除原因：**H1** 题干依赖配图，而原 docx 不含任何图片
- 原答案：C
- 题干：关于如图所示信息描述正确的是:
  - A．G 0/0/0接口没有配置IP地址
  - B．G 0/0/0接口连接了一条错误的线缆
  - C．G 0/0/0接口被管理员手动关闭了
  - D．G 0/0/0接口没有启用动志路由协议

### 原第 9 题

- 剔除原因：**H1** 题干依赖配图，而原 docx 不含任何图片
- 原答案：B
- 题干：如图所示的网络,所有路由器运行ospf协议,链路开销值如图,则RTA路由表中达到网络10.0.0.0/8的路由条目的从上图值是多少
  - A．70
  - B．60
  - C．20
  - D．100

### 原第 10 题

- 剔除原因：**S1** 含缺损术语：\bleaing\b(Learning 错字)
- 原答案：A
- 题干：RSTP协议不包含以下哪个端口状态
  - A．Blocking
  - B．Leaing
  - C．Discarding
  - D．Forwarding

### 原第 12 题

- 剔除原因：**H1** 题干依赖配图，而原 docx 不含任何图片
- 原答案：B
- 题干：如图所示,假设SWA刚刚启动,MAC地址表为空,现在主机A发送一个目的MAC地址为MAC-B的数据帧,下列说法正确的是:
  - A．SWA将数据帧丢弃
  - B．将这个数据帧泛洪出去
  - C．将这个数据帧只从g0/0/3端口转发出去
  - D．将这个数据帧只从g0/0/2端口转发出去

### 原第 17 题

- 剔除原因：**H1** 题干依赖配图，而原 docx 不含任何图片；**S1** 含缺损术语：\bhitp\b(HTTP 错字)
- 原答案：A
- 题干：如图所示,私有网络中有一台web服务器需要向公网用户提供HITP服务,因此网络管理员需要在网关路由器RTA上配置NAT以实现需求,现下面配置中满足要求的是
  - A．A
  - B．B
  - C．C
  - D．D

### 原第 24 题

- 剔除原因：**S1** 含缺损术语：\bguration\b(configuration 缺字)
- 原答案：C
- 题干：现需要实现一个python自动化脚本Telnet到设备上查看设备运行配置。以下说法错误的是
  - A．可以使用telnet.write(b“display current-confi guration \n”)向设备输入查看当前配置的命令
  - B．使用telnet。Telnet(host)连接到Telnet服务器
  - C．telnet.close()用在每一次输入命令后,作用是用户等待交换机回显信息
  - D．Telnetlib 可以实现这个功能

### 原第 62 题

- 剔除原因：**H4** 选项 C 与 D 内容完全相同
- 原答案：C
- 题干：网络管理员希望能够有效利用192.168.176.0/25网段的IP地址。现公司市场部门有20个主机,则最好分配下面哪一个地址段给市场部
  - A．192.168.176.160/27
  - B．192.168.176.0/25
  - C．192.168.176.96/27
  - D．192.168.176.96/27

### 原第 64 题

- 剔除原因：**S1** 含缺损术语：\bleaing\b(Learning 错字)
- 原答案：D
- 题干：RSTP协议不包括以下哪个端口状态
  - A．Forwarding
  - B．Leaing
  - C．Discarding
  - D．Blocking

### 原第 65 题

- 剔除原因：**S1** 含缺损术语：\bblanif\d*\b(vlanif 错字)、\bbriaf\b(brief 错字)
- 原答案：B
- 题干：网络管理员在三层交换机上创建了vlan,并在该vlan的虚拟接口下配置了IP地址,当使用命令“display ip interface briaf”查看接口状态时,发现vlanif10 接口处于down状态,则应该通过怎样的操作来使用v拉你发10 接口恢复正常
  - A．在BLANIF10 接口下使用命令“undo shutdown”
  - B．将一个状态必为UP的物理接口划进vlan10
  - C．将任意物理接口划进vlan10
  - D．将一个状态必须为Up并且必须为trunk类型的接口划进vlan10

### 原第 84 题

- 剔除原因：**S1** 含缺损术语：\blant\b(NAT 错字)
- 原答案：D
- 题干：一个公司有50 个私有ip地址,管理员使用nat技术将公司网络接入公网,但是该公司仅有一个公网地址且不固定,则下列哪种lant转换方式符合需求
  - A．NAPT
  - B．Basic NAT
  - C．静态NAT
  - D．easy-ip

### 原第 86 题

- 剔除原因：**S1** 含缺损术语：\binteet\b(Internet 缺字)
- 原答案：C
- 题干：下面选项中,能使一台ip地址为10.0.0.1的主机访问inteet的必要技术是
  - A．静态路由
  - B．动态路由
  - C．NAT
  - D．路由引入

### 原第 114 题

- 剔除原因：**S1** 含缺损术语：\bupd\b(UDP 错字)
- 原答案：B
- 题干：UPD是面向无连接的,必须依靠什么协议来保养传输的可靠性
  - A．传输控制协议
  - B．应用层协议
  - C．网络层协议
  - D．网际协议

### 原第 115 题

- 剔除原因：**S1** 含缺损术语：Versatile Redundancy(VRRP 全称错字)
- 原答案：D
- 题干：通用路由平台VRP的全称为
  - A．Versatile Redundancy Platform
  - B．Versatile Routing Protocol
  - C．Virtual Routing Platform
  - D．Versatile Routing Platform

### 原第 117 题

- 剔除原因：**S1** 含缺损术语：\betheet\b(Ethernet 错字)
- 原答案：B
- 题干：关于ARP协议的作用和报文封装,描述正确的是
  - A．ARP协议支持在PPP链路与HDLC链路上部署
  - B．ARP协议基于Etheet封装
  - C．通过ARP协议可以获取目的端的MAC地址和UUID的地址
  - D．网络设备上的ARP缓存只可以通过ARP协议得到

### 原第 129 题

- 剔除原因：**S1** 含缺损术语：\binteet\b(Internet 缺字)
- 原答案：B
- 题干：主机使用以下哪个IPV4地址不能直接访问Inteet
  - A．50.1.1.1
  - B．10.1.1.1
  - C．100.1.1.1
  - D．200.1.1.1

### 原第 131 题

- 剔除原因：**H6** 与第 15 题题干重复（保留第 15 题）
- 原答案：B
- 题干：RSTP协议存在几种端口状态
  - A．1
  - B．3
  - C．4
  - D．2

### 原第 133 题

- 剔除原因：**S1** 含缺损术语：\bdsiabled\b(disabled 错字)
- 原答案：C
- 题干：下列关于STP协议F肉ward Delay的作用说法正确的是
  - A．提高STP的收敛速度
  - B．提升BPDU的生存时间,保证配置BPDU可以转发到更多的交换机
  - C．在Blocking状态和Dsiabled状态转化时需要延时
  - D．减少BPDU发送时间间隔

### 原第 139 题

- 剔除原因：**S1** 含缺损术语：\bfrowarding\b(Forwarding 错字)、\bleaing\b(Learning 错字)；**H6** 与第 10 题题干重复（保留第 10 题）
- 原答案：C
- 题干：RSTP协议不包含以下哪个端口状态
  - A．Leaing
  - B．Frowarding
  - C．Blocking
  - D．Discarding

### 原第 149 题

- 剔除原因：**S1** 含缺损术语：\bparamater\b(parameter 错字)
- 原答案：A
- 题干：VRP操作平台对于输入命令不完整使用下列哪一条信息提示
  - A．Error:Incomplete command found at ‘^’ position
  - B．Error:Wrong paramater found at ‘^’ position
  - C．Error:Ambiguous command found at ‘^’ position
  - D．Error:Too many parameters found at ‘^’ position

### 原第 157 题

- 剔除原因：**H1** 题干依赖配图，而原 docx 不含任何图片
- 原答案：C
- 题干：如下图所示的网络,主机A通过telnet登录到路由器A,然后在远程的界面通过FTP获取路由器B的配置文件,此时路由器A存在多少个TCP连接
  - A．4
  - B．1
  - C．3
  - D．2

### 原第 164 题

- 剔除原因：**S1** 含缺损术语：\bcountry-conde\b(country-code 错字)、\bnation-conde\b(nation-code 错字)、\bprovince-conde\b(province-code 错字)、\bstate-conde\b(state-code 错字)
- 原答案：B
- 题干：AC配置国家码的命令是
  - A．province-conde
  - B．country-conde
  - C．state-conde
  - D．nation-conde

### 原第 167 题

- 剔除原因：**H4** 选项 B 与 C 内容完全相同
- 原答案：B
- 题干：主机ipv4地址为200.200.200.200/30,拥有下列ipv4地址的主机和其通信不需要经过路由器转发
  - A．200.200.200.203
  - B．200.200.200.1
  - C．200.200.200.1、
  - D．200.200.200.200

### 原第 175 题

- 剔除原因：**S1** 含缺损术语：\bfroward\b(Forward 错字)
- 原答案：E
- 题干：RSTP协议使用P/A机制加快了上游端口转到Forwarding状态的速度,但是却没有出现临时环路的原因是什么
  - A．缩短了Forward Delay的时间
  - B．缩短了Froward Delay的时间
  - C．引入了边缘端口
  - D．加快了端口角色选举的速度
  - E．通过同步机制保证不会出现临时环路

### 原第 177 题

- 剔除原因：**S1** 含缺损术语：\bfrowarding\b(Forwarding 错字)、\balteate\b(alternate 错字)
- 原答案：B
- 题干：RSTP协议中。当根端口失效的情况下,()就会快速转换为新的根端口并立即进入转发状态
  - A．Frowarding端口
  - B．Alteate端口
  - C．Backup端口
  - D．Edge端口

### 原第 180 题

- 剔除原因：**S1** 含缺损术语：\btroute\b(Tracert 错字)
- 原答案：A
- 题干：网络管理员在路由器设备上使用了Tracer tRoute功能后,路由器发出的数据包中,ipv4首部的Protocol字段取值为
  - A．17
  - B．2
  - C．1
  - D．6

### 原第 186 题

- 剔除原因：**S1** 含缺损术语：\betheetll\b(Ethernet II 错字)
- 原答案：A
- 题干：包含以太网头部的Etheetll帧的长度为
  - A．64-1518B
  - B．60-1560B
  - C．46-1500B
  - D．64-1500B

### 原第 197 题

- 剔除原因：**H4** 选项 A 与 B 内容完全相同；**S1** 含缺损术语：\bfrowarding\b(Forwarding 错字)、\bfroward\b(Forward 错字)
- 原答案：E
- 题干：RSTP协议使用P/A机制加快了上游端口转到机制加快了上游端口转到Frowarding状态的速度,但是却没有出状态的速度,但是却没有出现临时环路的原因是什么,现临时环路的原因是什么()
  - A．缩短了Froward Delay的时间
  - B．缩短了Froward Delay的时间
  - C．引入了边缘端口
  - D．加快了端口角色选举的速度
  - E．通过同步机制保证不会出现临时环路

### 原第 199 题

- 剔除原因：**H1** 题干依赖配图，而原 docx 不含任何图片
- 原答案：C
- 题干：如图所示,下列交换机的哪个端口会成为指定端口
  - A．SWC的g0/0/1
  - B．SWC的g0/0/2
  - C．SWA的g0/0/3
  - D．SWB的g0/0/3

### 原第 200 题

- 剔除原因：**H1** 题干依赖配图，而原 docx 不含任何图片
- 原答案：C
- 题干：如图所示,所有主机之间都可以正常通行,则SWA MAC地址和端口的对应关系正确的是
  - A．MAC-A G0/0/1MAC-B G0/0/2MAC-C G0/0/3
  - B．MAC-A G0/0/1MAC-B G0/0/1MAC-C G0/0/3
  - C．MAC-A G0/0/3MAC-B G0/0/3MAC-C G0/0/1
  - D．MAC-A G0/0/2MAC-B G0/0/2MAC-C G0/0/3

### 原第 204 题

- 剔除原因：**H1b** 题干引用了"如下信息/配置"，但正文中没有该内容（原图中才有的内容已丢失）
- 原答案：A
- 题干：某网络工程师在输入命令时提示如下信息:
  - A．输入命令不明确
  - B．参数类型错误
  - C．没有查找到关键字
  - D．输入命令不完整

### 原第 214 题

- 剔除原因：**S1** 含缺损术语：\bal1\b(all 错字)、allowpass(allow-pass 错字)
- 原答案：D
- 题干：命令port trunk allowpass vlan al1有什么作用
  - A．如果为相连的远端设备配置了port default vlan 3 命令
  - B．与该端口相连的对端端口必须同时配置port trunk permit vlan al1
  - C．相连的对端设备可以动态确定允许哪些vlan ID通过
  - D．该端口上允许所有vlan 的数据帧

### 原第 224 题

- 剔除原因：**S1** 含缺损术语：\bpackbag\b(package 错字)、\breuest\b(request 错字)；**H6** 与第 20 题题干重复（保留第 20 题）
- 原答案：C
- 题干：AP通过以下哪项报文从AC.请求软件版本
  - A．VRP System Reuest
  - B．Software Request
  - C．Image DatA.Request
  - D．Image packbag Request

### 原第 226 题

- 剔除原因：**H6** 与第 68 题题干重复（保留第 68 题）
- 原答案：B
- 题干：DHCP DISCOVER报文的主要作用是
  - A．服务器对REQUEST报文的确认响应
  - B．客户端用来寻找DHCP服务器
  - C．客户端请求配置确认,或者续租租期
  - D．DHCP服务器用来响应DHCP DISCOVER 报文,此报文携带了各种配置信息

### 原第 227 题

- 剔除原因：**S1** 含缺损术语：\bohcp\b(DHCP 错字)
- 原答案：C
- 题干：DHCP服务器分配给客户端的动态ip地址,通常有一定的租借期限,那么关于租借期限的描述正确的是
  - A．租期更新定时器为总租期的50%,当“租期更新定时器”到期时,DHCP客户端必须进行HP地址的更新
  - B．重绑定定时器为总租期的87.5%
  - C．若“重绑定定时器”到期但客户端还没有收到服务器的响应则会一直发送
  - D．在租借期限内,如果客户端收到OHCP NAK报文客户端就会立即停止使用此IP地址,并返回初始化状态,更新申请新的IP地址

### 原第 229 题

- 剔除原因：**S1** 含缺损术语：\bafll\b(all 错字)
- 原答案：C
- 题干：DSCP中的业务优先级描述正确的是
  - A．AF的优先级高于EF
  - B．AF11丢包概率高于AF12
  - C．CS的优先级最高
  - D．AFLL优先级高于AF4

### 原第 232 题

- 剔除原因：**S1** 含缺损术语：\bopx\b(OPEX 错字)
- 原答案：C
- 题干：OPX的定义是
  - A．维护成本
  - B．总体拥有成本
  - C．运营成本
  - D．运维成本

### 原第 233 题

- 剔除原因：**S1** 含缺损术语：\bfed\b(RED 错字)、FED技术(RED 技术错字)
- 原答案：A
- 题干：FED技术可以解决以下哪些缺点
  - A．TCP全局同步现象
  - B．TCP饿死现象
  - C．无差别的丢弃

### 原第 236 题

- 剔除原因：**S1** 含缺损术语：\bqw2\b(ONF 错字)
- 原答案：B
- 题干：SDN主要技术流派主张SDN采用分层的开放架构,qw2倡导、定义集中式架构和Openflow的是哪一个技术流派
  - A．ETSI
  - B．ONF
  - C．ITU
  - D．IETF

### 原第 237 题

- 剔除原因：**S1** 含缺损术语：\broyting-table\b(routing-table 错字)、Royting(Routing 错字)；**H6** 与第 26 题题干重复（保留第 26 题）
- 原答案：D
- 题干：VRP操作平台,以下哪条命令可以只查看静态路由
  - A．display ip routing-table statics
  - B．display ip routing-table verbose
  - C．display ip royting-table
  - D．display ip routing-table protocol static

### 原第 241 题

- 剔除原因：**H2** 选项不足 2 项（原文档此段为残片）；**H2** 原文档未给出有效答案（答案：空）
- 原答案：空
- 题干：不同虚拟机见可以利用vswitch建立VTEP隧道来进行VXLAN的通信,那么VXLAN的通信过程是

### 原第 242 题

- 剔除原因：**H2** 选项不足 2 项（原文档此段为残片）；**H2** 原文档未给出有效答案（答案：空）
- 原答案：空
- 题干：1源VTEP将源VM发通的ARP广播封装为组播报文发送到L3网络中

### 原第 243 题

- 剔除原因：**H2** 选项不足 2 项（原文档此段为残片）；**H2** 原文档未给出有效答案（答案：空）
- 原答案：空
- 题干：2目的VTEP收到组播报文后,学习源VW与VTEP映射关系,并将组播报文转发给本地VM

### 原第 244 题

- 剔除原因：**H2** 选项不足 2 项（原文档此段为残片）；**H2** 原文档未给出有效答案（答案：空）
- 原答案：空
- 题干：3本地进行单播应答

### 原第 245 题

- 剔除原因：**H2** 选项不足 2 项（原文档此段为残片）；**H2** 原文档未给出有效答案（答案：空）
- 原答案：空
- 题干：4目标VTEP封装Vxlan隧道,并建立映射封装后单播发给VTEP

### 原第 246 题

- 剔除原因：**H2** 选项不足 2 项（原文档此段为残片）；**H2** 原文档未给出有效答案（答案：空）
- 原答案：空
- 题干：5源VTEP收到应道建立vm与目标VTEP映射关系,去掉隧道转发给源vm

### 原第 250 题

- 剔除原因：**H6** 与第 35 题题干重复（保留第 35 题）
- 原答案：A
- 题干：高级ACL的编号范围是
  - A．3000-3999
  - B．2000-2999
  - C．4000-4999
  - D．6000-6031

### 原第 251 题

- 剔除原因：**H6** 与第 120 题题干重复（保留第 120 题）
- 原答案：D
- 题干：关于ospf协议区域划分说法错误的是
  - A．Area.0是骨干区域,其他区域都必须与此区域相连
  - B．同一个ospf区域中的路由器中的LSDB是完全一致的
  - C．划分ospf区域可以缩小部分路由器的LSDB规模
  - D．只有ABR才能作为ASBR

### 原第 253 题

- 剔除原因：**S1** 含缺损术语：\bprotovol-view\b(protocol-view 错字)
- 原答案：C
- 题干：管理员在什么情况下才能为路由器修改设备名称
  - A．User-view
  - B．Protovol-view
  - C．System-view
  - D．Interface-view

### 原第 254 题

- 剔除原因：**H6** 与第 30 题题干重复（保留第 30 题）
- 原答案：A
- 题干：交换网络中STP协议的桥ID如下,拥有哪个桥ID的交换机会成为根桥
  - A．4096 00-01-02-03-04-DD
  - B．32768 00-01-02-03-04-AA
  - C．32768 00-01-02-03-04-CC
  - D．32768 00-01-02-03-04-BB

### 原第 267 题

- 剔除原因：**S1** 含缺损术语：\bweite\b(write 错字)
- 原答案：D
- 题干：现在需要实现一个python自动化脚本Telnet到设备上查看设备运行配置,以下说法错误的是
  - A．telnetlib可以实现这个功能
  - B．使用telnet。Telnet(host)连接Telnet服务器
  - C．可以使用telnet.weite(b\)向设备输入查看当前配置的命令
  - D．telnet。close()用在每一次输入命令后,作用是用户等待交换机回显信息

### 原第 269 题

- 剔除原因：**S1** 含缺损术语：\betheet0\b(ethernet0 错字)
- 原答案：B
- 题干：已知某一台路由器的路由表中有两个表项,如果该路由器要转发目的地址为9.1.4.5的报文,则下列说法正确的是
  - A．选择第二项作为最优匹配项,因为RIP协议的代价值较小
  - B．选择第二项作为最优匹配项,因为该路由器相对于目的地址9.1.4.5来说,是更精确的匹配
  - C．选择第二项作为最优匹配项,因为etheet0的速度比serial0的速度更快
  - D．选择第一项作为最优匹配项,因为ospf协议的优先级值较高

### 原第 277 题

- 剔除原因：**S1** 含缺损术语：\bdod\b(含中文的英文注释)、哦那(英文注释里混入中文)
- 原答案：A
- 题干：在MPLS网络中,交换机会分配标签,标签分配方式描述正确的是
  - A．可以由下游SR决定将标签分配给特定FEC,再通知上游礼SR
  - B．下游按需方式DoD(downstream 哦那 demand)是指对于一个特定的FEC,LSR无需从上游获得标签请求消息即进行标签分配与分发
  - C．下游自主分配标签方式是指对于一个特定FEC,LSR获得标签请求消息后才进行标签分配与非法
  - D．具有标签分发邻居关系的上游SR和下游LSR使用的标签发布方式可以一致

### 原第 278 题

- 剔除原因：**S1** 含缺损术语：\bjntrust\b(Untrust 错字)、\btrustd\b(Trust 错字)、localp区域(区域名错字)
- 原答案：C
- 题干：在防火墙域间安全策略中,请问以下哪一项的数据流不是Outbound方向的
  - A．从Trust区域到DMz区域的数据流
  - B．从Trust区域到Untrust区域的数据流
  - C．从TrustD区域到localp区域的数据流
  - D．从DMZ区域到Jntrust区域的数据流

### 原第 280 题

- 剔除原因：**S1** 含缺损术语：\blnterface\b(Interface 错字)
- 原答案：D
- 题干：在配置MPLS VPN时,管理员配置了如下几条命令,对于该命令描述错误的是Lnterface G0/0/0 ip binding vpn-instance VPN1 interface g0/0/1 IP binding vpn-instance Vpn2
  - A．该配置命令通常在PE设备上配置的
  - B．该命令的作用时将PE设备上的g0/0/1和g0/0/2接?与分配给客户网络的vpn实列进行绑定
  - C．设备上的接口与VPN实例绑定后,该接口将变为私网接口,并可以配置私网地址、运行私网路由协议
  - D．如果取消接口与实列的绑定设备不会自动清空与VPN实例绑定接口下的ipv4或者ipv6的相关配置

### 原第 288 题

- 剔除原因：**S1** 含缺损术语：\bpremit\b(permit 错字)
- 原答案：ABD
- 题干：如下选项中的配置,哪些属于二层ACL
  - A．rule 20 permit source-mac 0230-0405-0607
  - B．rule 10 premit 12-protocol arp
  - C．rule 25 permit source 192.168.1.1 0.0.0.0.0
  - D．rule 15 premit vlan-id 100

### 原第 300 题

- 剔除原因：**S1** 含缺损术语：\bauthenrication\b(authentication 错字)
- 原答案：BCD
- 题干：路由器radius信息配置如下,下列说法正确的是Radius-server template HuaweiRadius-server shared-key cipher HuaweiRadius-server authenrication 200.0.12.1 1812Radius-server accounting 200.0.12.1 1813Radius-attribute nas-ip 200.0.12.2
  - A．路由器发送radius报文源ip地址为200.0.12.1
  - B．授权服务器的IP地址为200.0.12.1
  - C．认证服务器的IP地址为200.0.12.1
  - D．计费服务器的IP地址为200.0.12.1

### 原第 301 题

- 剔除原因：**S1** 含缺损术语：\betheet\b(Ethernet 错字)
- 原答案：ABD
- 题干：如果以太网数据帧Length/Type=80806,下列说法正确的是
  - A．此数据帧的目的MAC地址有可能是FFFF-FFFF-FFFF
  - B．此数据帧的源MAC地址一定不是FFFF-FFFF-FFFF
  - C．此数据帧为IEEE 802.3帧
  - D．此数据帧为Etheet II 帧

### 原第 303 题

- 剔除原因：**S1** 含缺损术语：\bmulit-access\b(multi-access 错字)
- 原答案：ABCD
- 题干：Ospf协议支持的网络类型有哪些
  - A．Point-to-Point
  - B．Non-Broadcast Mulit-Access
  - C．Point-to-Multipoint
  - D．Broadcast

### 原第 306 题

- 剔除原因：**S1** 含缺损术语：\briouter\b(router 错字)
- 原答案：ABCD
- 题干：在华为设备中,ospf选举riouter id的方法可以是下列哪种
  - A．如果未配置loopback接口,则在其他接口的IP地址中选取最大的IP地址作为Router ID
  - B．华为交换机可能使用最大的vlanif的IP地址作为router ID
  - C．如果配置了loopback接口,则从loopback接口的IP地址中选择最大的ip地址作为router ID
  - D．通过手工定义一个任意的合法router ID
  - E．使用默认的127.0.0.1

### 原第 311 题

- 剔除原因：**S1** 含缺损术语：\binteet\b(Internet 缺字)
- 原答案：AB
- 题干：某个私有网络内有主机需要访问inteet,为实现此需求,管理员应该在该网络的边缘路由器上做出如下哪些配置
  - A．默认路由
  - B．NAT
  - C．STP
  - D．DHCP

### 原第 314 题

- 剔除原因：**S1** 含缺损术语：\bzhuanfa\b(拼音残留(转发))
- 原答案：ABD
- 题干：ip route-static 10.0.2.2 255.255.255.255 10.0.12.2 preference 20,关于此命令说法正确的是
  - A．该优先级为20
  - B．该路由可以指导目的IP地址为10.0.2.2的数据报转发
  - C．该路由可以指导目的ip地址为10.0.12.2的数据zhuanfa
  - D．该路由的NextHop为10.0.12.2

### 原第 318 题

- 剔除原因：**S1** 含缺损术语：\bfrowarding\b(Forwarding 错字)
- 原答案：AB
- 题干：下面关于生成树协议中Frowarding状态描述错误的是
  - A．frowarding状态的端口不学习报文源MAC地址
  - B．frowarding状态的端口一定会发送BPDU报文
  - C．frowarding状态的端口可以转发数据报文
  - D．frowarding 状态的端口可以接收BPDU报文

### 原第 319 题

- 剔除原因：**H6** 与第 299 题题干重复（保留第 299 题）
- 原答案：AB
- 题干：用Telnet方式登录路由器时,可以选择哪几种认证方式
  - A．password认证
  - B．AAA本地认证
  - C．不认证
  - D．MD5密文认证

### 原第 320 题

- 剔除原因：**S1** 含缺损术语：\bauthenrication\b(authentication 错字)；**H6** 与第 300 题题干重复（保留第 300 题）
- 原答案：BCD
- 题干：路由器radius信息配置如下,下列说法正确的是Radius-server template HuaweiRadius-server shared-key cipher HuaweiRadius-server authenrication 200.0.12.1 1812Radius-server accounting 200.0.12.1 1813Radius-attribute nas-ip 200.0.12.2
  - A．路由器发送radius报文源ip地址为200.0.12.1
  - B．授权服务器的IP地址为200.0.12.1
  - C．认证服务器的IP地址为200.0.12.1
  - D．计费服务器的IP地址为200.0.12.1

### 原第 321 题

- 剔除原因：**S1** 含缺损术语：\betheet\b(Ethernet 错字)；**H6** 与第 301 题题干重复（保留第 301 题）
- 原答案：ABD
- 题干：如果以太网数据帧Length/Type=80806,下列说法正确的是
  - A．此数据帧的目的MAC地址有可能是FFFF-FFFF-FFFF
  - B．此数据帧的源MAC地址一定不是FFFF-FFFF-FFFF
  - C．此数据帧为IEEE 802.3帧
  - D．此数据帧为Etheet II 帧

### 原第 322 题

- 剔除原因：**H6** 与第 302 题题干重复（保留第 302 题）
- 原答案：ACD
- 题干：运行stp协议的交换网络在进行生成树计算时用到了以下哪些参数
  - A．端口ID
  - B．Forward Delay
  - C．桥ID
  - D．根路径开销

### 原第 323 题

- 剔除原因：**S1** 含缺损术语：\bmulit-access\b(multi-access 错字)；**H6** 与第 303 题题干重复（保留第 303 题）
- 原答案：ABCD
- 题干：Ospf协议支持的网络类型有哪些
  - A．Point-to-Point
  - B．Non-Broadcast Mulit-Access
  - C．Point-to-Multipoint
  - D．Broadcast

### 原第 324 题

- 剔除原因：**H6** 与第 304 题题干重复（保留第 304 题）
- 原答案：ACD
- 题干：以下关于IPv6地址配置说法正确的是
  - A．ipv6支持无状态主动配置
  - B．ipv6地址只能手工配置
  - C．ipv6地址支持多种方式主动配置
  - D．ipv6支持DHCPV6的形式进行地址配置

### 原第 325 题

- 剔除原因：**H6** 与第 305 题题干重复（保留第 305 题）
- 原答案：BCD
- 题干：华为企业级AP支持的工作模式有以下哪几种
  - A．Local
  - B．FIT
  - C．FAT
  - D．CLOUD

### 原第 326 题

- 剔除原因：**S1** 含缺损术语：\briouter\b(router 错字)；**H6** 与第 306 题题干重复（保留第 306 题）
- 原答案：ABCD
- 题干：在华为设备中,ospf选举riouter id的方法可以是下列哪种
  - A．如果未配置loopback接口,则在其他接口的IP地址中选取最大的IP地址作为Router ID
  - B．华为交换机可能使用最大的vlanif的IP地址作为router ID
  - C．如果配置了loopback接口,则从loopback接口的IP地址中选择最大的ip地址作为router ID
  - D．通过手工定义一个任意的合法router ID
  - E．使用默认的127.0.0.1

### 原第 327 题

- 剔除原因：**H6** 与第 307 题题干重复（保留第 307 题）
- 原答案：AB
- 题干：在ospf协议中,下面对DR的描述正确的是
  - A．若两台路由器的优先级相等,则选择router ID 的路由器作为DR
  - B．DR和BDR之间也要建立邻居关系
  - C．默认情况下,本广播网络中所有的路由器都将参与DR选举
  - D．若两台路由器的优先级值不同,则选择优先级值较小的路由器作为DR

### 原第 328 题

- 剔除原因：**H6** 与第 308 题题干重复（保留第 308 题）
- 原答案：ABCD
- 题干：链路聚合是企业网络中的常用技术,下列描述中是链路聚合的优点的是
  - A．提高可靠性
  - B．提高安全性
  - C．实现负载分担
  - D．增加带宽

### 原第 329 题

- 剔除原因：**H6** 与第 309 题题干重复（保留第 309 题）
- 原答案：BD
- 题干：为了实现vlanif接口上的网络层功能,需要在vlanif接口上配置、
  - A．ip前缀
  - B．子网掩码
  - C．MAC地址
  - D．IP地址

### 原第 330 题

- 剔除原因：**H6** 与第 310 题题干重复（保留第 310 题）
- 原答案：ABCD
- 题干：如果一个以太网数据帧的length/type=0x8100,那么这个数据帧的载荷可能是
  - A．TCP数据段
  - B．ICMP报文
  - C．ARP报文
  - D．UDP数据

### 原第 331 题

- 剔除原因：**S1** 含缺损术语：\binteet\b(Internet 缺字)；**H6** 与第 311 题题干重复（保留第 311 题）
- 原答案：AB
- 题干：某个私有网络内有主机需要访问inteet,为实现此需求,管理员应该在该网络的边缘路由器上做出如下哪些配置
  - A．默认路由
  - B．NAT
  - C．STP
  - D．DHCP

### 原第 332 题

- 剔除原因：**H6** 与第 312 题题干重复（保留第 312 题）
- 原答案：CD
- 题干：使用动态主机配置协议DHCP分配IP地址有哪些优点
  - A．可以实现IP地址重复利用
  - B．工作最大且不好管理
  - C．配置信息发生变化(如DNS)。,只需要管理员在DHCP服务器上修改,方便统一管理
  - D．避免IP地址冲突

### 原第 333 题

- 剔除原因：**H6** 与第 313 题题干重复（保留第 313 题）
- 原答案：AC
- 题干：关于ipv6中的RA和RS报文说法错误的是
  - A．RS用于请求地址前缀信息
  - B．RS用于回复地址前缀信息
  - C．RA用于回复地址前缀信息
  - D．RA用于请求地址前缀信息

### 原第 334 题

- 剔除原因：**S1** 含缺损术语：\bzhuanfa\b(拼音残留(转发))；**H6** 与第 314 题题干重复（保留第 314 题）
- 原答案：ABD
- 题干：ip route-static 10.0.2.2 255.255.255.255 10.0.12.2 preference 20,关于此命令说法正确的是
  - A．该优先级为20
  - B．该路由可以指导目的IP地址为10.0.2.2的数据报转发
  - C．该路由可以指导目的ip地址为10.0.12.2的数据zhuanfa
  - D．该路由的NextHop为10.0.12.2

### 原第 335 题

- 剔除原因：**H6** 与第 315 题题干重复（保留第 315 题）
- 原答案：ABCD
- 题干：路由器开启FTP服务,用户名和密码均为huawei,并且设置FTP的根目录为
  - A．local-user Huawei ftp-directory flash:/dhcp/
  - B．ftp Server enable
  - C．local-user Huawei password cipher Huawei
  - D．local-user Huawei service-type ftp

### 原第 336 题

- 剔除原因：**H6** 与第 316 题题干重复（保留第 316 题）
- 原答案：ABC
- 题干：目前,公司有一个网络管理员,公司网络中的AR2200通过telnet直接输入密码后就可以实现远程管理。新来了两个网络管理员后,公司希望给所有的管理员分配各自的用户和密码,以及不同权限等级,那么应该如何操作
  - A．在配置每个管理员的账户时,需要配置不同的权限级别
  - B．telnet配置的用户认证模式必须选择AAA模式
  - C．在AAA视图下配置三个用户名和各自对应的密码
  - D．每个管理员在运行telnet命令时,使用设备的不同公网ip地址

### 原第 337 题

- 剔除原因：**H6** 与第 317 题题干重复（保留第 317 题）
- 原答案：AC
- 题干：以下哪些属于局域网
  - A．一个家庭网络
  - B．宽带域域网
  - C．某公司办公网络
  - D．因特网

### 原第 338 题

- 剔除原因：**S1** 含缺损术语：\bfrowarding\b(Forwarding 错字)；**H6** 与第 318 题题干重复（保留第 318 题）
- 原答案：AB
- 题干：下面关于生成树协议中Frowarding状态描述错误的是
  - A．frowarding状态的端口不学习报文源MAC地址
  - B．frowarding状态的端口一定会发送BPDU报文
  - C．frowarding状态的端口可以转发数据报文
  - D．frowarding 状态的端口可以接收BPDU报文

### 原第 341 题

- 剔除原因：**S1** 含缺损术语：\bfrowarding\b(Forwarding 错字)、\bleaing\b(Learning 错字)
- 原答案：ABD
- 题干：RSTP协议包括以下哪些端口状态
  - A．Discarding
  - B．Frowarding
  - C．Listening
  - D．Leaing

### 原第 343 题

- 剔除原因：**S1** 含缺损术语：\bfrowarding\b(Forwarding 错字)、\bfroward\b(Forward 错字)、\bfrowarding-disabled\b(Forwarding 错字)、\bleaing\b(Learning 错字)
- 原答案：BE
- 题干：STP端口在下列哪种状态之间转化时存在Froward Delay
  - A．Frowarding-Disabled
  - B．Leaing-Frowarding
  - C．Disabled-Blocking
  - D．Blocking-Listening
  - E．Listening-Leaing

### 原第 344 题

- 剔除原因：**H4** 选项 A 与 B 内容完全相同；**H4** 选项 A 与 C 内容完全相同；**H4** 选项 B 与 C 内容完全相同；**H6** 与第 407 题题干重复（保留第 407 题）
- 原答案：ABCD
- 题干：通过SR( )可以简易的定义一条显示路径,网络中的节点只需要维护Segment Routing信息,即可应对业务的实时快速发展。Segment Routing具有如下哪些特点
  - A．同时支持控制器的集中控制模式和转发器的分布控制模式,提供集中控制和分布控制之间的平衡
  - B．同时支持控制器的集中控制模式和转发器的分布控制模式,提供集中控制和分布控制之间的平衡
  - C．同时支持控制器的集中控制模式和转发器的分布控制模式,提供集中控制和分布控制之间的平衡
  - D．通过对现有协议(例如IGP)进行扩展,能使现有网络更好的平滑演进

### 原第 345 题

- 剔除原因：**S1** 含缺损术语：\blv1\b(v1 错字)
- 原答案：BD
- 题干：下列关于SNMP协议各个版本说法正确的是
  - A．SNMPv2c报文具有身份验证和加密处理的功能
  - B．SNMPv3报文具有身份验证和加密处理的功能
  - C．SNMPv1采用UDP作为传输层协议,而SNMPv2c和SNMPv3采用TCP作为传输层协议,因此可靠性更高
  - D．SNMPv2c沿用lv1版本定义的5种协议操作并额外新增了两种操作

### 原第 346 题

- 剔除原因：**S1** 含缺损术语：\bbirtualised\b(virtualized 错字)、\bnvfm\b(VNFM 错字)
- 原答案：ABCD
- 题干：下面选项中关于NFV架构的慨念描述正确的是
  - A．MANO由NFVO、NVFM和VIM组成
  - B．NFVO(NFV Orchestrator)负责业务的编排
  - C．VIM(Birtualised infrastructure Manager)虚拟资源管理,负责实现基础设施的虚拟化
  - D．VNFM虚拟网络功能管理,负责VNF的生命周期管理

### 原第 349 题

- 剔除原因：**S1** 含缺损术语：\bosppf\b(OSPF 错字)
- 原答案：AC
- 题干：说法不正确的是
  - A．若路由cost值越大,则路由优先级月高
  - B．缺省情况下,直连路由优先级高于osppf路由优先级
  - C．VRP中,路由优先级数值月大,则表示路由优先级月高
  - D．每条静态路由优先级可以不同

### 原第 354 题

- 剔除原因：**H1b** 题干要求"根据下面配置/内容"作答，但正文中没有该配置（原图中才有的内容已丢失）
- 原答案：ABC
- 题干：根据下面配置下列说法正确的是
  - A．主机A(pc3)能够和主机B(PC4)ping通
  - B．交换机g0/0/1口的pvid为20
  - C．两条链路数据帧都不包含vlan tag
  - D．主机A(PC3)不能ping通主机B(PC)

### 原第 362 题

- 剔除原因：**H6** 与第 309 题题干重复（保留第 309 题）
- 原答案：BC
- 题干：为了实现vlanif接口上的网络层功能,需要在vlanif接口上配置
  - A．MAC地址
  - B．子网掩码
  - C．IP地址
  - D．IP前缀

### 原第 363 题

- 剔除原因：**S1** 含缺损术语：\bkeeplive\b(keepalive 错字)
- 原答案：AC
- 题干：为检测CAPWAP隧道的连通状态,在CAWAP隧道建立后AC使用哪些CAPWAP报文进行检测
  - A．keeplive
  - B．DPD
  - C．Echo
  - D．Hello

### 原第 370 题

- 剔除原因：**H6** 与第 292 题题干重复（保留第 292 题）
- 原答案：ABCD
- 题干：控制器是SDN的核心组件,控制器通过南向接口连接设备,以下属于控制器南向协议的是
  - A．SNMP
  - B．OpenFlow
  - C．PCEP
  - D．NETCONF

### 原第 373 题

- 剔除原因：**H6** 与第 357 题题干重复（保留第 357 题）
- 原答案：CD
- 题干：以下关于无线设备描述正确的是
  - A．FAT AP一般与无线控制器配合工作
  - B．无线设备没有有线接口
  - C．FIA AP一般独立完成用户接入认证业务转发
  - D．无线控制器AC一般位于整个网络的汇聚层,提供高速、安全、可靠的wlan业务

### 原第 392 题

- 剔除原因：**S1** 含缺损术语：\betheet\b(Ethernet 错字)
- 原答案：ABC
- 题干：如果以太网数据帧Length/type=0x0806,下列说法正确的是
  - A．此数据帧的目的mac地址有可能是FFFF-FFFF-FFFFF
  - B．此数据帧为Etheet II帧
  - C．次数据帧的源MAC地址一定不是FFFF-FFFF-FFFFF
  - D．此数据为IEEE802.3帧

### 原第 400 题

- 剔除原因：**S1** 含缺损术语：\bcrtl\b(ctrl 错字)
- 原答案：AB
- 题干：在VPR平台上,可以通过下面哪种方式访问上一条历史命令
  - A．ctrl+P
  - B．上光标
  - C．Crtl+U
  - D．左光标

### 原第 402 题

- 剔除原因：**H6** 与第 290 题题干重复（保留第 290 题）
- 原答案：AB
- 题干：为检测CAPWAP隧道的连通状态,在CAPWAP隧道建立之后AC使用以下哪些CAPWAP报文进行探测
  - A．keepalive
  - B．echo
  - C．DPD
  - D．Hello

### 原第 423 题

- 剔除原因：**S1** 含缺损术语：\bleaing\b(Learning 错字)
- 原答案：BC
- 题干：stp端口在下列哪种状态之间相互转换时存在forward delay
  - A．blocking listening
  - B．listening leaing
  - C．leaing forwarding
  - D．disabled blocking
  - E．forwarding disabled

### 原第 431 题

- 剔除原因：**H6** 与第 291 题题干重复（保留第 291 题）
- 原答案：ABD
- 题干：ipv6报文支持哪些扩展报头
  - A．分片扩展报头
  - B．目的选项扩展报头
  - C．Vlan扩展报头
  - D．逐跳选项扩展报头

### 原第 433 题

- 剔除原因：**S1** 含缺损术语：\boffest\b(Offset 错字)
- 原答案：ACD
- 题干：ipv4首部中的哪些字段和分片相关
  - A．flags
  - B．TTL
  - C．Identification
  - D．Fragment Offest

### 原第 448 题

- 剔除原因：**S1** 含缺损术语：\blookback\b(loopback 错字)
- 原答案：BCDE
- 题干：在华为设备中,ospf选举router id方法可以是下列哪种
  - A．使用默认的127.0.0.1
  - B．如果未配置lookback接口,则在其他接口的ip地址选举最大的IP地址作为ROUTER id
  - C．如果配置了loopback接口,则从loopback接口的IP地址中选择最大的IP地址作为router id
  - D．华为交换机可能使用最大的vlanif的IP地址作为router id
  - E．通过手工定义一个任意的合法的router id

### 原第 457 题

- 剔除原因：**S1** 含缺损术语：\bcapddr\b(CAPWAP 错字)
- 原答案：ABD
- 题干：DHCP Snooping时一种DHCP安全特性,可用于防御多种攻击,其中包括
  - A．防御改变CAPDDR值的饿死攻击
  - B．防御DHCP仿冒者攻击
  - C．防御TCPflag攻击
  - D．防御中间人攻击和IP/MAC Spoofing攻击

### 原第 465 题

- 剔除原因：**S1** 含缺损术语：\betheet\b(Ethernet 错字)
- 原答案：ABC
- 题干：MPLS封装有不同的方式,下列选项中关于封装方式的说法正确的是
  - A．MPLS封装有帧模式和信元模式
  - B．Etheet和PPP使用帧模式封装
  - C．ATM使用信元模式封装
  - D．信元模式封装时如果报文中已经解怠了MPLS Header,第一个信元会保留该MPLSHeader)用于转发

### 原第 466 题

- 剔除原因：**S1** 含缺损术语：\bfiust\b(first 错字)、\bfurst\b(first 错字)、\blasth\b(Last 错字)
- 原答案：ABD
- 题干：MPLS称为多协议标签交换,关于MPLS中的标签描述正确的是
  - A．标签栈按后进先出(Last In Furst Out)方式组织标签,从栈顶开始处理标签
  - B．标签封装在链路层和网络层之间
  - C．标签栈按后进先出(Lasth Fiust Out)方式组织标签,从栈底开始处理标签
  - D．标签上固定长度的4个字节

### 原第 484 题

- 剔除原因：**S1** 含缺损术语：\bvindows\d*\b(Windows 错字)
- 原答案：AB
- 题干：关于PC机从DHCP server获取地址,所使用的命令描述正确的是
  - A．在用户pc机的vindows7 vindows xp环境下使用ipconfig/renew命令来申请新的IP地址,此时用户PC机向DHCP服务器发送的是DHCP RENEW报文
  - B．在用户PC机的Windows7vndows XP环境下使用ipconfig/renew命令来主动释放IP地址,此时用户PC机向DHCP服务器发送的是DHCP RENEW报文
  - C．在用户PC机的Windows7vndows XP环境下使用ipconfig/renew命令来主动释放IP地址,此时用户PC机向DHCP服务器发送的是DHCP REQUEST报文
  - D．在用户PC机的Windows7vndows XP环境下使用ipconfig/renew命令来主动请新的IP地址,此时用户PC机向DHCP服务器发送的是DHCP DISCOVER报文

### 原第 486 题

- 剔除原因：**H6** 与第 342 题题干重复（保留第 342 题）
- 原答案：AC
- 题干：关于动态AC地址表说法正确的是
  - A．通过报文中的源AC地址学习获得的动态AC表项会老化
  - B．通过查看指定动态MAC地址表项的个数,可以获得接口下通信用户数会在设备重启后,之前的动态表项会丢失
  - C．在设备重启后,之前的动态表项会丢失

### 原第 498 题

- 剔除原因：**H1** 题干依赖配图，而原 docx 不含任何图片；**S1** 含缺损术语：\baccounding\b(accounting 错字)
- 原答案：BCD
- 题干：路由器radius信息配置如图,下列说法正确的是#radius-server template Huawei radius-server shared.key cipher Huawei radius-server authentication 200.0.12.1 1812 radius-server accounding 200.0.12.1 1813#*
  - A．路由器发送radius报文的源IP地址为200.0.12.2
  - B．计费服务器的ip地址为200.0.12.1
  - C．授权服务器的IP地址为200.0.12.1
  - D．认证服务器的IP地址为200.0.12.1

### 原第 499 题

- 剔除原因：**S1** 含缺损术语：\binteet\b(Internet 缺字)
- 原答案：AD
- 题干：某个私有网络内有主机需要访问inteet,为实现此需求,管理员应该在该网络的边缘路由器是做出如下哪些配置
  - A．默认路由
  - B．STP
  - C．DHCP
  - D．NAT

### 原第 503 题

- 剔除原因：**H3** 选项 C 文本中混入了其它选项的内容（选项标记丢失）；**S1** 含缺损术语：\bserver-mapd\b(server-map 错字)、吴元组(五元组 错字)
- 原答案：AC
- 题干：下列关于ASP和servermap的说法正确的是
  - A．ASPF检查应用层协议信息并且监控连接的应用层协议状态
  - B．ASPF通过动态的生成ACL来决定数据包是否通过防火墙
  - C．配置NAT Server生成的是静态server-mapD。Servermap表用吴元组来表示一段会话

### 原第 504 题

- 剔除原因：**S1** 含缺损术语：\bingiess\b(ingress 错字)、\bout-lable\b(out-label 错字)、\bsatosd\b(命令错字)
- 原答案：BD
- 题干：下面关于选项描述错误的是[LSRA]mpls lsr-id 1.1.1.9[LSRA]int vlanif 10[LSRA-vlanif 10]mpls[LSRA-vlanif 10]quit[LSRA]static-Lsp ingiess SAtoSD destination 4.4.4.9 32 nexthop 10.1.1.2 out-lable 20
  - A．最后一条命令配置LSRA为人接口LSR,并且配置了一条静态LSP
  - B．Mpls使用全局mpls之后就不需要再接口视图下再次启用mpls
  - C．Mpls lsr-id是配置LSR的ID,是配置其他MPLS命令的前提,缺省是没有配置的
  - D．Mpls是在系统视图和接口视图下启用mpls功能,在使用mpls之后才能配置lsr-id

### 原第 509 题

- 剔除原因：**S1** 含缺损术语：\bavalibilty\b(availability 错字)
- 原答案：ABC
- 题干：信息安全最关心的三个属性是什么
  - A．机密性(confidentiality)
  - B．完整性(integrity)
  - C．可用性(avalibilty)
  - D．身份验证(authentication)

### 原第 513 题

- 剔除原因：**H6** 与第 512 题题干重复（保留第 512 题）
- 原答案：ABCD
- 题干：以下属于MPLS VPN路由的传递过程的是
  - A．CE与PE之间的路由交换
  - B．公网标签的分配过程
  - C．VRF路由注入MP-BGP的过程
  - D．MP-BGP路由注入VRF的过程

### 原第 515 题

- 剔除原因：**H6** 与第 413 题题干重复（保留第 413 题）
- 原答案：ABC
- 题干：在AC上添加AP的方式有
  - A．在线添加
  - B．自动发现AP
  - C．离线导入AP
  - D．手工确认未认证列表中的AP

### 原第 519 题

- 剔除原因：**H6** 与第 307 题题干重复（保留第 307 题）
- 原答案：ABC
- 题干：在ospf协议中,下面对DR的描述正确的是
  - A．DR与DR之间要建立邻接关系
  - B．若两台路由器的优先级值相等,则选择Router ID的路由器作为DR
  - C．默认情况下,本广播网络中所有的路由器都将参与DR选举
  - D．若两台路由器的优先级值不同,则选择优先级值较小的路由器作为DR

### 原第 541 题

- 剔除原因：**S1** 含缺损术语：BCCO(IPv6 地址中 0 误写为 O)、CDOO(IPv6 地址中 0 误写为 O)
- 原答案：A
- 题干：ipv6地址2001:ABEF:224E:FFE2:BCCO:CDOO:DDBE:8D58不能简写
  - A．正确
  - B．错误

### 原第 547 题

- 剔除原因：**S1** 含缺损术语：\bnmpv1\b(SNMPv1 错字)
- 原答案：A
- 题干：NMPV1定义了5种协议操作
  - A．正确
  - B．错误

### 原第 548 题

- 剔除原因：**S1** 含缺损术语：\bnmpv1\b(SNMPv1 错字)；**H6** 与第 547 题题干重复（保留第 547 题）
- 原答案：A
- 题干：NMPV1定义了5种协议操作
  - A．正确
  - B．错误

### 原第 550 题

- 剔除原因：**S1** 含缺损术语：一\s*致阻塞(一直阻塞 错字)
- 原答案：B
- 题干：telnetlib 中telnet read all( )的作用时读取所有数据直到EOF,如果回显没有返回EOF则会一致阻塞
  - A．正确
  - B．错误

### 原第 552 题

- 剔除原因：**S1** 含缺损术语：\bstartuo\b(startup 错字)
- 原答案：A
- 题干：VRP界面下,使用startuo saved-configuration backup.cfg配置下次启动时使用Backup.cfg文件
  - A．正确
  - B．错误

### 原第 556 题

- 剔除原因：**S1** 含缺损术语：\binteet\b(Internet 缺字)
- 原答案：A
- 题干：主机使用IP地址192.168.1.2访问inteet一点要经过NAT.
  - A．正确
  - B．错误

### 原第 575 题

- 剔除原因：**H6** 与第 525 题题干重复（保留第 525 题）
- 原答案：A
- 题干：RSTP协议中,边缘端口收到配置BPDU报文,就丧失了边缘端口属性
  - A．正确
  - B．错误

### 原第 582 题

- 剔除原因：**S1** 含缺损术语：\balteate\b(alternate 错字)
- 原答案：B
- 题干：RSTP中alteate端口和backup端口均无法转发流量,也不可以接收、处理、发送BPDU
  - A．正确
  - B．错误

### 原第 595 题

- 剔除原因：**S1** 含缺损术语：\bfrowarding\b(Forwarding 错字)
- 原答案：A
- 题干：缺省情况下,STP协议中的端口状态由disable转化为frowarding状态至少需要30s的时间
  - A．正确
  - B．错误

### 原第 596 题

- 剔除原因：**S1** 含缺损术语：\bsnipv3\b(SNMPv3 错字)
- 原答案：A
- 题干：华为ARG3系列路由器默认存在SNMP的所有版本(SNMPV1\SNMPV2C和snipv3)
  - A．正确
  - B．错误

### 原第 611 题

- 剔除原因：**S1** 含缺损术语：\bhytacacs\b(HWTACACS 错字)
- 原答案：A
- 题干：在AR路由器上创建的认证方案、授权方案、计费方案、hytacacs或者radius服务器模板,只有在域下应用后才能生效
  - A．正确
  - B．错误

### 原第 617 题

- 剔除原因：**H6** 与第 569 题题干重复（保留第 569 题）
- 原答案：B
- 题干：ospf的router id必须和路由器的某个接口ip地址相同
  - A．正确
  - B．错误

### 原第 631 题

- 剔除原因：**S1** 含缺损术语：\bwpai-psk\b(wpa-psk 错字)
- 原答案：B
- 题干：只有wpai-psk的安全策略才支持使用tkip进行数据加密
  - A．正确
  - B．错误

### 原第 646 题

- 剔除原因：**H6** 与第 569 题题干重复（保留第 569 题）
- 原答案：B
- 题干：ospf的router id必须和路由器的某个接口ip地址相同
  - A．正确
  - B．错误

### 原第 651 题

- 剔除原因：**S1** 含缺损术语：\bwpls\b(MPLS 错字)
- 原答案：A
- 题干：WPLS标签头封装在报文的数据链路层头部和网络层头部之间
  - A．正确
  - B．错误

### 原第 655 题

- 剔除原因：**S1** 含缺损术语：\bpreforence\b(preference 错字)
- 原答案：B
- 题干：对于达到同一个目的网络的多条路径,路由器需要通过比较preforence值的大小进行选择,如果preference相同,则依据cost值的大小进行选择
  - A．正确
  - B．错误

### 原第 671 题

- 剔除原因：**H6** 与第 526 题题干重复（保留第 526 题）
- 原答案：A
- 题干：根桥交换机上所有的端口都是指定端口
  - A．正确
  - B．错误

### 原第 672 题

- 剔除原因：**H6** 与第 549 题题干重复（保留第 549 题）
- 原答案：B
- 题干：管理信息库MIB(management information base)是一个虚拟的数据库,这个数据库只存在于NMS上
  - A．正确
  - B．错误

### 原第 673 题

- 剔除原因：**H6** 与第 626 题题干重复（保留第 626 题）
- 原答案：A
- 题干：交换机堆叠支持两台以上设备,通过堆叠可以将多台交换机组成逻辑上的一台设备
  - A．正确
  - B．错误

### 原第 693 题

- 剔除原因：**S1** 含缺损术语：\bmqs\b(MQC 错字)
- 原答案：B
- 题干：MQS与PBR一样,只能在设备的三层接口下调用
  - A．正确
  - B．错误

### 原第 694 题

- 剔除原因：**S1** 含缺损术语：\blinit\b(limit 错字)
- 原答案：B
- 题干：import-route linit命令不能够限制一个OSPF进程内可引入的最大外部路由数量
  - A．正确
  - B．错误

### 原第 699 题

- 剔除原因：**S1** 含缺损术语：\bnama\b(name 错字)
- 原答案：A
- 题干：在ospf广播或者NAMA网络类型中,DR priority大的设备不一定会成为DR
  - A．正确
  - B．错误

### 原第 713 题

- 剔除原因：**S1** 含缺损术语：\binteet\b(Internet 缺字)
- 原答案：B
- 题干：在ospf中,AS边界路由器是、可以是Inteet Router,或者是ABR,但是必须属于骨干区域
  - A．正确
  - B．错误

### 原第 720 题

- 剔除原因：**S1** 含缺损术语：\brouter-pokicy\b(router-policy 错字)
- 原答案：B
- 题干：VRP缺省情况下,当BGP的邻居出口路由策略(router-pokicy)改变后,需要手工操作才会向该邻居重新发送update消息
  - A．正确
  - B．错误

### 原第 750 题

- 剔除原因：**S1** 含缺损术语：\baerro-down\b(Error-down 错字)、进Aerro(进入 Error 错字)
- 原答案：B
- 题干：RSTP边端口无需等待forwarding delay,可以直接进入forwarding状态,如果边缘端口接收到了BPDU,则边缘端口会被直接关闭并进Aerro-down状态
  - A．正确
  - B．错误

### 原第 755 题

- 剔除原因：**S1** 含缺损术语：\bnqc\b(MQC 错字)
- 原答案：A
- 题干：实现流量过滤功能,可以使用traffic-flter,也可以使用MQC相当于traffic-filter,NQC可以在更多的视图内调用
  - A．正确
  - B．错误

### 原第 766 题

- 剔除原因：**S1** 含缺损术语：\blinit\b(limit 错字)
- 原答案：B
- 题干：import route linit命令不能限制一个ospf进程内可以引入的最大外部路由数量
  - A．正确
  - B．错误

### 原第 768 题

- 剔除原因：**S1** 含缺损术语：即侦听(既侦听 错字)
- 原答案：A
- 题干：ospf中,在广播类型网络中的选举出来的DR和BDR即侦听224.0.0.5地址,也侦听224.0.0.6地址
  - A．正确
  - B．错误

### 原第 769 题

- 剔除原因：**H6** 与第 615 题题干重复（保留第 615 题）
- 原答案：B
- 题干：RSTP中backup端口可以替换发生故障的根端口
  - A．正确
  - B．错误

### 原第 771 题

- 剔除原因：**S1** 含缺损术语：\brouter-poliy\b(router-policy 错字)
- 原答案：A
- 题干：VRP版本缺省情况下,当BGP的邻居入口路由策略(router-poliy)改变后,会自动向该邻居发生refresh以请求邻居重新发送update消息
  - A．正确
  - B．错误

### 原第 777 题

- 剔除原因：**S1** 含缺损术语：\blocalpreferebce\b(local-preference 错字)
- 原答案：A
- 题干：localpreferebce属性用于判断流量离开AS时的最佳路由,当通过不同IBGP对等体得到目的地址相同但下一跳不同的多条路由时,将优先选择localpreferebce属性值较高的路由
  - A．正确
  - B．错误

### 原第 782 题

- 剔除原因：**S1** 含缺损术语：\bb6p\b(BGP 错字)
- 原答案：A
- 题干：在BGP中有两种部署Fil Iter-Policy工具方法,一种是在B6P下全局部署,另一种是在指向对等体时部署
  - A．正确
  - B．错误

### 原第 790 题

- 剔除原因：**S1** 含缺损术语：\bcloudgampus\b(cloudcampus 错字)
- 原答案：A
- 题干：华为CloudGampus解决方案支持业务随行功能,该功能可以通过图形化策略配置,实现用户随时随地接入
  - A．正确
  - B．错误

### 原第 791 题

- 剔除原因：**S1** 含缺损术语：\bfrowarding\b(Forwarding 错字)
- 原答案：B
- 题干：一个非边缘端口是否迁移到frowarding状态是RSTP检测拓扑发生变化的标准之一
  - A．正确
  - B．错误

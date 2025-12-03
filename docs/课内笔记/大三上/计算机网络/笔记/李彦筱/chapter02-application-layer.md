# 第二章——应用层

> 易俊泉学长的原始笔记链接如下：
>
> [第二章——应用层](https://github.com/yijunquan-afk/XJTUSE-NOTES/blob/master/%E5%A4%A7%E4%B8%89%E4%B8%8B/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/chapter02%20Application-Layer/chapter02-application-layer.md)

## 概述

> :one: 网络应用协议的概念和实现方面
>
> > 传输层服务模型
> >
> > 客户端-服务器模式
> >
> > 点对点模式
>
> :two: 通过研究流行的应用程序级协议来了解协议
>
> > HTTP
> >
> > FTP
> >
> > SMTP / pop3 / imap
> >
> > DNS
>
> :three: 网络应用程序编程
>
> > 套接字socket API

## 一、应用层协议原理

广播、电视、报纸、网站：四大媒介

网络核心设备（路由器）并不在应用层上起作用，而是在较低层起作用。将应用软件限制在端系统，促进了大量的网络应用程序的迅速研发和部署。

研发网络应用程序的核心是写出能够运行在不同的端系统和通过网络彼此通信的程序。

> 客户端-服务端模式
>
> P2P模式
>
> 混合模式

### 1、网络应用程序体系结构

有两种主流的结构：客户端-服务器体系结构与 P2P（对等）体系结构

#### 客户-服务器体系结构C/S

服务器：主机需要永远在线；**永久不变的IP地址**（或者需要不变的域名）；有用于**扩展**的服务器群（防止故障）

客户端：与服务器通信；间歇性连接（不需要一直连接，需要时连接即可）；可以使用动态 IP 地址。

客户端发送请求，服务端根据请求返回相关服务结果；一般服务端不会主动向客户端发送内容。

> 常见的 C/S 模式服务：Web、FTP、Telnet 和电子邮件

![image-20220403110937576](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAOdaJAuQqKbRU6rpjgauR-MmAL6sgQAApUVAAIh_YBUfP_0F8JEKjU2BA.png)

#### P2P（对等）体系结构

没有永远在线的服务器，即没有服务器中转，两个端系统之间直接通信

**对等体**（两个对等的端系统）之间间歇式连接，IP地址变化

<mark>高度可扩展但难以管理</mark>

> 适用于流量密集型的应用

![image-20220403111044753](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAOeaJAuUNjYlVf35rE6hiB3FHbp_00AApYVAAIh_YBUJtq_ZJgW8Ro2BA.png)

P2P 模型从本质上来看仍然是使用客户/服务器方式，只是对等连接中的每一个主机即是客户又是服务器。多个客户机之间可以直接共享文档。

#### 混合 C/S 加 P2P 的体系结构

:one: **Skype**

> 基于ip的P2P应用程序
>
> 存在集中式服务器用于查找远程方地址。查找到地址后，
>
> 客户端-客户端之间直接连接，不经过服务器

:two: **即时通信**

> 两个用户之间的聊天是P2P
>
> 集中式服务：客户端在线检测/位置
>
> > 当用户上线时，向中央服务器注册IP地址
> >
> > 用户联系中央服务器，查找好友的IP地址
> >
> > 在通信时，用户之间是 P2P 的

### 2、进程通信

进程：运行中的程序。

:one: 在同一个主机中，两个进程使用<mark>进程间通信（IPC）(由操作系统定义)</mark>进行通信。

:two: 不同主机上的进程通过<mark>交换消息</mark>进行通信

#### 客户和服务器进程

客户端进程：发起通信的进程

服务器进程：等待其他进程联系的进程，自身不主动发起通信

#### 进程与计算机网络之间的接口

进程通过网络通信时，必须使用 socket 套接字。

进程通过一个称为 socket 套接字的软件接口向网络发送报文和从网络接受报文

> 进程可类比于一座房子:house: ， 而它的套接字可以类比于它的门:door:。 当一个进程想向位于另外一台主机上的另一个进程发送报文时，它把报文推出该门(套接字)。 
>
> 该发送进程假定该门到另外一侧之间有运输的基础设施，该设施将把报文传送到目的进程的门口。
>
> 一且该报文抵达目的主机，它通过接收进程的门(套接字)传递，然后接收进程对该报文进行处理。

![image-20220403111650959](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAOfaJAuYMbGgf1gw6ijuW3MHwLjAQEAApcVAAIh_YBUDGewzCIcRTU2BA.png)

套接字是同一台主机内**应用层与传输层**之间的接口（不过它不属于任何一层）。由于该套接字是建立网络应用程序的可编程接口，因此套接字也称为<mark>应用程序和网络之间的应用程序编程接口（API）</mark>。

Socket 下方的层都是操作系统控制的（传输层及以下），应用程序无法直接操纵下层的东西，只能在应用层使用 Socket 进行通信。

> **传输层为用户提供的资源是：TCP 和 UDP**（就是传输层的两种协议）

#### 进程寻址

为了接受报文，进程需要有标识符。一台机器上可能存在很多网络程序，那么通过 IP 地址把数据发送到机器上时，操作系统该把数据该交给哪个程序呢？

> :question: 运行进程的主机的IP地址(32位)是否足以识别进程?
>
> :label:不，许多网络通信进程可以运行在同一主机上
>

**标识符**包括与主机上的进程关联的 <mark>**IP 地址和端口号**</mark>。端口号用于区分同一机器运行的不同网络通信进程。

> 为什么不直接使用进程的 pid 呢？因为进程 pid 会随时变化，不是固定的。

常见接收端端口号：

**HTTP 服务器：80**

**SMTP 邮件发送服务器：25**

网络请求接收端的端口号通常是静态的，而发送网络请求端的端口号通常是动态的：随便开个 10000 以上的端口号用于临时发送和接受；之后需要发送请求时，再开另一个空闲端口号就行了。

### 3、应用层协议的定义

应用层协议定义了：

> :one: 交换的报文**类型**，例如请求/响应
>
> :two: 消息的**语法**：消息中的哪些字段，字段长度多少，是什么数据类型
>
> :three: 字段的**语义**：字段中信息的含义
>
> :four: 进程何时以及如何发送和响应报文的**规则**

RTP：实时传输协议

种类：

> :one: 公共协议：在 RFC[请求注解（Request For Comments）] 文件中定义；允许互操作
>
> 例如，HTTP, SMTP, BitTorrent（位流，就是种子下载那种协议）
>
> :two: 专用协议：例如，Skype, ppstream

**应用层只是网络应用的一部分**

### 4、互联网上的 QoS(服务质量)要求

在网络通信时，我们通常需要关注哪些参数？什么参数可以描述通信的质量？

:one: **丢包率 data loss**

一些应用程序(如音频、视频)可以承受一些损失

其他应用程序(例如，文件传输，telnet)需要100%可靠的数据传输

:two: **实时性 timing**

一些应用程序(如网络电话、PvP 游戏)需要低延迟才能“有效”。否则会出现诡异且让程序无法使用的问题。

其他程序（比如电子邮件、网页访问）的实时性要求不高

:three: **吞吐量 throughput**

一些应用程序(如多媒体)需要一定的吞吐量才能“有效”：带宽敏感应用

> 比如看 b 站视频的时候，如果带宽只有 50kb/s，那就只能看 480p 的视频了，体验会非常不好

其他应用程序(“弹性应用程序”)利用他们所获得的任何吞吐量

:four: **安全 security**

加密的数据，数据的完整性

比如敏感信息的传输（更改密码的请求）等内容需要高安全性

> 其他的 QoS：jitter（抖动，指包间隔的变化）
>
> 我们希望包发送的间隔和到达的间隔一致。如果在流式传输并播放音频，那么包间隔突然变大的话，会导致一段时间没有音乐；包间隔突然变小的话，会导致音乐加速。
>
> 大部分情况下，由于我们无法控制网络核心（路由器），抖动是无法避免的。一个解决方法是缓存：接收端开辟缓冲区，在接收到数据时，额外接收一段时间的数据，存储到缓冲区中，然后按正确的间隔播放早些时候缓冲接收到的数据，这样只要带宽足够，就不会出现抖动问题了。
>
> 带宽不够导致缓存长度不够时，接收端可以直接暂停播放，直到带宽足够、缓存接收速度足够之后再播放。大部分视频网站都是这么做的。

**一些常用应用的需求**

| 应用程序        | 丢包           | 吞吐量                                   | 时间敏感性                                   |
| --------------- | -------------- | ---------------------------------------- | -------------------------------------------- |
| 文件传输        | 不允许         | 弹性的                                   | 不敏感                                       |
| e-mail          | 不允许         | 弹性的                                   | 不敏感                                       |
| Web文档         | 不允许         | 弹性的                                   | 不敏感                                       |
| 实时音频/视频   | 容忍一定的丢包 | 音频: 5kbps-1Mbps<br />视频:10kbps-5Mbps | 敏感：数百毫秒                               |
| 存储式音频/视频 | 容忍一定的丢包 | 音频: 5kbps-1Mbps<br />视频:10kbps-5Mbps | 敏感：几秒                                   |
| 互动游戏        | 容忍一定的丢包 | 几 kbps                                  | 敏感：数百毫秒                               |
| 实时发信息      | 不允许         | 弹性的                                   | 是和不是（可以有几秒延迟，但不能大到几分钟） |

### 5、因特网提供的传输服务

从应用层向下看，从应用层-传输层的角度看，传输层只是对上层应用提供了两种通信方式选择：TCP 协议和 UDP 协议。只有这两种可选的传输层通信方式。

> 在传输层章节，我们会更加详细的学习这两种服务。

#### TCP 传输控制协议（Transmission Control Protocol）服务

TCP 就叫”传输控制协议“，它是可靠的（不会丢包，丢包会重传），不会有差错（包的内容不会出错），顺序一定（发送包的顺序和接受包的顺序一样）

> 不过并不保证每次上层发送内容都发一个 TCP 包；TCP 可能会把上层的多次发送内容捆绑起来发一个包，或者把上层的一个发送内容分出多个包发送。

:one: **连接管理**：客户端和服务器进程之间需要连接才能发送数据

> 这个连接是概念上的，不是实际意义上的建立新“物理连接”，主要用于让双方都开启发送/接收缓存。
>
> TCP 是全双工连接的（发送数据时也可以收数据，反之亦然）。

:two: **可靠性控制**：发送和接收过程之间的可靠传输

TCP 需要三次握手后才能建立连接

:three: **流量控制**：发送方不会淹没接收方

通过算法，在接收端的缓冲区已满时降低发送速度，防止接收端缓冲区溢出导致数据无法接受，白白传输了。

:four: **拥塞控制**：网络过载时对发送方进行节流

在路由器缓冲区将满，快要丢包时限制发送端的速度，防止大量丢包的发生。

总结：**三控一管**：可靠性控制、流量控制、拥塞控制；连接管理。

<mark>不提供</mark>：实时性，最小吞吐量保证（无法保证拥有特定大小的带宽），安全性

> 因特网界研制了 TCP 的加强版。称为安全套接字层 Secure Socket Layer (SSL)，这种强化是在应用层上实现的，和 TCP 本身没关系

#### UDP 用户数据报协议（User Datagram Protocol）服务

发送和接收过程之间**不可靠的数据传输**

<mark>不提供</mark>：连接管理，可靠性（可能丢包，而且丢了就真没了），流量控制，拥塞控制，实时性，吞吐量保证，安全性

好处：保证应用层要求发送一个数据时，UDP 就一定发送一个包，不会出现“多个数据打一个包”的问题。

UDP 的特点是**“best effort“**：尽最大的努力快速发送。TCP 由于存在流量控制和拥塞控制，有时会主动限制自己的发送速率；而 UDP 不会限制。

#### 流行的因特网应用机器应用层协议和支撑的传输协议

| 应用         | 应用层协议                          | 支撑的传输层协议      |
| ------------ | ----------------------------------- | --------------------- |
| 电子邮件     | SMTP [RFC 2821]                     | TCP                   |
| 远程终端访问 | Telnet [RFC 854]                    | TCP                   |
| 网页         | HTTP [RFC 2616]                     | TCP                   |
| 文件传输     | FTP [RFC 959]                       | TCP                   |
| 流式多媒体   | HTTP (eg Youtube),   RTP [RFC 1889] | TCP or UDP(局域网内） |
| 网络电话     | SIP, RTP, proprietary               | 通常是UDP             |

> 电子邮件其实还有 IMAP 和 POP3 协议
>
> RTP 协议是 Realtime transport protocol，实时传输协议，规定了如何传输数据和如何传输控制信息（由 RTCP：实时传输控制协议实现）
>
> 很遗憾，RTP 虽然名字带实时，但保证不了实时性，因为其传输层协议 TCP 和 UDP 没一个是能保证实时性的。
>
> SIP（Session Initiation Protocol，会话发起协议）用于建立、修改和终止多媒体会话（如网络电话、视频）。

## 二、Web 和 HTTP

Web 页面由**对象**组成：对象可以是 HTML 文件，JPEG 图像，Java applet，音频文件，…

Web 页面使用 HTTP 协议传输（Hyper text transfer protocol）

主页（Home page）是其中的第一个对象。

Web 页面由**基本 HTML (超文本标记语言)文件**组成，其中包括几个引用的对象

每个对象都可通过 URL （Unified resource locator，统一资源定位器，其实就是链接）寻址：

URL 链接分为如下几部分：

![![image-20220303175113350](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/qshell/image-20220303175113350.png)](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAOgaJAuYwaC5LOJ73S2R7ir5xKHzqwAAgLIMRsh_YBUT51jmHRH7mIBAAMCAAN4AAM2BA.png)

someschool.edu 是域名。域名可以包含多级标签，层级由注册与配置决定。

路径名就是域名后的所有内容。路径名指示了浏览器想要访问网站上的什么资源。

### 1、HTTP 概况

HTTP：hypertext transfer protocol 超文本传输协议

Web 采用的应用层协议：用于通信

HTTP 协议采用客户端/服务器模型

> 客户端：请求、接收、显示 Web 对象的浏览器
>
> 服务端：Web 服务器发送对象来响应请求

![image-20220403113429373](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAOhaJAuZtYP-3JYLgJ4jW1PJrWEOEUAAgPIMRsh_YBU9lnDZFJh7e0BAAMCAAN5AAM2BA.png)

HTTP 使用 TCP 作为它的支撑传输协议。

> 使用 TCP 时进行三次握手的目的：
>
> 1. 在通信双方的机器上开辟缓冲区
> 2. 交换部分初始变量

> :one: 客户端发起 TCP 连接(创建套接字)到服务器，目标为端口 80
>
> :two: 服务器接受来自客户端的 TCP 连接
>
> :three: 浏览器(HTTP客户端)和Web服务器(HTTP服务器)之间交换 HTTP 消息(应用层协议消息)。在传输层上，信息通过 TCP 连接发送。
>
> :four: TCP 连接关闭

HTTP 是一个**无状态 stateless 的协议**：服务器不保存以前的客户端的请求信息，因为保存这些状态十分复杂。

> 注：使用 Session，Access Token 之类的方法存储用户信息不算在内；你就说 Session 是不是在 HTTP 连接里定义的吧？显然不是。
>
> 事实上，Session 的存储也和 HTTP 没关系，一般是直接存在内存/存到 Redis 里头。

### 2、非持续连接和持续连接

非持续连接为 HTTP 1.0 版本的协议；持续连接为 HTTP 1.1 版本协议。

#### 非持续的 HTTP：Non-Persistent HTTP

<mark>非持续连接</mark>：每个请求/响应对是经过一个单独的 TCP 连接发送；一个 TCP 连接最多发送一个对象。发送完一个对象后，TCP 连接立刻关闭。

假设用户进入网址：`www.someSchool.edu/someDepartment/home.index`，其中包含了对十张JPEG图形的引用，这十一个对象位于同一个服务器中。

> :label: JPEG（ Joint Photographic Experts Group）即联合图像专家组，是用于连续色调静态[图像压缩](https://baike.baidu.com/item/图像压缩/8325585)的一种标准，[文件后缀名](https://baike.baidu.com/item/文件后缀名/492702)为.jpg或.jpeg，是最常用的图像文件格式

过程如下：

> :one: HTTP 客户进程在端口号 80 发起一个到服务器`www.someSchool.edu`的 TCP 连接,
> 该端口号是 HTTP 的默认端口。在客户和服务器上分别有一个套接字与该连接相关联。
>
> :two: HTTP 客户经它的套接字向该服务器发送一个HTTP请求报文。请求报文中包含了
> 路径名`/someDepartment/home.index` 。
>
> :three: HTTP 服务器进程经它的套接字接收该请求报文，从其存储器(RAM 或磁盘)中
> 检索出对象`www.someSchool.edu/someDepartment/home.index`，在一个 HTTP 响应报文中封装对象，并通过其套接字向客户发送响应报文。
>
> :four: HTTP 服务器进程通知 TCP 断开该 TCP 连接。(但是直到 TCP 确认客户已经完整地收到响应报文并发送确认报文为止，它才会实际中断连接。)
>
> :five: HTTP 客户接收响应报文，TCP 连接关闭。该报文指出封装的对象是一个 HTML 文件，客户从响应报文中提取出该文件，检查该 HTML 文件，得到对 10 个 JPEG 图形的引用。
>
> :six: 对每个引用的 JPEG 图形对象重复前 4 个步骤。

> 三次握手：TCP 发送端准备建立连接时算一次；TCP 接收端收到后返回一次“接受”报文；TCP 发送端接收到“接受”到文之后，再发送一次确认报文。

非持续性连接中每个 TCP 连接只传输一个请求报文和响应报文，因此上例中当用户请求该 Web 页面时需要产生 **11 个 TCP 连接**

<mark>**RTT(round trip time)**</mark> 的定义:往返时间，一个小数据包在客户端和服务器之间往返传输的时间。

全部的时间 = 2RTT+文件发送时间

![image-20220308102712563](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAOiaJAuayiGa5t7_uwXd1OpO_CZhWkAAgTIMRsh_YBUYdZ50tN1CZEBAAMCAAN4AAM2BA.png)

2RTT 是指：在初始化 TCP 连接的握手过程中会消耗一个 RTT 的时间；传送文件时也会额外消耗一个 RTT 时间。

注意 RTT 是**往返时间**而不是单程时间。别自己给 RTT 乘二了。

缺点：持续的关闭-建立连接会消耗更多的服务器资源。且由上方 RTT 计算结果可以看出，非持久性连接在传输时的总时长更长。

#### 持续连接的 HTTP：Persistent HTTP

**持续连接**：客户端和服务器之间可以通过单个 TCP 连接发送多个对象。

非持久的 HTTP 问题:

> 每个对象需要 2 个 RTT
>
> 每个 TCP 连接需要操作系统开销
>
> 浏览器经常打开并行 TCP 连接来获取被引用的对象

持续的 HTTP

> 服务器在发送响应后**保持连接打开**
>
> 在同一客户端/服务器之间通过打开的连接发送的后续 HTTP 消息
>
> 客户端一遇到引用的对象就发送请求
>
> 对于所有被引用的对象，只有一个RTT：**一开始的第一个对象传输由于需要握手，需要两个RTT。后面的对象获取只用 1 个RTT**

### 3、HTTP 报文格式

两种类型的 HTTP 消息:请求 request，响应 response

> 由三部分组成：开始行、首部行、请求/响应体

#### HTTP 请求报文request message

ASCII ((American Standard Code for **Information Interchange**): 美国信息交换标准代码）是基于[拉丁字母](https://baike.baidu.com/item/拉丁字母/1936851)的一套电脑[编码](https://baike.baidu.com/item/编码/80092)系统，主要用于显示现代[英语](https://baike.baidu.com/item/英语/109997)和其他[西欧](https://baike.baidu.com/item/西欧/3028649)语言

> 老师上课甚至讲了一会 II 这两个字母代表什么；不过我感觉这真的不重要吧……

![image-20220316133537668](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAOjaJAufMbkhG3q8ijblx3Uea5jVgQAApgVAAIh_YBUo1pD7mRsXb02BA.png)

请求包含三部分：

1. 请求行：指定请求的 URL，HTTP 协议和请求方法

   注意：主机名由 DNS 服务器转换为 IP 地址，然后 HTTP 直接向此 IP 发送信息。因此，没有必要在请求行中携带主机名（服务器也知道自己是谁呢）

   常见方法有 GET、POST、HEAD、PUT、DELETE、PATCH 等。

2. 请求头：字面意义，包含一些请求信息。常见的有 Content-Type、Cookie、Authorization（如 Bearer Token）等。

3. 请求体：承载请求数据。GET/DELETE 通常不携带请求体，但协议并不禁止。

#### HTTP 响应报文 response message

![image-20220308104134863](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAOkaJAuii704aiOhCWHaaT68BZJeFEAApkVAAIh_YBUyJ-dg6a0PvE2BA.png)

> 许多站点会移除或模糊化 Server 首部以减少指纹信息泄露；也有站点保留该首部用于调试或统计。

同样分为三部分：

1. 状态行：记录 HTTP 版本和响应码
2. 响应头：描述响应的内容（重要的是 Content-Type）
3. 响应体：响应的实际数据与内容

### 4、用户和服务器的交互：cookie

许多主要网站使用 cookie:存储在**客户端**（浏览器）中的小文件；用于身份验证

四个组件:

> :one: 在 HTTP 响应报文中的一个 cookie 首部行（Set-Cookie 行）
>
> 此行由服务器返回给客户端，客户端需要按照服务端的要求保存这些 Cookie
>
> :two: 在 HTTP 请求报文中的一个 cookie 首部行;（Cookie 行）
>
> 浏览器需要读取已经保存且符合路径要求的 Cookie，将其发送到服务器
>
> :three: 在用户端系统中保留有一个 cookie 文件，并由用户的浏览器进行管理;
>
:four: 位于 Web 站点的一个后端数据库（这个一般存的是 Session，内容和用户的 JSESSIONID 一样）

**举例**

> 假设 Susan 总是从家中 PC 使用 InternetExplorer 上网，她首次与Amazon.com 联系。我们假定过去她已经访问过 eBay 站点。当请求报文到达该 Amazon Web 服务器时，该 Web 站点将产生一个唯一识别码，并以此作为索引在它的后端数据库中产生一个表项。<mark> 接下来 Amazon Web 服务器用一个包含 Set-cookie 响应头的 HTTP 响应报文对 Susan 的浏览器进行响应</mark>。
> 例如，`该首部行可能是Set-cookie:1678`
>
> 当 Susan 的浏览器收到了该 HTTP 响应报文时，它会看到该 Set-cookie 头部。<mark>该浏览器在它管理的特定 cookie 文件中添加一行，该行包含服务器的主机名和在 Set-cookie：首部
> 中的识别码</mark>。值得注意的是该 cookie 文件已经有了用于 eBay 的表项，因为 Susan 过去访问过该站点。当Susan 继续浏览 Amazon 网站时，每请求一个Web页面，其浏览器就会查询该 cookie 文件并抽取她对这个网站的识别码，并放到 HTTP 请求报文中包括识别码的 cookie 首部行中。
>
> 如果 Susan 再次访问 Amazon 站点，比如说一个星期后，她的浏览器会在其请求报文中继续放入首部行 cookie：1678。Amazon 将根据 Susan过去在 Amazon 访问的网页向她推荐产品。
>
> ![image-20220403130524420](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAOlaJAummwvFAe8qvIR_4swT7mqDrkAApoVAAIh_YBUqe3h6KLceW02BA.png)
>
> 注意：上方的介绍是相当概念化而简略的，它忽略了服务器可以设置 Cookie 存活时间限制（会话结束后删除？五天？七天？），设置 Cookie 仅在某个子域名下使用。

### 5、Web 缓存(代理服务器)

使用 Web 缓存的原因：**减少客户端请求的响应的时间；改善用户体验；节省主干带宽的流量**。

> 类似于现在的 CDN，如果用户在访问静态资源，将用户请求重定向到较近的服务器上，以减少 RTT（一轮请求-响应时间）；此外，在内网建立 Cache 服务器可以让流量无需经过外网传输，速度更快。

**举例：假设浏览器正在请求对象：http://www.someschool.edu/campus.gif**

> 1)浏览器创建一个到 Web 缓存器的 TCP 连接，并向 Web 缓存器中的对象发送一个 HTTP 请求。
>
> 2)Web缓存器进行检查，看看本地是否存储了该对象副本。如果有，Web缓存器就向客户浏览器用HTTP响应报文返回该对象。
>
> 3)如果Web缓存器中没有该对象，它就打开一个与该对象的初始服务器（即www.someschool.edu)的TCP连接。Web缓存器则在这个缓存器到服务器的TCP连接上发送一个对该对象的HTTP请求。在收到该请求后，初始服务器向该Wb缓存器发送具有该对象的HTTP响应。
>
> 4)当Wb缓存器接收到该对象时，它在<mark>**本地存储空间存储一份副本**</mark>，并向客户的浏览器用HTTP响应报文发送该副本（通过现有的客户浏览器和Wb缓存器之间的TCP连接）。

即缓存服务器在缓存命中时直接向客户端返回缓存内容，缓存未命中时先向原始服务器请求数据，再保存一份到本地，同时返回给客户端。类似计算机里 Cache 的工作原理。

Web cache 的类别：

1. 代理 cache：proxy cache
2. 客户端 cache：client cache
3. 分布式cache：distributed cache
4. 服务端cache：cluster（集群）

我们主要讲解代理 Cache 和客户端 Cache。

> <mark>普遍用的是客户端 cache 和服务端 cache</mark>

![image-20220403131126538](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAOmaJAunXK-PhDQwkFH3XzDqYSBmXYAAgbIMRsh_YBUk0K_EMXV8mYBAAMCAAN4AAM2BA.png)

#### proxy cache

目标:在不涉及源服务器的情况下满足客户端请求

> 用户设置浏览器：通过缓存访问 Web
>
> 浏览器将所有的 HTTP 请求发送到缓存
>
> > 对象在缓冲中则让缓存返回对象；否则从源服务器缓存请求对象，然后返回对象给客户端

:globe_with_meridians: <mark>**举例**</mark>：如下图右两个网络：内部网络和公共因特网的一部分。内部网络是一个高速的局域网，它的一台路由器与因特网上的一台接入路由器通过一条 15Mbps 的链路。这些初始服务器与因特网相连但位于全世界各地。假设对象的平均长度为 1Mb,从机构内的浏览器对这些初始服务器的平均访问速率为每秒 15 个请求。假设 HTTP 请求报文小到可以忽略，因而不会在网络中以及接入链路（从机构内部路由器到接入路由器）上产生什么通信量。我们还假设在图中从接入路由器到任何源服务器和返回路由器的延迟= 2秒。（即 RTT=2s）

![image-20220403135244421](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAOnaJAurthuLnunlDvpW86_JEOT4i0AAp0VAAIh_YBUxT28WJjLTzQ2BA.png)

:one: 对于情况一

> LAN 的利用率为15x1/100=15%
>
> 接入链路的利用率为 15x1/15=100%（每秒 15 个请求，每个请求 1Mb，正好占满 15Mbps）
>
> 对于1个请求（1去1回）：总的延时为=因特网延时+接入链路延时+局域网延时=2s+2/15s+2/100s=2.15s
>
> 2/15s 是接入链路传输速率 / 时间得到的，2/100 同理。
>
> 可以看出，大部分时间（2s）都花在了接入服务器和原始服务器的通信上。

:two: 对于情况二

> 我们拓宽接入链路（结构内服务器-接入服务器）的带宽为 100 Mbps
>
> LAN 的利用率为15x1/100=15%
>
> 接入链路的利用率为15x1/100=15%
>
> 对于1个请求（1去1回）：总的延时为=因特网延时+链路延时+局域网延时=2s+2/100s+2/100s=2.04s
>
> 可见，对延时的改善效果并不好，因为没有节省大头时间：互联网上 2s 的传输时间，仅仅节约了内部网络到接入服务器的传输时间。

:three: 对于情况三

> 不升级链路带宽而是在机构内部服务器上安装一个 Web 缓存器
>
> 我们假设缓冲命中率为 0.4，即 40% 的请求将几乎立即得到满足，60%的请求被原始服务器满足
>
> 对于1个请求（1去1回）：总的延时为=(2s+2/100s+2/100s)x60%+(2/100)x40%=1.37s
>
> 可见，对延时的改善效果很好

#### Client Cache: Conditional Get

**客户端缓存：条件取**

> 为了避免 GET 请求的客户端缓存，很多前端会在发送 FETCH/XHR 请求时在后面跟上时间戳，让浏览器误认为此请求和前面的请求都不同（即使请求 URL 相同）
>
> 一般获取静态资源时不用想办法关掉客户端缓存

保存在服务器中的对象自该副本缓存在客户上以后可能已经被修改了。HTTP 协议有一种机制，<mark>允许缓存器证实它的对象是最新的</mark>。这种机制就是条件 GET（conditional GET）方法。如果：

1. 请求报文使用 GET方法；并且
2. 请求报文中包含一个 “If-Modified-Since” 首部行。那么，这个 HTTP 请求报文就是一个条件 GET 请求报文。

如果服务器发现在请求头的 If-Modified-Since 字段对应的时间之后，服务器对应的内容确实没有更改，就会返回 304 Not Modified 而不返回具体的请求内容；如果服务器资源已经修改/没有此请求头，那么就会正常返回内容。

服务器不返回内容而返回 304 的话，客户端怎么获得内容呢？

缓存器在将对象转发到请求的浏览器的同时，也会在本地缓存了该对象，同时会存储最后修改日期。如果服务器返回 304 Not Modified 的话，客户端会直接读取本地缓存，获取此数据。

在长时间没有请求访问时，本地的缓存会被删除。

#### distributed cache

许多缓存是“合作”的，即多个通过本地网络连接的电脑之间可以共享缓存。

> 本地访问丢失时，向邻居请求缓存（通过 http 协议或ICP）
>

如果邻居没有数据，则访问源服务器

问题：操作不便（怎么找到邻居？怎么确定邻居会不会响应？），一般采用镜像服务器代替。可以在多地放一个镜像服务器，用于加速各地本地的访问。

> 镜像服务器的功能和**原始服务器相同**，可以接受业务，不是 Cache/CDN 等只分发静态内容的东西。

#### server cache:cluster

多台服务器以集群方式构造，每个服务器被称为一个节点。

请求被分配到负载最轻的服务器。每个服务器可以存放相同/不同的内容。

> 即可以设立一个服务器专门放图片等静态资源，其他服务器处理业务

特点：

1. 高并行性、可靠性

2. 需要尽量负载均衡

3. 需要对象定位算法，来确定请求内容位于哪个服务器。

这种方法被广泛的使用。

## 三、因特网的电子邮件

> 虽然 FTP 和电子邮件一点关系都没有，但它还是被放在“电子邮件”目录下了。我不好说……

### 1、FTP—— file transfer protocol

![image-20220308112421791](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAOoaJAuvdvo7LCh77Xj5K20RDtQj8oAAp4VAAIh_YBUNSzlyWMrkZY2BA.png)

此协议用于传输文件，既可以向远程主机传输文件，也可以从远程主机将文件下载到本机。

采用客户机/服务器模型

> 客户端:发起传输（上传或者下载）的端
>
> 服务器:远程主机

FTP 标准: RFC 959

FTP 端口: **21端口**，用于控制连接

#### 独立的控制连接和数据连接

在进行文件传输时，FTP 的客户机和服务器之间要建立**两个TCP**连接，一个用于传输控制命令和响应，称为**控制连接**(21 端口)，一个用于实际的文件内容传输，称为**数据连接**(20 端口)

![image-20220308112628422](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAOpaJAuzctr6DBv29MicHFbHh9cKc8AAqAVAAIh_YBU3Rsd0uyAWmU2BA.png)

连接时，首先建立 21 端口的 TCP 控制连接；客户端通过控制连接进行认证和命令发送。

当客户端发出上传/下载命令时，服务器与客户端建立第二个连接——数据连接。完成传输后，数据连接将会关闭。

- 控制连接是持久性的
- 数据连接是非持久性的，传输完成后就会关闭

FTP 是**有状态**的协议，和 HTTP 不同。服务器需要保存之前客户端的认证信息和当前查看目录等信息。

### 2、电子邮件

> 电子邮件：Electronic Mail

三个主要组件:

1. 用户界面/代理（如浏览器，邮件应用，比如 Outlook, Gmail 客户端）user agent

2. 邮件服务器 mail server

3. 简单邮件传输协议 SMTP

   其实还有接受协议 IMAP，不过我们似乎不讲

以下通过 Alice 发电子邮件给接收方 Bob 的场景进行说明。

![fded854f6e442ef4795d44535383dc74](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAOqaJAu3WdjRiDAtbfXCSU3CuLD6wIAAqEVAAIh_YBUn4J3HvMnp0o2BA.png)

#### 用户代理

用户代理允许用户阅读、回复、转发、保存和撰写报文。微软的 Outlook 和 Apple Mail 客户端是电子邮件用户代理的例子。当 Alice 完成邮件撰写时，她的邮件代理向其邮件服务器发送邮件，此时<mark>邮件放在邮件服务器</mark>的外出报文队列中。当 Bob 要阅读报文时，他的用户代理在其邮件服务器的邮箱中取得该报文。

#### 邮件服务器

邮件服务器形成了电子邮件体系结构的核心。每个接收方（如Bob）在其中的某个邮件服务器上有一个**邮箱**（mailbox）。Bob 的邮箱管理和维护着发送给他的报文。一个典型的邮件发送过程是：从发送方的用户代理开始，传输到发送方的邮件服务器，再传输到接收方的邮件服务器，然后在这里被分发到接收方的邮箱中。当 Bob 要在他的邮箱中读取该报文时，他的邮件服务器使用用户名和口令来鉴别 Bob 的身份。

当邮件无法发送成功，在发送方邮件服务器的一个报文队列中保持该报文并在以后再次尝试发送，多次尝试失败后则进行删除并通知给发送方。

SMTP 协议在邮件服务器之间发送邮件消息，也可以将邮件从客户端发送到发送端的邮件服务器。

> 客户端:发送邮件服务器
>
> 服务端:接收邮件服务器

#### SMTP

使用 TCP 在客户端和服务器之间可靠地传输邮件消息，<mark>**端口号为25**</mark>

直连:发送服务器到接收服务器，没有通过中间服务器

> 命令:ASCII文本
>
> 响应:状态码和短语

早期 SMTP 要求 7 位 ASCII；现代通过 MIME、8BITMIME 扩展以及 SMTPUTF8 支持非 ASCII 内容与国际化地址。

SMTP 使用的是持续连接

:label: 具体的场景说明

> Alice 发邮件给 Bob
>
> :one: Alice 调用她的邮件代理程序并提供Bob的邮件地址（例如bob@ someschool.edu)，撰写报文，然后让客户端程序发送该报文。
>
> :two: Alice 的用户代理把报文发给她的邮件服务器，在那里该报文被放在报文队列中。
>
> 这段发送可能是直接通过 HTTP 传输消息，也可能通过 SMTP。
>
> :three: 运行在 Alice 的邮件服务器上的 SMTP 客户端发现了报文队列中的这个报文，它就创建一个到运行在 Bob 的邮件服务器上的 SMTP 服务器的 TCP 连接。
>
> :four: 在经过一些初始 SMTP 握手后，SMTP 客户端通过该 TCP 连接发送 Alice 的报文。
>
> :five: 在 Bob 的邮件服务器上，SMTP 的服务器端接收该报文。Bob 的邮件服务器将该报文放入 Bob 的邮箱中。
>
> :six: 在 Bob 方便的时候，他调用用户代理下载邮箱中的邮件，阅读到了这封邮件。
>
> ![image-20220403145842097](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAOraJAu4MTmn5mV74asOwHCdEthDTsAAgfIMRsh_YBUkQNxHIjMt0QBAAMCAAN5AAM2BA.png)

SMTP 是一种基于文本传输的协议，而且是服务器-客户端交互式的。也可用作调试的交互式会话，但实际收发由程序完成。

SMTP 使用**持久性**的 TCP 连接。

### 3、与 HTTP 的对比

**相同点**

> 这两个协议都用于从一台主机向另一台主机传送文件
>
> 当进行文件传输时，持续的 HTTP（HTTP 1.1） 和 SMTP 都使用持续连接

**区别**

> :one: HTTP 是一个**拉协议**(pull protocol)：TCP连接是由想要接收文件的机器发起的；SMTP是一个**推协议**(push protocol)：TCP连接是由要发送该文件的机器发起的
>
> 此外，SMTP 只能向服务器推送要发送的邮件数据，不能从服务器拉取邮件。因此，收邮件的功能由 IMAP 协议完成。
>
> :two: SMTP 要求每个报文使用 7bit ASCII 码格式，HTTP数据不受这种限制
>
> :three: HTTP将每个对象封装到他自己的HTTP响应报文中，而SMTP将所有报文对象都放在一个报文中

### 4、邮件报文格式

![image-20220403192705203](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAOsaJAu7frScDa06RHa-AEGjb5g_DgAAqIVAAIh_YBUZQEK-dOpwlg2BA.png)

邮件头：发送者，接受者和主题

邮件体：邮件的正文内容

### 5、邮件访问协议

![image-20220403193312668](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAOtaJAu8FTKTNrg0QAB6aYymUavMUt2AAIJyDEbIf2AVNK6_RTCgrPfAQADAgADeQADNgQ.png)

SMTP：发送/存储到接收者的服务器

邮件访问协议:从服务器取回邮件。SMTP 不支持这种“拉”的操作，因此需要其他协议完成

:one: POP3: Post Office Protoco-version 3 第三版邮局协议

> 授权(代理<——>服务器)和下载，端口:110
>
> POP3跨会话是<mark>无状态的</mark>

:two: IMAP: Internet Mail Access Protocol 因特网邮件访问协议

> 更多功能(更复杂)，端口:143
>
> 操作服务器上存储的MSGS
>
> IMAP 保持用户跨会话的状态:<mark>有状态的</mark>

:three: HTTP: gmail, Hotmail, Yahoo 邮件等。大部分邮件服务器商提供的网页客户端都通过 HTTP 协议直接拉取邮件。

SMTP 的端口为 25。

### 5、非 ASCII 数据的 MIME 扩展

MIME：Multipurpose Internet Mail Extension 多用途互联网邮件扩展，RFC 2045, 2056

对于非 ASCII 文本，需要在 msg 中添加额外的头信息

消息头中的其他行声明 MIME 内容类型

> 内容类型（Content-Type 头）:提醒接收器使用哪个显示程序
>
> 内容可以是 Text 文本，Image 图片， Audio 音频，Video 视频，Application 应用，Multipart 多物品（多部分附件）
>
> 内容传输编码（Content-Transfer-Encoding 头）: ASCII 编码时使用的编码类型

## 四、DNS：域名服务

> DNS：Domain Name System

主机的一种标识方法是用它的主机名 hostname，例如www.baidu.com

也可以使用 IP 地址进行标识，例如192.168.1.202

域名：baidu.com

<mark>IP 和域名是多对多的关系</mark>

大家上网时，普遍都通过主机名访问网站而非 IP 地址，毕竟一个英文单词可比四段 0-255 的数字好记太多了

DNS 负责将用户输入的主机名转换为对应的 IP 地址，以找到发送报文的目标。

ps：**DNS 属于网络内核的功能，但是放在网络边缘**

> 因特网：“瘦内核，胖边缘”，复杂的功能都放在边缘
>
> ATM 网络：“胖内核，瘦边缘”

### 1、DNS 提供的服务

DNS 是

:one: 一个由分层的 DNS 服务器实现的分布式数据库

即 DNS 具有很多世界各地的分散的服务器；各地的用户都可以查询最近的数据库，以得到域名映射信息，不会出现“某个地区访问 DNS 服务器很慢“的问题。

此外，DNS 还是分层的，下面会具体提到。

 :two: 一个使得主机能够查询分布式数据库的应用层协议

<mark>DNS 运行在 UDP 上，使用 53 号端口</mark>

> 传统 DNS 报文是明文传输的。现代可选加密传输：
> - DoT（DNS over TLS，端口 853）
> - DoH（DNS over HTTPS，走 HTTPS 端口，对代理更友好）

提供的服务如下：

> :one: 最主要：主机名到 IP 地址的转换
>
> 主机名和 IP 地址是多对多的关系。对于大型网站，通常采用很多服务器构成集群接收请求，这些服务器可能具有多个 IP，但都在一个主机名下。
>
> 同一个网站也可以买多个域名，让它们都指向自己。比如 chat.openai.com 和 chatgpt.com 都指向 GPT 的官网。
>
> :two: 主机别名:主机别名更容易记忆
>
> 本质上是多个域名指向同一个主机名。
>
> :three: 邮件服务器别名
>
> :four: 负载分配：DNS 在冗余的服务器之间进行负载分配，繁忙的站点，如 cnn.com 被冗余分布在多个服务器上，每个服务器运行在不同的端系统上，每个有不同的 IP 地址。一个主机对应有一个 IP 地址集合，DNS 数据库存储着这些  IP 地址集合。当客户对映射到某地址集合的名字发出一个 DNS 请求时，该服务器用 IP 地址的整个集合进行响应，但在每个回答中循环这些地址次序（改变 IP 地址的顺序）。因为客户通常总是向 IP 地址排在最前面的服务器发送 HTTP 请求报文，所以 DNS 就在所有这些冗余的 Web 服务器之间循环分配了负载。

### 2、DNS 工作机理概述

集中式的 DNS 服务器缺点：单点故障、通信容量、远距离的集中式数据库造成延时长、维护困难

#### 分布式、层次数据库

![image-20220403193754596](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAOuaJAu_iySVd-raDT_9zBY8yg4BtkAAqQVAAIh_YBUIbA7zGDqe102BA.png)

**根域名服务器**：400多个，13个组织管理

> 根域名服务器用来管辖顶级域名，它并不直接把查询的域名转换成IP地址，而是告诉本地域名服务器应当找哪一个顶级域名服务器进行查询。
>
> 本地域名服务器仅仅无法解析域名时，才会访问上层服务器（比如顶级域/根域名服务器）
>
> 根域名服务器**并没有存储所有内容**，只是告诉本地域名服务器该找哪个 TLD 服务器。

**顶级域(TLD)服务器**：负责一个域名后缀的服务器，比如 com DNS 服务器就负责所有 .com 后缀的域名解析

**授权 DNS 服务器**：域名注册到的 DNS 服务器，一定保留所有在此处注册的域名的信息。域名记录项一直存在，只要不欠费

> 负责一个区的域名服务器

本地 DNS 服务器：不属于上面的层次结构，通常与主机位于同一个局域网中。可以查询所有缓存的记录，用于加速访问。

相当于一个代理缓存服务器，类似 Web Cache 中的“代理服务器”。

#### DNS 域名解析示例

主机向本地域名服务器的查询都是采用**递归查询**，如果主机所在询问的本地域名服务器不知道被查询域名的IP地址，那么本地域名服务器就以 **DNS 客户**的身份向其他域名服务器继续发出查询请求报文。

例如：主机在 cis.poly.edu 需要 IP 地址 gaia.c.s.umass .edu

:one: 迭代式查询（接近广度查询）

当根域名服务器收到本地域名服务器的迭代查询请求报文时，要么给出所要查询的IP地址，要么告诉本地域名服务器“下一步要向哪一个域名服务器进行查询”，然后让本地域名服务器进行后续查询。

这种查询方式其实也是混合的，因为主机向本地域名服务器的查询都是采用**递归查询**

以 Local Server 为中心查询。Local Server 根据其他服务器的信息，主动向其他服务器获取信息。

1. 访问根 DNS 服务器，根服务器可能会直接返回 IP 地址/返回包含此域名结果的 DNS 服务器的地址
2. 如果没有结果，访问根服务器给出的 TLD 服务器地址
3. 如果 TLD. 服务器没有结果，再访问 TLD 给出的授权 DNS 服务器地址，然后肯定会得到结果（因为域名就是在此服务器注册的）

![image-20220403194630915](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAOvaJAvDc2O7G0BdaHw2iPM4heNynQAAqYVAAIh_YBUfSHDTiAwKPY2BA.png)

缺点：所有查询都由本地 DNS 服务器发起，负担比较重。

:two: 递归式查询（接近深度查询）

本地域名服务器只需要向根域名服务器查询一次，其他后面的几次查询都是在其他几个域名服务器之间进行的

![image-20220403194644912](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAOwaJAvHQlNN_KWn_E5PpfmdO-xRAkAAqcVAAIh_YBUOB6a7ILqZkA2BA.png)

使用较多。这种方法相当于根服务器帮你完成了询问 TLD 服务器和注册服务器的工作，因此本机不需要发送那么多请求了。

:three: 混合式查询

#### DNS 缓存和更新记录

在一个请求链中，当某个 DNS 服务器接收到一个响应，他能缓存包含在该响应中的任何域名信息。

此外，除了授权服务器（域名注册到的服务器）不能删除域名记录外，其他 DNS 服务器都可以在长时间无人访问时删除缓存条目，以减少数据库大小。在查询时，DNS 服务器可以再向授权服务器重新查询记录。

举一个例子，假定主机 `apricot.nyu.edu` 向 `dns.nyu.edu`查询主机名 `cnn.com`的 IP 地址。此后，假定过了几个小时，纽约大学的另外一台主机如`kiwi.nyu.edu`也向`dns.nyu.edu`查询相同的主机名。因为有了缓存，该本地 DNS 服务器可以立即返回 `cnn.com` 的 IP 地址，而不必查询任何其他 DNS 服务器。本地 DNS 服务器也能够缓存 TLD 服务器的 IP 地址，因而允许本地 DNS 绕过查询链中的根 DNS 服务器，直接向顶级域服务器查询。事实上，因为缓存，除了少数 DNS 查询以外，根服务器都被绕过了，很少被真正访问。

### 3、DNS 记录和报文

共同实现 DNS 分布式数据库的所有 DNS 服务器存储了每个网站的信息，这一信息的存储形式为“资源记录”（RR)

RR 的格式如下：

```c
(Name，Value，Type，TTL)
```

TTL 是该记录的生存时间，它决定了资源记录应当从缓存中删除的时间。在下面给出的记录例子中，我们忽略掉 TTL 字段。<mark>Name 和 Value 的值取决于Type</mark>

> TTL 表示该记录的存活时间，即在多久没有被访问后可以被删除。

:one: 如果 Type =A，则 Name 是主机名，Value是该主机名对应的IP地址。因此，一条类型为A 的资源记录提供了标准的主机名到IP 地址的映射。例如 `( relay1.bar.foo.com，145.37.93.126，A）`就是一条类型A记录。

即 主机名 - IP 地址映射

:two:如果 Type =NS，则 Name 是个域（如foo.com），而Value是个知道如何获得该域中主机 IP 地址的权威 DNS 服务器的主机名。这个记录用于沿着查询链来路由 DNS查询。例如`（foo.com，dns.foo.com，NS)` 就是一条类型为NS的

即 域名 - 对应 DNS 服务器映射

> 请区分主机名和域名：主机名是任何一个多部分的网址，域名仅仅指二级的网站（比如 baidu.com），前面不能再加一节。

:three: 记录如果Type = CNAME，则Value 是别名为Name的主机对应的规范主机名。该记录能够向查询的主机提供一个主机名对应的规范主机名，例如`（foo.com，relay1.bar.foo.com，CNAME)` 就是一条CNAME类型的记录。

即 别名 - 规范主机名的映射

:four: 如果Type = MX，则 Value 是个别名为 Name 的**邮件服务器**的规范主机名。举例来说，`(foo.com，mail.bar.foo.com，MX）`就是一条 MX 记录。MX 记录允许邮件服务器主机名具有简单的别名。值得注意的是，通过使用 MX 记录，一个公司的邮件服务器和其他服务器（如它的 Web 服务器）可以使用相同的别名。为了获得邮件服务器的规范主机名，DNS 客户应当请求一条 MX 记录；而为了获得一般服务器的规范主机名，DNS 客户应当请求 CNAME 记录。

即 别名 - 对应邮件服务器的映射

#### DNS 协议，报文

DNS 协议：查询和应答报文，**报文格式相同**

> HTTP 的请求和响应报文存在不同；DNS 的请求和应答报文完全一样

![image-20220316151736371](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAOxaJAvLbqvkz5krjmMXWqrShzhyFQAAqkVAAIh_YBUxZZAh0lho9I2BA.png)

前面 12 个字节是首部区域 header，其中的“标志”部分说明了这是 DNS 请求报文还是响应报文。

标志部分同样说明了这是递归查询成功还是需要递归查询。

DNS 采用 UDP 协议通信。因此可能出现丢包，导致“找不到xx网站“的错误。为什么一个经常使用的协议要采用 UDP 这种不可靠的传输层协议呢？

1. 查询 DNS 时，常常只需要使用本地 DNS 服务器即可得到结果，数据包传输距离很近，因此丢包的概率较小。
2. 为了追求速度，UDP 请求时延更低（无三次握手）。当报文超出 UDP 长度或需可靠传输时，DNS 会回退/改用 TCP。

## 五、搜索引擎

万维网可以视作一个大的`图`：页面是一个`结点`；url 是一个`边`，将用户从一个页面（节点）引导到另一个页面（节点）

**索引**

> 将页面的关键字作为索引
>
> 关键字<--> url 之间为多对多关系

提取关键字的方法：

- 访问 url，使用爬虫抓取网站的页面
- 使用关键字提取算法，提取页面上的关键字

需要三种数据结构

:one:  线性数组：URL 表，存储发现的 url 指针（指向 url）和标题/页面指针

:two:  堆：存储可变长度的标题/页面和 url

:three:  哈希表：存储每个 url 是否已经访问过

索引创建具体过程

:one: 第一:搜索（广度优先搜索）

> 使用递归过程：process_url，输入 url，对其求哈希值，利用哈希表确定 url 是否在 URL 表中
>
> 如果 url 在 URL 表中，跳过，处理下一个 url；否则访问页面并将 url 和标题/页面放入堆中，然后哈希 url 存入哈希表，并在线行数组中处理指针
>
> 递归的使用 process_url 方法，如上所示处理页面中的所有 url(超链接)

:two: 第二:索引

> 对于 URL 表中的每个条目，寻找堆中已经提取的标题和页面中的**关键字**
>
> 将关键字指向对应的 URL 表项
>
> 此外，还需要一个排序算法决定同一关键字对应的网站顺序先后。

## 六、Socket 编程

服务器必须在客户端连接前进入运行状态。

服务器必须有一个 socket(套接字)，通过它接收和发送数据。类似地，客户端也需要一个套接字。

套接字由一个端口号标识，和同一主机上的其他套接字相互区分。

客户端需要知道服务器的 IP 地址和 socket 端口号才能进行 socket 连接。

> 也可以使用主机名访问，不过此时需要一次 DNS 查询

socket 编程可以使用 TCP 或者 UDP 协议通信。TCP 协议需要 bind, listen 然后 accept，等待客户端建立连接；UDP 连接只需要 bind, readfrom 然后阻塞等待就行了

UDP 协议通信时，发送端发送的数据报包含了自身的 IP 地址和端口号。因此，接收方可以提取 IP 地址和端口号，发送 UDP 报文回客户端。

由于 UDP 协议和 IP 协议几乎是一样的，没什么封装，因此二者的数据名称有事可以通用，即 UDP 数据既可以叫 UDP 段（传输层），也可以叫做 UDP 数据报（网络层）

> 注意 TCP 发送的内容叫“字节流”，UDP 发送的内容叫做“段“或者”数据报“。

## 练习题

:one: What are features of the TCP/IP Transport layer? (Choose two.)

>  path determination 
>
>  handles representation, encoding and dialog control 
>
>  uses TCP and UDP protocols :white_check_mark:
>
>  packet switching 
>
>  reliability, flow control and error correction:white_check_mark:

:two: Which OSI layer defines the functions of a router? 

>  physical 
>
>  data link 
>
>  network :white_check_mark:
>
>  transport 
>
>  session 

:three: Which type of institution does the domain suffix .org represent? 

>  government 
>
>  education 
>
>  network 
>
>  non-profit :white_check_mark:

:four: What is established during a connection-oriented file transfer between computers? (Choose two.)

> connection-oriented （面向连接）的意思就是指使用 TCP 连接传输，因为 TCP 才是持久化连接的，UDP 是直接发送数据、不需要连接的。
>
> FTP 使用 TCP 协议传输，不过有一种简单 FTP 使用 UDP 协议连接（TFTP, trivial FTP）。题目中强调“connection-oriented“就是为了告诉你这个题目是指 FTP 而不是 TFTP。

在计算机之间的面向连接的文件传输过程中建立了什么?(选择两个)

>  a temporary connection to establish authentication of hosts 
>
>  a connection used for ASCII or binary mode data transfer  :white_check_mark:
>
>  a connection used to provide the tunnel through which file headers are transported 
>
>  a command connection which allows the transfer of multiple commands directly to the remote server system 
>
>  a control connection between the client and server  :white_check_mark:

:five: Which of the following services is used to translate a web address into an IP address?

> DNS :white_check_mark:
>
> WINS 
>
> DHCP 
>
> Telnet 

:six: Which part of the URL http://www.awsb.ca/teacher gives the name of the domain? 

>  www 
>
>  http:// 
>
>  /teacher 
>
>  awsb.ca  :white_check_mark:

:seven: Using the data transfer calculation T=S/BW, how long would it take a 4MB file to be sent over a 1.5Mbps connection? 

>  52.2 seconds 
>
>  21.3 seconds :white_check_mark:
>
>  6.4 seconds 
>
>  2 seconds 
>
>  0.075 seconds 
>
>  0.0375 seconds 

:eight: If a network administrator needed to download files from a remote server, which protocols could the administrator use to remotely access those files? (Choose two.)

>  NFS 
>
>  ASCII 
>
>  TFTP :white_check_mark:
>
>  IMAP 
>
>  FTP :white_check_mark:
>
>  UDP 

:nine: Which of the following protocols are used for e-mail transfer between clients and servers? (Choose three.) 

> TFTP 
>
> SNMP 
>
> POP3  :white_check_mark:
>
> SMTP  :white_check_mark:
>
> IMAP4  :white_check_mark:
>
> postoffice 
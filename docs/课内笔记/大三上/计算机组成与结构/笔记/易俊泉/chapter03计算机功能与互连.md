# 第三章 计算机功能与互连(总线)

## key points

**1、计算机的功能**

> - 指令周期的概念，指令周期的每一个步骤
> - 中断、中断的概念、目的、过程，特别要注意断点的保护和恢复，过程一定要清楚
> - 多重中断的处理方法有几种，各自的优缺点是什么

**2、互连结构：互连结构的概念、传输数据的类型**

**3、总线互联**

> - 总线的概念、关键特征、系统总线的概念、分类、什么是数据总线、它的宽度有什么意义、地址总线、它的宽度又决定什么，典型的控制总线有哪些
> - 总线设计要素有哪些
> - 类型、仲裁方式、特点、时序、总线宽度、数据传输类型

**4、对于PCI，要知道它是专门为高速I/O配置的总线，其他的了解一下就行**

## 3.1 计算机的功能


计算机的基本功能是**执行程序(指令序列)**，以完成特殊任务

CPU是执行指令的组件

> CPU处理一条指令的时间称为指令周期
>
> 指令的执行可以简单地看成两个步骤:
>
> > 读取指令：取指周期
> >
> > 执行指令：执行周期
> > ![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img5/b3d8aa89d8b54fa0a35c14e57475465f.png)

### 3.1.1 指令的读取与执行

在每一个指令周期的一开始，处理器会从内存中获取一条指令。而在一般的处理器中计数器PC保存了下一条要取的指令地址，没有特殊说明，PC会增加，以便取下一条指令。

而取指令会被加载进指令寄存器IR中，然后处理器会解析指令并执行所需的操作。总的来说，这些操作归为4类:

> :one: **处理器—存储器**:数据可从处理器传送到存储器或从存储器传送到处理器。
> :two: **处理器—I/O**:通过处理器和I/0模块之间的传输，数据可传送到或来自外部设备。
> :three: **数据处理**:处理器可以对数据执行一些算术或逻辑操作。
> :four: **控制**:指令可以用来改变执行顺序。

**举例说明**，使用一台包含下图所列特点的假想机器，其处理器包含唯一的一个数据寄存器，被称为累加器(AC); 其指令和数据都是16位长，这样便于用16位的字来组织存储器;其指令格式提供4位的操作码，表示最多可以有2* 4= 16种不同的操作码，最多有21=
4096(4K)个字的存储器可以直接寻址。下面说明部分程序的执行，显示了存储器和处理器寄存器的相关部分
![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img5/602e0aed12284bf6a7c2cd82666b0b10.png)
![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img5/405356687d094ef088753f5eaf62863b.png)
:one: 程序计数器(PC) 的内容是300，即第1条指令的地址。这条指令(其值为十六进制数1940)被装入指令寄存器IR并且PC加1。注意,为简便起见，忽略对存储器地址寄存器(MAR) 和存储器缓冲寄存器(MBR)的使用

:two: **IR中的前4位(第1个十六进制数字)指出要装入累加器(AC)，而其余12位(3个十六进制数字)指定从那个地址(940) 取数据装载**。即地址940的数据0003装人AC。

:three: 从单元301中取下一条指令(5941)， 并且PC加1。

:four: AC中存放的内容和941单元的内容相加，结果放人AC。

:five: 从单元302中取下一条指令(2941)， 并且PC加1

:six: 将AC的内容存人941单元。

在这个例子中，将940单元的内容加到941单元用了3个指令周期，每个指令周期都包含了一个取指周期和一个执行周期。如果用更复杂的指令集，则需要更少的周期。

基本的指令周期所需的状态如下：

:one: **指令地址计算(Instruction address calculation)**: 决定下一条将要执行的指令的地址。通常是将- 一个固定的值与前一条指令的地址相加。例如，如果每条指令有16位长，并且存储器是由16位字构成的，则将原地址加1;如果存储器是由可独立寻址的8位字节构成的，则将原地址加2。
:two: **读取指令(Instruction fetch)**:将指令从存储器单元读到处理器中。
:three: **指令操作译码(Instruction operation decoding)**: 分析指令,以决定将执行何种操作以及将使用的操作数。
:four: **操作数地址计算(operand address calculation)**: 如果该操作包含对存储器或通过I/0的操作数访问，那么决定操作数的地址。
:five: **取操作数(Operand fetch)**:从存储器或从I/0中读取操作数。
:six: **数据操作(Data operation)**: 完成指令需要的操作。
:seven: **存储操作数(Operand storage)**: 将结果写人存储器或输出到I/O。
![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img5/f5eb07f534be48a0b9889674dd7d5197.png)

### 3.1.2中断

**概念**：允许其他模块中断CPU执行序列的机制

**目的**：提升CPU的效率；允许CPU处理紧急事件

**中断的分类**
![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img5/770cc4363e414afab56cafa22c5ad487.png)

下图说明了事件的这种状态。用户程序执行一系列WRITE调用，WRITE调用与处理过程
交错进行。代码段1、2、3是指不包含I/O操作的指令序列。WRITE 调用是对一段I/0程序的调
用，它是执行实际I/0操作的系统实用程序。

![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img5/3bfffcd7ce9a4408b04b3a918ad07fd1.png)
这段I/0程序包含以下三个部分:

:one: 用于为实际I/O操作**准备的指令序列**，在图中标记为4。它可能包括将待输出数据复制到专用的缓冲区，以及为设备命令准备参数。

:two: **实际的I/O命令**。如果没有中断的使用，一旦此命令发出，程序必须等待I/0设备完成需要的功能( 或周期性地测试设备)。程序可以通过简单地重复执行一个测试操作来决定该I/0操作是否完成。

:three: **完成该操作的指令序列**，在图中标记为5。这可能包含设置标志位来表示操作是成功还是失败。

由于I/O程序挂起，用户程序在WRITE调用这一点会暂停很长一段时间。

##### 1、中断和指令周期

当外部设备准备好接收服务，外部设备的I/O模块发送中断请求信号给处理器。处理器通过挂起当前程序的操作，**跳转**服务于某个特定I/O设备的程序来响应，这个程序被称为**中断处理程序**，并且在设备服务完后恢复原来的执行。中断发生的断点在上图中用星号(*)表示。

为适应中断，将中断周期加人指令周期中，如下图所示。在中断周期中，处理器检查是否发生了
中断，这将由中断请求信号的出现来指示。如果没有中断请求，则处理器继续进入取指周期，读取当前程序的下一条指令。如果出现中断请求，则处理器执行以下操作:

> ●挂起当前正在执行的程序，并保存其状态。保存下一条即将执行的指令的地址以及任何与处理器当前活动相关的数据。
> ●将程序计数器设置为中断处理程序的起始地址。

![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img5/897544602bea41feaddb9c3a48fa4529.png)
加入了中断周期处理的指令周期状态图如下：

![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img5/a94a5e5b17dc41b8a06031e8d244ed48.png)

##### 2、多重中断

**概念**：顾名思义，多重中断就是在同一时间发生多个中断

对于多重中断，有两种解决办法：**禁止中断与定义优先级**

:one: 禁止中断(disable interrupts)

禁止中断就是在中断处理过程中禁止其他中断，此时的中断严格按照顺序处理，等一个中断处理完成以后不用等到用户程序恢复就可以再次允许中断

![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img5/1b44dcac4b464c3da365e73672b085e9.png)
![:two: 定义优先级(de](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img5/57bf22d6ed664592b01b04bd52d556f4.png)
f

第二种处理多重中断的方法就是定义中断的优先级，允许优先级高的中断引起低级中断处理程序本身被中断

**举例说明**：一个有3个I/O设备的系统:打印机、硬盘和通信线路，它们的优先级逐个递增，分别是2、4、5。

**一、**用户程序开始于i=0时刻。当t=10时，发生了打印机中断，用户信息放入系统栈，并继续从打印机的中断服务程序(ISR) 开始执行。

**二、**当程序仍在执行时，在t=15时刻，通信中断发生。由于通信线的优先级比打印机高，这个中断得到响应。打印机ISR被中断，它的状态压人栈，继续从通信ISR执行。

**三、**当这个通信ISR正在执行时，发生了磁盘中断(t=20)。由于它的优先级相对较低，只好挂起，而通信ISR运行到结束。

**四、**当通信ISR完成时(1=25), 原来的处理器的状态恢复，即执行原来的打印机ISR。但是在这一例程中的一条指令都没有来得及执行以前，处理器响应优先级更高的磁盘中断，将控制权传送给磁盘ISR。

**五、**仅当这一例程结束后(1=35)， 打印机的ISR才恢复。在它完成后(t=40),控制权才最终交还给用户程序。
![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img5/b165ddcc377b4ed696a02259962e4c2a.png)


## 3.2 计算机的互连结构

### 3.2.1 互联结构的定义

**互连结构**：连接各个模块的通路

不同设备的主要输入输出所需信息交换的种类如下：
![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img5/11555addbdc84f398cce863c902338ac.png)
由上图可知，互连结构必须支持下列类型的传送

存储器到处理器、处理器到存储器、I/O到处理器、处理器到I/O、I/O与存储器之间(可以使用**DMA**直接存储器来实现)

### 3.2.2 总线与总线结构

**总线**：总线是连接多个部件共享的信息传输线，是各部件共享的传输介质

**总线传输的特点**：某一时刻，只允许由一个部件向系统发送信息，而多个部件可以同时从总线上接受相同的信息。

**总线总类**：系统总线、外围总线、内部总线

#### 1、系统总线及其分类

**系统总线**是指CPU、主存、I/0设备(通过I/0接口)各大部件之间的信息传输线。

按系统总线传输信息不同，可分为3类:**数据总线、地址总线和控制总线。**
![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img5/0c7ae5794551424eb55833dfa1f3dfff.png)


:one: **数据总线**: 数据总线是用来传输个功能部件之间的数据信息，它是**双向**传输总线，其位数与机器字长、存储字长有关，一般为 8位、16位或32位。

> **总线宽度**：总线中包含的线的数目

:two: **地址总线**:地址总线主要是用来指出数据总线上的源数据或目的数据在主存单元的地址或I/O设备的地址，地址总线上的代码是用来指明CPU欲访问的存储单元或I/0端口的地址,由CPU输出，是**单向**的，地址线的位数与存储单元的个数有关，如地址线有20根，则对应的存储单元个数为20。地址总线的宽度决定了系统的最大容量。

:three: **控制总线**: 控制总线是用来发出各种控制信号的传输线，其传输是**单向**的。典型的控制信号如下：

> ●**存储器写**(Memory Write):引起总线上的数据写人被寻址的单元。
> ●**存储器读**( Memory Read):使所寻址单元的数据放到总线上。
> ●**I/O写**(I/O Write):引起总线上的数据输出到被寻址的L/O端口。
> ●**I/O读**(I/0 Read): 使被寻址的I/0端口的数据放到总线上。
> ●**传输响应**(Transfer ACK):表示数据已经从总线上接收，或已经将数据放到总线上。
> ●**总线请求**( Bus Request):表示模块需要获得对总线的控制。
> ●**总线允许**( Bus Grant):表示发出请求的模块已经被允许控制线。
> ●**中断请求**( Interupl Request): 表示某个中断正在悬而未决。
> ●**中断响应**( Iterrupt ACK):未决的中断请求被响应。
> ●**时钟(Clock)**:用于同步操作。
> ●**复位(Reset**):初始化所有模块。

#### 2、总线的物理结构

从物理上讲，系统总线实际上是多条平行的电导线。这些导线是在卡或板(印刷电路板).上刻出来的金属线。总线延伸至所有系统部件，每一个系统部件都连接到总线的全部或部分线
![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img5/69e236d9a3bd44fb8af08d81967b8239.png)

#### 3、多总线层次结构|Multiple-bus Hierarchies

单总线结构存在以下的问题：

:one: 总线上连接的设备越多，总线就越长，传输延迟就越大，这些延迟会显著影响性能

:two: 当聚集的传输请求接近总线容量时，总线就会成为瓶颈

所以，大多数计算机都使用多总线层次结构
![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img5/b2d4d34bc83440c2b29f8d18599b4453.png)

高速总线使高需求的设备和处理器有更紧密的集成，同时有独立于处理器

### 3.2.3 总线的设计要素

![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img5/6b946c4dc51b4855a41c91f39897a04d.png)

#### 1、总线类型

总线分为两种基本类型：专用的Dedicated Bus和复用的Multiplexed Bus

| 类型     | 专用总线                     | 复用总线                   |
| -------- | ---------------------------- | -------------------------- |
| **举例** | 使用分立专用的数据线和地址线 | 分时复用，共用线路         |
| **优势** | 高吞吐量                     | 布线数量少，节省空间和成本 |
| **缺点** | 规模和成本较高               | 控制更复杂                 |

#### 2、总线的仲裁方式

由于在总线上每次只有一个器件能够成功发送，因此需要某种仲裁方式。

仲裁方式主要有两种：集中式centralized和分布式distributed

**集中式**：总线控制器的硬件设备负责分配总线时间，可以独立于CPU

常见的集中式总线控制有三种:**链式查询、计数器定时查询、独立请求**;

> 链式查询方式连线简单，易于扩充，对电路故障**最敏感;**
>
> 计数器定时查询方式优先级设置较灵活，对故障不敏感，连线及控制过程较复杂;
>
> 独立请求方式速度**最快**，但硬件器件用量大，连线多，成本较高。
> ![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img5/65fb113ebb3a4b75a6e6ee94379195ec.png)


**分布式**：没有中央控制器，每一个模块中包含有访问控制逻辑，分享总线

这两种仲裁方式的目的都是为了指定一个设备（CPU或者I/O）作为主控器，启动与其他设备的数据传输

#### 3、时序

时序是指总线上协调事件的方式，包括同步时序和异步时序、半同步通信与分离式通信

**同步时序**：事件的发生是由时钟信号决定的

> 总线包括时钟信号线
>
> 时钟周期/总线周期：一次1~0传送
>
> 大多数事件占用一个时钟周期
>
> 容易实现但是不灵活

![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img5/69d085b76de84dcda2de2d1d48e649d7.png)


**异步时序**：总线上一个事件的发生取决于前一个事件的发生

> **优点**：无论使高速设备还是低速设备都适用
>
> **缺点**：实现复杂

![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img5/ad4325e336e54cd1b886b5ce69f55e57.png)


**半同步通信** 

需要时钟、需要等待线、允许各种速度模块协调通信、用于连接低速和较大速度差设备

**分离式通信**

核心思想：将总线周期分为两个子周期

> 在第一个子周期中，主周期将命令、地址和其他信息放入巴士，然后放弃总线 
>
> 在第二个子周期中，从周期开始准备数据（选择、解码、加载），然后应用总线并发送数据 

优点：避免总线怠速等候，用于大型计算机

#### 4、总线宽度与总线带宽

**总线宽度**： 数据总线的宽度对系统性能有影响，单位：bit 

					地址总线的宽度对系统容量有影响，单位：bit

**总线带宽**：总线的传输速率，单位：b/s

#### 5、数据传输类型

![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img5/8eda828d8b974d19956cb8a32b58801f.png)

## 3.3 PCI

PCI（外围组件互连）：也称为高速I/O总线 ，是一种高带宽、独立于处理器的总线。

PCI是专门为满足现代系统的I/O要求而设计的较为经济的总线，实现它只需要很少的芯片，而且支持将其他总线连到PCI总线上。

1990年英特尔开发，后向公众发布


# 第十三章 I/O系统

**I/O硬件**

> I/O设备、设备控制器、I/O通道、总线系统

**I/O控制方式**

> 程序I/O方式、中断驱动方式、DMA方式、I/O通道控制方式

**缓冲技术**

> 缓冲的引入、单缓冲、双缓冲、循环缓冲、缓冲池

**I/O软件**

## I/O系统的组成

计算机系统中，除了需要直接用于I/O和存储信息的**设备**外，还需要有相应的**设备控制器**。在大、中型计算机系统中，还需有**I/O通道**，由这些设备以及相应的**总线**构成了I/O系统

### I/O设备

I/O设备类型繁多，从OS观点看，其性能指标有：

> 数据传输速率
>
> 数据的传输单位
>
> 设备共享属性等 

#### 按速率分类

> **低速设备**
> 传输速率仅为每秒钟几个字节至数百个字节。属于低速设备的典型设备有键盘、 鼠标器、语音的输入和输出等设备。
>
> **中速设备**
> 传输速率在每秒钟数千个字节至数万个字节。典型的中速设备有**行式打印机、激光打印机**等。
>
> **高速设备**
> 传输速率在数百K个字节至数十兆字节。 典型的高速设备有**磁带机、磁盘机、光盘机等。** 

#### 按信息交换的单位分类

> **块设备**
> <font color="red">**用于存储信息。**</font> 由于信息的存取总是以数据块为单位，故而得名。 典型的块设备是**磁盘**，每个盘块的大小 为 512 B~4 KB 。磁盘设备的基本特征是其**传输速率较高**,通常每秒钟为几兆位；另一特征是可寻址 ,即对它可随机地读 / 写任一块；此外，磁盘设备的 I/O 常采用DMA 方式。 
>
> **字符设备** 
> <font color="red">**用于数据的输入和输出。**</font> 其基本单位是字符， 故称为字符设备。 

**时钟**：**既不是块设备也不是字符设备**

#### 按设备的共享属性分类

> **独占设备**:在一段时间内只能有一个进程使用的设备，一般为低速I/O设备（如打印机，磁带等）
>
> **共享设备**:在一段时间内可有多个进程共同使用的设备，多个进程以交叉的方式来使用设备，其资源利用率高（如硬盘）
>
> **虚拟设备**:通过虚拟技术把一台独占设备变换为若干台逻辑设备，可供多个用户使用

### Controller

设备并不是直接与CPU进行通信，而是与设备控制器通信。

每个 I/O 设备通过设备控制器与计算机的数据总线和地址总线相连接。

某些设备（如磁盘设备）有内置的控制器

是一个可编址设备

当它仅控制一个设备时，它只有一个唯一的设备地址

若控制器可连接多个设备时，则应具有多个设备地址，使每一个地址对应一个设备

![image-20211222214715761](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img13/image-20211222214715761.png)

### I/O通道

**定义**：通道是独立于**CPU的专门负责数据I/O传输工作的处理机**，对外部设备实现统一管理，**代替CPU对I/O操作进行控制**，从而使I/O操作可与CPU并行操作。 通道可以执行通道程序.

**目的**：建立独立的I/O操作，不仅**使数据的传送独立于CPU**，而且使有关对I/O操作的组织、管理及其结束处理也尽量独立，即把CPU从繁杂的I/O任务中解脱出来，提高CPU与设备，设备与设备之间的并行工作能力. 、

<img src="https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img13/image-20211222214823420.png" alt="image-20211222214823420" style="zoom:50%;" />

由于通道价格昂贵，致使机器中所设置的通道数量势必较少，这又往往使它成为I/O 的瓶颈，造成整个系统吞吐量的下降。 

<img src="https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img13/image-20211222215101983.png" alt="image-20211222215101983" style="zoom:67%;" />

## I/O控制方式

#### 程序I/O方式(轮询Polling)

CPU与设备串行工作

CPU循环测试—浪费大量CPU时间

#### 中断驱动I/O

在现代计算机系统中，对I/O设备的控制，广泛采用**中断驱动**（Interrupt---Driven）方式。

在I/O设备输入/输出每个数据的过程中，无须CPU干预。

仅当输完一个数据时，才需CPU花费极短的时间去做些中断处理。

#### DMA控制方式

中断驱动I/O是以**字（节）为单位**进行I/O的，若将这种方式用于块设备的I/O，显然将会是极其低效的。

为了进一步减少CPU对I/O的干预，而引入了直接存储器访问（Direct Memory Access）方式。

DMA方式的特点是：

> 数据传输的基本单位是**数据块；**
>
> 所传输的数据是从设备直接送入内存的,或者相反；
>
> 整块数据的传送是由控制器完成的

#### I/O通道控制方式

> DMA每次只能执行一条I/O指令，不能满足复杂的I/O操作要求。在大、中型计算机系统中，普遍采用由专用的I/O处理机来接受CPU的委托，独立执行自己的通道程序来实现I/O设备与内存之间的信息交换，这就是通道技术。

## 缓冲池

循环缓冲属专用缓冲。当系统较大时，为了提高缓冲区的利用率，目前广泛流行公用缓冲池，池中的缓冲区可供多个进程共享。

引入缓冲的主要原因有以下三点：

> **缓和CPU与I/O设备间速度不匹配的矛盾**
>
> **减少对CPU的中断频率，放宽对中断响应时间的限制**
>
> **提高CPU和I/O设备之间的并行性** 

OS提供以下几种缓冲形式：单缓冲、双缓冲、循环缓冲、缓冲池

<img src="https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img13/image-20211222222207252.png" alt="image-20211222222207252" style="zoom:50%;" />

缓冲池（Buffer Pool）的组成 ：

> 空（闲）缓冲区；
>
> 输入缓冲区:装满输入数据；
>
> 输出缓冲区:装满输出数据

为了管理上的方便，可将相同类型的缓冲区链成一个队列，形成以下三个队列：

> 空缓冲队列emq；
>
> 输入队列inq；
>
> 输出队列outq

四种工作缓冲区：

> 收容输入缓冲区
>
> 提取输入缓冲区
>
> 收容输出缓冲区
>
> 提取输出缓冲区； 

<img src="https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img13/image-20211222222500057.png" alt="image-20211222222500057" style="zoom:60%;" />

## I/O软件

**I/O软件功能**

> **提供设备使用的用户接口**：命令接口和编程接口。设备的符号标识
>
> **设备分配和释放**：使用设备前，需要分配设备和相应的通道、控制器。
>
> **设备的访问和控制**：包括并发访问和差错处理。
>
> **I/O缓冲和调度**：目标是提高I/O访问效率

**I/O软件的基本思想**:

> 按**分层**的思想构造软件
>
> 较低层的软件要使较高层的软件独立于硬件
>
> 较高层的软件则要向用户提供一个友好、规范、清晰的界面

I/O软件组织成以下4个层次：

> (1)用户空间的I/O软件
>
> (2)与设备无关的I/O软件(设备独立软件)
>
> (3)设备驱动程序
>
> (4)中断处理程序

<img src="https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img13/image-20211222224318393.png" alt="image-20211222224318393" style="zoom:67%;" />

## 设备分配

在多道程序环境下，系统中的设备**不允许**用户自行使用，必须由系统分配。

为了实现设备分配，必须在系统中设置相应的数据结构。

在进行设备分配时所需的数据结构有：

> 设备控制表DCT
>
> > 系统为每一个设备都配置了一张设备控制表，用于记录本设备的情况
>
> 控制器控制表COCT
>
> 通道控制表CHCT
>
> 系统设备表 SDT
>
> > 整个系统有一张系统设备表

![image-20211125142402239](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img13/image-20211125142402239.png)

为了使系统有条不紊地工作，系统在进行设备分配时，应考虑这样几个因素：

> 设备的固有属性
> 设备分配算法
> 设备分配的安全性
> 设备独立性 

**:one: 固有属性**

独占

> 需考虑效率和死锁问题
>
> 静态分配：
>
> > 在进程运行前, 完成设备分配；运行结束时，收回设备
> >
> > 缺点：设备利用率低
>
> 动态分配：
>
> > 在进程运行过程中，当用户提出设备要求时，进行分配，一旦停止使用立即收回
> >
> > 优点：效率高；缺点：分配策略不好时, 产生死锁

共享

> 提出I/O请求的不同进程以排队方式分时地占用设备进行I/O
>
> 由于有多个进程同时访问，且访问频繁，就会影响整个设备使用效率，影响系统效率。因此要考虑多个访问请求到达时服务的顺序，使平均等待时间越短越好

把独占设备改造成虚拟设备

**:two: 设备分配算法**：

与进程的调度算法有些相似，但相对要简单些：先来先服务、优先级高者优先 

**:three: 设备分配中的安全性**

从进程运行的安全性上考虑，设备分配有以下两种方式：

> 安全分配方式：每当进程发出I/O请求后，便进入**阻塞状态**，直到其I/O操作完成时才被唤醒。
>
> 不安全分配方式：进程发出I/O请求后仍继续运行，需要时又可发出第二个I/O请求、第三个I/O 请求。仅当进程所请求的设备已被另一进程占用时，进程才进入阻塞状态。 

:four: **设备独立性**

**目的**：为了提高OS的可适应性和可扩展性。

**基本含义**： 应用程序独立于具体使用的物理设备。

为了实现设备独立性而引入了**逻辑设备和物理设备**这两个概念

> 应用程序使用逻辑设备名称来请求使用设备
>
> 系统使用物理设备名
>
> 系统需将逻辑设备名称转换为某物理设备
>
> 这非常类似于存储器管理中所介绍的逻辑地址和物理地址的概念。 

逻辑设备表LUT(Logical Unit Table) ： 将应用程序中所使用的逻辑设备名映射为物理设备名。

LUT的设置可采取两种方式

> 单用户系统整个系统设置一张LUT
>
> 多用户系统可为每个用户设置一张LUT 

![image-20211125143617795](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img13/image-20211125143617795.png)



## 以SPOOLing方式使用外设

SPOOLing技术是用于**将一台独占设备改造成共享设备**的一种行之有效的技术

SPOOLing技术是在批处理操作系统时代引入的，即所谓**假脱机**输入/输出技术

#### 概念

SPOOLing：

> 利用多道程序中的**一道程序来模拟脱机输入时的外围控制机**的功能，把低速I/O设备上的数据传送到高速磁盘上；
>
> 用**另一道程序来模拟脱机输出时外围控制机**的功能，把数据从磁盘传送到低速输出设备上
>
> 这样，便在**主机的直接控制下，实现脱机输入、输出功能**。
>
> 此时的外围操作与CPU对数据的处理同时进行，这种在联机情况下实现的同时外围操作称为SPOOLing (Simultaneous Peripheral Operations On-Line)，或称假脱机操作。

#### 组成

SPOOLing系统是对脱机输入、输出工作的模拟，它必须有高速随机外存的支持，这通常是采用磁盘。

SPOOLing系统组成如下：

> 输入井和输出井；
>
> 输入缓冲和输出缓冲；
>
> 输入进程和输出进程。
>

#### 实现

SPOOLing技术可将一台打印机改造成一台可供多个用户共享的设备。

当用户进程请求打印输出时，SPOOLing做以下两件事：

> 由输出进程在输出井中为之申请一空闲盘块区，并将要打印的数据送入其中；
>
> 输出进程为用户进程申请一张空白的用户请求打印表，并将用户的打印要求填入其中，再将该表挂到请求打印队列上。

输出进程从请求打印队列中依次取出请求打印表，根据表中的要求将要打印的数据从输出井传送到内存缓冲区，再由打印机打印。

#### 特点

> 提高了I/O速度
>
> 将独占设备改造为共享设备
>
> 实现了虚拟设备功能
>

## 设备处理

设备处理工作由两部分完成：设备驱动程序、中断处理程序

### 设备驱动程序

操作系统能够以统一的方式对待不同的I/O设备，因为具体的差别被称为**设备驱动程序** 的内核模块所封装。与设备相关的代码放在设备驱动程序中。应为**每一类设备**配置一种驱动程序

**设备驱动程序实际是处理或操作硬件控制器的软件**

**处理过程**

<img src="https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img13/image-20211125150444380.png" alt="image-20211125150444380" style="zoom:67%;" />

### 中断处理程序

在 I/O 时，设备控制器如果准备好服务会向CPU发出一中断请求。

这些中断表示输入数据已有，或输出已完成，或已检测到错误。

CPU响应后便转向中断处理程序

无论是哪种I/O设备，其中断处理程序的处理过程都包含了以下几个步骤

> 唤醒被阻塞的驱动程序进程；
>
> 保护被中断进程的CPU环境；
>
> 分析中断原因、转入相应的设备中断处理程序；
>
> 进行中断处理；
>
> 恢复被中断进程的现场。


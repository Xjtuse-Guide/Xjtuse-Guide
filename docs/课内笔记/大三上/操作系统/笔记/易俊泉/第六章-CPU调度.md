

# 第六章 CPU调度

**高级(Long-term)调度——作业调度**

> 决定把外存输入井上处于作业后备队列上的哪些作业调入内存，并为它们创建进程、分配必要的资源，然后再将新创建的进程排在就绪队列上，准备执行。

**低级(Short-term)调度——进程调度**

> 决定就绪队列中哪个进程将获得处理机，然后由分派程序执行把处理机分配给该进程的操作。

**中级(Medium-term)调度——对换**

<img src="https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img/image-20211012163118655.png" alt="image-20211012163118655" style="zoom:67%;" />

## 一、Basic Concepts  (基本概念）

通过多道程序设计**得到CPU的最高利用率**

CPU脉冲的分布,在系统中,存在许多短CPU脉冲,只有少量的长CPU脉冲

> 比如:I/O型作业具有许多短CPU脉冲,而CPU型作业则会有几个长CPU脉冲,这个分布规律对CPU调度算法的选择是非常重要的

**CPU调度**：当CPU空闲时(当进程离开running状态时)，OS就选择**内存中**的某个就绪进程，并给其分配CPU

![image-20211012163742438](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img/image-20211012163742438.png)

CPU**调度的时机**：

:one: 从运行到等待	:two: 从运行到就绪	:three: 从等待到就绪	:four: 终止运行

1、4属于非抢占方式调度，2、3属于抢占式调度

### 抢占式与非抢占式调度[重点]

**非抢占方式**(nonpreemptive)

> **把处理机分配给某进程后，便让其一直执行，直到该进程完成或发生某事件而被阻塞时，才把处理机分配给其它进程，不允许其他进程抢占已经分配出去的处理机。**
>
> 优点:实现简单、系统开销小，适用于大多数批处理系统环境
> 缺点:难以满足紧急任务的要求，不适用于实时、分时系统要求

**抢占方式**（Preemptive mode）

> **允许调度程序根据某个原则，去停止某个正在执行的进程，将处理机重新分配给另一个进程。**

**抢占原则**

> **时间片原则**:各进程按时间片运行，当一个时间片用完后，便仃止该进程的执行而重新进行调度。这个原则适用于**分时系统。**
>
> **优先权原则**:通常对一些重要的和紧急的进程赋予较高的优先权。当这种进程进入就绪队列时，如果其优先权比正在执行的进程优先权高，便仃止正在执行的进程，将处理机分配给优先权高的进程，使之执行
>
> **短作业优先原则**:当新到达的作业比正在执行的作业明显短时，将暂停当前长作业的执行，将处理机分配给新到的短作业，使之执行。

### Dispatcher 分派程序

分派程序负责将对CPU的控制权转交给短调度选择的进程，包括**切换上下文、切换到用户态与跳转到用户程序的适当位置并重新运行之**

**分派延迟** – 分派程序终止一个进程的运行并启动另一个进程运行所花的时间

## 二、Scheduling Criteria （调度准则） 

**CPU利用率高**

**吞吐量要大**——单位时间内运行完的进程数

**周转时间要短**——进程从**提交到运行**结束的全部时间

**等待时间要短**——进程在**就绪队列中等待调度**的时间片总和 

**响应时间要短**——从**进程提出请求到首次被响应**的时间段[在分时系统环境下不是输出完结果的时间] 

**带权周转时间**——**作业周转时间与作业时间的比**

## 三、Scheduling Algorithms （调度算法）[重点]

<font color="red">调度算法影响的是等待时间，而不能影响进程真正使用CPU的时间和I/O时间</font>

### FCFS 先来先服务

先来先服务First-Come-First-Served:

> 最简单的调度算法
>
> 可用于作业或进程调度
>
> 算法的原则是按照作业到达后备作业队列（或进程进入就绪队列）的先后次序来选择作业（或进程） 

FCFS算法属于**非抢占方式**:一旦一个进程占有处理机，它就一直运行下去，直到该进程完成或者因等待某事件而不能继续运行时才释放处理机。

FCFS算法易于实现，表面上很公平，实际上**有利于长作业，不利于短作业；有利于CPU繁忙型，不利于I/O繁忙型**。

![image-20211221192641664](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img/image-20211221192641664.png)

### Shortest-Job-First (SJF)短作业优先

选择执行时间最短的作业优先去调度

**两种方式**

> **非抢占式调度**nonpreemptive – 一旦进程拥有CPU，它的使用权限只能在该CPU 脉冲结束后让出
>
> **抢占式调度**Preemptive – 发生在有比当前进程剩余时间片更短的进程到达时，也称为最短剩余时间优先调度

SJF是最优的 – 对一组指定的进程而言，它给出了最短的平均等待时间

<font color="red">**举例运算**</font>

![image-20211012172102109](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img/image-20211012172102109.png)

采用SJF**有利于系统减少平均周转时间,提高系统吞吐量。**

一般情况下SJF调度算法比FCFS调度算法的效率要高一些, 但实现相对要困难些。

如果作业的到来顺序及运行时间不合适，会出现**饥饿现象**，例如，系统中有一个运行时间很长的作业JN，和几个运行时间小的作业，然后，不断地有运行时间小于JN的作业的到来，这样，作业JN就因得不到调度而饿死。另外，作业运行的估计时间也有问题。

### 优先级调度

每个进程都有自己的优先级【整数，CPU分配给最高优先级的进程[假定最小的整数拥有最高的优先级]

确定进程优先权的依据有：

:one: :star2:**静态优先权**在进程创建时确定，且在整个生命期中保持不变。:star2:

> **进程类型**，通常系统进程的优先权高于一般用户进程的优先权。在用户进程中，I/O繁忙的进程应优先于CPU繁忙的进程，以保证CPU和I/O设备之间的并行操作。
>
> **进程对资源的需求**，如进程执行时间及内存需要少的进程应赋予较高的优先权；
>
> **根据用户要求**，由用户的紧迫程度及用户所付费用的多少来确定进程的优先权。
>
> 在分时系统中，**前台进程应优先于后台进程**

问题:**饥饿 – 低优先级的可能永远得不到运行**

解决饥饿现象——老化：**视进程等待时间的延长提高其优先数**

:two: **动态优先权**是指进程的优先权可以随进程的推进而改变，以便获得更好的调度性能

改变优先权的因素

> 进程的等待时间
>
> 已使用处理机的时间
>
> 资源使用情况

### 时间片轮转算法(Round Robin)

每个进程将得到小单位的CPU时间[时间片]，通常为10-100毫 秒。时间片用完后，该进程将被抢占并插入就绪队列末尾

![image-20211012172922857](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img/image-20211012172922857.png)

一般来说，RR的平均周转时间比SJF长，但**响应时间要短一些**

时间片太长的话会影响系统的性能，一组进程的平均周转时间并不一定随着时间片的增大而降低

**一组进程的平均周转时间并不一定随着时间片的增大而降低。一般来说，如果大多数（80%）进程能在一个时间片内完成，就会改善平均周转时间**

### 多级队列Multilevel Queue Scheduling

按进程的属性来分类，如进程的类型、优先权、占用内存的多少,每类进程组成一个就绪队列，每个进程固定地处于某一个队列，如

> 就绪队列分为:（前台）[交互式]、（后台） [批处理]
>
> 每个队列有自己的调度算法： foreground – RR、  background – FCFS
>
> 调度须在队列间进行

固定优先级调度，即前台运行完后再运行后台。有可能产生饥饿

给定时间片调度，即每个队列得到一定的CPU时间，进程在给定时间内执行；如，80%的时间执行前台的RR调度，20%的时间执行后台的FCFS调度

### 多级反馈队列Multilevel Feedback Queue

<font color="blue">**多级反馈队列调度算法是时间片轮转调度算法和优先级调度算法的综合与发展**</font>

- 存在多个就绪队列，具有不同的优先级，各自**按时间片轮转法调度**
- 允许进程在队列之间**移动**
- 各个就绪队列中时间片的大小各不相同，**优先级越高的队列时间片越小**。
- 当一个进程执行完一个完整的时间片后被抢占处理器，被抢占的进程优先级**降低一级**而进入下级就绪队列，如此继续，直至降到进程的基本优先级。而一个进程从阻塞态变为就绪态时要提高优先级
- 最后会将I/O型和交互式进程留在较高优先级队列

![image-20211012173708040](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img/image-20211012173708040.png)

Highest Response Ratio Next (HRRN)

###  高响应比优先 (作业)调度算法

SJF中长作业运行得不到保证，引入动态优先权

高响应比优先调度算法—基于优先权算法

  在每次选择作业投入运行时，先计算后备作业队列中每个作业的响应比RP,然后选择其**值最大**的作业投入运行。

RP值定义为：

>   RP＝（已等待时间＋要求运行时间）／要求运行时间＝1＋已等待时间／要求运行时间

**优点**：

> 等待时间相同，则SJF；
>
> 要求的服务时间相同，则FCFS；
>
> 长作业的优先级随着等待时间的增加而提高，不会出现得不到响应的情况。

**缺点**:

> 作业调度程序要统计作业的等待时间，**作浮点运算（这是系统程序最忌讳的）浪费大量的计算时间。**

![image-20211221194238534](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img/image-20211221194238534.png)

![image-20211221195129316](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img/image-20211221195129316.png)

## 四、Multiple-Processor Scheduling （多处理器调度）

多个CPU可用时，CPU调度将更为复杂

**对称多处理器** – 每个处理器决定自己的调度方案。每个CPU自己到**公共就绪队列**去取进程来执行。这需保证多个CPU对公共就绪队列的**互斥访问**）

**非对称多处理器** – 仅一个处理器能处理系统数据结构，这就减轻了对数据的共享需求

当进程从一个CPU迁移到另外一个CPU时,其CACHE的内容也必须随之更新--代价很高

多数SMP系统不支持进程在不同CPU间迁移,而是试图使进程一直在同一个CPU上运行-- Processor affinity(处理器亲和) ——硬亲和与软亲和

## 五、Real-Time Scheduling （实时调度）

实时调度是为了完成实时处理任务而分配计算机处理器的调度方法。通常是**基于优先级且是抢占式的**

实时处理任务要求计算机在用户允许的时限范围内给出响应信号。

实时处理任务可分为：硬实时任务（hard real-time task）与软实时任务（soft real-time task）

**实现**：对OS的调度程序及其他相关方面提出了要求.**首先,系统要实现基于优先级的调度,实时进程须具有最高优先级,且不能随着时间的推移降低优先级; 其次,调度延迟必须很小.**

### 分派延迟Dispatch Latency

为降低分派延迟，需要允许系统调用**被抢占**

> 一种方法是在长系统调用中插入抢占点
>
> 另一种方法是使得整个内核可被抢占,但所有内核数据结构必须通过各种同步机制加以保护

如果较高优先级进程需读或修改正在被另一个低优先级进程所访问的内核数据,高优先级进程需要等待低优先级进程的完成.这种现象称为**优先级倒置**

**优先级继承**:(正在访问高优先级进程所需资源的)低优先级进程继承高优先级,直到相关资源处理完毕,它们的优先级再返回原来的值.

## 六、操作系统例子

### Solaris调度

采用优先级的进程调度，按调度的优先级定义了4类：实时、系统、分时、交互，对每一类有不同的优先级和调度算法

> **默认的调度类是分时**。分时调度动态地改变线程的优先级，赋予不同的时间片长度（**多级反馈队列**）
>
> 分时和交互采用相同的调度策略,但**交互式线程有较高的优先级**
>
> 系统类的优先级是不会改变的,其调度策略是不分时的
>
> 实时类具有**最高**的优先级
>
> 每一类有一组优先级，然而调度程序需先将其转换成全局优先级，然后选择全局优先级最高的线程运行。

### Windows XP 调度

- 基于优先级的，可抢占的调度算法
- 线程按时间片来使用CPU
- 使用32个优先级来确定线程的执行顺序
- 优先级相同的线程按时间片轮转调度
- 非实时优先级是动态调整的
- 当线程从等待操作被唤醒时,提高其优先级(如I/O结束)
- 延长时间片:给前台任务更长的时间片,以提高响应速度
- **实时优先级是固定不变的**

### Linux Schduling

Linux支持SMP,**每个CPU有自己的runqueue,并各自独立进行调度.**

每个runqueue有:

> Active: contains all tasks with time remaining in their time slices 
>
> Expired: contains all expired tasks

调度程序从Active array中选取优先级最高的进程使用CPU,当所有进程都用尽了自己的时间片,交换Active array与expired array

![image-20211014144400258](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img/image-20211014144400258.png)

## 七、Algorithm Evaluation （算法评估）

CPU调度算法很多,如何选择适当的算法?

> 首先定义一个标准 (根据要实现的系统所追求的目标,如CPU利用率\系统吞吐量\平均周转时间\响应时间等)
>
> 然后根据标准来选择适当的算法
>
> 采用相应的模型来评价算法

**确定模型法、排队模型、仿真、实际运行**


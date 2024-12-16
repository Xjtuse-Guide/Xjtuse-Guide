# 第四次作业

6.9  Show that, if the wait() and signal() semaphore operations are not executed atomically, then mutual exclusion may be violated.

wait 操作即为 P 操作，signal 操作即为 V 操作。如果两个操作不是原子的话，那么按照如下顺序执行时，可能出现问题：

假设原先信号量 S = 1，同时按如下顺序进行 P/V 操作

| P            | V            |
| ------------ | ------------ |
| Read S（1）  |              |
| S-1（0）     | Read S（1）  |
| Write S（0） | S+1（2）     |
|              | Write S（2） |

可以看出，按如下顺序执行时，P/V 操作的互斥被破坏了，P 操作完全没有写入 S-1 的 结果。

6.11  The Sleeping-Barber Problem. A barbershop consists of a waiting room with n chairs and abarber room with one barber chair. If there are no customers to be served, the barber goes to sleep. If a customer enters the barbershop and all chairs are occupied, then the customer leaves the shop. If the barber is busy but chairs are available, the customer sits in one of the free chairs. If the barber is asleep, the customer wakes up the barber. Write a program to coordinate the barber and the customers.

 设立四个信号量：customer=0，barber=1，mutex=1，设置共享变量 waiting = 0（表示当前等待人数），假设店里有 n 把椅子

Customer 执行的操作如下：

- P(mutex)
- if waiting > n V(mutex);exit
- else waiting +=1
- V(mutex)
- V(customer)
- P(barber)
- 理发

Barber 执行的操作如下：

while true:

- P(customer)

- P(mutex)

- waiting -= 1

- V(mutex)
- 理发
- V(barber)



1. 有一个系统，定义 P 、 V 操作如下：

P(s):

s:=s-1;

if s<0 then

将本进程插入相应队列末尾等待；

V(s) **：**

s:=s+1;

if s<=0 then

从相应等待队列队尾唤醒一个进程，将其插入就绪队列；

问题：

这样定义 P **、** V 操作是否有问题？

用这样的 P **、** V 操作实现 N 个进程竞争使用某一共享变量的互斥机制。

1. 有问题，会导致饥饿。V 操作每次唤醒队列尾部的进程，而新插入的进程也在尾部，导致每次 V 操作唤醒的进程都是最晚执行 P 操作的，从而等待队列前端的进程可能饥饿。

2. 可以设置 N-1 个上述定义的信号量：$S_1, S_2, ..., S_{n-1}$，它们的初始值分别为 1，2，3，……，n-1。每个进程访问时，就由大到小依次对这些信号量做 P 操作；访问完成后，按编号从小到大对这 n-1 个信号量做 V 操作。

   下面以 3 个进程互斥访问为例，说明此方法的正确性。假设三个进程为 P1, P2, P3

   | P1    | P2    | P3    |
   | ----- | ----- | ----- |
   | P(S1) | P(S2) | ...   |
   | READ  | P(S1) | P(S2) |
   | READ  | ...   | ...   |
   | READ  | ...   | ...   |
   | V(S1) | READ  | ...   |
   | ...   | V(S1) |       |
   | ...   | V(S2) | P(S1) |
   |       |       | READ  |
   |       |       | V(S1) |
   |       |       | V(S2) |

 

2. 第二类读者写者问题：写者优先

条件：

多个读者可以同时进行读

写者必须互斥（只允许一个写者写，也不能读者写者同时进行）

写者优先于读者（一旦有写者，则后续读者必须等待，唤醒时优先考虑写者）

设置 2 个信号量：R=0 为变量；mutex=0 互斥信号量，控制 R 的读写；w=1 为互斥信号量（用于写者主动封锁后续读者），wr =1 为互斥信号量（用于控制读写分离）



读者的操作如下：

- P(w)
- P(mutex)
- R += 1
- if R == 1 P(wr)
- V(mutex)
- V(w)
- 读取
- P(mutex)
- R -= 1
- if R == 0 V(wr)
- V(mutex)

写者的操作如下：

- P(w) // 封锁后续写者
- P(wr) // 如果没人读，就开始写
- WRITING
- V(wr)
- V(W)

 

3. 把学生和监考老师都看作进程 **,**  学生有 N 人 **,**  教师 1 人 **.**  考场门口每次只能进出一个人 **,**  进考场原则是先来先进 **.**  当 N 个学生都进入考场后 **,**  教师才能发卷子 **.**  学生交卷后可以离开考场 **.**  教师要等收上来全部卷子并封装卷子后才能离开考场。

   问题 **:**

   问共需设置几个进程 ?

   试用 P **、** V 操作解决上述问题中的同步和互斥关系。
   
   共需要设置两类进程：学生进程和老师进程。
   
   设置信号量如下：door=1 互斥信号量（互斥出入考场），count 共享变量，mutex 互斥信号量（互斥访问 count），empty=0 同步信号量, full=0 同步信号量

学生的操作如下：

- P(door)
- 进门
- V(door)
- P(mutex)
- count += 1
- if count == N then V(full)
- V(mutex)
- P(full)
- 答题
- P(mutex)
- count -= 1
- if count == 0 then V(empty)
- V(mutex)
- P(door)
- 离开
- V(door)

教师的操作如下：

- P(door)
- 进门
- V(door)

- P(full)
- 发卷
- 等待
- 收卷
- P(empty)
- 离开
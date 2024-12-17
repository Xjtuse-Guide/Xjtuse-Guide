# 第一次作业

## Introduction

1. What is the main advantage of multiprogramming?

   多道处理的好处在于让 CPU 和外接 I/O 设备实现了并行，保证 CPU 每时每刻都在处理一个作业，从而提高了 CPU 处理作业的效率

2. Define the essential properties of the following types of operating systems:
   1. Batch：批处理，把一批内容相似的作业放在一起，由计算机系统自动执行，解决了人工 I/O 速度过慢的问题
   2. Time sharing：分时，指多个用户同时共享一台计算机，或多个程序共享相同的硬件和软件资源。
   3. Real time：实时，即操作系统能以极快的速度对外界发来的信息作出相应，实时性要求高
   4. Network：网络，是指在通常操作系统的基础上，额外提供网络通信和网络服务。
   5. Distributed：分布式，分布式系统是很多物理机器的集合，通过网络/线缆等方式连接起来对用户提供服务，让用户认为只有一台机器。

3. 下面哪些指令是特权指令？

  A．设置定时器的值  B. 读时钟

  C. 清除内存    D 关闭中断

  E．从用户模式切换到监督模式

 A、C、D 是特权指令。

## OS structures

1. What is the purpose of system calls?

   系统调用是为了让运行在用户态下的应用程序能够执行管态的操作，由操作系统设置的服务接口。应用程序通过系统调用将控制权转交给操作系统，操作系统完成管态下才能执行的操作（比如 I/O）后将控制权交还用户程序。

2. What is the main advantage of the layered approach to system design?

   分层系统结构的好处是：低层和高层之间可以分别实现，易于扩充；高层错误不会影响低层，便于调试；调用关系清晰（高层->低层）

3. What is the main advantage of the microkernel approach to system design?

   微内核系统结构的好处是：将非核心内容移出内核，添加新内容时只需要扩充外部内核，易于实现和扩充；提高系统的可靠性；可以便捷的提供多种操作环境。
# OS 第七次作业

9.4  A certain computer provides its users with a virtual-memory space of $2^{32}$ bytes. The computer has $2^{18}$ bytes of physical memory. The virtual memory is implemented by paging, and the page size is 4,096 bytes. A user process generates the virtual address 11123456H. Explain how the system establishes the corresponding physical location. Distinguish between software and hardware operations.

1. 虚拟地址为 11123456H，由于页面大小为 $4096=2^{12}$，可以将此地址划分为页号和页内偏移两部分：

   后 3 位（二进制的后 12 位）456H 为页内偏移，前 5 位（二进制的前 20 位）11123H 为页号

2. 由于计算机的主存有 $2^{18}$（256KB），因此主存总共包含 $2^{18}/2^{12}=2^6=64$ 块

3. 查询页表中页号为 11123H 的表项对应的内存块号，如果不存在表项，终止当前用户进程；如果存在，则取得块号后，计算内存块号+页内偏移，得到该地址对应的物理地址。

分隔页号和页内偏移、查询内存块号和计算组合地址通常是硬件完成的；操作系统负责处理用户进程访问内存的请求，并告诉硬件需要转换地址。

9.10  Consider a demand-paging system with the following time-measured utilizations:

| CPU utilization   | 20%   |
| ----------------- | ----- |
| Paging disk       | 97.7% |
| Other I/O devices | 5%    |

For each of the following, say whether it will (or is likely to) improve CPU utilization. Explain your answers.

先分析所有部分的利用率。可以看出，CPU 的利用率不高，而分页磁盘的利用率几乎满了，因此目前系统可能处于抖动状态：内存大小不足以容纳当前所有程序，导致内存和磁盘之间不断交换页面，使 CPU 利用率下降。

a. Install a faster CPU.

加快 CPU 的速度不太可能增加 CPU 利用率，因为目前系统的瓶颈在于内存，而非 CPU。当前 CPU 的性能仍然足够处理程序。

b. Install a bigger paging disk.

增加磁盘分页区域的大小不太可能增加 CPU 利用率，因为增加磁盘大小无法缓解内存不足、内存和磁盘交换次数过多的问题。

c. Increase the degree of multiprogramming.

增加多道程序的道不能增加 CPU 利用率，甚至可能导致 CPU 利用率继续降低。在内存中载入更多程序后，抖动现象会加剧，导致程序花费在页面交换上的时间进一步增加，CPU 利用率进一步降低。

d. Decrease the degree of multiprogramming.

减少多道程序的道可能增加 CPU 利用率。减少内存中的程序后，抖动现象得到缓解，进程不会在页面交换上花费这么多的时间，可以消耗更多时间在 CPU 上执行。

e. Install more main memory.

增加主存大小可以增加 CPU 利用率。增加主存大小后，主存大小可以容纳当前所有程序，抖动现象得到缓解，进程可以花费更多时间在 CPU 上执行

f. Install a faster hard dist or multiple controllers with mutiple hard disks.

安装更快速的磁盘可以增加 CPU 利用率，因为可以加速主存和磁盘之间的页面交换速度

g. Add prepaging to the page-fetch algorithms.

增加预取操作可以增加 CPU 利用率，因为可以加速请求调页的过程。

h. Increase the page size.

增加页面大小可能增加 CPU 利用率，也可能减少 CPU 利用率。如果大部分请求都是顺序访问的，那么页面大小增加后，每页包含需要的地址的概率更大，因此请求调页次数更少。但如果大部分请求是随机访问的，那么每次 I/O 的开销会更大，而且额外读入的内容都没有用处。

  

9.13  A page-replacement algorithm should minimize the number of page faults. We can achieve this minimization by distributing heavily used pages evenly over all of memory, rather than having them compete for a small number of page frames. We can associate with each page frame a counter of the number of pages associated with that frame. Then, to replace a page, we can search for the page frame with the smallest counter.

a. Define a page-replacement algorithm using this basic idea. Specifically address these problems:

1. What the initial value of the counters is

   计数器的初始值应当为 0

2. When counters are increased

   当一个新的，从未与此帧关联过的页被放入此帧时，增加计数器

3. When counters are decreased

   当已经与此帧关联的某页再也不会被使用后，减少计数器

4. How the page to be replaced is seleced

   选择计数器最少的帧，将其存储的页面替换；如果有多个页面的计数器都是最少的，就替换第一个位置的页面

> 注：这种算法思想类似于：如果某帧和太多页关联了，那么我把新换入的页放在这里可能很快就被挤走了；所以，我要把新换入的页放到关联最少的帧中。
>
> 这种算法在实际中也是不可实现的，和 OPT（最佳替换）一样，是因为无法预测后续需要换入的内存页。

b. How many page faults occur for your algorithm for the following reference string, with four page frames?

​        1,2,3,4,5,3,4,1,6,7,8,7,8,9,7,8,9,5,4,5,4,2.

页面分配如下：

| 输入 | 1    | 2    | 3    | 4    | 5    | 3    | 4    | 1    | 6    | 7    | 8    | 7    | 8    | 9    | 7    | 8    | 9    | 5    | 4    | 5    | 4    | 2    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | 1    | 1    | 1    | *1*  | 5    | 5    | 5    | 5    | *5*  | 7    | 7    | 7    | 7    | 7    | 7    | 7    | 7    | 7    | 7    | 7    | *7*  | 2    |
| 2    |      | 2    | 2    | 2    | 2    | 2    | *2*  | 1    | 1    | 1    | 1    | 1    | *1*  | 9    | 9    | 9    | 9    | 9    | 9    | 9    | 9    | 9    |
| 3    |      |      | 3    | 3    | 3    | 3    | 3    | *3*  | 6    | *6*  | 8    | 8    | 8    | 8    | 8    | 8    | *8*  | 5    | 5    | 5    | 5    | 5    |
| 4    |      |      |      | 4    | 4    | 4    | 4    | 4    | 4    | 4    | 4    | 4    | 4    | 4    | 4    | 4    | 4    | 4    | 4    | 4    | 4    | 4    |

*斜体*代表被换出的页面

共出现 12 次页面错误

c. What is the minimum number of page faults for an optimal page-replacement strategy for the reference string in part b with four page frames?

最优算法是置换之后最长时间不使用的帧，因此其替换过程如下：

| 输入 | 1    | 2    | 3    | 4    | 5    | 3    | 4    | 1    | 6    | 7    | 8    | 7    | 8    | 9    | 7    | 8    | 9    | 5    | 4    | 5    | 4    | 2    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | 1    | 1    | 1    | 1    | 1    | 1    | 1    | *1*  | 6    | *6*  | 8    | 8    | 8    | 8    | 8    | 8    | 8    | *8*  | 4    | 4    | 4    | 4    |
| 2    |      | 2    | 2    | *2*  | 5    | 5    | 5    | 5    | 5    | 5    | 5    | 5    | 5    | 5    | 5    | 5    | 5    | 5    | 5    | 5    | 5    | 5    |
| 3    |      |      | 3    | 3    | 3    | 3    | 3    | 3    | *3*  | 7    | 7    | 7    | 7    | 7    | 7    | 7    | 7    | 7    | 7    | 7    | *7*  | 2    |
| 4    |      |      |      | 4    | 4    | 4    | 4    | 4    | 4    | 4    | 4    | 4    | *4*  | 9    | 9    | 9    | 9    | 9    | 9    | 9    | 9    | 9    |

一共出现过 11 次页面错误。
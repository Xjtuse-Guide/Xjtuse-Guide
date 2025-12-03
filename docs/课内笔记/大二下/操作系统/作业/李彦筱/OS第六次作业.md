# 第六次作业

8.1  Explain the difference between internal and external fragmentation.

 内碎片是指进程没有完全使用分配给其的内存空间，出现的空余空间；外碎片是指某块未被分配的内存空间太小，无法被分配给任何一个进程。

静态分区产生内碎片，动态分配产生外碎片：

内碎片是由固定分区/分页分配造成的：进程可能没有使用所有其被分配的内存空间

> 分页本质上和固定分区分配类似，因为其分配的基本单元都是相同大小的

外碎片是由可变分区分配造成的：外碎片的产生本质上是因为剩余的内存空间每块都太小，不足以放下一整个进程，而进程又必须连续的存放在内存中。

> 分段本质上和可变分区分配类似，因为其分配给进程的内存空间大小可以不同

8.3  Given five memory partitions of 100 KB, 500 KB, 200 KB, 300 KB, and 600 KB (in order), how would each of the first-fit, best-fit, and worst-fit algorithms place processes of 212 KB, 417 KB, 112 KB, and 426 KB (in order)? Which algorithm makes the most efficient use of memory?

首次匹配算法：

第一次分配（分配 212KB 大小的空间）时，分配结果如下

| 内存大小 | 需要分配内存大小 | 剩余内存 |
| -------- | ---------------- | -------- |
| 100KB    |                  |          |
| 500KB    | 212KB            | 288KB    |
| 200KB    |                  |          |
| 300KB    |                  |          |
| 600KB    |                  |          |

之后，将 500KB 这块的剩余空间也记录下来，继续分配内存，最后得到的结果为：

| 内存大小 | 需要分配内存大小 | 剩余内存 |
| -------- | ---------------- | -------- |
| 100KB    |                  |          |
| 288KB    | 112KB            | 176KB    |
| 200KB    |                  |          |
| 300KB    |                  |          |
| 600KB    | 417KB            | 183KB    |
| 无法分配 | 426KB            |          |

内碎片大小为 176+183=359KB，外碎片为 500KB，剩余一个 426KB 的进程由于内存空间不足，无法为其分配内存

最佳匹配算法：

| 内存大小 | 需要分配内存大小 | 剩余内存 |
| -------- | ---------------- | -------- |
| 100KB    |                  |          |
| 500KB    | 417KB            | 83KB     |
| 200KB    | 112KB            | 88KB     |
| 300KB    | 212KB            | 88KB     |
| 600KB    | 426KB            | 174KB    |

内碎片大小为 83+88+88+174=433KB，外碎片为 100KB。

最差匹配算法：选择能够存放下所需内存的最大内存块

第一次分配（分配 212KB 大小的空间）时，分配结果如下

| 内存大小 | 需要分配内存大小 | 剩余内存 |
| -------- | ---------------- | -------- |
| 100KB    |                  |          |
| 500KB    |                  |          |
| 200KB    |                  |          |
| 300KB    |                  |          |
| 600KB    | 212KB            | 388KB    |

之后，将 600KB 这块的剩余空间（388KB）也记录下来继续分配，接着分配内存，最后得到的结果为：

| 内存大小 | 需要分配内存大小 | 剩余内存 |
| -------- | ---------------- | -------- |
| 100KB    |                  |          |
| 500KB    | 417KB            | 83KB     |
| 200KB    |                  |          |
| 300KB    |                  |          |
| 388KB    | 112KB            | 276KB    |
| 无法分配 | 426KB            |          |

内碎片大小为 83+276=359KB，外碎片为 600KB，且由于内存空间不足，需要 426KB 的进程无法获得内存。

综上：最佳匹配算法对内存的利用率是最高的，无论考虑内碎片还是外碎片。

8.9 . Consider a paging system with the page table stored in memory.

   a. If a memory reference takes 200 nanoseconds, how long does a paged memory reference take?

   b. If we add TLBs, and 75 percent of all page-table reference are found in the TLBs, what is the effective memory reference time?(Assume that finding a page-table entry in the TLBs takes zero time, if the entry is there)

 a. 由于一次内存访问需要 200ns，且页表位于内存中，则总共需要访问页表+访问实际内容，共计访问内存两次，因此需要 400ns

 b. 访问时间 = 访问 TLB 命中概率 * (访问 TLB 时间+访问内存时间)+TLB 未命中概率\*（访问 TLB 时间+2\*访问内存时间）=$75\%\times (0 + 200) + 25\% \times (0+2\times 200) $= 250ns



8.12  Consider the following segment table:

| Segment | Base | Length |
| ------- | ---- | ------ |
| 0       | 219  | 600    |
| 1       | 2300 | 14     |
| 2       | 90   | 100    |
| 3       | 1327 | 580    |
| 4       | 1952 | 96     |

   What are the physical addresses for the following logical addresses?

​    a. 0,430

​    b. 1,10

​    c. 2,500

​    d. 3,400

​    e. 4,112

物理内存地址 = 段号对应起始地址 + 段内偏移。

> 如果段内偏移大于段长度，则此地址越界，视为无效

通过此公式，可以得到：

a. 物理地址为 219 + 430 = 649

b. 物理地址为 2300+10 = 2310

c. 此地址无效，因为编号 2 的段长度仅有 100，而此地址指定段内偏移为 500

d. 物理地址为 1327 + 400 = 1727

e. 此地址无效，因为编号 4 的段长度仅有 96，而此地址指定段内偏移为 112
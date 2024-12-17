# OS 第八次作业

10.1  Consider a file system where a file can be deleted and its disk space reclaimed while links to that file still exist. What problems may occur if a new file is created in the same storage area or with the same absolute path name? How can these problems be avoided?

 如果一个文件被删除且其空间被回收了，但是指向文件路径的链接仍然存在，那么创建一个和该文件同名的新文件时，此前指向被删除文件的链接就会错误的指向新创建的文件。

 解决方案：维护一个「指向文件的链接」表，在删除文件时，参照此表的内容，同时删除所有指向该文件的链接，不要保留。

11.1  Consider a file system that uses a modified contiguous-allocation scheme with support for extents. A file is a collection of extents, with each extent corresponding to a contiguous set of blocks. A key issue in such system is the degree of variability in the size of the extents. What are the advantages and disadvantages of the following schemes?

​    a. All extents are of the same size, and the size is predetermined.

​    b. Extents can be of any size and are allocated dynamically.

​    c. Extents can be of a few fixed sizes, and these sizes are predetermined.

a. 优点：类似静态分配方式，每个分配块大小相同，不会出现外碎片，分配简单（只需要类似页表的结构记录分配方法）；缺点：部分块中会出现内碎片，不够灵活

b. 优点：类似动态分配方式，每个分配块大小不同，不会出现内碎片，分配灵活；缺点：容易出现外碎片，且记录块分配情况的表较为复杂

c. 缺点：块大小一定，可能出现内碎片；优点：由于块有几种固定的大小可选，文件存储时可以选择符合要求的最小的块，产生的内碎片大小会比 a 方法小。c 的灵活性和复杂性介于 a、b 之间。

11.2  What are the advantages of the variant of linked allocation that uses a FAT to chain together the blocks of a file?

FAT 的好处是：可以在不访问磁盘中文件的情况下， 通过顺序访问 FAT 表，快速得到文件某个块的地址；也可以快速计算出某个文件占用块的数量。

FAT 相比隐式链接，在计算文件大小和求文件特定块的地址时，由于 FAT 块通常保存在内存，无需访问磁盘，消耗的时间更短。

11.3  Consider a system where free space is kept in a free-space list.

​    a. Consider a file system similar to the one used by UNIX with indexed allocation. How many disk I/O operations might be required to read the contents of a small local file at /a/b/c? Assume that none of the disk blocks is currently being cached.

​    b. Suggest a scheme to ensure that the pointer to the free space list is never lost as a result of memory failure.

a. 需要四次磁盘访问才能读取到文件：第一次读取路径 / 下的目录文件，寻找 /a 目录的物理帝中；第二次访问路径 /a 下的目录文件，获取 /a 路径下的子目录的物理地址；第三次访问 /b 路径下的目录文件，获取 /a/b 路径下的文件的物理地址；第四次访问 /a/b/c 文件

b. 可以将空闲空间链表备份一份，存储在磁盘中。在分配和回收空闲空间时，先修改磁盘中的备份，再修改内存中的链表。
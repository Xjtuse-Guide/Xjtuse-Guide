# OS 第五次作业

7.1  Consider the traffic deadlock depicted in Figure 7.10.

   a. Show that the four necessary conditions for deadlock indeed hold in this example.

   b. State a simple rule for avoiding deadlocks in this system.

1. 互斥：图片中车辆通过路口是互斥的；每次只能有一辆车通过十字路口

   占有并保持：堵车时，车辆通过路口时会堵在路口，从而导致其他车无法通过

   非抢占：当一辆车在十字路口时，其他车辆无法让此辆车离开，自己先通过路口

   循环等待：四个十字路口通过的车辆形成了环路；每个车都在等待其他车辆先通过路口，这些车辆的等待关系构成了环

2. 打破循环等待的条件：在四个十字路口设置红绿灯，四个路口的红绿灯每次只允许所有车辆同时横向或纵向通行；规定即使一方直行变为红灯，另一方直行车辆仍然需要等待这一方的车全部离开路口后才能驶入路口。

 

7.11  Consider the following snapshot of a system:

|      | *Allocation\*A B C D | *Max\*A B C D | *Available\*A B C D |
| ---- | -------------------- | ------------- | ------------------- |
| P0   | 0012                 | 0012          | 1520                |
| P1   | 1000                 | 1750          |                     |
| P2   | 1354                 | 2356          |                     |
| P3   | 0632                 | 0652          |                     |
| P4   | 0014                 | 0656          |                     |

Answer the following questions using the banker’s algorithm:

 a. What is the content of the matrix Need?

需求矩阵的内容如下：

|      | **Need** A B C D |
| ---- | ---------------- |
| P0   | 0000             |
| P1   | 0750             |
| P2   | 1002             |
| P3   | 0020             |
| P4   | 0642             |

 b. Is the system in a safe state?

当前系统是安全的，推导过程如下：

- P0 不需要任何额外资源，因此可以直接结束并释放持有的资源。P0 完成后剩余可用资源如下：

  |      | Need ABCD | Available ABCD |
  | ---- | --------- | -------------- |
  | P0   | Finished  | 1532           |
  | P1   | 0750      |                |
  | P2   | 1002      |                |
  | P3   | 0020      |                |
  | P4   | 0642      |                |

- 此时，剩余资源足够满足 P3 的所有需求，因此 P3 可以完成。P3 释放资源后剩余资源如下：

  |      | Need ABCD | Available ABCD |
  | ---- | --------- | -------------- |
  | P0   | Finished  | 1 11 6 4       |
  | P1   | 0750      |                |
  | P2   | 1002      |                |
  | P3   | Finished  |                |
  | P4   | 0642      |                |

- 此时，剩余资源足够满足 P2 的所有需求，因此 P2 可以完成。P2 释放资源后剩余资源如下：

  |      | Need ABCD | Available ABCD |
  | ---- | --------- | -------------- |
  | P0   | Finished  | 2 14 11 8      |
  | P1   | 0750      |                |
  | P2   | Finished  |                |
  | P3   | Finished  |                |
  | P4   | 0642      |                |

- 此时，剩余资源足够满足 P4 的所有需求，因此 P4 可以完成。P4 释放资源后剩余资源如下：

  |      | Need ABCD | Available ABCD |
  | ---- | --------- | -------------- |
  | P0   | Finished  | 2 14 12 12     |
  | P1   | 0750      |                |
  | P2   | Finished  |                |
  | P3   | Finished  |                |
  | P4   | Finished  |                |

- 此时，剩余资源足够满足 P5 的所有需求，因此 P5 可以完成。

  综上，当前存在安全序列 (P0, P3, P2, P4, P5)，因此当前系统是安全的

 c. If a request from process P1 arrives for (0,4,2,0), can the request be granted immediately?

假设系统接受了此请求，则剩余资源如下：

|      | *Allocation\*A B C D | *Max\*A B C D | Need ABCD | *Available\*A B C D |
| ---- | -------------------- | ------------- | --------- | ------------------- |
| P0   | 0012                 | 0012          | 0000      | 1100                |
| P1   | 1420                 | 1750          | 0330      |                     |
| P2   | 1354                 | 2356          | 1002      |                     |
| P3   | 0632                 | 0652          | 0020      |                     |
| P4   | 0014                 | 0656          | 0642      |                     |

此时，P0 进程可以完成，完成后资源剩余如下：

|      | *Allocation\*A B C D | *Max\*A B C D | Need ABCD | *Available\*A B C D |
| ---- | -------------------- | ------------- | --------- | ------------------- |
| P0   | Finished             | Finished      | Finished  | 1112                |
| P1   | 1420                 | 1750          | 0330      |                     |
| P2   | 1354                 | 2356          | 1002      |                     |
| P3   | 0632                 | 0652          | 0020      |                     |
| P4   | 0014                 | 0656          | 0642      |                     |

此时，P2 进程可以完成，完成后剩余资源如下：

|      | *Allocation\*A B C D | *Max\*A B C D | Need ABCD | *Available\*A B C D |
| ---- | -------------------- | ------------- | --------- | ------------------- |
| P0   | Finished             | Finished      | Finished  | 2466                |
| P1   | 1420                 | 1750          | 0330      |                     |
| P2   | Finished             | Finished      | Finished  |                     |
| P3   | 0632                 | 0652          | 0020      |                     |
| P4   | 0014                 | 0656          | 0642      |                     |

此时，进程 P1、P3 都可以完成，完成后剩余资源如下：

|      | *Allocation\*A B C D | *Max\*A B C D | Need ABCD | *Available\*A B C D |
| ---- | -------------------- | ------------- | --------- | ------------------- |
| P0   | Finished             | Finished      | Finished  | 3 14 11 8           |
| P1   | Finished             | Finished      | Finished  |                     |
| P2   | Finished             | Finished      | Finished  |                     |
| P3   | Finished             | Finished      | Finished  |                     |
| P4   | 0014                 | 0656          | 0642      |                     |

最后，进程 P4 可以完成：

|      | *Allocation\*A B C D | *Max\*A B C D | Need ABCD | *Available\*A B C D |
| ---- | -------------------- | ------------- | --------- | ------------------- |
| P0   | Finished             | Finished      | Finished  | 3 14 12 12          |
| P1   | Finished             | Finished      | Finished  |                     |
| P2   | Finished             | Finished      | Finished  |                     |
| P3   | Finished             | Finished      | Finished  |                     |
| P4   | Finished             | Finished      | Finished  |                     |

因此，存在安全序列（P0，P2，P1，P3，P4），因此系统处于安全状态，从而可以批准 P1 的资源需求。
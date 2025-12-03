# ARM 指令集

本章中会具体提到 ARM 架构包含哪些指令，这些指令的含义和作用。

本章主要讲解 ARM 指令集，在最后会稍微提到 Thumb 指令集。

## ARM 指令集

ARM 指令集为 32 位的指令集，其运行效率较高（每条指令可以进行较多的工作），不过指令密度低（由于所有指令固定 32 位长，简单指令也需要占用同样大的空间）；Thumb 指令集的效率没有那么高（同样的功能需要更多的指令实现），但指令密度较高。

> 指令密度低：ARM 指令格式中包含条件码、多个操作数，即使不需要条件执行/不需要这么多操作数的指令也必须有 32 位长（因为指令集是定长的），因此说密度较低。

- Thumb 指令集是 ARM 指令集的子集
- 所有 ARM 指令都可以是有条件执行的（可以附加一个条件字段，仅在条件为真时才会执行）；但 Thumb 指令的条件执行能力相比 ARM 指令集受到了限制，主要用于分支指令。
- 两种指令之间可以相互调用。

### 指令分类

ARM 指令集总体上可以分为六种指令：

1. 数据处理指令：数据传输、算术指令、逻辑指令、比较指令、乘法指令等内容
2. 程序状态访问指令：mrs 和 msr
3. 跳转指令：b 和 bl；其中 bl 指令带有链接，可以将转移指令后的下一条指令地址放到当前模式的 R14 寄存器下，从而可以实现子程序调用的功能。
4. 访存指令：单数据/多数据访存指令，信号量操作指令
5. 异常中断产生指令：swi 和 bkpt
6. 协处理器指令

### 指令特点

- 所有的 ARM 指令都是 32 位，不论简单/复杂
- 大多数 ARM 指令可以在单个周期内完成（**注意不是所有指令都能在单周期内完成**）
- 所有指令都可以是条件执行的
- load/store 的体系结构（需要通过 load/store 指令显式访问内存）
- 指令集可以通过协处理器扩展

### ARM 指令的格式

![image-20250622142741843](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBFGia98cIKeaOKhMTAiC9_oYTJvxmAAIYHAACnTzZVFhAChCjddezNgQ.png)

<Opcode>{<cond>}{S}<Rd>, <Rn>, <Operand2>

上方图片是指令的格式，下方是 ARM 指令的简单记法。注意**先写目的操作数，再写所有源操作数**。

Cond：28-31 位，共四位，表示指令的条件码

Opcode：21-24 位，共四位，表示指令的操作码

S：第 20 位，表示此操作是否会影响 CPSR（主要是 CPSR 前四个状态位）

Rn：16-19 位，共四位，表示第一个操作数的寄存器编码（采用寄存器寻址）

Rd：12-15 位，共四位，表示目标寄存器（结果存储位置）的编码

Operand2：0-11 位，第二操作数；第二操作数可能采用立即寻址（立即数），寄存器寻址等方法。

### 指令的条件执行

所有 ARM 指令都包含一个条件码（Cond 字段），只有 CPSR 的条件标志位满足条件码时，指令才会被正常执行。**不符合条件而不执行的指令仍然要占用一个时钟周期**。

条件码包含如下内容：

![image-20250622143225604](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBFWia98ozk_S3DnQohCx5rIRw3wAB1QACGRwAAp082VT3PZ8TS0i4jzYE.png)

![image-20250622143236305](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBFmia987nKy5tokqnAzEaOKAvugNSAAIaHAACnTzZVI47YPzB695jNgQ.png)

在简单记法中，条件码会直接写在指令名称的后面。比如：

```c
if (a==b && c==d){
 e++
}
```

翻译为：

```c
cmp r0,r1
cmpeq r2,r3
addeq r4,r4,#1
```

其中 `cmpeq` 就表示仅仅当 CPSR 的 Z 标志为 1（即上一条修改 CPSR 的指令两个操作数相等）时，才会执行此指令。

默认的条件码为 `AL`（Always）；条件码 `NV` (Never) 在 ARMv5 及更高版本的体系结构中已被废弃，不建议使用。虽然它会使指令永远不执行，但该指令仍会占用一个时钟周期，造成性能浪费。

## 寻址方式

寻址方式是指根据指令中的地址码字段寻找真实操作数地址的过程。ARM 处理器具有 9 种寻址方式：

寄存器寻址；立即数寻址；寄存器间接寻址；寄存器移位寻址；基址寻址；多寄存器寻址；块拷贝寻址；栈寻址；相对寻址。

> 由于 ARM 指令集要求通过 LOAD/STORE 指令才可以访问内存，因此没有直接从内存中寻址的方式。

**注意：除了寄存器寻址外的所有方式都只能应用于第二操作数**。**第一个操作数总是只能使用寄存器寻址**。

**寄存器寻址**

操作数的值在寄存器中，指令中的地址码字段指出的是寄存器编号，指令执行时直接取出寄存器值来操作。最常见的寻址方式，比如：

`MOV R1, R2` 中，源操作数和目标操作数都是寄存器寻址（地址码字段给出寄存器的名称）

**立即数寻址**

地址码部分存储的就是操作数本身，也就是说**数据就包含在指令中**。

立即数寻址需要在操作数前面加 **#** 表示这是立即数。

**寄存器间接寻址**

指令中的地址码字段给出了一个通用寄存器的编号。该寄存器中的值被用作操作数的内存地址，处理器通过此地址从内存中读取或写入操作数。

写法实例：`LDR R0, [R2]`，方括号表示寄存器间接寻址。

![image-20250622150524027](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBF2ia99Cgr-PeL639-XESvPEc1Za9AAIbHAACnTzZVJMz5j0WbZ6ONgQ.png)

**寄存器移位寻址**

这是一种寻址和计算混合的方法，只有最后一个操作数可以采用。当第 2 个操作数是寄存器移位方式时，第 2 个寄存器操作数在与第1个操作数结合之前，可以进行移位操作：

`MOV R0, R2, LSL #3` 表示先取 R2 寄存器的数据，将数据左移三位后再作为操作数给出。在此指令中，这意味着写入 R0 的数据是 R2 左移三位后的结果。

`ADD R3, R2, R1, LSL #3` 表示 R3=R2+R1x8（因为 R1 在寻址后左移了三位）

这种寻址方式可以帮助指令集在一条指令中同时完成乘法和其他运算。

**移位方式**

LSL：逻辑左移，将数据左移，左侧溢出丢弃，右侧空白区域补为 0

LSR：逻辑右移，左侧固定采用 0 补全

ASR：算术右移，左侧采用符号位数字补全空位

ROR：循环右移，右侧溢出的位重新从左侧移入

RRX：扩展为 1 的循环右移，用一个一位的 C 标志填充左侧的空白位，随后右侧移出的内容写入 C 标志中。

注意：**只有指令中最右侧的操作数可以进行寄存器移位取址**。

**基址寻址**

将基址寄存器的内容和一个立即数相加，得到真正操作数的地址，常常用于访问基址附近的存储单元。

`LDR R2, [R3, #0x0C]` 表示先取 R3 寄存器的内容，将其和 #0x0C 相加，得到真正操作数的地址。

前索引寻址：`LDR R0, [R1, #4]`

1. 先取 R1 寄存器的内容，将其加上 4 作为实际操作数的地址
2. 取这个实际地址的内容
3. 如果指令后面带有 !，说明需要将 +4 后的地址写回 R1 中

后索引寻址：`LDR R0, [R1], #4`

1. 取 R1 寄存器的内容，将其作为实际操作数的地址
2. 取这个实际地址的内容
3. 一定将 R1+4 回写到 R1 中，这里没得选是否要回写

假设 R0 = 0x1000; 内存区域对应的值如表所示。 执行如下指令后，R0、R1、R2、R3的值分别是 多少?

注意这种题目中 R0=0x1000 表示 **R0 存储的内容为 0x1000**，而不是说 R0 的地址是 0x1000；寄存器没有地址这种说法。

**多寄存器寻址**

此指令允许同时读取/写入 16 个寄存器（或者这些寄存器的任意子集），过程中读取/写入目标会自动自增，具体实例如下：

`LDMIA  R1!,{R2-R7,R12}`：将 R1 存储的地址作为起始地址，连续读取多个字（word）的数据到 R2-R7 和 R12 寄存器中。每读取一个 32 位字后，地址会自动增加 4。

![image-20250622154854339](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBGGia99OudF6bco_PuIzF4kTfXOrmAAIcHAACnTzZVHKdDZVjf1-2NgQ.png)

注意这种寻址方式中，从小到大的连续寄存器可以用 R1-R4 这种形式省略的给出，不连续的寄存器需要通过逗号分隔并且一一给出。

注意 LDMIA 指令是“先读取再加地址”（Increment After）。例如，如果 R1 初始值为 0x1000，该指令会从地址 0x1000 读取数据到 R2，从 0x1004 读取到 R3，以此类推。因为总共加载了 7 个寄存器，所以 R1 的最终值将是 0x1000 + 7 * 4 = 0x101C。

**栈寻址**

基本上只用于 R13 寄存器（因为它是个栈），存在四种方法：

（下图是块寻址指令和栈寻址指令的映射关系，考到了再看）

![image-20250623222901847](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBGWia99bwvEiOyZIIYT5gX3FN3_-NAAIdHAACnTzZVIsOjHjadkLkNgQ.png)

![image-20250530171216858](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBGmia9-nVjqFBTnLqS139oxOxVDivAAIeHAACnTzZVPrt-l0h2hS2NgQ.png)

| 缩写   | 全称             | 栈方向 | SP 指向        | 说明                   |
| ------ | ---------------- | ------ | -------------- | ---------------------- |
| **FA** | Full Ascending   | 向上   | 最后使用地址   | 入栈前 SP 先自增       |
| **FD** | Full Descending  | 向下   | 最后使用地址   | 入栈前 SP 先递减 ✅常用 |
| **EA** | Empty Ascending  | 向上   | 下一个可用地址 | 入栈后 SP 才自增       |
| **ED** | Empty Descending | 向下   | 下一个可用地址 | 入栈后 SP 才递减       |

最常用的是 STMFD 和 LDMFD，即栈方向向下（每次新添加的内容都位于低地址空间），满栈（栈指针指向最后一个入栈的元素，而非下一个空白的元素），因此在读取/写入时需要按照顺序

1. 减小栈的 SP 指针
2. 向当前 SP 指针的位置写入内容

栈寻址同样支持多寄存器的同时读取/写入语法。比如：

`STMFD R13!,{R3-R9}`：存储 R3-R9 多个寄存器到栈，每次存储后栈指针自动变化。

`LDMFD R13!,{R3-R9}`：从栈中弹出对应数量的元素，恢复 R3-R9

> 栈访问指令（如 `STMFD`）通常与 `!` 配合使用，以确保在操作后更新栈指针 `SP` 的值。虽然 `!` 在语法上表示地址回写，但在进行栈操作时，更新栈指针是保持栈正确性的关键，必须添加。

**相对寻址**

相对寻址是基址寻址的一种变通。由程序计数器PC提供基准地址，指令中的地址码字段作为偏移 量，两者相加后得到的地址即为操作数的有效地址。

实际展示为：

```c
BEQ LOOP
LOOP MOV R6, #1
```

实际表现上就是打标签然后跳转到标签对应的语句。相对寻址**不用于取数据，只用于跳转**。

> 在实现中，编译器会寻找调用标签的指令和标签目标指令的偏移量，然后通过 PC+偏移量跳转；不过我们不需要关心这个，只需要知道可以通过标签跳转就行了

## 指令格式补充

![image-20250622161525729](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBG2ia9-zPvFWnuQu4oEnXS2hGTSUeAAIfHAACnTzZVLwOtJj35mfaNgQ.png)

> 说真的，我感觉用不到这张图，但既然是开卷考试，该打印还是打印吧。

![image-20250622161546354](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBKmia-BPo65oukg0L-hmbsUtTLfnWAAIvHAACnTzZVBPwuEDd9eRhNgQ.png)

### 数据处理指令的特点

1. 所有的操作数要么来自寄存器，要么来自立即数，不会来自内存
2. 如果有结果，则结果一定是为32位宽，并且放在一个寄存器中，不会写入内存。(有一个例外:长乘法指令产生64位结果)

### 各种寻址方式对应的第二操作数部分编码

![image-20250622161751896](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBHGia9-9U0XkdGlOuwxNxN7UnLiNTAAIgHAACnTzZVPn1YmdTxf7pNgQ.png)

### 合法立即数与非法立即数

合法立即数：(0->255) 循环右移 2N位（移动偶数位）得到的数字一定都是合法立即数。

> 常见快速判断方法：数据中只有一个字节（2 个 16 进制位）非零——是合法的；
>
> 0-255 范围内的数字——一定合法

非法立即数：不满足上述条件的立即数。

同一个立即数可能有多个表示方法。如: 0x3f0 = 0x3f 循环右移 28位/0x3f0 = 0xfc 循环右移 30位

对立即数的编码规则:

- 如果立即数在 0 – 0xff （0-255，无需位移）之间，移位数为0。

- 否则，就取决于编译器了

![image-20250622162402093](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBHWia9_Io8EbK6-PQDBc6ct8uzjM1AAIhHAACnTzZVPx90JVr7S4-NgQ.png)

### 寄存器移位寻址的两种方式

如果移位的位数由立即数 (5bit，取值范围0 - 31) 给出，就叫作 immediate specified shift;

如果由某个寄存器 Rs 的低 5 位决定，就叫做 register specified shift。

Register specified shift 的两点问题: 

- 不能使用pc：如果将pc寄存器用在 Rn，Rd，Rm 和 Rs 的位置上时，会产生不可预知的结果。 
- 额外代价(overhead)：需要更多的周期而非单一周期才能完成指令，因为ARM没有能力一次读取3个寄存器

### 后缀 s 与 CPSR

数据处理指令携带 s 后缀时，其结果就会影响 CPSR 中的 N、Z、C、V 等标志；比较指令（cmp、cmn、tst、teq）不需要携带 s 后缀就会影响 CPSR。

在数据操作指令中，除了比较指令以外，其它的指令如果带有 s 后缀，同时又以 pc 为目标寄存器进行操作，则操作的同时从 spsr 恢复 cpsr（特殊定义）。

如果在用户模式和系统模式下执行这样的带有 s 后缀且以 pc 为目标寄存器的指令，那么会产生无法预料的后果，因为这两种模式下不存在 SPSR。

## 数据传送指令

### MOV 和 MVN 指令

`MOV Rd, operand2`：进行数据传送，将 operand2 的内容存入 Rd 地址中。格式：

```c
MOV{cond}{S}    Rd,operand2
```

比如 `MOV R1, #0x10` 将 0x10 存入 R1 寄存器中；`MOV R0，R1` 将 R1 的内容存入 R0 寄存器中。

`MVN Rd, operand2`：进行数据传送，先将 operand2 的内容按位取反，再存入 Rd。

注意：

- mvn意为“取反传输”，它把源寄存器的每一位取反，将得到的结果写入结果寄存器。

- movs和mvns指令对pc寄存器赋值时有特殊含义， 表示要求在赋值的同时从spsr中恢复cpsr。

  这样的指令在没有 SPSR 的模式下（用户模式/系统模式）执行时会导致未定义的问题。

- 对于mov和mvn指令，编译器会进行智能的转化。 比如指令“mov r1, 0xffffff00”中的立即数是非法的。在编译时，编译器将其转化为“mvn r1, 0xff”，这样就不违背立即数的要求。所以**对于 mov和mvn指令，可以认为:合法的立即数反码也是合法的立即数。**

## 算术指令

> 注意指令的第一个寄存器都是**目标地址**。后面两个寄存器才是源操作数地址。

### 加法/减法运算

`ADD{cond}{S} Rd, Rn, operand2`：

将 Rn 的值和 operand2 的值相加，（可选的）影响 CPSR 条件位，将其存入 Rd 中。

比如：`ADD R1, R1, R2` 表示 R1 = R1 + R2

`SUB{cond}{S} Rd, Rn, operand2`

将 Rn 的值减去 operand2 的值，存入 Rd 中。

比如：`SUBS R2, R1, R2` 表示 R2=R1-R2，并且影响 CPSR。

### 逆向减法运算

`RSB{cond}{S} Rd, Rn, operand2`

逆向是指**减数和被减数相反**。即计算 `Rd = operand2 - Rn`。

比如：`RSB R2, R1, R2` 表示 R2=R2-R1

### 带进位加法运算

`ADC{cond}{S} Rd, Rn, operand2`

计算 `Rd = Rn + operand2 + C`，即考虑 CPSR 中的 C 寄存器。

> C 寄存器在加法出现进位时为 1，没有进位为 0；减法出现借位时为 0，正常完成1

![image-20250622164752262](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBHmia9_XPkbw9xtP3CSAjqLIDkYSaAAIiHAACnTzZVCdnOt_23_3JNgQ.png)

相当于手动处理每个字中存储数据的加法，并且将每个低位字是否有进位输入给高位。

注意第一个指令不能使用 ADCS，因为之前 CPSR 可能因为其他运算导致 C 位被写为 1，然后因为没有加减法指令导致 C 位一直保留为 1。如果使用 ADCS 的话，就会多加 1 了。

### sbc：考虑借位的减法指令

`sbc r0,r1,r2`：r0 = r1 - r2 + carry - 1

> 注意 sbc 在产生借位时将 CPSR 的 C 标识置为 0，没有借位时为 1，在计算时采用 carry -1 表示借位部分，从而实现“有借位时数值额外 -1”。
>
> 注意 CPSR 产生进位时 C 标识置为 1，产生借位时置为 0，二者的操作是相反的

![image-20250622165103437](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBH2ia9_dQmVkXCKvt0p_V-wqibog7AAIjHAACnTzZVBptFCDbTr5-NgQ.png)

### RSC：带进位逆向减法指令

`RSC{cond}{s} Rd, Rn, operand2`：Rd = operand2 - Rn + carry - 1

![image-20250622165522817](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBIGia9_n-BupgdoWPtgZkvG1pqS94AAIkHAACnTzZVGgxL_SoHSBbNgQ.png)

## 逻辑指令

### AND 指令

指令格式如下：

```
AND{cond}{S} Rd,Rn,operand2
```

cond 的含义：指令的条件码，决定此指令是否真的会执行

S：添加 S 后，此指令可以影响 CPSR 的四个寄存器；不添加 S 时不会影响。

> cmp 等比较指令会强制更新 CPSR；这种指令不强制要求在后面加 S。

此指令将 Rn 和 operand2 **按位求与**，将结果存入 Rd 中。

### ORR 指令

指令格式如下：

```
ORR{cond}{S} Rd,Rn,operand2
```

注意这个指令不叫 OR，而是叫 ORR。

此指令将 Rn 和 operand2 **按位求或**，将结果存入 Rd 中。

举例：

`ORR R0,R0,#0x0F` 可以让 R0 寄存器的低 4 位置为 1

> #0x0F 表示此操作数是一个立即数，不需要根据此操作数访问对应地址的寄存器了，直接取出其内容 0x0F 作为操作数即可

这是因为 0x0F 后四位为 1，和任何一个数字取或时，都会导致结果的后四位恒定为 1。

### EOR 指令

逻辑异或指令，格式如下：

```
EOR{cond}{S} Rd,Rn,operand2
```

此指令将 Rn 和 operand2 **按位异或**，将结果存入 Rd 中。

举例：

`EOR R1,R1,#0x0F` 可以把 R1 的后四位取反。这是利用了“0/1 异或 0 后不变，异或 1 后变为相反的数”这一性质实现的。

### 位清除指令

```
BIC{cond}{S} Rd,Rn,operand2
```

此指令将 operand2 先按位取反，然后和 Rn 做按位与的操作，结果存储到 Rd 中。

举例：

`BIC R1,R1,#0x0F` 可以把 R1 的后四位清零。因为 operand2 的反就是除了低四位全 0 外，其他位都是 1；再做按位与时，得到的结果中低四位肯定为 0.

这么看来，此指令可以通过将 operand2 对应的位标为 1 来清除 Rn 中特定位的值（强制置为 0），因此它叫做位清零指令。

## 比较指令

### CMP 指令

CMP 指令将寄存器 Rn 的值减去 operand2，根据操作的结果更新 CPSR 中的相应条件标志位，以便后面的指令根据相应的条件标志来判断是否执行。

> 如果计算结果为 0，就**更新 CPSR 中的 Z 标志位为 1**，其他情况下设置为 0。
>
> 因此 CMP 指令相当于一条比较两个操作数是否相等的指令。其输出到 CPSR 中，因此不需要目的地址。

```
CMP{cond} Rn.operand2
```

注意 CMP 指令**一定会更新 CPSR**。你加不加 S 是不影响的。

### CMN 指令

CMN 指令使用寄存器 Rn 的值加上 operand2 的值，根据操作的结果更新 CPSR 中的相应条件标志位。

```
CMN{cond} Rn,operand2
```

相当于检查 Rn + operand2 == 0，如果成立则设置 Z 标志位为 1。

举例：

`CMN R0,#1` 判断 R0 是否为 1 的补码。是的话就更新 Z 标志位为 1。

### TST 指令

TST 指令检查 Rn 和 operand2 的与结果，设置 CPSR 的标志位 N 和 Z。

和 ANDS 的区别在于 TST 指令不需要目标操作数来存储与运算的结果。

`TST R0, #0x01`：判断 R0 的后四位是否为 0。如果为 0，那么与运算结果就是 0，CPSR Z 标志为 1，可以通过 EQ 条件码检测这一情况。

### TEQ 指令

TEQ 指令检查 Rn 和 operand2 的异或值，如果为 0 则设置 CPSR Z 标志位为 1。由于二者异或为 0 的前提是完全相等，TEQ 指令相当于判断两个值是否完全相等。

```
TEQ{cond} Rn,operand2
```

> TEQ 指令不会影响 CPSR 的 V 位和 C 位。

### 总结

如果不考虑结果的写回，cmp、cmn、tst 和 teq 分别等价于 subs、adds、 ands 和 eors。

这四条指令的“修改 CPSR”效果本质上是 CPSR 实现的，而不是指令实现的：CPSR 可以根据指令的执行结果是否为 0 设置自身的 Z 标志位。因此，这四条指令无需特殊实现，也能保证结果为 0 时 CPSR 的 Z 位设置为 1（其他情况为 0）

## 程序状态访问指令

当需要修改cpsr/spsr的内容时，首先要读取它的值到一个通用寄存器，然后修改某些位，最后将数据写回到状态寄存器。

cpsr/spsr 不是通用寄存器，不能使用 mov 指令来读写。在 ARM 处理器中，只有 mrs 指令可以读取 cpsr/spsr；只有 msr 可以写 cpsr/spsr。

### 读指令MRS

`mrs r0, cpsr` 读取 cpsr 的值到 r0 中。

`mrs r0, spsr` 读取 spsr 的值到 r0 中。

> 上一章讲过，用户模式和系统模式没有 spsr，因此无法在这些模式下使用 mrs 指令读取 spsr。

### 写指令 msr

![image-20250528204806767](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBIWia9_sOc-41v2lU-ZQzeu0LFoBHAAIlHAACnTzZVEYK82GQvXJONgQ.png)

fields 位的内容可以为 c、x、s、f 或者这四个字母的任意组合。比如，我想通过寄存器 Rm 仅仅更新 CPSR 的低八位（即仅仅使用 Rm 寄存器的低八位），那么我就需要将 fields 填写为 'c'。

如果我想更新 CPSR 的低八位和高八位，那么我就需要将 fields 填写为 'cf'。此时中间十六位仍然会被忽略。

举例：

`msr cpsr_c, #0xd3`

更新 cpsr 寄存器（而不是 SPSR），仅仅使用输入的 0-7 位（即使用 1101 0011 这部分）。此时后五位控制位变为 10011，从而导致处理器切换到管理模式（SVC 模型）；第六位为 0 表示当前仍然执行 ARM 指令；七、八位为 1 表示禁止 FIQ 和 IRQ 中断。

**CPSR 每位的具体含义见课本 63 页**，需要根据每位的含义才能判断 msr 指令复制后的  CPSR 到底是个什么状态。

说明：

1. user和system模式没有spsr，因此这些模式下不能对spsr操作。

2. 由于权限问题，在 user 模式下对 cpsr 的控制位域（cpsr[7:0]）的修改是无效的。

3. 如果使用立即数，必须使用合法的立即数。

   事实上，如果使用立即数的话，只能修改 CPSR 八位的内容；更长的立即数会导致 0-255 右移 2n 位的限制从而形成非法立即数。

4. 程序不能通过“ msr 修改 cpsr 的 T 位”来完成 ARM/Thumb 态的切换。必须使用 bx 指令，因为 bx 属于分支指令，它会打断流水线， 实现处理器状态切换。

5. 如果要修改读出的值，仅修改必要的位，其它位保持不变，这样保持了最大兼容性。

修改 CPSR 的实例：

> 下面的代码比较复杂，是为了保留 CPSR 6-8 位的原始值

从监控模式切换到IRQ模式(例如启动时初始化IRQ堆栈指针) 

- MRS R0，CPSR：将 CPSR 传送到 R0
- BIC R0,R0,#0x1F：R0 低 5 位清零
- ORR R0，R0，#0x12：设置 R0 低位为 IRQ 模式对应值
- MSR CPSR_c,R0：传送回CPSR

设置标志字段：

- MSR CPSR_f, #0xf0000000：设置N，V，N，C均为1

  **注意这里后面 24 位不需要设置的话也要填 0**。

## 跳转/分支指令

在ARM中有两种方式可以实现程序的跳转，一种是使用分支指令直接跳转，另一种则是直接向PC 寄存器赋值实现跳转。 分支指令有以下三种:

- 分支指令B：先为跳转目标定义一个标签 label，然后就可以通过 `B label` 实现无条件跳转。
- 带链接的分支指令BL：和 B 指令差不多，但在跳转前会记录 PC 的值，子程序执行结束后，将记录的值推回 PC，实现子程序执行结束后跳回原先的调用位置。
- 带状态切换的分支指令BX。

B 和 BL 指令的编码格式如下（二者格式基本相同，只有一个标志位不同）：

![image-20250528211258940](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBImia9_35TaEuPGdjKB0f-4eJWg8jAAImHAACnTzZVCmRhy32hD9lNgQ.png)

### B/BL 指令

B指令，该指令跳转范围限制在当前指令 的±32MB字节地址内。

```
B{cond} Label
```

两种使用方法：

`B WAITA`：跳转到 WAITA 标签处

`B #0x1234`：跳转到绝对地址 0x1234 处

当转移指令执行时，处理器将指令中的offset(24bit) 左移2bit，变成26bit，表示± 32M的范围。

> 因此最低两位地址是固定为 0 的，也就是说 B 指令只能跳转到最后两位为 0 的地址。

执行后， pc从新的地址执行，流水线清空。

如果使用的是“bl”指令，将返回地址写入lr寄存器。子程序返回时只需要用 lr 恢复 pc 就可以: mov pc, lr。“b”指令不影响 lr 寄存器

### BX 指令

`B{L}X {<cond>} Rm`，其中 Rm 是一个四位的数字。

如果 Rm 的最后一位为 1，那么表示要切换处理器状态为 Thumb 状态。这是因为正常状态下，Rm 的末位一定是 0。

## 访存指令

LDR 指令用于加载内存中的字/字节到寄存器中。其格式如下：

`LDR Rd,[Rbase]`

Rd 表示加载后存放的目标寄存器，Rbase 为需要加载数据的开始地址。

LDR 指令包含多种变种，可以用于加载不同长度/不同类型的数据，具体的各种指令如下：

![image-20250530164302732](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBI2ia-AAB0VslApa2HPMNj0fb0V3Z-wACJxwAAp082VQNkSJq-X1dxjYE.png)

默认为加载一个字（4 字节）数据。加 B 代表加载单个字节；加 H 代表加载半字（一个字是 4 字节，半字就是 2 字节）；加 S 代表加载有符号的数据，且 S 和 B/H 可以同时使用。

`STR Rd,[Rbase]` 可以用于存储寄存器中的数据到内存中，同样包含几个变种指令。加 B 表示只存储 Rd 的第一个字节，加 H 表示存储 Rd 的第一个半字（2 字节数据）。

> 注意一般第一个操作数是目标操作数，但这里 Rd 是源操作数，我们将 Rd 的内容存储到 Rbase 对应的内存地址里。

### 访存指令的格式

两种访存指令的具体格式如下：

![image-20250530164834824](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBJGia-ANHb4QIebrQoTaNVp_3Mg6UAAIoHAACnTzZVLLlah3wtQHHNgQ.png)

P 代表前/后变址。前变址是指先计算偏移地址，再用新地址访问内存；后变址是指先用原始地址访问内存，再计算偏移地址（通常用于更新基址寄存器）。

P、I、B 等内容都在变址部分讲到过。

L 用于区分加载/存储，即区分指令到底是 LDR 还是 STR。

### 访存指令寻址方式

 LDR/STR 指令寻址非常灵活，它由两部分组成，其中一部分为一个基址寄存器，可以为任一个通用寄存器;另一部分为一个地址偏移量。地址偏移量有以下3种格式:

- 立即数:立即数可以是一个无符号的数值。这个数据可以加到基址寄存器，也可以从基址寄存器中减去这个数值。

  如:`LDR R1,[R0,#0x12]`

  这里是**前变址**，因为需要先加地址（R0+0x12）再访问对应位置的数据。

  > 后变址的写法为 `LDR R1,[R0], #0x12`，即后面的数字在方括号外面

- 寄存器:寄存器中的数值可以加到基址寄存器，也可以从基址寄存器中减去这个数值。

  如:LDR R1,[R0,R2]

  其实就是改用寄存器而非立即数存储变址了。

- 寄存器及移位常数:寄存器移位后的值可以加到基址寄存器，也可以从基址寄存器中减去这个数值。

  如:LDR R1,[R0,R2,LSL #2]

从寻址方式的地址计算方法分，加载/存储指令有以下4种格式:

- 零偏移：不进行变址，如:LDR Rd,[Rn]

- 前索引偏移：先计算 `Rn + offset` 得到有效地址，然后从该地址加载数据。如:LDR Rd,[Rn,#0x04]!

  如果指令以 `!` 结尾，表示需要将计算出的有效地址写回到基址寄存器 Rn 中（地址回写）。

- 程序相对偏移： 如:LDR Rd,label

- 后索引偏移：先使用 Rn 的值作为有效地址加载数据，然后计算 `Rn + offset` 并将结果写回到 Rn。如:LDR Rd,[Rn],#0x04

  后索引模式总是会回写更新后的地址到基址寄存器。

## 多寄存器访存指令

有时我们需要同时读取/写入多个寄存器（比如切换 CPU 运行状态时），此时就需要多寄存器的访存指令了。

![image-20250530170652801](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBJWia-AUwBCwaSEHQnMSwGm9jjzpUAAIpHAACnTzZVHln7Tjq3mJBNgQ.png)

寄存器加载/存储指令可以实现在一组寄存器和一块连续的内存单元之间传输数据。LDM 为加载多个寄存器 STM 为存储多个寄存器。允许一 条指令传送16个寄存器的任何子集或所有寄存器。

多寄存器加载/存储指令的8种模式如下表所示，右边四种为堆栈，有边为四种数据传送操作。

![image-20250530171216858](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBJmia-AgDV4Fjy2oEI53sluzWfDDtAAIqHAACnTzZVA3v0_5i2ECCNgQ.png)

包含 A：前变址；包含 B：后变址。

![image-20250530171550053](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBJ2ia-At0E51ENAN78hsa0x_jcyCQAAIrHAACnTzZVA9fdjL3r4lLNgQ.png)

上图上面两个是前变址，下面两个是后变址。最小号的寄存器对应最低的内存地址；最大的寄存器一定对应一个较大的内存地址。

新加入的地址会放到地址的高位处。

数据传送指令同样可以用于堆栈操作（需要采用后变址的），即 DA 后缀对应了 ED；IB 对应了 ED。

## Thumb 指令集简介

Thumb 指令集的特点：

1. 16 位的指令子集，代码密度高（相比 ARM 指令集）
2. 在指令集名中，含有T的均可执行Thumb指令。
3. CPSR 中的 T 标志位决定是执行Thumb指令还是ARM指 令，如置位，执行Thumb指令，否则执行ARM指令。
4. Thumb状态下没有协处理器指令。
5. 所有Thumb指令均有对应的ARM指令。
6. Thumb 是一个不完整的体系结构，不能指望处理器只执行 Thumb 代码而不支持 ARM 指令集。

Thumb 指令集中，只有 ISA（分支跳转指令）可以条件执行，不像 ARM 中任何指令都可以条件执行；

由于 16 位的限制，桶形移位操作也变成单独指令

> ARM 中数学运算和移位可以在同一指令中完成

### Thumb 指令寄存器的使用

1. 只有R0-R7可以被任意指令访问

2. R8-R12只能通过MOV、ADD和CMP访问

3. R13 (sp)、R14(lr)、R15(pc)限制访 问

4. cpsr 间接访问 ( CMP 和数据处理指令影响) 
5. spsr 不能访问

在 ARM 中，R0-R12 寄存器可以任意访问，R13-15 理论上也可以访问，实际中建议只使用特定指令访问。CPSR 和 SPSR 可以访问，不过需要注意用户/系统态下没有 SPSR。



## 练习

![image-20250530181950776](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBKGia-A1KNnlqC7fgy4-rdY7Y1AABNQACLBwAAp082VRGCRvtaWZFhDYE.png)

注意函数返回一个值的方法为：

- 和外界函数约定好一个返回值存放位置（比如 r0）
- 在 `mov pc, lr` 之前，先设置 r0 内容为需要返回的值（`mov r0, #0`）
- 外层函数去读取 r0 的值（`ldr r1, [r0]`），然后使用

这个返回值存放位置是很自由的，没有什么协议约定。自己手写汇编的话，只需要保证外层函数和内层函数存放位置是对的就行了。编译器写汇编的话，实在不知道怎么做……

![image-20250623214455575](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBKWia-BCGse6cN_9nutmcNAVycffhAAItHAACnTzZVI4d7MC0B2JMNgQ.png)

注意 ldr 和 str 实现内存数据的读写；#4 是因为 int 占据四个字节，所以每次复制后索引变址四个字节。

此外，注意 *(src++) 这种语句**是先取值再自增指针**，并不会因为 src++在括号内就先自增指针；只有 ++src 才会先自增指针。

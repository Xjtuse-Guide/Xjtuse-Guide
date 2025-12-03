# ARM 程序设计

## ARM 汇编语言的伪操作、宏指令和伪指令

伪操作：ARM 汇编语言中一些特殊的助记符，它的作用主要是为完成汇编程序做各种准备工作，在源程序进行汇编时由汇编程序处理，而不是在计算机运行期间由机器执行。 也就是说，这些伪操作只在汇编过程中起作用，一旦汇编结束，伪操作的使命也就随之结束了。

宏指令：类似 C 语言的 `#define` 宏。宏指令就是一段预先定义的代码，定义后，每次使用宏指令时，都会将使用处的代码直接替换为宏定义中的内容。

伪指令：特殊的指令助记符；在实际生成汇编代码时，会使用具体的汇编指令替代掉伪指令。

伪指令和伪操作很相似，不过伪指令一般是用于简化程序员记忆负担的，伪操作是编译器用于辅助汇编的。

### ARM 语言的开发环境

ADS 开发环境：ARM 公司自己推出的 IDE+编译器

集成了 GNU 工具的开发环境

本书只讲解 ADS 开发环境下的开发。

## ADS 开发环境下的伪操作

这里伪操作比较多，重点掌握老师 ppt 上标红的伪操作。

**P125 开始**

### 符号定义操作

`GBLA`，`GBLL`，`GBLS`

这三种伪操作用于定义一个全局范围内的变量，其中 GBLA 声明一个算数变量（0），GBLL 为逻辑变量（FALSE），GBLS 为字符串变量（空串）。格式：

`GBLX <variable>`

variable 在全局范围内必须是唯一的名称。

可以通过 `<variable> SETA/SETL/SETS <value>` 指令为某个已经声明的变量赋值。

`LCLA, LCLL, LCLS` 定义了局部的算术/逻辑/字符串变量。

### 数据定义操作

`MAP` 伪操作用于定义一个结构表。结构表类似 C 语言中的一个结构体（struct）。

`MAP expr`：定义一个首地址为 expr 的结构表。定义完成后，内存表的位置计数器设置为 expr

`FIELD`：用于定义结构表中的一个元素。相当于 C 结构体中的单个元素。格式如下：

`{label} FIELD expr`

expr 表示这个元素占用的内存空间（长度）。可选的 {label} 会成为此元素的变量名称。

在使用 FIELD 语句时，编译器自动找到最近的一个 MAP 声明，找到其内存表的位置计数器，让变量 label 对应此计数器（从而让 label 对应了此元素的实际地址），之后内存表的位置计数器 += expr（后移）。

定义一个内存表后，其后面的 FIELD 指令都会跟随此内存表的位置计数器（即都视为此内存表的元素），直到通过 MAP 定义下一个内存表为止。

通过结合 MAP 和 FIELD 指令，就可以定义一个内存表（类似结构体）。

`SPACE` 伪操作：分配一块连续的内存单元

`{label} SPACE expr`

expr 表示需要分配的内存单元的长度；{label} 是一个可选的标签，如果写了，那么此标签会指向新的内存单元的首地址，可以在其他指令中通过此标签使用这块内存的内容。

`DCD/DCDU` 伪操作：分配一段字内存单元，DCDU 与 DCD 的不同之处在于 DCDU 分配的内存单元并不严格为字对齐。DCD/DCDU 一般用来定义数据表格（数字数组）或其他常数

`{label} DCD expr`：分配一个或者多个字单元，其长度正好能够放下 expr 的内容，并使用 expr 初始化这块单元。比如：

`Data1 DCD 1,5,10`：初始化三个字单元，分别存放数字 1,5,10。Data1 标签指向这段单元的第一个地址，因此后面可以通过 Data1 访问这段数据。

`student DCB "student"`：和 DCD 类似，只不过按照字节为单位分配，更加适合字符串

翻译方法：

**每个元素不同的数组用 DCD 定义，字符串用 DCB 分配**

**全部为 0 的数组用 SPACE 定义**

### 控制操作

IF 语句：

```
IF {表达式 1}

    {表达式 2}

ELSE

    {表达式 3}

ENDIF
```

IF 伪操作长得和 C 语言中的 IF 语句还是比较像的。注意需要 ENDIF 标记语句的结束。

WHILE 语句：

```
WHILE {表达式 1}
    {表达式 2}
WEND
```

注意同样需要 WEND 标记语句的结束。

程序举例：

```
GBLA abc
GBLA testval
abc SETA 3
IF testval < 5
mov r0, #abc
ELSE
mov r1, #abc
ENDIF
IF :DEF:testval
mov r2, #abc
ELSE
mov r3
ENDIF
```

```
GBLA test
test SETA 5
WHILE test >= 0
test SETA test - 1
mov r0,#test
WEND
```

宏操作定义：

```
MACRO
{$label} macroname {$para1{,$para2{,$para3...}}}
...（宏内容）
MEND
```

定义一个宏，包含 para1, para2, para3 等三个参数，名称为 macroname，label 为一个可选的标号。仍然注意需要 `MEND` 表示宏的结束。

宏内容中的所有 \$label, \$para1, \$para2, \$para3 等内容在被调用时都会替换为实际传输的内容。比如，假设宏中内容为：

```
MACRO
$label LOOP $para1
mov r6, #10
$label.loop1
mov r0, #$para1
subs r6,r6,#1
bne r6, $label.loop1
MEND
```

那么通过 `AA LOOP 10` 调用时，编译前代码就会替换为：

```
mov r6, #10
AA.loop1
mov r0, #10
subs r6,r6,#1
bne r6, AA.loop1
```

### 信息报告操作

`ASSERT` 伪操作（断言伪操作）：

`ERROR` 操作：

### 其他操作

`ENTRY` 操作：指定程序的入口点

`ENTRY` 操作没有参数，直接写在第一行程序开始前就行。

`END` 操作：标志源程序的结束

`END` 操作没有参数，直接写在源程序最后就可以了。

具体几个实例请见 ppt。

## ARM 伪指令

ARM 伪指令包括 ADR、ADRL、 LDR 和 NOP 指令。这些指令格式类似 ARM 指令集，但不真正是指令集中的内容，需要在编译时替换为实际指令。这四个指令都和地址读取有关。

### ADR 指令

小范围的地址读取指令

`ADR{cond} register, expr`

此指令将 expr（基于 PC 或者基于寄存器的地址表达式）解得的内容（地址/偏移后的地址）存储在 register 寄存器中。

expr 的取值范围如下：（受到此字段长度总共 9 位的限制）

- 地址值不是字对齐时，需要精确到字节，取值为 -255~255 字节
- 地址值是字对齐时，只需要精确到字，省出两位，取值为 -1020-1020 字节

其通常用法是**读取一个标号对应指令的地址**，即获得**一条指令存放在哪里**，将其写入第一个参数（寄存器）中。

实际中，该指令会被翻译为一条 ADD/SUB 指令，通过和 PC 的偏移量来计算需要的地址。比如：

```
ADR R0, Delay
...
Delay: MOV R0, r14
```

会被翻译为：

```
0x20 ADD r0,pc,#0x3c
...
0x64 MOV R0,r14
```

0x64 和 0x20 之间的偏移量为 0x44。但是，由于执行到 0x20 指令时，PC 实际上在 0x28（因为取指-译码-执行流水线中，一条指令处于执行状态时，PC 已经跑到后两条指令上了），因此只需要偏移 0x64-0x28=0x3c。

此指令要求在编译时必须可以转换为单条 ADD/SUB 指令，即后面的立即数偏移（比如 0x3c）必须要能在一个参数的大小中放下；放不下的话，编译器就会报错。

### ADRL 指令

中等范围的地址读取指令

`ADRL{cond} register expr`

功能几乎和 ADR 指令完全相同。区别在于编译器会尝试将其编译为**两条** ADD/SUB 指令，因此，expr 偏移量取值范围如下：

- 非字对齐：-64KB-64KB
- 字对齐：-256KB-256KB

如果两条指令还是无法完全存放下总偏移量，编译器会报错。

比如：

```
start MOV R0, #10
...   ADRL R4, start+60000
```

会被翻译为：

```
0x1c MOV R0,#10
0x20 ADD R4,PC,#0xE800
0x24 ADD R4,R4,#0x254
```

注意执行到 0x20 指令时，PC =0x20+8=0x28，因此 start = PC - 12。我们需要计算 start +60000，就是计算 PC + 59988。实现中，我们把 59988 拆分成 59392+594，即 0xE800+0x254。

### LDR 指令

LDR伪指令将一个 32 位的立即数或者一个地址值读取到寄存器中。 语法格式:

> 注意这里**不是读取地址值对应的数据**，而是**直接读取地址值**。

`LDR{cond} register,=expr`

> 真正的 LDR 指令没有这个等号，`LDR R1, [0xFF]` 是真正的指令，表示读取 0xFF 指向的内容到 R1 中。
>
> LDR 伪指令带有等号，`LDR R1, =0xFF` 就是把 0xFF 这个立即数赋值到 R1 中。

当参数 expr 是立即数时，**可以不受合法立即数长度的限制**进行赋值；当参数 expr 是标签时，可以**读取标签所对应指令的地址到寄存器中**。

其中 :cond 为可选的指令执行条件

register 为目标寄存器

expr 为 32 位常量。编译器将根据 expr 的取值情况 ，对 LDR 伪指令做如下处理 :

> 当expr表示的地址值在MOV或MVN指令中地址的取值范围以内时，编译器用合适的 MOV 或者MVN 指令代替该LDR 伪指令。
>
> 当 expr 表示的地址值超过 MOV 或 MVN 指令中地址的取值范围时，编译器 一般将该常数放在数据缓冲区(也称为文字池)中，同时用一条基于 PC 的 LDR 指令读取该常数。

![image-20250623232131708](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBK2ibCwSpWGgWb4RE4x6OF_8K-AmVAAJmHAACnTzZVPC9Ld1Fb8qKNgQ.png)

![image-20250623232141653](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBLGibCwdWVURb94C2t2gQGLvA8BP-AAJnHAACnTzZVOZ_2n19zzYeNgQ.png)

### NOP 指令

空操作指令，主要作用就是让流水线空一拍。在实际编译时，会被编译器替换为没有效果的指令（比如 MOV r0,r0）

不需要参数。比如：`NOP`。

## ARM 汇编语言程序设计

ARM 汇编源文件的后缀名为 .s，C 文件编程（混合式编程）的后缀为 .c，头文件后缀为 .h

ARM 汇编语言语句格式如下:

`{symbol) {instruction| directive| pseudo-instruction) {;comment}`

其中:

instruction 为指令。在 ARM 汇编语言中，指令不能从一行的行头开始。在一行语句中， 指令的前面必须有空格或者符号（symbol)。

directive 为伪操作。

pseudo-instruction 为伪指令。

symbol 为符号。在ARM汇编语言中，符号必须从一行的行头开始，且符号中不能包含空格。在指令和伪指令中

符号用做地址标号；在有些伪操作中，符号用做变量或常量。
comment 为语句的注释。在ARM汇编语言中注释以分号 “;” 开头。注释的结尾即为一行的结尾。注释也可以单独占用一行。

### 子程序调用和返回

采用 `BL `指令调用子程序，传入子程序的名称作为参数（因此子程序的第一行代码需要标签作为子程序名称）

子程序返回时，将 LR 的内容存入 PC 即可（注意嵌套调用时，需要将 LR 的内容保存到 R14 栈中）

![image-20250623232441539](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBLWibCwpZpStbY_lQ89cQNxhXgoAeAAJoHAACnTzZVBx_QVSG8E3CNgQ.png)

### 拷贝程序示例

![image-20250623232722966](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBLmibCw26gHaA2cavdsnbBvsMTiT1AAJpHAACnTzZVM3b_jzsMjxiNgQ.png)

![image-20250623232736045](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBL2ibCxC1QOjGq3Qfncb8w2wbWaoEAAJqHAACnTzZVEHuRt9rEAuDNgQ.png)

## C 语言的嵌入式编程

> 课程中只讲述部分 C 语言嵌入式编程的技巧

### 变量定义

在变量声明的时候，最好把所有相同类型的变量放在一起定义，这样可以优化存储器布局。

![image-20250606165919264](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBMGibCxPlQ5NgSW2JURQVyls29wh8AAJrHAACnTzZVO1Fws9GlHR-NgQ.png)

如果没有将相同长度的变量放在一起定义，由于嵌入式设备字长度为 4 字节，因此可能导致左侧那样几个变量存在一个字中时，无法填满这个字，导致部分空间被浪费了。

局部变量类型的定义，使用short或char来定义变量并不 是总能节省存储空间。有时使用32位int或unsigned int局部变量更有效率一些：

![image-20250606170238194](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBMWibCxUYg1kQzZT8ILKJ0y1dCXhDAAJsHAACnTzZVIcCBkL2l4DdNgQ.png)

第二种情况（采用 short 数据类型）时，需要先将 a1 左移 16 位再右移 16 位以便置高位为 0，相比第一种采用 int 类型反而多了两条指令。

如果参数是 char 类型，那么需要通过与操作把高 32 位置为 0，只保留第 8 位，因此相对 int 也多了一条指令。

本质是因为 ARM 嵌入式设备按照字（4 字节）寻址，int 正好占满四字节因此不需要特殊处理，其他数据类型都需要把一个字的高位设置为零。

3. 变量定义中，为了精简程序，程序员总是竭力避免使用冗余变量。但有时使用冗余变量可以减少存储器访问的次数这可以提高系统性能.

比如：

```c

int f (void)
int g (void)
int errs;
void test1(void)
{
    errs+=f();
    errs+=g();
}
void test2(void)
{
    int temp=errs;
	temp+=f();
	temp+=g();
	errs=temp;
}
```

test1 函数的 errs 是内存变量，因此每次 errs+=f() 都需要读取并写入内存一次；test2 函数中定义的 temp 局部变量会被分配一个寄存器，每次修改都是寄存器读写，远快于第一种函数的内存读写。

### 参数传递

为了使单独编译的 C 语言程序和汇编程序能够互相调用，定义了统一的函数过程调用标准 ATPCS。 ATPCS 定义了寄存器组中的 **{**R0**~**R3**}** 作为参数传递和结果返回寄存器，如果参数数目超过四个，则使用栈进行传递

内部寄存器的访问速度是远远大于存储器的，所以要尽量使参数传递在寄存器里面进行，即应**尽量把函数的参数控制在四个以下**。

### 循环条件

计数循环（特定次数循环）是程序中十分常用的流程控制结构，一般有以下两种形式:

- for(loop=1;loop<=limit;loop++)

- for(loop=limit;loop!=0;loop--) 

  这两种循环形式在逻辑上并没有效率差异， 但是映射到具体的体系结构中时，就产生了不同

![image-20250606171441429](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBMmibCxikkzOxHgTBtR1cjab_UiFbAAJtHAACnTzZVBcEaKg5R95UNgQ.png)

右侧少一条指令，是因为 SUBS 指令完成了左侧 CMP 指令的任务：SUBS 指令带 s，会更新 CPSR 寄存器，因此当 R1 内容变为 0 时，CPSR 的对应条件位就会变成 1，这样通过 BNE 指令就可以在 R1==0 时不跳转（离开循环），其他情况下跳转（继续循环）了，省略了 CMP 指令。

## C 与汇编语言的混合编程

ATPCS 是 ARM程序和 Thumb 程序中子程序调用的基本规则，目的是为了使单独编译的 C 语言程序和汇编程序之间能够相互调用。这些基本规则包括子程序调用过程中寄存器的使用规则、数据栈的使用规则和参数的传递规则。

即 C 语言程序和汇编程序想要相互调用，就必须遵守以下的规则：

R0-R15 寄存器的功能：

![image-20250606172047920](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBM2ibCxszzd4VcC-o22bc-Lhm1ZVQAAJuHAACnTzZVJXhHmRWrUcENgQ.png)

R12：在嵌套函数调用时，存储第一个函数参数的功能。`r0-r3`四个寄存器用于存储函数调用的参数，即进行嵌套调用前，通过 `mov r12, r0` 保存当前参数 r0 到 r12 中，调用完成后通过 `mov r0, r12` 恢复保存的参数，否则嵌套过程调用时参数就会丢失了。

### 寄存器的使用规则

1. 子程序间通过寄存器R0-R3来传递参数，此时寄存器R0-R3可以记作 A1-A4，被调用的子程序在返回前无需恢复寄存器R0-R3的内容。

2. 子程序中，使用寄存器R4-R11来保存局部变量，这时寄存器可以记作 V1-V8。若子程序中用到了寄存器 V1-V8 中的某些，**子程序进入时必须保存这些用到的寄存器，在返回时必须恢复**。 
3. 寄存器R12用作子程序间调用时临时保存栈指针，记作IP。 
4. 4.寄存器P13用作堆栈指针，记作SP。在子程序中，R13不能用作其他 用途，进入和退出子程序时的值必须相等。 
5. 5.寄存器R14用作链接寄存器，LR，一般用于保存子程序的返回地址。 
6. 6.寄存器R15是程序寄存器：PC，它不能用作其他用途。

ARM 栈指针采用**满地址栈**，满递减的 FD 类型。

### 参数适用的规则

参数个数可变的子程序参数传递规则

- 当参数不超过 4 个时，可以使用寄存器 R0~R3来传递参数

- 当参数超过4个时，剩余参数使用数据栈来传递参数。

  > 注意只是**多于四个的参数采用数据栈传递**。前四个参数仍然可以通过寄存器 R0-R3 传递。

- 入栈的顺序与参数顺序相反,即最后一个字数据先入

结果返回规则：

结果为一个 32 位的整数时，可以通过寄存器 R0 返回;结果为一 个 64 位整数时，可以通过寄存器 R0 和 R1 返回，依次类推

## C 和 ARM 嵌入式汇编程序的相互调用

### 汇编程序访问 C 语言的全局变量

汇编程序可以通过地址间接访问在 C 语言程序中声明的全局 变量。通过使用IMPORT关键词声明全局变量，再将该变量地址装载 到寄存器中(利用LDR和STR指令根据全局变量的地址可以访问它们)

对于不同类型的变量，需要采用不同选项的LDR和STR指令，如下所示:

```
unsigned  char LDRB/STRB（读写一字节）
unsigned  short LDRH/STRH（读写两字节）
unsigned  int LDR/STR（读写一整个字，即 4 字节）
char LDRSB/STRSB（带 S 的指令可以读取负数，并存储为有符号数）
short LDRSH/STRSH
```

![image-20250606174600437](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBNGibCx2zKUO5dffzVOkaizrLGVgiAAJvHAACnTzZVNNg0-FBPJycNgQ.png)

上例程序中的 globv1 是一个调用了此汇编片段的 C 程序中声明的全局变量。在汇编程序中要用 IMPORT 声明该变量，并将该变量的内存地址读取到 R1 中（注意采用的指令是 ldr 伪指令而不是 ldr 指令，因此 r1 中存储的是 **globv1 的地址**而非 globv1 地址的内容），然后通过真正的 LDR 指令就可以从此地址中读取内容了。

### C 语言中调用汇编程序

为了保证程序调用时参数的正确传递，汇编程序的设计要遵守 ATPCS。C中调用汇编文件的函数主要工作有两个: 

1. 在汇编程序中需要使用 EXPORT 伪操作来导出函数名， 并用该函数名作为汇编代码段的标识，最后用 mov pc,lr 返回
2. 在 C 程序调用该汇编程序之前需要在 C 语言程序中使用 extern 关键词声明汇编程序对应函数的原型（函数名称和参数类型），函数名称需要和汇编语言中起的函数名相同。

![image-20250606175508644](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBNWibCyDJwm4lHuld_fX7Ych6NK55AAJwHAACnTzZVLlgK6MWp8agNgQ.png)

右侧汇编程序是一个字符串拷贝程序。其中 `CMP r2, #0` 这行就是比较当前拷贝的单个字符是否为 0，如果为 0 说明遇到了 C 中的字符串终止符号，因此结束拷贝。

C 语言中声明了此汇编函数，名称和汇编中定义的函数名相同，参数 d 和 s 直接对应了汇编中访问的 r0 和 r1 寄存器（因为汇编调用就是这么传参的）。

注意汇编程序的最后必须是 `MOV pc, lr`。

### 汇编程序中调用 C 语言函数

**P188**

- 为了保证程序调用时参数的正确传递，汇编程序的设计要遵守ATPCS

- 在 C 程序中不需要使用任何关键字来声明将被汇编语言调用的 C 程序，但是在汇编程序调用该 C 程序之前需要在汇编语言程序中使用 IMPORT 伪操作来声明该 C 程序。在汇编程序中通过 BL 指令来调用子程序

> 这和 C 语言调用汇编程序不同。C 语言调用汇编程序时，汇编程序需要通过 EXPORT 语句声明自己。

![image-20250606180702366](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBNmibCyK59em_qZxHYVto92OdKRDjAAJxHAACnTzZVPzzK0SA04qzNgQ.png)

`STR r3, [sp, #-4]` 是因为汇编传参只能使用 r0-r3 四个寄存器，第五个参数需要放到数据栈中（即 SP 栈中），因此做先移位再写入，将第五个参数存储到数据栈中。

前面 r3 存储的都是 5i（即 r3 被当成临时变量了），直到 `ADD r3, r1, r1` 这条语句执行完之后，r3 中才真正的存储了正确的参数 r1。

后面恢复了 SP 指针（之前把 SP 指针移动了 -4）

## 课程重点回顾

本课程的核心内容可以总结为以下几个方面，掌握这些将有助于你更好地理解嵌入式系统开发：

1.  **嵌入式系统基础**:
    *   理解嵌入式系统的定义、组成结构及其与通用计算机的异同。
    *   熟悉嵌入式系统的软硬件开发流程。

2.  **ARM 处理器架构**:
    *   掌握 CISC 和 RISC 架构的特性与区别。
    *   理解 ARM7TDMI 的基本硬件结构，包括冯诺依曼与哈佛架构的区别及其影响。
    *   熟悉三级流水线的工作原理、可能遇到的冲突及其解决方法。
    *   掌握 ARM 的基本寄存器用途，特别是 R13 (SP), R14 (LR), R15 (PC)。

3.  **ARM 编程模型**:
    *   理解 ARM 的异常和中断机制，包括优先级、处理流程和寄存器变化。
    *   了解大端与小端存储模式。

4.  **ARM & Thumb 指令集**:
    *   熟悉 ARM 指令集的特点、机器码格式和条件执行。
    *   掌握九种基本寻址方式，理解合法与非法立即数的概念。
    *   对数据处理指令、访存指令、跳转指令等有深入理解。
    *   了解 Thumb 指令集的特点（无需深入编程）。

5.  **汇编与 C 语言混合编程**:
    *   区分伪操作、伪指令和宏指令的定义与用途。
    *   掌握常用伪操作，特别是与地址读取相关的 `ADR`, `ADRL`, `LDR`。
    *   理解 ATPCS（ARM 过程调用标准），掌握汇编与 C 语言相互调用的方法和规则。

学习本课程需要多加练习，深入理解指令和编程范例的含义，而不仅仅是记忆。
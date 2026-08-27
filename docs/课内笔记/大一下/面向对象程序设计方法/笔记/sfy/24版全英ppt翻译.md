# 24版全英ppt翻译

问答部分以及部分示例的解释为笔者自行补充，其余为ys老师24级版本ppt原文翻译

[原文链接](https://blog.csdn.net/Genevieve_xiao/article/details/147710673)

# 第 1 单元：Java 基本介绍
## Java 是什么？

- Java 是由 Sun Microsystems 公司开发的一种面向对象的编程语言。
- Java 拥有一系列标准化的类库，支持预定义的可重用功能。
 - Java 还具有可以嵌入到 Web 浏览器和操作系统中的运行时环境。

## Java 编程语言的特点
 * **面向对象** ：Java 支持使用对象的概念进行软件开发。用 Java 开发的软件由类和对象组成。
 * **网络功能强大** ：Java 支持分布式应用程序的开发。某些类型的 Java 应用程序是通过 Web 浏览器访问设计的。
  * **健壮性** ：Java 的许多方面都促进了可靠软件的开发。Java 使用的指针模型不允许直接访问内存，因此内存不能被覆盖。
  * **安全性** ：Java 的认证基于公钥加密方法。Java 的指针模型保护对象中的私有数据，防止未经授权的应用程序访问数据结构。
  * **多线程** ：允许程序同时运行多个任务。可以提高程序的效率和响应速度。
  * **编译型和解释型** ：Java 源代码由 Java 编译器编译成 Java 虚拟机（JVM）可理解的指令，即字节码。然后，Java 虚拟机的解释器解释并执行字节码指令。
  * **架构中立** ：字节码指令是架构中立的，因为它们在 JVM 上运行，不特定于某个架构。只要安装了 JVM，同一个应用程序可以在所有平台上运行。
  * **可移植性** ：源代码在编译时生成一套字节码指令，可在任何平台和架构上运行，无需重新编译代码。

## Java 的发展过程
- Java 是一种相对年轻的语言
	- 自1995年以来一直在使用。
	- 最初是为消费类电子设备（电视、录像机、冰箱、洗衣机、移动电话）设计的。
	- 互联网和网络刚刚兴起，因此 Sun 将其转变为一种互联网编程语言。
	- 它允许你发布包含 Java 代码的网页。
- Java 拥有庞大的开发者基础
	- 存在大量来自 Sun 和其他来源的类库。

## Java 平台


- **平台是一个开发或部署环境**：平台指的是用于软件开发和部署的环境。它为开发者提供了一套工具、库和运行时支持，以便他们能够编写、测试和运行应用程序。
- **Java 平台可以在任何操作系统上运行**
  - 其他平台通常是硬件和供应商特定的：这意味着许多其他平台（如某些嵌入式系统或专有软件平台）可能仅限于特定类型的硬件或特定供应商的产品。而 Java 平台则不同，它设计成可以跨多种不同的操作系统和硬件架构工作，从而实现了“一次编写，到处运行”的理念。
- **Java 平台提供了：**
  - Java 虚拟机 (JVM)：JVM 是一个抽象的计算机，它执行以 Java 字节码形式编写的程序。字节码是一种中间语言，由 Java 编译器生成，并在 JVM 上解释或即时编译为机器代码执行。这使得 Java 程序能够在任何安装了适当 JVM 的平台上运行，而无需重新编译。
  - 应用编程接口 (API)：Java API 是一组预先定义的类和方法，它们提供了丰富的功能，使开发者能够更轻松地编写复杂的程序。这些 API 包括各种实用工具、数据结构、网络通信、图形界面等，涵盖了从基础到高级的各种编程需求。


图中展示了 Java 平台的层次结构：
![](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIDDmqNsjr6JBQkxHlvpM2Vf1T0gnqrAAJYF2sb5mpoVDqncfOCJQIrAQADAgADeAADPQQ.png)

1. **Host Platform**（宿主平台）：这是底层的操作系统和硬件环境，Java 平台在此基础上运行。
2. **Java Virtual Machine (JVM)**（Java 虚拟机）：JVM 在宿主平台上运行，负责解释或编译 Java 字节码并执行。
3. **Java API**（Java 应用编程接口）：这一层包含了 Java 提供的各种类库和方法，供开发者调用以实现所需的功能。
4. **Java Program**（Java 程序）：这是开发者编写的 Java 应用程序，它使用 Java API 并在 JVM 上运行。

通过这种分层设计，Java 实现了高度的可移植性和灵活性，使得开发者可以专注于编写应用程序逻辑，而不必担心底层硬件和操作系统的差异。

## Java 的执行模型 
The Java execution model
编译型语言的执行模型是将源代码编译成主机机器可理解的指令，主机机器执行这个二进制文件。而 Java 的执行模型是将源代码编译成 JVM 可理解的指令，即字节码，然后由 JVM 解释执行。
- 传统编译模型
源代码 → 编译器 → 机器码 → 操作系统执行
- Java执行模型
源代码 → Java编译器 → 字节码 → JVM解释执行
## Java 的用途

Java 可以用于构建程序和软件组件。

  * **程序** ：是可以在 Java 虚拟机上独立运行的实体。包括应用程序和小程序。
    * **应用程序** ：是一个独立的程序，可以访问系统资源，如文件等。它不需要在 Web 浏览器中运行，通过命令行或菜单选择明确调用。main（）方法是应用程序的入口点。
    * **小程序（Applet）** ：是嵌入在 Web 页面中的 Java 程序，几乎总是图形化的。出于安全考虑，对系统资源的访问有限制。代码在客户端的 Web 浏览器中执行。
  * **组件** ：是用于创建程序的构建块。包括 Servlet、JavaServer Pages（JSP）、JavaBeans 和 Enterprise JavaBeans（EJB）。
    * **Servlet** ：处理来自 Web 浏览器的请求并返回响应。在服务器上创建动态内容，运行在应用程序服务器中。
    * **JavaServer Page（JSP）** ：是嵌入了 Java 代码的 HTML 页面。在服务器上而不是在浏览器上创建动态内容，运行在应用程序服务器中。
    * **JavaBeans** ：是具有属性、方法和事件的 Java 代码，以便在开发人员之间促进重用。是一种可重用的软件组件，可以在构建工具中进行可视化操作。
    * **Enterprise JavaBeans（EJB）** ：是允许不同 JVM 中的 Java 对象之间相互通信的分布式对象。封装应用程序的业务逻辑和模型，在应用程序服务器中运行。

## Java 示例程序

  * **创建、编译和执行 Java 程序** ：这是 Java 编程的基础操作，通过编写代码、编译代码生成字节码、然后由 JVM 执行字节码的过程，来实现程序的运行。
![在这里插入图片描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIC7GqNsB6ilV7SmleZr2gQ7ZMgh2Q2AAI0F2sb5mpoVMWLnFI9uUp1AQADAgADeQADPQQ.png)


  * **（GUI）在消息对话框中显示文本** ：这是 Java 图形用户界面编程的一个简单示例，展示了如何使用 Java 的 GUI 库来创建用户界面元素，如对话框，并在其中显示文本。
![在这里插入图片描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIC7WqNsCDmn7N76yF2QIk9Bc-1fOrpAAI1F2sb5mpoVBL0y8w7lqOGAQADAgADeAADPQQ.png)
## 问答

###  1. Java 虚拟机（JVM）是什么，它有什么作用？
JVM 是 Java 虚拟机，它是一种抽象的计算设备。其主要作用是将 Java 编译后的字节码转换为特定计算机硬件和操作系统可以执行的机器码。JVM 为 Java 程序提供了一个独立于平台的运行环境，使得 Java 程序可以在不同的操作系统和硬件平台上运行，而无需重新编译。
###  2. 字节码是什么？
字节码是 Java 编译器将 Java 源代码编译后生成的一种中间代码。它是一种与平台无关的二进制代码，可以在任何安装了 JVM 的设备上运行。字节码是 Java 跨平台特性的关键，它使得 Java 程序可以在不同的操作系统和硬件平台上执行。
###  3. 程序和组件之间的区别是什么？
程序是一个完整的、可以独立运行的软件单元，如 Java 应用程序和小程序。而组件是程序的一部分，是用于构建程序的可重用单元，如 Servlet、JSP、JavaBeans 和 EJB。程序通常是为最终用户直接使用的软件，而组件则是开发者用来构建软件的构建块。

## 单元总结

在本模块中，你应已学会：
  * 描述 Java 编程语言的历史和发展过程。
  * 解释 Java 的执行模型，包括字节码和 Java 虚拟机的使用。
  * 概述可以使用 Java 构建的程序和组件的类型。


***

# 第 2 单元：Java 语法基础（一）

## 标识符 Identifiers

  * **定义** ：标识符是代表变量、方法、类或标签的文本字符串。Java 是大小写敏感的，`yourname`、`yourName`、`Yourname`、`YourName` 是四个不同的标识符。
  * **组成字符** ：可以是数字、字母、美元符号`$`或下划线`_`。
  * **限制** ：不能以数字开头；不能与保留字（reserved word）相同。
  * **命名约定** ：
    * **包** ：全小写，如 `theexample`。
    * **类** ：首字母大写，复合词每个单词的首字母大写，如 `TheExample`。
    * **方法 / 字段** ：首字母小写，复合词每个单词（除首个单词）的首字母大写，如 `theExample`。
    * **常量** ：全大写，如 `THE_EXAMPLE`。

### 保留标识符 Reserved Identifiers
- 字面量 Literals： `null` `true` `false`
**注：** 字面量是基本类型、字符串类型或null类型的值在源代码中的表示形式。

- 关键字 Keywords 共53个
![](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIC5mqNr-z8qP_Wo_fhdb50xruE4p1fAAItF2sb5mpoVOJvSTlFfZS_AQADAgADeQADPQQ.png)

- 保留字 Reserved Word：`const` `goto`

## Java 类型

  * **原始类型（PrimitiveType）** ：
    * **整数类型** ：用于表示有符号整数。
    * **浮点数类型** ：用于表示带小数部分的 “通用” 数字。
    * **字符类型** ：表示无符号 Unicode 字符。
    * **布尔类型** ：表示逻辑值，只有 true 和 false 两个值。
  * **引用类型（ReferenceType）** ：
    * **类或接口类型** ：代表类或接口。
    * **类型变量** ：用于泛型。
    * **数组类型** ：表示数组数据结构。

## 原始数据类型 Primitive Type

  * **整数** ：有符号整数，初始化为零。
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIC82qNsDAILNMlSLeRk2iRBm3fHTyrAAI7F2sb5mpoVCvbaJ5fHM-8AQADAgADeQADPQQ.png)
  * **浮点数** ：可以有小数部分的 “通用” 数字，初始化为零。
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIC9GqNsDLNBWSLunuwtZf9JZO74n3OAAI8F2sb5mpoVHzPXPdtO1b7AQADAgADeAADPQQ.png)
  * **字符** ：任何无符号 Unicode 字符都是 char 原始数据类型。字符是单引号内的单个 Unicode 字符，初始化为零 `'\0'`。
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIC9WqNsDRdulQ2slSSqGodV3QJEXYmAAI9F2sb5mpoVCwojJsG6affAQADAgADeAADPQQ.png)
  * **布尔类型** ：在 Java 中是独立的，int 值不能代替布尔值。布尔值可以存储 `true` 或 `false`，初始化为 `false`。
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIC9mqNsDhwoOMh1A51_E7rp-J7lMd8AAI-F2sb5mpoVIRuy8A7aIh_AQADAgADeAADPQQ.png)
## 字面量 Literals

  * **定义** ：字面量是值的源代码表示形式，包括原始类型、String 类型或 null 类型的值。
  * **整数字面量** ：默认为十进制；八进制数以零开头（032）；十六进制数以零和 x 开头（0x1A）；在直接量后跟 “L” 表示 long 类型（26L）。大小写字母等效。
  * **浮点数字面量** ：float 直接量以 f（或 F）结尾（7.1f）；double 直接量以 d（或 D）结尾（7.1D）；使用 e（或 E）表示科学计数法（7.1e2）；没有结尾字母的浮点数默认是 double 类型（7.1 等同于 7.1d）。大小写字母等效。
  * **转义序列 escape sequences** ：用于模拟某些按键或在字符串字面量中表示特殊字符。例如：
	- `\b`（退格 BS，Unicode `\u0008`）
	- `\t`（水平制表符 HT，Unicode `\u0009`）
	- `\n`（换行 LF，Unicode `\u000a`）
	- `\f`（换页 FF，Unicode `\u000c`）
	- `\r`（回车 CR，Unicode `\u000d`）
	- `\"`（双引号 "，Unicode `\u0022`）
	- `\'`（单引号 '，Unicode `\u0027`）
	- `\\`（反斜杠 \，Unicode `\u005c`）
	- 十六进制 Unicode 值也可以写成 `\uXXXX`
## 原始类型转换 Casting primitive types

  * **定义** ：Java 是严格类型语言，给变量分配错误类型的值可能导致编译错误或 JVM 异常。类型转换允许将值视为另一种类型。
  * **隐式转换与显式转换 Implicit & explicit casting** ：
    * **隐式转换** ：当不会丢失信息时自动完成，如从较窄类型到较宽类型。
```byte → short → int → long → float → double```
    * **显式转换** ：当存在潜在精度损失时需要明确转换。
```java
long p = (long) 12345.56;    // p == 12345
int g = p;                   // 即使int可以容纳12345，这也是非法的
char c = 't';
int j = c;                   // 自动提升
short k = c;                 // 为什么这是一个错误？
short k = (short) c;         // 显式转换
float f = 12.35;             // 这里有什么问题？
float f = 12.35f;			 
// 这里，12.35是一个double类型的字面量，默认情况下，浮点数字面量被视为double类型。
// 要将其赋给一个float类型的变量，需要显式转换或使用f后缀来指定其为float类型：
```
## 声明和初始化 Declarations and initialization

  * **变量声明** ：在使用变量之前必须声明。
  * **初始化** ：非数组的单值变量在首次用于表达式之前必须初始化。声明和初始化可以合并，使用 = 进行赋值（包括初始化）。
  * **数组** ：数组在使用前也必须声明。数组具有固定大小，可以通过字面量、表达式或隐式指定。可以可选地初始化数组。数组具有默认值，取决于其类型，且始终基于零（数组 [0] 是第一个元素）。


## 运算符和优先级 Operators and precedence

  * **定义** ：运算符是表达式的 “粘合剂”。运算符的优先级决定了运算的顺序，括号可以明确指定运算顺序，也可以按照默认的优先级进行运算。
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIC92qNsDrbwsti7bId6YE255W4zSZ3AAI_F2sb5mpoVNRg-0mR01cKAQADAgADeAADPQQ.png)

## 注释 Comments
Java 支持三种类型的注释，用于添加注释和说明代码。

```java
// 这一行的其余部分是一个注释
// 没有换行符

/* 从这里
到这里的
全部内容都是一个注释 */

/** 从这里
到这里的
全部内容都是一个Javadoc注释 */
```
## 语句 Statements

  * **定义** ：语句以分号终止。一行可以写多条语句，一条语句也可以分多行书写。
  * **条件语句** ：
    * **if-else 语句** ：条件表达式必须计算为布尔值。else 子句是可选的。对于单条语句，大括号不是必需的，但为了清晰起见强烈推荐使用。
    * **三元运算符** ：是 if-else 语句的快捷方式，格式为（布尔表达式 ? 真值选择 : 假值选择）。可导致代码更短，但要确保代码仍可读。
    * **switch 语句** ：测试单个变量的多个替代值并执行相应的 case。没有 break 的 case 将导致 “贯穿”，即执行下一个 case。default 子句处理未明确处理的值。
  * **循环语句** ：
    * **while 和 do…while 语句** ：只要条件保持为真，就执行语句或代码块。while() 执行零次或多次；do...while() 至少执行一次。
    * **for 语句** ：执行后面的语句或代码块。先评估 “开始表达式” 一次；只要 “测试表达式” 为真就继续执行；每次迭代后评估 “增量表达式”。可以在 for 语句中声明变量，通常用于声明 “计数器” 变量，通常在 “开始” 表达式中声明，其作用域仅限于循环。
  * **分支语句** ：
    * **break** ：可用于 switch 语句之外的其他语句。终止 for、while 或 do...while 循环。有两种形式：
    	* 带标签的 break，执行继续到标记循环后的下一条语句
    	* 不带标签的 break，执行继续到循环外的下一条语句。
    * **continue** ：类似于 break，但仅跳过当前循环迭代的剩余部分，然后继续评估内层循环的布尔表达式。也有带标签和不带标签的形式。
    * **return** ：退出当前方法。可以包含要返回的表达式，返回类型必须与方法的返回类型匹配。void 返回类型表示不能返回值。
![在这里插入图片描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIC72qNsCXy2H3xwxyVXKaBEmUdHX7qAAI3F2sb5mpoVDe3TdhgnyhmAQADAgADeAADPQQ.png)

带标签的`break`和`continue`语句并不限于使用"outer"作为标签。实际上，标签可以是任何符合Java标识符规则的名字：

```java
labelFirst:
for (int i = 0; i < 3; i++) {
    labelSecond:
    for (int j = 0; j < 3; j++) {
        if (i == 1 && j == 1) {
            break labelFirst; // 跳出名为labelFirst的循环
        }
        System.out.println("i = " + i + ", j = " + j);
        
        labelThird:
        for (int k = 0; k < 2; k++) {
            if (k == 1) {
                continue labelSecond; // 跳过名为labelSecond的循环的当前迭代
            }
            System.out.println("i = " + i + ", j = " + j + ", k = " + k);
        }
    }
}
```

## 作用域 Scope

  * **定义** ：变量的作用域是程序中可以引用该变量的区域。在方法中声明的变量只能在该方法中访问；在循环或代码块中声明的变量只能在该循环或代码块中访问。

## 单元总结

完成本单元后，你应能够：

  1. 概述 Java 程序中使用的命名约定。
  2. 构造有效的标识符。
  3. 描述 Java 原始数据类型，并解释每种类型如何使用及使用原因。
  4. 声明和初始化 Java 变量和数组。
  5. 识别保留字。

---

# 第 3 单元：Java 语法基础（二）
## 对象和消息 Objects and messages

  * **对象的复杂性** ：对象提供的行为比原始数据类型更复杂。
  * **对象响应消息** ：对象可以响应消息，消息通过点（.）运算符发送给对象。
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIC-GqNsDza6tzdOLNuzYc-54VI1nBPAAJAF2sb5mpoVC9uGB3oixU1AQADAgADeAADPQQ.png)

## 声明和初始化对象 Declaring and initializing objects

  * **声明的必要性** ：和原始类型及数组一样，对象在使用前必须声明。声明时需要指定对象的类型，即对象的类。
  * **赋值和初始化** ：使用 = 进行赋值（包括初始化）。初始化对象通常使用 new 运算符，如果你想创建一个新对象就用它。对象也可以初始化为 null。
  * **对象数组** ：对象数组的声明方式与原始类型数组相同。对象数组默认初始化为 null。

## 身份 Identity

  * **== 关系运算符** ：当用于对象时，测试的是对象的精确身份，即检查两个变量是否引用同一个对象。而当用于原始类型时，检查的是值是否相等。
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIC-WqNsD4cvyYnxh8MhBRNLWHKurRSAAJBF2sb5mpoVDXhLi8RoGGRAQADAgADeAADPQQ.png)

## 包装类 Wrapper classes

  * **原始类型的局限性** ：原始类型没有关联的方法，没有与原始数据类型相关联的行为。
  * **包装类的概念** ：每个原始数据类型都有一个对应的包装类。每个包装对象仅存储一个原始变量，并提供处理它的方法。包装类是 Java 基础 API 的一部分。
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIC-mqNsEBsbyMQbmJ5p6Cb763XrlECAAJCF2sb5mpoVGopH9E3UhTcAQADAgADeAADPQQ.png)

## 字符串 Strings

  * **字符串的本质** ：字符串类型（String）是一个类，而不是原始数据类型。字符串字面量是由双引号括起来的任意数量的字符。
  * **字符串的初始化** ：字符串对象可以通过其他方式初始化，例如使用 new 运算符创建字符串对象，或者直接赋值字符串字面量。
```java
String a = "A String";
String b = "";
String c = new String();
String d = new String("Another String");
String e = String.valueOf(1.23);
String f = null;
```
## 拼接字符串 Concatenating strings

  * **+ 运算符的使用** ：+ 运算符可以拼接字符串，例如 `String a = "This" + " is a " + "String";`。
  * **拼接的效率问题** ：拼接字符串有更高效的方法，这将在后面讨论。当原始类型用于 println 方法调用时，会自动转换为字符串。
  * **示例** ：
`System.out.println("answer = " + 1 + 2 + 3); `和 `System.out.println("answer = " + (1+2+3));` 这两个示例的输出是否相同？

**示例解答**：
在Java中，当你在`System.out.println()`方法中使用原始类型（如整数、浮点数等）时，这些原始类型会被自动转换为字符串，以便能够与字符串进行连接并输出。

```java
System.out.println("answer = " + 1 + 2 + 3);
```

在这条语句中，`1`、`2`和`3`都是整数类型的原始值。由于它们出现在字符串连接表达式中，因此会被自动转换为字符串。具体来说，`1`被转换为字符串"1"，`2`被转换为字符串"2"，`3`被转换为字符串"3"。然后，这些字符串按照顺序进行连接，最终输出的结果是"answer = 123"。

然而，如果你希望先进行数值计算再进行字符串连接，可以使用括号来改变运算的优先级：

```java
System.out.println("answer = " + (1+2+3));
```

在这条语句中，`(1+2+3)`首先进行数值计算，结果为`6`。然后，这个数值结果被转换为字符串"6"，并与前面的字符串"answer = "进行连接，最终输出的结果是"answer = 6"。

因此，上述两个示例不会产生相同的输出。第一个示例输出 `answer = 123` ，而第二个示例输出 `answer = 6` 。

## 字符串消息 String messages

  * **字符串作为对象** ：字符串是对象，可以响应消息。使用点（.）运算符发送消息。
  * **字符串方法** ：字符串是一个类，具有方法（将在后面详细讨论）。
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIC-2qNsENUH83Hte4H7C_2Ua2r3-_tAAJDF2sb5mpoVDtJd9FqYy9kAQADAgADeAADPQQ.png)

## 比较字符串 Comparing strings

  * **比较的方法** ：可以向字符串发送多个消息以测试与另一个字符串是否等价。
  * **`equals()` 方法** ：用于测试等价性，返回 true 或 false。
  * **`equalsIgnoreCase()` 方法** ：用于不区分大小写的等价性测试，返回 true 或 false。
  * **`==` 的问题** ：使用 == 比较字符串时会存在问题，因为**它比较的是对象的引用，而不是内容**。
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIC_GqNsEXLYuzrIsUJPS_erW3IAtVnAAJEF2sb5mpoVFtof8b0ufXSAQADAgADeAADPQQ.png)

## 字符串缓冲区 StringBuffer

  * **字符串缓冲区的优势** ：字符串缓冲区类（StringBuffer）提供了更高效的字符串构建机制。字符串拼接可能会非常耗费资源，而大多数编译器会将字符串拼接转换为字符串缓冲区的实现。如果构建的是简单字符串，可以直接拼接；如果通过循环构建字符串，则使用`StringBuffer`。

```java
StringBuffer buffer = new StringBuffer(15);// 创建一个StringBuffer对象，初始容量为15
buffer.append("This is ");// 向buffer中追加字符串"This is "
buffer.append("String");// 向buffer中追加字符串"String"
buffer.insert(7, " a");// 在第7个位置(前)插入字符串" a", 将原先第七个位置及之后的内容向后移
buffer.append('.');// 向buffer末尾追加句号'.'
System.out.println(buffer.length());// 打印buffer的当前长度（字符数）输出17
System.out.println(buffer.capacity());// 打印buffer的当前容量 输出32
String output = buffer.toString();// 将buffer转换为普通String对象
System.out.println(output);// 打印最终的字符串内容 输出: "This is a String."
```

## 单元总结

在本单元中，你应已学会：

  1. 创建和初始化对象。
  2. 使用身份（==）运算符。
  3. 识别和使用原始包装类。
  4. 概述 Java 对字符串的实现，并操作字符串。
  5. 解释字符串类（String）和字符串缓冲区类（StringBuffer）之间的区别。

---

# 第 4 单元：面向对象概念

## 对象和类 Object and Class

### 对象的概念 Object

  * **对象的定义** ：对象是应用程序领域中一个有意义的事物，它可以是一个物理实体或一个概念。
    * **物理实体** ：例如一台电视、一部电话等。
    * **概念** ：如化学过程等。

  * **对象的特性 Properties of an object** 
    * **身份（Identity）** ：每个对象必须有一个名称，以便与其他对象区分开来。在程序中使用 “标识符” 来实现这一目标。
    * **状态（State）** ：状态是对象在某一时刻的所有属性值的集合。例如，学生的学号、姓名、年龄、成绩等属性构成了学生对象的状态；电视的颜色、音量、亮度、频道等属性构成了电视对象的状态。
    * **行为（Behavior）** ：行为由一系列操作组成，每个操作决定了对象的一种行为。在程序中使用 “函数” 来实现这一功能。

### 对象数据的封装 Encapsulation of object data
- **对象封装的思想是保护对象的内部信息。**
  - 这意味着对象的内部细节（如属性和实现逻辑）被隐藏起来，外部无法直接访问或修改这些内部信息。
  
- **人们只能通过对象接口上允许的操作来对对象进行操作，并改变对象的状态。**
  - 对象提供了一组公共方法（接口），用户必须通过这些方法与对象交互。例如，如果要改变对象的某个属性，必须调用相应的设置方法，而不能直接访问和修改该属性。
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIC_WqNsEcaAjI2R6Biq-e5GglnFRRSAAJFF2sb5mpoVIFx5oAlt8TNAQADAgADeAADPQQ.png)


**图片示例解释：**

图片中展示了一个电视机的例子，用来形象地说明对象封装的概念：

- **电视机作为一个对象**：
  - 内部包含多个属性，如颜色（color）、亮度（brightness）、音量（volume）、频道（channel）和系统（system）等。
  - 这些属性代表了电视机的内部状态。

- **电视机提供的操作接口**：
  - 调整音量（adjustVolume）
  - 调整颜色（adjustColor）
  - 调整亮度（adjustBrightness）
  - 调整频道（adjustChannel）
  - 调整系统（adjustSystem）

这些操作接口就像是电视机上的按钮，用户可以通过按这些按钮来间接地改变电视机的内部状态，但用户无法直接访问和修改电视机内部的具体实现细节。

例如，用户可以按“调整音量”按钮来改变电视机的音量，但用户并不需要知道电视机内部是如何具体实现音量调节的。

### 对象的交互 Interaction of objects

  * **交互的必要性** ：完全隔离的对象是没有用的，系统运行时对象之间应该存在交互。
  * **消息传递** ：对象之间的交互通过消息传递来实现。消息是发送对象向接收对象发送的请求信息，用于调用接收对象的某个行为，必要时包含适当的参数信息。
  * **消息的组成**
    * **接收对象的身份** ：明确要向哪个对象发送消息。
    * **被调用的操作（函数、行为）的名称** ：指定让接收对象执行哪个操作。
    * **参数** ：为操作提供必要的数据。
  * **消息的特性**
    * **同一对象接收不同形式的消息** ：同一对象可以接收多种不同形式的消息，并做出不同的响应。例如，`TV11 adjustChannel down` `TV11 adjustVolume louder` `TV11 adjustColor intense` 。
    * **相同形式的消息发送给不同对象** ：相同形式的消息可以发送给不同的对象，它们做出的响应可能不同。例如，`TV11 adjustChannel up`（从 15 切换到 16）和 `TV12 adjustChannel up`（从 5 切换到 6）。
    * **消息发送无需考虑具体接收者** ：发送消息时无需考虑具体的接收对象，接收对象可以选择响应或不响应消息。甚至可以实现消息的多播。

### 类的概念 Class

  * **类的定义** ：类是一组具有相同数据组成和相同行为的对象的集合。例如，电视类包含了一组具有相同属性（如颜色、音量、系统、频道、亮度等）和相同行为（如调整颜色、调整音量、调整系统、调整频道、调整亮度、开关机等）的电视对象。
  * **类与对象之间的关系**
    * **实例化** ：每个对象都是某个类的一个实例。在任何给定时刻，每个类可以有零个或多个实例（对象）。
    * **静态与动态** ：**类是静态的**，它们的存在、语义和关系在执行之前就已经定义好了；**对象是动态的**，可以在程序执行过程中创建和删除。

### 抽象与封装 Abstraction and Encapsulation

  * **数据抽象** ：对象是现实世界中一个实体的抽象，是一种简化的描述，强调与给定应用程序相关的特征，忽略不相关的特征。类是一组对象的抽象。
  * **封装** ：类分为接口和实现两部分，对于用户来说，接口是可见的，而实现是不可见的。只有类提供的操作才能修改属性值，隐藏类的实现细节称为封装。
  * **封装的优点**
    * **两种保护** ：一方面保护对象不被用户误用，用户没有权利访问实现细节，如属性值和操作过程；另一方面，当对象的实现发生变化时，保护客户端代码不受影响，避免了因对象实现变更而引起的客户端代码修改，减少了 “涟漪效应”。
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIC_mqNsEk1GhKq1qkyatUb7k6FJVNVAAJGF2sb5mpoVBnETyQ_5cIIAQADAgADeAADPQQ.png)

### 一个实例
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIC_2qNsExTOGyAQ_7cCa4Jc5SORSTlAAJHF2sb5mpoVHfCYzIUJu_BAQADAgADeQADPQQ.png)

## 继承 Inheritance
### 超类与子类
超类其实就是父类

  * **继承的定义** ：继承是类的重要特性之一，用于实现可复用性和可扩展性。一个类可以定义为另一个更通用类的特例，更通用的类是超类，特例类是子类。
  * **继承关系** ：子类继承超类的所有属性和操作，也可以定义自己的独特属性和操作。例如，电子类是一个超类，电视类、电话类、计算机类都是电子类的子类。计算机类继承了电子类的属性（如制造商、型号、价格、颜色）和操作（如获取型号），同时还可以定义自己的独特属性（如显示器类型、内存大小）和操作（如获取显示器类型）。
  * **“is a” 关系** ：继承关系是一种 “is a” 关系，具有传递性。例如，“电视” “是” 电子产品；正方形类继承自矩形类，矩形类和三角形类都继承自多边形类，那么正方形类也间接继承自多边形类，正方形对象 “是” 多边形对象。
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIDAAFqjbBOdIDkxFGAvJHikHUGsLtV7AACSBdrG-ZqaFQkxUlhaR_4zwEAAwIAA3gAAz0E.png)
### 继承的优点
1. **增加软件重用的机会**：通过设计可重用的类和组件，可以在不同的项目或模块中重复使用这些代码，从而减少开发和维护的成本。
2. **开发更接近现实的模型**：面向对象编程允许开发者创建更贴近现实世界的模型，使得程序更容易理解和维护。
3. **使系统更加灵活**：
   - **继承机制**：子类可以自动继承父类的属性和方法，并且可以根据需要进行扩展或修改，这使得系统能够更好地适应变化。
   - **应对需求变化**：当需求发生变化时，可以通过添加新的子类来满足新的需求，而不需要对现有的代码进行大规模的改动。
4. **确保类之间的一致性**：
   - **父类定制规则**：父类可以定义一些通用的行为和属性，子类在继承这些规则的基础上进行特定的实现，保证了类之间的行为一致性。
   - **继承接口和实现**：子类不仅继承了父类的接口（即方法签名），还继承了具体的实现细节，这有助于保持系统的统一性和规范性。
   - **支持多态性**：多态性允许不同类型的对象以相同的方式被处理，提高了代码的灵活性和可扩展性。例如，可以通过一个统一的接口来操作不同类型的对象，而不需要关心它们的具体类型。
## 单元目标

完成本单元后，你应能够：

  1. **理解对象** ：了解对象的定义、特性及与其他对象的交互方式。
  2. **掌握类的概念** ：清楚类的定义、类与对象之间的关系。
  3. **理解继承** ：区分单继承与多继承，并能解释其应用场景。
  4. **掌握多态** ：了解多态的概念及在面向对象编程中的重要性。

---



# 第 5 单元：构建类

## 类的定义与作用

  * **类的定义** ：类是具有相同属性和行为的对象的集合，是创建对象的模板或蓝图。
  * **类的作用** ：通过类可以创建具有相同结构和行为的对象（实例），实现代码的复用和抽象。

## 类的成员

  * **字段（属性）** ：用于存储对象的状态信息。每个对象都有自己的字段副本。例如，一个 “学生” 类中的 “学号”“姓名” 字段。
  * **方法** ：定义对象能进行的操作。比如 “学生” 类中的 “学习”“考试” 方法。

## 类的分类

  * **互不相关类** ：彼此之间没有继承或接口关联的类。
  * **通过继承相关联的类** ：存在超类和子类的关系。子类继承超类的属性和方法，实现代码复用。
  * **通过接口相关联的类** ：类实现接口，遵循接口定义的方法规范。

## 类的实现
### 类的声明与修饰符Class declaration and modifiers

  * **声明格式** ：`[修饰符] class 类名 [extends 超类名] [implements 接口名列表] { ... }`
  * **修饰符** Class modifiers ：
    * **public** ：公共类，可在包含包以外被访问。一个 `.java` 文件只能有一个公共类，文件名需与公共类名相同。
    * **abstract** ：抽象类，不能实例化，需被子类继承。抽象类可以包含抽象方法（无实现的方法）和具体方法。
    * **final** ：最终类，不能被继承。

### 构造函数 Constructors

  * **定义** ：用于创建和初始化对象。
  * **特点** ：构造函数的**名称与类名相同**，没有返回类型。
  * **使用** ：使用 `new` 关键字调用构造函数创建对象。例如：`Student s = new Student();`。
  * **重载** ：允许定义多个具有不同参数列表的构造函数，以满足不同初始化需求。
  * **链式调用** ：通过 `this()` 调用同一类中的其他构造函数，通过 `super()` 调用父类构造函数。注意，`this()` 和 `super()` 不能同时出现在一个构造函数中，编译器为所有构造函数提供了一个隐式的 `super()`构造函数。

![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIDAWqNsFFsJTKhH81Q-WFRcrC6Z_73AAJJF2sb5mpoVNDAp37Q_l5IAQADAgADeAADPQQ.png)

关于默认构造函数：
- 没有参数的构造函数是默认构造函数。
- 只有当你没有显式定义任何构造函数时，Java 平台才会提供默认构造函数。
- 当定义构造函数时，你也应该提供默认构造函数。
### 字段 Fields
定义在类中，用于存储对象的数据。可以在声明时初始化，若未初始化则有默认值（如数字类型默认为 0，布尔类型默认为 false 等）。

![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIDD2qNslv_kB8gYd7q-rcgLNSVCS5hAAJZF2sb5mpoVEen9BsE8clzAQADAgADeQADPQQ.png)

### 消息 Messages

使用消息来调用对象的行为
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIDEGqNsl2UCQkhDVvwXSld1rMbxwm0AAJaF2sb5mpoVH-WiLFgNXgBAQADAgADeAADPQQ.png)
### 方法 Methods 
方法定义对象如何响应消息。定义对象的行为。
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIDEWqNsl_L4cXesaDOGa-q_GUj6TleAAJbF2sb5mpoVDEMBDqsEo4VAQADAgADeQADPQQ.png)
#### 方法签名 Method signatures
方法签名由方法名和参数列表组成。一个类可以有多个名称相同的方法，但是每个方法必须具有不同的签名，则可以有相同的名称但参数列表不同的方法重载。
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIDAmqNsF9kvLTXNPFhDlpNqdyXPRCeAAJKF2sb5mpoVAABj7sXPxm1DwEAAwIAA3gAAz0E.png)
#### 方法参数 Method parameters

参数传递方式如下：
- 对于原始数据类型，**按值传递**。不会被修改。
- 对于引用类型，**按对象引用来传递**。会被修改。
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIDA2qNsGG1s-Oq95e7toGxyDMNWNvWAAJLF2sb5mpoVD3P-w9dE4hvAQADAgADeQADPQQ.png)

图中样例，传递的参数为原始数据类型int，a的值不会被修改。

#### 方法重载 Overloading methods
只要具有不同的签名，就可以为许多不同的方法使用相同的名称，这被称为重载。
例如 `System.out.println()` 方法有 10 个不同的参数声明：
boolean、char[]、char、double、float、int、long、Object、String 以及一个没有参数的。
你不需要为可能想要打印的每种数据类型使用不同的方法名（例如 “printString” 或 “printDouble”）。

#### 方法重写 Overriding methods
如果子类中的方法具有与父类中方法相同的签名和返回类型，则该方法重写父类中的方法。
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIDBGqNsGNcPll35qGk0X6aHdlEE6HDAAJMF2sb5mpoVH5nQaUbNe5YAQADAgADeQADPQQ.png)

#### main()方法
如果没有至少一个类具有 main（）方法，应用程序将无法运行。JVM 加载一个类并通过调用 main（String[] args）方法开始执行。
- public：该方法可以被任何对象调用。
- static：不需要先创建对象。
- void：该方法不会返回任何内容。
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIDBWqNsGXLBglzdgugtsdErij9rPc1AAJNF2sb5mpoVKk_9VBOr9YHAQADAgADeAADPQQ.png)


---
<h3> <a href="https://blog.csdn.net/Genevieve_xiao/article/details/147746114#HideButNotOverride">关于理解子类的静态方法只能隐藏父类的同名静态方法而非重写</a></h3>

---
<h3> <a href="https://blog.csdn.net/Genevieve_xiao/article/details/147746114#Override&Overload">关于方法重载和方法重写的区别</a></h3>

---

## 类的特殊成员
### 静态成员 Static members

  * 静态字段和方法属于类本身，而不是某个对象。
  * **访问方式** ：通过类名直接访问，所有对象共享同一份静态成员。在该类的一个对象中更改值将改变所有对象的值。
  * 静态成员
	- 静态变量（类变量）：所有实例共享同一份内存，存储在方法区（Method Area）。
	- 静态方法：属于类的方法，无需实例即可调用。不能访问实例变量/方法（无 this 上下文）。子类定义的同名静态方法会隐藏（Hide）父类方法而非重写（Override）。
	- 静态代码块：在类加载时执行一次，用于初始化静态资源。
	- 静态内部类：不依赖外部类实例的嵌套类。
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIDBmqNsGdWnfkR9gZQ87U7ECg2c-3lAAJOF2sb5mpoVLjW6JBqq6y3AQADAgADeAADPQQ.png)

### final 成员 Final members

  * **final 字段** ：final 字段是常量，一旦初始化后不能改变。通常声明为 `static final` 以方便访问，常量名习惯用大写字母。
  * **final 方法** ：final 方法不能被子类重写，确保方法的实现不会被改变。
  * **final 类** ：final 类不能被继承，确保类的完整性和安全性。
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIDB2qNsGhJx1ZUi7JW_s5MQKC6ZhRFAAJPF2sb5mpoVPJqstPOrEBDAQADAgADeAADPQQ.png)
### 抽象类 Abstract classes
提供通用的模板，包含抽象方法和具体方法，其中抽象方法没有实现。抽象类不能实例化，它们旨在作为其他类的超类。
如果一个类有一个或多个抽象方法，则该类是抽象的，必须声明为抽象类，且子类必须实现抽象方法。具有完整实现的类可以被实例化，称为具体类。

![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIDCGqNsGqYXjTdXpGrBIYdAAGNjETjUwACUBdrG-ZqaFTxOqd7HCBNsAEAAwIAA3gAAz0E.png)

## 包 Packages
### 包的作用和基本介绍
  * **组织类** ：包用于组织类，将相关的类归类到一起，提高代码的可维护性和可读性。
  * **命名空间** ：包名通常使用小写字母，不同包中可以有同名类。
  * **导入类** ：使用 `import` 语句可以引入其他包中的类，方便代码编写。

### 类的可见性 Class visibility
类的全名： 

![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIDCWqNsGxDoqCZvPblAAEHxsf2OpzLsQACURdrG-ZqaFR1Q1rIJDEW5wEAAwIAA3gAAz0E.png)

类可以通过类名仅引用同一包中的其他类。
引用不同包中定义的类时，必须提供类的完全限定名。
![描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIDCmqNsG5IFkS6KO-rfAnQsQzvn96ZAAJSF2sb5mpoVO8zd9J4Co3aAQADAgADeAADPQQ.png)
### 导入语句 Import statement
使用导入语句导入包或类，使其他类直接对你的类可见。可以避免引用不同包的类要写全称的麻烦。
![在这里插入图片描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIC8GqNsChYGLOuZ0_eZcdtA-yod3IyAAI4F2sb5mpoVBpI-nzoYhHSAQADAgADeAADPQQ.png)

### 核心java包
![在这里插入图片描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIC8WqNsCvO71DOPI8PI2S7z0f4rEXkAAI5F2sb5mpoVK6TyvXox3D2AQADAgADeQADPQQ.png)




---
# 第 6 单元：继承 Inheritance

## 类的继承与层次结构

  * **定义** ：每个对象属于一个类，除 `Object` 类外，每个类都有超类。在 Java 中，`Object` 是整个类层次结构的根。
  * **作用** ：开发时需决定哪个类作为新类的超类。



## 继承关系
-   * **子类** ：是对超类的专门化，通过添加字段、扩展或更改方法来专门化状态和行为。
  	* **超类** ：是子类的概括化，将通用状态和行为移到超类，供所有子类使用，实现代码的集中编写和维护。

- 	
	- 继承描述了子类实例是超类特殊情况的关系，称为 **“is-a”** 关系。例如，浮点数是数，数是对象。
	- 继承不能描述 **“has-a”**（具有）关系，这通常通过类的字段和相关方法实现（比如通过在类中声明其他类类型的成员变量），如浮点数具有符号、基数和尾数。

 * **子类继承超类的字段和方法** ：子类继承超类的所有字段和方法，这些字段和方法可能来自更高级别的超类。
 * **对象的方法理解能力** ：对象会理解其类实现的方法或超类继承 / 实现的方法。

- **单继承**：在 Java 中，一个类只能继承一个直接父类。这种机制被称为单继承（Single Inheritance）。Java 不允许一个类同时继承多个类，主要是为了避免复杂性和歧义性，尤其是所谓的 "菱形问题（Diamond Problem）"。
## 访问修饰符 Access modifiers

  * **private** ：成员仅限于声明它的类访问。
  * **默认（无修饰符）** ：成员仅限于声明它的包访问。
  * **protected** ：成员可被其声明的包和所有子类访问。（注意 子类实例可以访问其从父类继承而来的protected方法，而不能访问父类实例的protected方法）
  * **public** ：成员可被所有包中的类访问。

## 方法重写 Overriding methods

  * **定义** ：在子类中通过创建与超类同签名的方法来扩展或更改超类行为。
  * **机制** ：Java 使用子类的新方法替代继承的方法，新方法替换或细化超类中同名方法。
 * **限制** ：
	  * **参数列表必须与继承的方法完全匹配** 。
	  * **返回类型必须与继承的方法相同** 。
	  * **访问修饰符不能比继承的方法更严格** 。例如，重写 protected 方法时，新方法可以是 protected 或 public，但不能是 private。
![](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIDEmqNsnZBkAMZhTI4O4a3i-wlZ2J0AAJcF2sb5mpoVGlBmG1FUzxMAQADAgADeAADPQQ.png)


## 方法查找

  * **编译器查找方法的实现** ：从对象的类定义开始，若未找到则在超类中继续查找，直到找到并调用该方法。
  * **错误处理** ：若方法在层次结构中的所有类中均未实现，编译时会报错。

## 静态方法的继承
- 子类可以像调用自身方法一样调用超类的静态方法
- 子类的静态方法可以隐藏超类的静态方法。
![](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIDE2qNsnkrjggIc7-OAnvPLHqV-fUoAAJdF2sb5mpoVAXEopo5vH4dAQADAgADeAADPQQ.png)

## 构造函数的继承
- 只能调用正在实例化的类及其直接父类中的构造函数。
	- 在创建对象时，只有当前类和其直接父类的构造函数可以被调用。
- 构造函数可以通过 `super` 关键字和参数列表调用其父类中的另一个构造函数。
	- 参数列表必须与父类中某个现有构造函数的参数列表相匹配。
- 同一个类中的构造函数通过 `this` 关键字和参数列表进行调用。
- 构造函数的第一行可以是以下之一：
	- `super(...);`
	- `this(...);`
### 对象构建中的超类

  * **超类对象先于子类构建** ：编译器为所有构造函数提供隐式的 super() 调用，super(...) 初始化超类成员。
  * 若构造函数首行未调用其他构造函数，则自动调用 super()，若超类无零参数构造函数则会出错。

### 默认构造函数

  * **未提供构造函数时** ：系统提供默认零参数构造函数，它仅调用 super()。
  * **提供构造函数后** ：Java **不再提供**默认零参数构造函数，可自行编写零参数构造函数。

### 关于 `this` 和 `super` 的更多内容

- **`this` 和 `super` 可以在 Java 中的实例方法和构造函数中使用**
  - 它们不能在类（静态）方法中使用。
- **`this` 和 `super` 影响方法查找**
  - `this`：方法查找从当前类开始。
  - `super`：方法查找从直接父类开始。
- **关键字 `super` 让你可以在当前类中重写一个方法时使用父类中的代码**
  - 当子类重写父类的一个方法时，对该方法的调用将转到覆盖父类方法的代码。
  - 使用 `super` 可以让你从直接父类开始查找方法。

---
## 多态 Polymorphism

  * **定义** ：不同类的对象可接收相同消息，但表现出不同的行为。

紧凑型汽车、豪华汽车和跑车是几种接受相同消息集并提供相同服务的汽车类。每辆汽车都接受 `accelerate()`（加速）、`decelerate()`（减速）、`steer()`（转向）和 `calculateMilesToEmpty()`（计算剩余里程）等消息，使您能够驾驶到目的地。每种汽车可能以不同的方式实现这些服务，但这些类可以互换使用而不影响发送消息给车辆的驾驶员。

这一原则被称为**多态性**。

## 实现多态：通过一个具体实例
- **一个变量可以被赋值为其声明类型的对象，或者其声明类型的子类型对象。**
  - 例如：
    - `Car auto = new Car();`
    - `Car auto = new CompactCar();`
    - `Car auto = new LuxuryCar();`
    - `Car auto = new SportsCar();`

- **将一种类型的对象赋值给另一种类型（在层次结构中更高）的对象，会使该对象忘记其真实类型。**
  - 从上面的例子来看，`auto` 将不再知道它是一个 `CompactCar` 类的对象，并且只会响应 `Car` 类的消息。
  - 你可以通过将对象转换为该类型来让这些对象记住它们的真实类型，例如：
    - `CompactCar cc = (CompactCar)auto;`
  - 转换为一个未识别的子类将会抛出一个 `ClassCastException`。

代码样例
```java
// Driver.java
public class Driver {
    private String name;  // 驾驶员姓名
    private int age;      // 驱动年龄
    private Car auto;     // 当前驾驶的汽车（父类引用）

    // 构造函数：初始化驾驶员的名字和年龄
    public Driver(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // 设置当前驾驶的汽车，可以是任何 Car 类型或其子类对象
    public void setCar(Car auto) {
        this.auto = auto;
    }

    // 模拟驾驶行为的方法
    public void drive() {
        auto.accelerate();  // 加速

        // 假设遇到红灯
        if (stopLight.equals("red")) {
            auto.decelerate();  // 减速
            auto.accelerate();  // 再次加速
        }

        // 假设有转弯
        if (corner == true) {
            auto.steer();  // 转向
        }
    }
}
```
由于**变量在声明为父类类型后会忘记其真实类型**，它们只会响应 Car 类型中的消息。
它们可以响应相同的消息，并且可以互换使用而不影响消息发送者。
```java
// TestDriver.java
public class TestDriver {
    public static void main(String[] args) {
        // 创建一个驾驶员对象
        Driver driver = new Driver("zhangsan", 25);

        // 创建一个包含不同类型汽车的数组（多态体现）
        Car[] autos = {new SportsCar(), new CompactCar(), new LuxuryCar()};

        // 遍历每辆车，设置为当前驾驶的车，并调用驾驶方法
        for (Car car : autos) {
            driver.setCar(car);   // 多态赋值：父类引用指向子类对象
            driver.drive();       // 根据实际对象执行相应的方法
        }
    }
}
```
***
<h2> <a href="https://blog.csdn.net/Genevieve_xiao/article/details/147746114#ForgetItsRealClass"> 关于理解变量在声明为父类类型后会忘记其真实类型</a></h2>


***
## 问答
### 1. "is-a" 和 "has-a" 关系及其与类层次结构的关联？

  * **"is-a" 关系** ：是继承关系的典型特征，**表示某个类是另一个类的子类**，即子类是超类的一种特殊情况。例如，"FloatingPointNumber is-a Number"（浮点数是数的一种），"Number is-a Object"（数是对象的一种）。在类层次结构中，这种关系构成了从超类到子类的层级继承体系，子类继承超类的属性和方法，实现代码的复用和扩展。
  * **"has-a" 关系** ：**表示一个类拥有或包含另一个类的实例作为其属性**，即类之间的一种关联关系，而不是继承关系。例如，"FloatingPointNumber has-a sign, a radix and a mantissa"（浮点数有一个符号、一个基数和一个尾数）。在类层次结构中，这种关系通常通过类的字段来体现，一个类可以通过其字段来引用其他类的对象，以实现对不同类对象的组合和利用，从而构建更复杂的数据结构和功能模块。

以下是具体代码示例 仅供理解：

- "is-a" 关系实例

```java
// Number 类作为父类
class Number {
    public void display() {
        // 显示数字信息
    }
}

// FloatingPointNumber 类继承自 Number 类，体现 "is-a" 关系
class FloatingPointNumber extends Number {
    private double value;

    public FloatingPointNumber(double value) {
        this.value = value;
    }

    @Override
    public void display() {
        // 显示浮点数信息
    }
}
```

- "has-a" 关系实例

```java
// FloatingPointNumber 类除了继承自 Number 外，还包含 sign, radix 和 mantissa 属性，体现 "has-a" 关系
class FloatingPointNumber extends Number {
    private boolean sign;   // 符号
    private int radix;      // 基数
    private double mantissa; // 尾数

    public FloatingPointNumber(boolean sign, int radix, double mantissa) {
        this.sign = sign;
        this.radix = radix;
        this.mantissa = mantissa;
    }

    public void displayDetails() {
        // 显示符号、基数和尾数的信息
    }
}
```

- 结合 "is-a" 和 "has-a" 的完整实例

```java
// Number 类保持不变
class Number {
    public void display() {
        // 显示数字信息
    }
}

// FloatingPointNumber 类同时展示了 "is-a" 和 "has-a" 关系
class FloatingPointNumber extends Number {
    private boolean sign;   // 符号
    private int radix;      // 基数
    private double mantissa; // 尾数
    private double value;    // 实际数值

    public FloatingPointNumber(boolean sign, int radix, double mantissa, double value) {
        this.sign = sign;
        this.radix = radix;
        this.mantissa = mantissa;
        this.value = value;
    }

    @Override
    public void display() {
        // 显示浮点数信息
    }

    public void displayDetails() {
        // 显示符号、基数、尾数和实际值的信息
    }
}
```

`FloatingPointNumber` 类通过继承 `Number` 类体现了 **"is-a"** 关系，并且通过包含额外的属性（如符号、基数和尾数）来展示 **"has-a**" 关系。

### 2. Java 的四个访问修饰符是什么？他们对类成员范围的限制是什么？
  * **private** ：**私有访问修饰符。被 private 修饰的类成员只能在其被声明的类内部访问，其他类（包括子类）都无法直接访问。**
例如，如果在类 A 中声明了 private int x; 那么只有类 A 中的方法可以访问 x，其他类的方法都无法直接访问 x，这种限制确保了类的内部数据封装和隐藏，提高了类的安全性和可维护性。
  * **默认（无修饰符）** ：**包级访问修饰符。被默认修饰符修饰的类成员只能在同一个包内的类中访问，不同包中的类无法访问。**
例如，在包 com.example 中的类 A 声明了 int x; 那么只有 com.example 包中的其他类可以访问 x，其他包中的类则无法访问 x。这种限制有助于将相关的类组织在一起，形成一个相对独立的包级作用域，便于代码的模块化管理和维护。
  * **protected** ：**受保护访问修饰符。被 protected 修饰的类成员可以被其声明的类所在的包中的所有类访问，以及该类的所有子类访问，无论子类位于哪个包中。**
例如，在类 A 中声明了 protected void setName() { ... }，那么 com.example 包中的其他类以及类 A 的所有子类（无论子类在哪个包中）都可以访问 setName() 方法。这种修饰符在继承体系中非常有用，它允许子类访问超类中的一些受保护的成员，从而实现一定程度的代码复用和扩展，同时又限制了其他非相关类的访问，保护了类的内部实现细节。
  * **public** ：**公共访问修饰符。被 public 修饰的类成员可以被所有类访问，无论这些类位于哪个包中。**
例如，在类 A 中声明了 public String getName() { ... }，那么任何包中的类都可以调用 getName() 方法来获取对象的名称。public 修饰符提供了最大的访问权限，使得类的成员可以被广泛地使用和调用，是实现类之间交互和功能集成的重要手段，但同时也需要谨慎使用，以避免过度暴露类的内部实现细节，影响类的稳定性和可维护性。

### 3. 以下这段示例代码有什么问题？

```java
public class MyClass extends MySuper {
    MyClass() {
        super();
    }
    MyClass(int i) {
        super();
        this();
    }
}
```

-  **无参构造函数**：
   ```java
   MyClass() {
       super();
   }
   ```
   这个构造函数正确地调用了父类 `MySuper` 的无参构造函数 `super()`。这是正确的用法，因为每个子类构造函数必须首先调用父类的构造函数（显式或隐式）。

-  **带参构造函数**：
   ```java
   MyClass(int i) {
       super();
       this();
   }
   ```
   这个构造函数存在以下问题：
   - **构造函数链式调用的错误**：在一个构造函数中，`super()` 和 `this()` 是互斥的。它们不能同时出现在同一个构造函数中。构造函数的第一行只能是 `super()` 或 `this()`，不能两者都使用。
   - **`this()` 的调用位置错误**：即使 `super()` 没有被显式调用，编译器也会自动插入一个隐式的 `super()` 调用。因此，在显式调用 `super()` 后再调用 `this()` 是不合法的。

**修正后的代码**：

```java
public class MyClass extends MySuper {
    MyClass() {
        super();
    }
    MyClass(int i) {
        super(); // 调用父类的无参构造函数
        // 其他初始化代码
    }
}
```

或者，如果希望在带参构造函数中调用本类的无参构造函数，可以这样做：

```java
public class MyClass extends MySuper {
    MyClass() {
        super();
    }
    MyClass(int i) {
        this(); // 调用本类的无参构造函数
        // 其他初始化代码
    }
}
```
原示例代码中的问题在于带参构造函数中同时调用了 `super()` 和 `this()`，这是不允许的。修正后的代码根据需求选择调用父类或本类的其他构造函数，确保构造函数链式调用的正确性。

***
<h2> <a href="https://blog.csdn.net/Genevieve_xiao/article/details/147746114#NotTheSameTimeSuper&This" >关于到底为什么不能同时调用 `super()` 和 `this()`</a></h2>


***

## 单元总结
在本单元中，你应该已经学会了：
- 描述字段和方法的继承
- 解释类层次结构的概念
- 概述子类如何专门化超类
- 解释方法查找的工作原理
- 创建和使用子类
- 描述多态是如何实现的

***

# 第 7 单元：接口 Interfaces
## 接口的概念

  * **定义** ：接口是 Java 中声明类型的一种方式，它代表对象所支持服务的承诺，是一种合同，规定了实现该接口的类必须提供的方法。
  * **特点** ：接口只包含方法声明，不包含实现。接口不是类，但与抽象类有相似之处。

## 接口的声明与实现

  * **声明接口** ：使用 `interface` 关键字声明接口，接口中可以包含常量和抽象方法（Java 8 以后还可以包含默认方法和静态方法）。
  * **实现接口** ：类通过 `implements` 关键字实现接口，必须实现接口中声明的所有抽象方法，否则该类必须声明为抽象类。

某些接口，如 `Cloneable`，不包含任何方法。这些接口向 Java 发出信号，表示一个类遵循某种可能无法用一组特定方法表达的协议。在 `Cloneable` 的情况下，它通知 JVM 实现该接口的对象可以通过 `clone()` 方法进行复制

**具体实例**：
![](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIDFGqNsnpvLk9k6dFgC_nkE4atHI91AAJeF2sb5mpoVHxgk4rGXctkAQADAgADeAADPQQ.png)

这个例子定义了一个名为 `File` 的接口，其中包含了两个方法声明`open()` 和 `close()`。任何实现这个接口的类都必须提供这两个方法的具体实现。例如，一个 `TextFile` 类可能实现 `File` 接口，并提供打开和关闭文本文件的具体逻辑。

![](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIDFWqNsnxB7hk13IxMKMzIjAcunhEVAAJfF2sb5mpoVG-40adikx-HAQADAgADeQADPQQ.png)

在接口中声明的方法是在支持该接口的类中实现的。

### 语法

- 在类声明中，超类的命名在类支持的任何接口之前。
（也就是先extends再implements
  ```java
  public class Directory extends Secure implements File {
      ...
  }
  ```

- 如果一个类实现了多个接口，这些接口将全部列出，并用逗号分隔。
  ```java
  public class Directory implements File, Secure {
      ...
  }
  ```

## 类型和接口

- **变量的类型可以是一个接口。** 这意味着只有实现了该接口的类的对象才能绑定到这个变量上，并且只能使用接口中定义的方法。
例如，如果一个变量是 `File` 接口类型，那么只能将实现了 `File` 接口的类的对象赋值给它，并且只能调用 `File` 接口中定义的方法，即使实际对象可能有更多的方法。

- **接口不能直接用于创建对象，因此不能在 `new` 表达式中出现。** 
例如，`File r = new File();` 是错误的，因为 `File` 是一个接口，不能直接实例化。但是，你可以创建一个实现了 `File` 接口的具体类的对象，并将其赋值给 `File` 类型的变量，如 `File f = new TextFile();` 这样是正确的。
![](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIDFmqNsn9dNXx9hFjvB3rvNuHZZUi5AAJgF2sb5mpoVC-hl8WSvUYaAQADAgADeAADPQQ.png)


## 子接口 Subinterfaces

- 接口不是类，因此这种层次结构独立于类的层次结构。
- 扩展另一个接口的接口继承了所有方法声明。
![](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIDF2qNsoK1Pe4ipjrM2OJTHqjGMkCmAAJhF2sb5mpoVKN9S_IeE2-fAQADAgADeAADPQQ.png)

**示例解释**

1. **`File` 接口**：
   - 定义了两个方法：`open(String name)` 和 `close()`。
   - 这些方法是任何文件操作的基本功能，例如打开一个文件和关闭一个文件。
2. **`ReadableFile` 接口**：
   - 通过 `extends File` 关键字扩展了 `File` 接口。
   - 继承了 `File` 接口中定义的所有方法（`open` 和 `close`）。
   - 添加了一个新的方法 `readByte()`，用于从文件中读取一个字节的数据。
3. **`WritableFile` 接口**：
   - 同样通过 `extends File` 关键字扩展了 `File` 接口。
   - 继承了 `File` 接口中定义的所有方法（`open` 和 `close`）。
   - 添加了一个新的方法 `writeByte(byte b)`，用于向文件中写入一个字节的数据。
4. **`ReadWriteFile` 接口**：
   - 通过 `extends ReadableFile, WritableFile` 关键字同时扩展了 `ReadableFile` 和 `WritableFile` 接口。
   - 继承了 `ReadableFile` 和 `WritableFile` 接口中定义的所有方法（包括 `open`、`close`、`readByte` 和 `writeByte`）。
   - 添加了一个新的方法 `seek(int position)`，用于将文件指针移动到指定的位置。



## 协议 Protocols

- **接口定义了一个协议（一组方法）**
    - 如果一个类实现了给定的接口，那么这个类就实现了该协议。
  
- **接口可以用于在一组没有继承关系的类上强加一个共同的协议**
	- 接口的一个重要用途是让一组没有直接继承关系的类能够**共享同一个行为规范**。
    - 在通过继承关系连接的一系列类中，共同的协议是通过**子类化**来实现的。这种方式有一定的局限性，因为它要求类之间必须有直接的继承关系。而接口则提供了另一种方式，使得不相关的类也可以共享相同的行为规范。

![在这里插入图片描述](https://telegraph-image-5ms.pages.dev/file/AgACAgUAAyEGAASIfjD1AAIC8mqNsC6_3ECsSy6Su-y3th-XD9mcAAI6F2sb5mpoVH-Xxl7VOK0KAQADAgADdwADPQQ.png)

示例图展示了 `Comparable` 接口如何被 `Date`、`String` 和 `Integer` 类实现：

- `Comparable` 接口定义了一个 `compareTo` 方法，用于比较两个对象的大小。
- `Date`、`String` 和 `Integer` 类分别实现了 `Comparable` 接口，并提供了各自版本的 `compareTo` 方法实现。
- 尽管 `Date`、`String` 和 `Integer` 类之间没有直接的继承关系，但它们都实现了 `Comparable` 接口，因此都可以通过 `compareTo` 方法进行比较。

这种设计使得我们可以编写通用的排序算法，只需要传入实现了 `Comparable` 接口的对象即可，而不需要关心具体的类型。


## 接口的编程场景

- **跨层次多态可以通过接口实现**：这意味着即使两个类不在同一个继承树中，只要它们实现了相同的接口，就可以通过该接口类型的引用来引用这两个类的对象，并调用接口中定义的方法。

- **接口允许访问不同类树中的方法**

	- **可以用一个对象替换另一个与之在类层次结构中没有关系的对象**：如果两个或多个类实现了相同的接口，那么它们可以在需要该接口类型的地方互换使用。
	
	- **实现相同接口的类理解相同的消息，无论它们在类层次结构中的位置如何**

~~（虽然我觉得以上几点说的都是同一个意思 罗里吧嗦的~~

考虑如下场景：

```java
interface Flyable {
    void fly();
}

class Bird implements Flyable {
    public void fly() {
        System.out.println("A bird can fly.");
    }
}

class Airplane implements Flyable {
    public void fly() {
        System.out.println("An airplane can fly.");
    }
}
```

在这个例子中，`Bird` 和 `Airplane` 都实现了 `Flyable` 接口。虽然它们之间没有任何直接的继承关系，但都可以被视为 `Flyable` 类型的对象，并且可以调用 `fly()` 方法。这样做的好处是，任何接受 `Flyable` 类型参数的方法都能接收并正确处理 `Bird` 或 `Airplane` 的实例，体现了接口带来的强大灵活性和重用性。

## 接口的优势

- **使用接口可以对对象的使用方式提供更多的控制**
  - 可以捕捉到没有继承关系的类之间的相似性，而不会强加一种不自然的关系。
  - 开发者知道对象将响应哪些消息；可以揭示对象的接口而不必揭示其类。
  - 提高代码的可重用性。

## 接口的命名约定

- **创建“able”接口**
  - 如 `Cloneable`、`Serializable` 等。
- **使用专有名词为接口命名，并为你的接口提供“Impl”实现**
  - `Bank` 接口，`BankImpl` 类
  - `BankAccount` 接口，`BankAccountImpl` 类
  - 使用这种约定，接口通常包含实现类的所有（或大多数）公共方法的定义。
- **在接口名称前加上“I”，并为你的类使用专有名词**
  - `IBank` 接口，`Bank` 类
  - `IBankAccount` 接口，`BankAccount` 类


## 问答


### 1. 接口和类的区别

* **定义和功能**：
  * **类** ：类是对象的模板，用于创建具有相同结构和行为的对象。它可以包含字段（属性）、方法（行为）以及构造函数等。类可以实例化对象，这些对象拥有类定义的属性和行为。
  * **接口** ：接口是一种特殊的抽象类型，它只包含方法声明（在 Java 8 之前是抽象方法，在 Java 8 及以后可以包含默认方法和静态方法）、常量和类类型声明等。接口定义了一组操作规范，实现了接口的类必须按照接口声明的方法名、参数列表和返回值类型来实现这些方法。
* **实现方式**：
  * **类** ：类通过继承关键字 `extends` 来继承另一个类，并且可以实现多个接口，使用 `implements` 关键字。子类可以继承父类的属性和方法，并且可以重写或扩展它们。
  * **接口** ：接口通过 `extends` 关键字继承其他接口。一个类实现接口时，需要实现接口中声明的所有抽象方法，否则该类必须声明为抽象类。
* **实例化**：
  * **类** ：普通类（非抽象类）**可以被实例化**，创建出具体的对象。
  * **接口** ：接口**不能被实例化**，只能通过实现接口的类来创建对象。

### 2. 接口和抽象类的相似点与不同点
* **相似点**：
  * 都可以**包含抽象方法**，用于定义规范，实现类必须按照这些规范实现方法。
  * 都可以**包含常量**，并且这些常量默认是 `public static final` 的。
  * 都**支持继承**，接口可以继承接口，类可以继承类并实现接口。
* **不同点**：
  * **方法实现** ：接口在 Java 8 之前只能包含抽象方法，不能包含具体实现（构造函数、普通方法等），而抽象类可以包含抽象方法和具体方法（包括构造函数）。从 Java 8 开始，接口可以包含默认方法和静态方法，但它们有具体的实现。
  * **成员变量** ：接口中的成员变量默认是 `public static final` 的常量，不能被修改。而抽象类中的成员变量可以是普通的变量，也可以是常量，它们可以有各种访问修饰符。
  * **构造函数** ：抽象类可以有构造函数，用于初始化操作。接口不能有构造函数。
  * **继承** ：类只能继承一个抽象类，但可以实现多个接口。接口可以继承多个接口。


## 单元总结

- 完成本单元后，你应该能够：
  - 解释接口的概念并概述它提供的功能
  - 在 Java 中声明一个接口
  - 声明一个类实现一个或多个接口
  - 解释实现接口的类必须提供什么
  - 识别接口有用的编程场景

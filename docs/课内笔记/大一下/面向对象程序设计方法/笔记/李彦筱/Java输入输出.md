# Java输入与输出

本部分简单介绍 Java 的几种输入输出方式。

## Java 输入

### 使用 Scanner 从键盘输入

```java
import java.util.Scanner;

public class NumberInput {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double number, sum = 0;
        while (scanner.hasNextDouble()){
            number = scanner.nextDouble();
            sum += number;
        }
        System.out.println(sum);
    }
}

```

注意：

Scanner 中类似 hasNextxxx 在命令行界面失败的条件是读到 EOF。使劲往命令行输入回车并不能使 hasNextDouble 返回 false。

在命令行里敲出 EOF 的方法是按 ctrl+D（Mac：command+D）.

Scanner 类对下一个东西是什么的检测似乎用的是正则表达式。

### 利用命令行执行时的参数

```java
public class RandomSeq {
    public static void main(String[] args) {
        if (args.length < 1){
            System.out.println("用法： java RandomSeq <要生成的随机数个数>");
        }
        else{
            for (int i=0;i<Integer.parseInt(args[0]);i++){
                System.out.println(Math.random());
            }
        }
    }
}
```

main 函数开头的 `String[] args` 里面保存了命令行调用程序时后面跟着的参数。

### 从文件输入（借助Scanner和FileInputStream）

```java
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;


public class InputByFile {
    public static void main(String[] args) throws IOException{
        Scanner scanner = new Scanner(new FileInputStream("Hello.txt"));
        double number, sum = 0;
        while (scanner.hasNextDouble()){
            number = scanner.nextDouble();
            sum += number;
        }
        System.out.println("The sum is " + sum);
    }
}
```

Scanner里叠一个FileInputStream就行了。

## Java 输出

### 直接使用 System.out.println

```java
public class WelcomeSout {
    public static void main(String[] args){
        int year = 2023;
        String name = "软件学院22级的学生们";
        System.out.println(name + ", welcome to Java in " + year + ".");
        System.out.printf("%s, welcome to Java in %4d.", name, year);
    }
}
```

### 输出到文件

输出到文件需要使用 Java 的 PrintWriter 类

> System.out 是一个 PrintStream 对象，和 PrintWriter 拥有几乎完全一样的接口（）

比如：

```java
import java.io.PrintWriter;
import java.io.FileNotFoundException;

public class WelcomeFile {
    public static void main(String[] args) throws FileNotFoundException{
        PrintWriter printWriter = new PrintWriter("Hello.txt");
        printWriter.println("Welcome to Java lessons");
        printWriter.close();
    }
}
```

注意：

- PrintWriter 在向文件输出时没有自动刷新缓冲的功能。而且这玩意的析构函数也不会自动刷新缓冲区……也就是说，如果不手动调用 PrintWriter.close 的话，这玩意根本就不会真正输出到文件里

- `throws FileNotFoundException` 是必须要添加的；如果你想知道这是什么，请参考 [Java 异常处理](docs/课内笔记/大一下/面向对象程序设计方法/笔记/李彦筱/Java例外处理.md)

### 打印到 `System.out`，但输出到文件

程序打印到System.out的所有信息可以被重定向到某一个文件。这个操作需要你通过终端运行程序，而不能通过IDE，因为IDE中运行不能自定义程序的运行参数。

使用这样的命令：

`java my > Hello.txt`

这会把名为 `my.class` 字节码程序向 System.out 的所有输出重定向到 Hello.txt 中。终端里将不会再显示任何 System.out 打印的信息。

> 本质上来说，这是终端提供的功能，而非 Java 自身的功能。


# 面向对象程序设计方法 模拟题

## 判断题（5分 5题）

1. `package` 语句能多次使用。
2. 静态成员不因为实例的不存在而存在。
3. 抽象类不能拥有构造方法。
4. 类只能能有一个继承，接口可以有多个继承。
5. `try` 语句必须后跟 `catch` 语句，`finally` 语句可有可无。

## 选择题（15分10题）

1. char的表示范围：

A. 0~65536

B. -32768~32767

C. -32767~32768

D. -65536-65536

2. 以下程序输出结果正确的是：

```java
public class test {
    public static void main(String[] args) {
         StringBuilder a = new StringBuilder("-");
         StringBuilder b = a.append("-");
         System.out.print(a == b);
         System.out.print(" ");
         System.out.print(a.length());
     }
}
```

A. `false 1`

B. `false 2`

C. `true 1`

D. `true 2`

3. 可以填在横线上的是哪两个：`!=`, __, __, `++`（优先级从左到右由小到大）

A. `!` `*`

B. `>=` `+`

C. `+` `<`

D. `*` `-` 

4. 以下程序输出结果正确的是：

```java
public class test {
    public static void main(String[] args) {
         int foo = 120;
         switch (foo) {
             default -> {
                 System.out.println("default");
                 break;
             }
             case 1 -> {
                 System.out.println("1");
                 break;
             }
             case 120 -> {
                 System.out.println("120");
                 break;
             }
             case 127 -> {
                 System.out.println("127");
             }
             case 193 -> {
                 System.out.println("193");
             }
         }
    }
}
```

A. `120 127 193`

B. `120`

C. `default`

D. `1 120`

5. 以下哪两个说法是正确的：

```java
public class test {
    public test() {
        this(7);
    }
    public test(int a) {
        this("Sunday");
        System.out.print("makabaka ");
    }
    public test(String b) {
        this("today", 7);
        System.out.print("wuxidixi ");
    }
    public test(String a, int b) {
        System.out.print("tangbolibo ");
    }
    
    public static void main(String[] args) {
         test a = new test();
    }
}
```

A. 程序中出现三次构造函数重载

B. 程序中出现两次构造函数重载，其中有一个不被允许

C. 输出结果为 `makabaka wuxidixi tangbolibo `

D. 输出结果为 `tangbolibo wuxidixi makabaka `

E. 编译不通过

6. `//` 处填入哪两个可以编译通过：

```java
public class superclass {
    public superclass() {}
    public void paint() {
        System.out.println("makabaka");
    }
}


public class test extends superclass {
    public test() {}
    public void paint() {
        System.out.println("wuxidixi");
    }

    public static void main(String[] args) {
        test a = new test();
        // 填入？
        a.paint();
        b.paint();
    }
}
```

A. `superclass b = new superclass();`

B. `test b = new test();`

C. `Superclass b = new test();`

D. `Test b = new superclass();`

E. `Superclass b = (test) superclass();`

F. `Test b = (test) superclass();`

7. 定义一个函数头 `public String xjtuse(int a, String b, double c)`，以下哪两个可以算方法的重载：

A. `private String xjtuse(int a, String b, double c)`

B. `String xjtuse(String a, int b, double c)`

C. `public void xjtuse(int a, String b, double c)`

D. `Public String xjtuse()`

8. 例外处理，以下哪个是错的：

A. 程序员可以通过例外处理将代码主程序和例外处理分开

B. 例外处理可以提高代码的运行速率

C. 在解决 `checked` 的例外处理函数中仍然可能出现 `unchecked` 的例外

9. - [ ] TODO

10. - [ ] TODO

## 填空题（5题5分）

1. 面向对象的三大特征是：____________。
2. 对象与对象之间的互动是通过 ____ 机制实现的。
3. `final` 修饰变量的功能是 ____，修饰成员方法的功能是 ____，修饰类的功能是 _____。

## 综合题（8题55分，有名词解释，简答，读程序写结果等）

1. 名词解释：JVM
2. 名词解释：方法覆盖
3. 名词解释：方法签名
4. 简答：数据成员分为类成员，实例成员，请从定义，初始化，使用三个方面区分两者。
5. 简答：什么是异常？请解释 `throws` 和 `throw`。
6. 画出第 2，5 行执行后的内存分布图

```java
String[] names = {"Zhang", new String("Zhang"), new String("Wang")};
int[] ages = {18, 20, 19};
Object[] objs = {names, ages};
((String[]) objs[0])[1] = "Zhang";
((int[]) objs[1])[1] = ((int[])objs[1])[0];
```

7. - [ ] TODO （UML图）
8. 读下面程序，回答问题：

```java
public class Base {
    protected static int i;
    public float f;

    public Base(int i, float f) {
        Base.i = i;
        this.f = f;
    }

    public void move() {
        move(10);
        move(10f);
    }

    public void move(int i) {
        Base.i += i;
        System.out.println("in int Base " + Base.i);
    }

    public void move(float f) {
        this.f += f;
        System.out.println("in float Base " + this.f);
    }
}

public class SubBase extends Base {
    protected static int i;
    public float f;

    public SubBase(int i, float f) {
        super(i, f); // ------------(*)
        SubBase.i = i;
        this.f = f;
    }

    public void move() {
        move(5);
        move(5f);
    }

    public void move(int i) {
        SubBase.i += i;
        System.out.println("in float SubBase " + this.f);
    }
}

public class Test {
    public static void main(String[] args) {
        Base[] bases = {new Base(0, 0), new SubBase(0, 0), new Base(1, 2)};
        bases[0].move();
        bases[1].move();
        bases[2].move();
        SubBase sub = (SubBase) bases[1];
        System.out.println("i = " + bases[1].i + " f = " + bases[1].f);
        System.out.println("i = " + sub.i + " f = " + sub.f);
    }
}
```

(1). 写出运行 `Test.main` 结果。

(2). 删去有 `// ------------(*)` 注释的一行，是否能编译成功？

(3). 把类 `SubBase` 和 `Base` 放到不同的包里，是否能编译成功？

## 编程题（2题20分）

- [ ] TODO
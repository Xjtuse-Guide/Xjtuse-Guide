# Java 类的继承

## 类之间有层次关系

- 任何一个对象都属于一种类类型

- 在 Java 中，任何一个类型都拥有一个父类（除了 Object 类）

  Object 类是 Java 类的层次结构中的**顶层类**（也就是说一直寻找一个类的父类，最终总会在 Object 类停止），因为任何一个没有继承其他类的类都继承 Object，而继承了其他类的类，其父类也是 Object 的子类。

- 在自定义数据类型并继承的时候，只需要指明这个类的直接父类。（事实上，在 Java 里你根本没法直接继承多个类）

## 子类和父类的关系

子类是父类情况的特殊化。也就是说，子类和父类是一种 "is a" 的关系。

比如，Java 中有个 Number 类，它是 Integer 的父类。因此可以说，"Integer is a number" （实际上 Integer，即整数也确实是数的一种）

那子类特殊化在哪里呢？有两个方面：

- 状态（即对象包含的所有数据成员）

  怎么「特殊化」数据成员呢？难道是改个更好听的名字吗？

  一般来说，子类会通过**添加新的数据成员**的方法来特殊化自己的状态。这是因为从父类得到的已经有的数据成员可能不足自己使用，必须再新增一些。

- 行为（即对象持有的方法）

  「特殊化」行为一般包含两种方法：

  - 重写已经存在的方法（修改）

  - 添加新的方法（扩展）

    比如，以 「Integer 类继承了 Number 类」来看，Integer 类中多了一个 intValue 函数用来获取它自己的值。而 Number 类并没有这一函数。

父类是子类情况的一般化。

- 父类聚集了“所有子类”都需要使用的数据和方法。即，父类包含子类**公共的部分**。这样的好处是，子类中都需要的代码只需要写一次，修改时也只需要在一处修改。
- 集中数据和方法到父类有助于实现代码的重用

## 继承关系

「继承」是指一个子类和它的父类之间的关系。继承是一种「is a」关系，而不是「has a」关系。

> 「has a」：比如一个计算机类中可能包含CPU，内存，显卡，显示器，鼠标键盘…这些东西，那么计算机和这些东西的关系就是「has a」关系，即包含关系：我当中包括你
>
> 「is a」：服务器，笔记本电脑都是一种计算机。这么来说，服务器、笔记本电脑…与计算机的关系就是「is a」：我是一种特殊情况下的你。比如，“笔记本电脑 是一种 计算机”。

### 继承数据和方法

当一个子类继承了一个父类后，这个子类会**继承父类的数据**，即**该类会拥有父类所有的数据成员**，且这一过程不需要你主动完成（事实上，你甚至阻止不了这事的发生）。

此外，这个子类还会**继承父类的方法**。不过，这个时候子类就**不会继承所有的方法**。如果父类中的方法没有被在子类中重写，那么父类的该方法会被继承；如果子类已经覆盖了父类的一个方法（重新定义了该方法），那么父类的该方法就不会被继承，子类仍然拥有自己定义的方法。

## 访问修饰符

这是 [该文件第 2.3 节 ](docs/课内笔记/大一下/面向对象程序设计方法/笔记/李彦筱/Java类.md)中内容的拓展。

访问修饰符可以对**数据和方法生效**。但是，只有一部分这里的修饰符可以对类生效。

### private

被声明为 private 的成员（**不管是方法还是数据**）只能被定义它的那个类访问。这个类的子类都不能使用。

### public

所有包中的所有类都能够访问被声明为 public 的成员（不管该成员是方法还是数据）

### default

default 是一个比较特殊的修饰符：它只在你没有指定任何访问修饰符时被应用；

只有定义了被修饰为 default 的成员的类**所在的包**中的其他类可以访问该成员。

### protected

- 该成员**所在包**的所有类可以访问该成员（这部分和 default 一样）

- 此外，继承该成员所在类的另一个类也可以访问该成员（**即使这两个类不在同一个包中**）

  > 注意：对于这一点的说明：
  >
  > 子类只能访问**自己从父类继承的那个数据成员**。比如考虑如下代码：
  >
  > ```java
  > package xjtu.se.a;
  > public class Alpha{
  >     protected int c;
  > } // package xjtu.se.a
  > ```
  >
  > ```java
  > package xjtu.se.b;
  > public class AlphaSub extends Alpha{
  >     void method(){
  >         // 这是可以进行的。因为 AlphaSub 类是 Alpha 类的子类，根据 protected 的访问性，AlphaSub 类可以访问 Alpha 类中定义的那个 c。
  >         c++;
  >         Alpha obj = new Alpha();
  >         // 不可以。AlphaSub 类只能访问自己从 Alpha 中继承来的那个 c 属性。（即 c/this.c）。
  >         // 而你新建一个 Alpha 类的对象的话，AlphaSub 类不能访问这个对象的 c 属性。
  >         obj.c++;
  >     }
  > }
  > 
  > ```
> protected 是比 default 更宽泛的访问类型。default 可以访问的内容，protected 一定也可以访问

## 方法的覆盖

子类如果要覆盖的父类的方法的话，需要定义一个和父类方法**签名相同**的方法。如果签名不同，编译器就会认为子类的方法和父类的不是同一方法，并且不会进行覆盖。

条件：

- **签名一致**

- **返回类型兼容**

  对于基础数据类型：二者的返回类型**必须完全一致**

  对于引用数据类型：**父类的返回类型必须兼容子类**。即，子类只能返回父类那个引用数据类型自身**或者其子类**。GPT给的例子：

  例如，如果基类方法返回一个基类类型，子类可以返回基类的子类类型。如果基类方法返回`Object`，子类可以返回`String`，因为`String`是`Object`的子类。这样的覆盖是合法的。

  ```java
  class Base {
      public Object getData() {
          return new Object();
      }
  }
  
  class Subclass extends Base {
      @Override
      public String getData() {
          return "Hello, World!";
      }
  }
  ```

  （当然，你完全可以让子类方法和父类方法的返回值类型一致，都返回 `Object`。）

- 访问修饰符不能比父类方法的修饰符要求更严格。

  > 父类方法**不能被定义为 private**。否则，子类就“看不到”这个方法，自然就没法覆盖了。

如果两个方法的签名相同，但返回类型不兼容，那么覆盖无法完成，并且编译器会报错。

### 内存图的修改：

在引入继承后，内存图表示类时，堆需要分为两个部分：**数据部分**和**方法部分**需要：

当一个类是子类后，**内存图中需要包含该类从父类中继承的属性和方法**。每个方法和数据前必须：**包含定义它的类的名字**。

比如，对于以下类B的内存图：

```java
public class A{
    public int a;
}

public class B extends A{
    public int b;
}
```

B 内存图中的数据表示为：

`A::a` 和 `B::b` 。

对于数据：**额外添加父类的所有数据**

对于方法：如果没有覆盖父类的方法，**添加父类的方法**。否则，**添加自己的方法**

### 数据的隐藏

如果子类中定义了和父类名称一样，类型一样的数据，那么父类的数据会被**隐藏**。子类和父类的这个数据**会同时存在**。隐藏的名称可以通过一定的方法重现。

怎么重现呢？记住一点：

**Java 调用一个对象上的哪个成员，看的是这个对象实际属于哪个类，而不看这个对象在定义时是哪个类型**。

> 在Java中，对象实际属于的类，和对象定义时是哪个类型是有区别的。这是因为Java允许给父类类型的一个变量赋值一个其子类的对象。例如：
>
> ```java
> Object a = new String("Hello world!");
> ```
>
> 是被允许的。尽管 Object 和 String 不是一个类型，但 String 是 Object 的子类。
>
> 此时，「对象实际属于哪个类」的结果为 String。「对象在定义时是哪个类型」的结果为 Object。

体会一下代码：

```java
class A{
    public String name;
    public A(){
        name = "Base";
    }
    public String getName(){
        return name;
    }
}

class B extends A{
    public String name;
    public B{
        name = "Sub";
    }
    public String getName(){
        return name;
    }
}

class Main{
    public static void main(String[] args){
        B b = new B();
        System.out.println(b.name); // Sub
        System.out.println(((A)b).name); // Base
        System.out.println(b.getName()); // Sub
        System.out.println(((A)b).getName()); // Sub
        A a = new B(); // 注意这里给A赋值了B类型的对象。
        System.out.println(a.name); // Base
    }
}
```

被隐藏的数据成员是根据存放这个对象的变量的数据类型来的。比如最后一个语句中，由于存放B对象的变量是A，所以得到的数据成员 a.name 就是被隐藏的 base 而不是 sub。

只要满足两个条件的一个，隐藏的数据成员就可以重现：

1. 存放这个数据成员所在对象的变量类型是父类类型的
2. 这个数据成员所在对象被强制转换为了父类类型的对象

这两种情况下，通过调用这个变量.数据成员都可以取到那个被隐藏的成员。

## 多态的引入

在 Java 中，可以把一个**子类类型的对象**赋值给**父类类型**。接受就好，这是个…某种意义上的“设定”。

这也导致了，编译器不可能确切的知道 **一个变量到底是存放着自己类型的对象，还是自己子类类型的对象**。

上边的例子里也已经提到过了。

比如：

```java
class A{
    public String name;
    public A(){
        name = "Base";
    }
    public String getName(){
        return name;
    }
}

class B extends A{
    public String name;
    public int id;
    public B{
        name = "Sub";
    }
    public String getName(){
        return name;
    }
}

class Main{
    public static void main(String[] args){
        A a = new A();
        a = new B(); // 这句话是正确的：把父类类型的变量指向了子类类型的对象。而且，这个操作没有任何风险。
        System.out.println(a.getName()); // 本句话输出 Sub
        // 这是因为Java在调用一个对象的方法时，只看这个对象是什么类型的（是 B)
        // 不看这个对象所在的变量是什么类型（是 A)
        // 因此，它调用 B::getName() 方法，而不调用 A::getName() 方法
    }
}
```

以上的例子有什么意义呢？

这说明了，我们可以对任何一个子类的对象，执行它父类能够做的方法；并且，如果子类覆盖了父类的方法，实际执行的是**子类覆盖后的方法**。是不是很神奇（

### 多态出现的条件

1. 存在继承关系
2. 子类的方法**覆盖了**父类的方法
3. 将一个父类变量指向了子类的对象
4. 在刚刚的父类变量上**调用了那个被覆盖的方法**

这个时候，实际被调用的是**子类的新方法**

### 类的各种成员

| 成员                            | 隐藏 | 覆盖 | 编译阶段做什么               | 运行阶段（动态链接）           |
| ------------------------------- | ---- | ---- | ---------------------------- | ------------------------------ |
| 数据成员                        | 是   | 否   | 检查语法，并确定附属于那个类 | 直接执行                       |
| 成员方法-类方法（带static）     | 是   | 否   | 检查语法，并确定附属于那个类 | 直接执行                       |
| 成员方法-实例方法（不带static） | 否   | 是   | 仅检查语法                   | 根据对象的实际类型调用对应函数 |

隐藏：指当子类和父类的某成员重复时，子类中一般无法找到父类的这个成员，但可以通过特殊方法得到

覆盖：指当子类和父类的某成员重复时，子类成员完全覆盖父类成员，父类成员永远无法通过子类对象访问到。

### 多态有什么用处

可以让你用**统一的接口处理不同的对象**

下面有一个很复杂的例子：

```java
public class Employee{
    private String name;
    public String getName(){
        return name;
    }
    public void setName(String name){
        this.name = name;
    }
    public double earnings(){
        
    }
}

public class WeeklyEmployee extends Employee{
    private double week_earning;
    public double earnings(){
        return week_earning;
    }
}

public class HourlyEmployee extends Employee{
    private double hour_earning;
    private double work_hours_in_a_week;
    public double earnings(){
        return hour_earning * work_hours_in_a_week;
    }
}

public class CountEmployee extends Employee{
    private double sell_count;
    private double profit;
    public double earnings(){
        return profit * sell_count;
    }
}

public class Main{ 
    public static void main(String[] args){
        CountEmployee count_employee = new CountEmployee();
        WeeklyEmployee weekly_employee = new WeeklyEmployee();
        HourlyEmployee hourly_employee = new HourlyEmployee();
        System.out.printf("CountEmployee pay: %.2f", count_employee.earnings());
        Employee employee[] = {count_employee, weekly_employee, hourly_employee};
        for (Employee one: employee){
            // 这里实际调用了每个对象自己类的 earnings 方法
            // 而不是 Employee 父类里头那个啥都没有的 earnings 方法
            // 这就是多态的应用：
            // 我不需要关心你具体是哪种类型，我只需要知道你是我的子类，而且你有我想调用的方法
            System.out.printf("Employee pay: %.2f", one.earnings());
        }
    }
}
```


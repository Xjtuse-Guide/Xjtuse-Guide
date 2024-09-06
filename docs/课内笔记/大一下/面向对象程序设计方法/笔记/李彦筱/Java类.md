# Java Building Class

如何创建自己的 Java 数据类型？

## 已有的数据类型

我们已经学习过了哪些数据类型？

### 基本数据类型

> Primitive Data Type

| 数据类型 | 内容                | 操作    |
| -------- | ------------------- | ------- |
| int      | 数字（比如1，2，3） | + - * / |

### 引用数据类型

> Reference Data Type

| 数据类型           | 内容               | 操作                   |
| ------------------ | ------------------ | ---------------------- |
| 数组（Array）      |                    |                        |
| 字符串（String）   | 字符串内容，长度等 | .substring, .length    |
| **自定义数据类型** | 属性/状态          | 行为（Python里叫方法） |

引用类型的操作使用其附带的函数（或者说方法）完成。比如：

```java
String a = "Hello";
String b = new String("Hello");
a.equals(b); // 在（身为字符串的引用类型的） a 上执行了一个操作
```

基础类型的操作使用 Java 的运算符完成。比如，

```java
int a = 3;
int b = 4;
int c = a + b; // 在基本数据类型上执行操作
```

#### Java 的类

Java 的类有一个需要注意的地方：它既可以是「类库」（即一大堆函数的集合），也可以是一种数据类型

**类库**

类库汇合了很多功能间有关联的函数。作为类库时，这个类不能被称为一种数据类型。比如，java.util.Math 就是一个类库，放置了一堆和数学计算有关的东西（比如 Math.sin Math.abs ……）。

在 Java 中，类库里的每一个函数前一定是 **static** 修饰的，即**不需要创建对象就可以使用这些函数**。

为什么不直接用函数，非得把这些函数定义在一个类里呢？这是因为 **Java 不允许直接定义函数**。所有的函数必须在类中存在。在 Python 中，就不需要把这种函数放在类里。

```java
class Math{
    public static abs(double x);
    public static sin(double x);
    ...
}
```
在 Python 里，上面这样的 Math 类可能会如下定义：
```python
# 在 Math.py 中：
def abs(x):
    ...

def sin(x):
    ...
```

**数据类型**

一个「真正的类」。你可以产生该类的对象，在下面会详细的讲述。

## 什么是类：自定义数据类型

- 类封装了 **属性** 和 **行为**

  属性：在编程语言中是 **变量**

  行为：在编程语言中是 **函数**

  以下是三种语言中类里的属性和行为：

  ```c++
  class Student{
      public:
      // 属性（类内的变量）：
      	int age;
      	String name;
      // 行为（类内的函数）：
      	void GetScore();
  }; // C++
  ```

  ```java
  public class Student{
      // 属性
      public int age;
      public String name;
      // 行为
      public void GetScore();
  } // Java
  ```

  ```python
  class Student:
      # 构造函数
      def __init__(self):
          # 我记得规范里 Python 成员变量似乎是在构造函数里添加的…
          # 属性
          self.age = 0
          self.name = ""
      
      # 行为
      def GetScore():
          ...
  # Python
  ```

  属性和行为都是类的**成员**

- 类中的成员（属性和行为）可以**隶属于成员或类自身**

  （如果你学过其他语言的面向对象内容，应该能看懂这句话）简单来说，类中的属性可以是 成员变量 或者 类变量（加 static 修饰的变量）。类里的 行为 也可以是 类方法（静态方法） 或者 成员方法 

- 类之间大多数时候是相互独立的，但也可以通过以下方式产生关联：

  类可以由 **继承** 得到其他类的成员

  类可以由继承 **接口** 实现 **多态**（这个比较抽象，后面会有，现在不用管）

### 如何管理类：包

包可以把一堆有关的类聚集在一起。因为 Java 的一个文件中只允许出现一个 public 类型的类，因此多个 public 类必须分文件编写。

类就像一张蓝图，可以用来创建对象。很多编程书上有一个比喻，如果对象是一辆车，类就是这辆车的图纸。这可能不太准确。不过还算直观。

### 定义一个类

举个例子：

```java
public class BankAccout extends Accout implements Serializable, BankStuff; 
```

BankAccout ：这是这个类的名字，你定义的数据类型的一个标识符。

`extends` 关键字：表示该类继承一个已经存在的类

`implements` 关键字：表示该类实现一些接口

这两个关键字用来让类和其他类产生关系，是可选的。如果没有的话，这个类就是**独立的**，和其他类没有关系的。

> 可选阅读：C++ 中有没有接口和继承？
>
> 有继承，没有接口。「接口」是实现多继承的一种方式。Java 不允许多继承，但类似于多继承的需求客观存在，因此出现了接口来满足这种需求。而 C++ 直接支持多继承，因此就没有这事了。
>
> 为什么 Java 不支持多继承呢？我感觉是因为多继承会把你的类搞得一团糟。我只试着在 Python 里用过多继承，Python 为了多继承发明了 super 函数，（某种程度上）会自动的找到你要调用哪个父类的方法。即便如此，Python 在进行多继承时代码还是一团糟。（仅个人观点，具体原因建议上网搜搜看）
>
> C++ 里的类的声明（与继承的声明）：
>
> 上面的 Java 声明在 C++ 里头可能是这样的：
>
> ```c++
> class BankAccout: public Accout{
>     ...
> };
> ```
>
> 因为 C++ 没有接口的概念，所以没法翻译 `implements Serializable` 这一块继承接口的东西。

### 类型的修饰符

在上面那个类的定义中，你肯定能看到开头有一个 `public` 关键字。这个是类型的**访问修饰符**，不同的访问修饰符会让类“可被访问”的状态不同。

这里只简单的列举一些修饰符，并不在这里解释为什么 Java 中存在这些修饰符。

**下面的修饰符并不包含 Java 中全部修饰符**

#### 访问修饰符

> 这些访问修饰符全都相互冲突

**public**

如果一个类的访问修饰符为 public ，这个类就可以被任何的 Java 代码访问。（只要能访问到它所在的包）

**default**

如果一个类没有任何访问修饰符，它的访问修饰符就是 default 。这种类只能被同一个包内的 Java 代码访问。

> 类只能被这两种访问修饰符修饰；private 和 protected 不能在类上使用

#### 其他修饰符

这些修饰符不是访问修饰符。

**abstract**

这种类可以包含任何正常类的成员（属性和方法），但这种类**不能被实例化**（不能使用 `new` 关键字创建该类型的对象）因此，它一般是用来做父类的，定义了一种 **类的规范**

**final**

被声明为 final 的类型不能被继承，也就是不能作为新类型的父类。

> abstract 和 final 相互冲突：一个必须作为父类，一个不允许作为父类。

### 构造函数（Constructor）

构造函数是一个**方法**（或者说行为），用来帮助创建类的一个新实例。

构造函数会在 `new` 创建对象时被自动调用，也**只能**这样被调用。无法使用 类名.构造函数 这样的方法手动调用。

所有类必须**至少有一个构造函数**。

构造函数：

- 名称**必须和类的名称相同**。

- 不能有返回类型（void 型也不可以）

  ```java
  public class BankAccout{
      // 错误：不能指定构造函数的返回值类型，void 也不行。
      void public BankAccout(String name){
          this.name = name;
      }
      // 这样是正确的
      public BankAccout(String name){
          this.name = name; // 暂时不需要理解这行是啥
      }
  }
  ```

- 访问修饰符必须是 public

#### 默认构造函数（Default Constructor）

  当你没有为一个类定义任何构造函数的时候，Java 会自动为它创建一个无参数的构造函数。

大概是这样：

你写的：

```java
public class BankAccout{
    
}
```

实际上这个类是这样的：

```java
public class BankAccout{
    public BankAccout(){
    }
}
```

当你定义了任何一个构造函数之后，Java 就不会再创建这个无参数构造函数了。不过，建议你主动定义一个默认构造函数（长得和上面一样的那种），这样在继承的时候比较舒服。

### 方法签名与重载

在 Java 和 C++ 里头（**C不可以**），可以定义多个相同名称但是不同参数/返回值的函数。对不同参数的调用，就可以自然的调用正确的函数。这种行为叫做**重载**（OverLoading）。

编译器如何区分这么多同名的函数呢？通过方法的**签名**：

签名包括：**函数的名称**，**参数的个数，类型和顺序**

```java
public BankAccout(double a, int b);
public BankAccout(int a, double b);
// 它们被视为签名不同。
```

所有函数的**签名必须不冲突**。签名中不包含**参数的名字**和函数**返回值的类型**。

**重载**

重载就是定义很多**名称相同，但签名不同**的函数，以便根据需要调用。重载需要满足以下条件：

- 在同一个作用域下

- 方法的名称需要相同

### 构造函数中的 this

this 可以理解为“当前实例”。可以在构造函数内 **通过 this** 发起对其他同一类中的构造函数的调用。比如：

```java
public BankAccout(String name){
    owner = name;
}
```

```java
public BankAccout(){
    // 调用了上方那个有参数的构造函数
    this("Test");
}
```

>  this 对应Python 中的 self，就是 Python 所有成员方法中的第一个参数
>
> ```python
> class BankAccout:
>     # 这段代码的作用和上面的第一个 Java 构造函数一样
>     def __init__(self, name):
>         # self 相当于 this
>         self.owner = name
> ```

使用 this 调用其他构造函数的时候，不会再创建新的对象，只是单纯的调用而已。

调用另一个构造函数，而不是直接把另一个构造函数的代码复制过来的好处是：可以防止代码重复。

```java
public BankAccout(String name){
    owner = name;
}
public BankAccout(){
    owner = "Test";
}
```

这样写的话目前来说没什么问题。但如果需要对账户的所有者，即 name 的值进行检查，你就需要在这两个函数里都检查一遍；不仅麻烦，如果你忘记了在一个函数中加入检查，可能会导致一些很惨烈的后果。

### 构造链

在类的继承中，子类需要调用父类的构造方法。在 Java 里，这是通过 super() 来完成的。

super([Argument list])

```java
public class BankAccout{
    public BankAccout(String name){
        // 调用父类的构造函数
        super();
        owner = name;
    }
}
```

- 构造函数的第一行必须调用 super() 或者 this()
- 如果你构造函数的第一行即不是 this()，也不是 super()，那么 Java 在编译时会强行加上一行 `super()` （即无参数的，对 super 的调用）

- super() 与 this() 不能在同一个构造函数中被调用

但是，有的类并没有继承其他类（比如上面提到过的 `BankAccout` ），那为什么还要必须调用 super() 呢？

在 Java 中，有一个非常牛的类，叫做 Object。所有的 Java 类，在没有继承任何类时，默认继承 Object 类。

（这种做法叫做「单根继承」）

> Python 中也有类似的做法：Python 中有一个叫 object 的类（连名字都一样…），所有没有继承任何类的类都是 object 的子类，即：
>
> ```python
> class Student:
>     ...
> ```
>
> 相当于：
>
> ```python
> class Student(object):
>     ...
> ```

因此，所有的 Java 类都是有父类的；没有继承其他类的类，它们的父类就是 Object。因此，你永远可以在一个类里调用 super()，因为一个 Java 的类总会有父类。

### 析构函数

Java 当中有着自动垃圾回收的机制，叫做 gc （Garbage Collection，大概），因此，Java 并没有所谓“堆上不用的对象要主动释放”的说法（不像 C艹 一样有 new 就必须有 delete）



## 类中的成员

### 数据域（Field）

对象的状态存储于「数据域」当中。每个对象都有自己的数据域（即不同对象的数据域（属性）不互通），每个对象属性的的**存储空间独立存在**

什么是「数据域」？在 Java 中，数据域就是 一个对象的属性 的集合。

```java
public class BankAccout{
    private String owner;
    private double balance = 0.0;
}
```

比如，在上面的这个类的定义中，数据域就是指 owner 和 balance 两个变量。

属性的定义一般包含三个部分：

- 访问修饰符（private）
- 数据类型（String）
- 变量名（owner）

数据域可以赋值一个初始值；如果没有初始值，它的值会是自己数据类型的默认值。

除非特殊需要，否则对象的属性应当使用访问修饰符 private ,以便实现面向对象思想中的封装。

如果需要修改一个属性，仍然最好不要公开该属性，而是写两个方法 `getxxx` 和 `setxxx`。（这个在 Java 下叫做 getter 和 setter，C++ 应该也是这么做的）

### 方法（Method）

方法是对象响应消息的方法（看起来有点绕），它决定了对象在收到消息时候的行为。

在 Java 中，方法就是类里头定义的一个函数。比如：

```java
public void debit(double amount){
}
```

一个方法必须包含四个部分：

- 访问修饰符（public）
- 返回值（void）
- 函数名称（debit)
- 函数的参数列表（double amount)

```java
BankAccout a1 = new BankAccout();
// 调用对象上的方法，即向对像发送消息
a1.withdraw(50);
```

#### 方法的调用

```java
public class Test{
    public void method1(){
        int a = 0;
        // 注意下面这行
        method2(a);
    }
    public void method2(int a){
        a += 1;
    }
}
```

在上边这个例子里，有两个方法：method1, method2。`method2(a);` 这行中，method1 **调用**了 method2。method1 被称为**主调方法**，method2 被称为**被调方法**。

调用一个方法中，执行参数的传递时，会出现两种情况：

- 被调方法参数为基本数据类型：

  只进行**值传递**。也就是说，主调方法中的实参和被调方法的形参赋值时，二者的地址不相同。

- 被调方法参数为引用数据类型：

  进行**引用传递**，也就是说，主调方法中的实参和被调方法的形参赋值时，二者的地址相同。

  更精确的说，在 Java 中，这两个变量在栈区那个存放对象4字节地址的4字节空间存放了相同的地址。

#### 方法的返回

在 Java 中，一个方法最多只能返回一个东西（一个基础数据类型的值或者一个引用数据类型的对象）。如果方法声明返回值为 void，则该方法不返回任何内容。

返回会把“控制权”交还给调用该方法的其他方法。

#### 方法的重载（Overload）

**不同签名**的方法即使在同一作用域下也可以同时存在。对于函数签名的概念，请向上翻。这种方法称为**重载**

如果有一个重载函数，编译器可以自动的根据用户调用函数所用的参数类型/个数，自动找到需要被调用的函数。

#### 方法的覆盖（Override）

在继承当中，如果子类中编写了一个和**父类某个方法签名一样**的方法，则子类中新的方法会**覆盖**旧的方法。

覆盖必须在**不同作用域**中出现。在继承中，子类和父类显然不在一个作用域下，所以是可以进行方法覆盖的。

**方法的重载和覆盖完全不同**：

重载：需要方法的签名不同，且在同一作用域下

覆盖：需要方法的签名完全一致，且在不同作用域下

## 修饰符

### static 与非 static

| static?   | 数据成员 | 成员方法 |
| --------- | -------- | -------- |
| static    | 静态成员 | 静态方法 |
| 非 static | 实例数据 | 实例方法 |

实例数据和实例方法只能使用 对象.数据成员 的方法来使用。这是因为不同实例当中，实例相同名字的数据实际的内容是不一样的。比如：

```java
public class Student{
    public int age;
    public String name;
    public Student(int age, String name){
        this.age = age;
        this.name = name;
    }
    public Student(){
    }
}

Student student1 = new Student(14, "Li");
Student student2 = new Student(15, "Cai");
student1.age; // 14
student2.age; // 15
// 相同的变量名在不同实例下内容不同
```

静态成员和静态方法既可以通过 对象.数据成员 调用，也可以通过 类名.数据成员 调用。

```java
public class Student{
    public static String school = "Xi'an Jiaotong University";
    public String name;
    public Student(String name){
        this.name = name;
    }
    public Student(){
    }
}

Student student1 = new Student("Li");
Student student2 = new Student("Cai");
student1.school; // Xi'an Jiaotong University
Student.school; // Xi'an Jiaotong University
student2.school; // Xi'an Jiaotong University
// 三种调用方法得到的结果完全一致
```

静态数据在内存中**只有一份拷贝**，存放于静态区，**不在堆区**。

成员数据有几个实例，在内存中就有几份拷贝，**在堆区**

静态数据可以被任意对象修改；这个修改会对所有对象生效（很简单，因为静态数据其实只有一份，改了的话大家的都会改）

### final

被 final 修饰的数据成员不能够被修改。因此，final 常常被用来修饰常量。

注：不能修改指的是，对于基础数据类型：确实不能改

对于引用数据类型：这个 final 在栈区的四字节指针的内容不能变；其指向的对象自身仍然可以通过调用其方法，修改其指向对象的属性。

一般来说，Java 中的常量最好用全大写命名，同时用 final 修饰。

被 final 修饰的类类型不能被继承。

### abstract

abstract 关键字可以用来定义抽象类。抽象类型不能被实例化，只能用来作为其他类的父类。

一般来说，定义抽象类是因为类中有一部分可以重用的内容无法「笼统地实现」。比如，三角形、四边形的父类「Shape」（形状）必须有一个 draw 方法，但你肯定写不出来画任何一个图形的方法，因此需要把该方法留空，称为**抽象方法**

抽象方法是种 空的方法。如果一个类里头有至少一个抽象方法，那他必定是一个抽象类。

## 包（Package）

功能相近（用途相似）的类打包在一起可以构成包。包是用来管理很多类的东西。

包名一般来说，建议全部小写

如果一个类型被放到了一个包里，它会获得另一个名字：类型全称，包含类自己的名字和包的名字。一般组成方法是 包的名称.类的名称。不同的包中可以包含相同类名的类，但类型全程不能相同（即包名和类名不能都相同）

一个包里的类在使用另一个包中的另一个类的时候，可以直接使用另一个类的**类型全称**，或者使用 import 语句

一个包的类在使用同包下的类时，可以直接使用类名，不需要类型全称。

包中的 `.` 是分隔符，每个 `.` 对应了一个物理意义上的目录。一般来讲，包名是目录的逆序：即包名的每一级都从大范围到小范围。

```
cn.xjtu.se
- cn
- - xjtu
- - - se
```

表示cn下面有一个xjtu文件夹，再下面有se子文件夹。通过这个物理嵌套方式可以看出，xjtu 属于 cn，而 se （软件学院）属于 xjtu。

注意：子包不被视为父包下的一部分。比如，xjtu.se.A 不算 xjtu 包下的一个类；而是算 xjtu.se 包下的一个类。

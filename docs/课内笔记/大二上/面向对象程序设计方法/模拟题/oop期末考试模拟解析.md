# 面向对象程序设计方法 模拟题 解析

## 判断题（5分 5题）

1. `package` 语句能多次使用。

> **错！** 一个Java源文件只能包含一个package语句，但可以包含多个import语句，多个import语句用于导入多个包层次下的类

2. 静态成员不因为实例的不存在而存在。

> **错！** 静态成员（也称为静态变量或静态方法）与类本身相关联，而不是与类的实例相关联。因此，静态成员不依赖于类的实例的存在，它们在类被加载时就被初始化，并且只有一份副本

3. 抽象类不能拥有构造方法。

> **错！** 抽象类可拥有构造方法。关于抽象类的更多细节可见 [cs61b-Abstract-classes](https://joshhug.gitbooks.io/hug61b/content/chap4/chap44.html)，[CSDN-abstract class和interface有什么区别?-](https://blog.csdn.net/weixin_44422604/article/details/107184591)

4. 类只能能有一个继承，接口可以有多个继承。

> 这题有歧义，有多种理解方法：
> - 一个类只能 `extends` 一个其他类，一个接口可以 `extends` 多个其它接口
> - 一个类只能被一个其它类 `extends`，一个接口可以被多个类 `implements`
> 
> 为了防止歧义，我们将解释每句话：
> - 一个类只能 `extends` 一个其他类：**对！**，在 Java 中，类的继承是单一继承，也就是说，一个子类只能拥有一个父类
> - 一个接口可以 `extends` 多个其它接口：**对！**，在 Java 中，一个接口可以继承多个接口，这被称为接口的多重继承。通过使用接口的继承，可以将多个接口中定义的方法合并到一个接口中，以便类只需要实现一个接口而获得多个接口的特性
> - 一个类只能被一个其它类 `extends`：**错！**，可以有很多类 `extends` 一个类，只要子类和父类是 `is-a` 关系即可
> - 一个接口可以被多个类 `implements`：**对！**，Java 中可以实现多个类，它们共享相同的接口行为
> - 一个类只能`implements`一个接口：**错！**，一个类可以实现多个接口

5. `try` 语句必须后跟 `catch` 语句，`finally` 语句可有可无。

> **错！** `try` 语句后必须跟 `catch` 和 `finally` 其一，或者两者都有。更多关于异常处理的内容见第 8 道选择题

## 选择题（15分10题）

答案：A D B B AD AB BD B

1. `char`：单一的 16 位 Unicode 字符，无符号。范围是 `\u0000`（十进制等效值为 0） ~ `\uffff`（即为 65535 = 2^16 - 1）
   
   更多基本数据类型可见 [菜鸟教程-Java 基本数据类型](https://www.runoob.com/java/java-basic-datatypes.html)

2. 逐行分析：
   1. 第一行执行完后：`a --> "-"` 
   2. 第二行执行：
      1. `a.append("-")` 将 `a` 指向 `"--"`
      2. `a.append("-")` 返回 `a` 的地址（引用），赋值给 `b`。此时 `b --> "--"`
   3. 第三行判断 `a == b`
      1. 任何的 `==` 均判断两个变量的 **值**。这里两个变量装的都是同一个地址，所以为 `true`
      2. 另外，不是所有 `.equals()` 都比较两个对象的 “内容”，这取决于这个类是否 `override` 的最原始的写在类 `Object` 里的 `equals` 方法。`Object` 里的 `equals` 方法实际上就是使用 `==`。比如：
         1. `String` 类覆写了 `equals`，两个 `String` 用该方法比较的就是字符串内容
         2. `StringBuilder` 类，`StringBuffer` 类没有覆写 `equals`，他们之间用该方法比较的就是引用

   综上，第二题选 D 

3. 考察运算符优先级，详见 [菜鸟教程-Java 运算符](https://www.runoob.com/java/java-operators.html)

4. 先只说本题：显然选 B，`default` 放到哪里都不影响。但是说到本题还是有比较多槽点：
   1. `->{}` 形式的 `case` 语句不用人为的加 `break`，去掉所有 `break` 不影响结果
   2. 一般我们都把 `default` 放最后
   3. 若用 `case X:` 形式的 `case` 语句，也不影响结果，无论 `default` 放哪
   4. 但是！！若用 `case X:` 形式的 `case` 语句，`break` 就不能随便不加了，详细可见 [菜鸟教程-Java switch case 语句](https://www.runoob.com/java/java-switch-case.html)
   5. `->{}` 形式的 `case` 语句 和 `case X:` 形式的 `case` 语句 **不能混用**，否则编译不通过

5. 出现了 3 次重载

   函数代码流示意图：
    
   ![](https://telegraph-image-5ms.pages.dev/file/59e81aac7fb50031828f1.jpg)

6. A, B 都不用多说，肯定是可以编译通过的

   C 选项中若把  `Supertest` 改为 `supertest`，则可以正常编译通过，此时 `b` 的静态类型为 `supertest`，动态类型为 `test`。方法选择根据动态类型，此时 `b.paint()` 输出 `wuxidixi`

   D 选项不能这么干，编译器只知道 子类 is a 父类，所以子类的可以装到父类里（哪怕有损失数据）。他不能把 父类 装到 子类 里面。

   E，F 选项中都没有 `new`，哪怕加了 `new`，改好了大小写，都无法将 `superclass` 强制转换成 `test`

关于类型转换（Casting），可见 [java-type-casting](https://www.baeldung.com/java-type-casting)，[cs61b-extend-casting-HOF](https://joshhug.gitbooks.io/hug61b/content/chap4/chap42.html)

7. **注意方法重载跟返回值类型和修饰符无关，Java的重载是发生在本类中的，重载的条件是在本类中有多个方法名相同，但参数列表不同（可能是参数个数不同，参数类型不同），跟返回值无关。**

   由上可知，B D 是重載。A C 参数表没变，无法通过编译

8. 易知选 B

   关于 Java 异常可见 [菜鸟教程-Java 异常处理](https://www.runoob.com/java/java-exceptions.html)，[异常处理：抓抛模型](https://www.cnblogs.com/niujifei/p/14293299.html)，[cs61b-Checked-vs-Unchecked-Exceptions](https://joshhug.gitbooks.io/hug61b/content/chap6/chap66.html)

## 填空题（5题5分）

1. 面向对象的三大特征是：封装（Encapsulation），继承（Inheritance），多态（Polymorphism）
2. 对象与对象之间的互动是通过 消息传递（Message Passing） 机制实现的
3. `final` 修饰变量的功能是 变量的值一经初始化后不能再更改，修饰成员方法的功能是 防止方法被子类重写（覆盖），修饰类的功能是 防止类被继承。

### 综合题（8题55分，有名词解释，简答，读程序写结果等）

1. 关于 JVM，JRE，JDK 详见 [differences-jdk-jre-jvm](https://www.geeksforgeeks.org/differences-jdk-jre-jvm/)，[jdk-jre-jvm-区别](https://www.wdbyte.com/java/jdk-jre-jvm/)
2. - 方法重载(Overloading)：如果有两个方法的方法名相同，但参数不一致，哪么可以说一个方法是另一个方法的重载。
   - 方法覆盖（Overriding）：如果在子类中定义一个方法，其名称、返回类型及参数签名正好与父类中某个方法的名称、返回类型及参数签名相匹配，那么可以说，子类的方法覆盖了父类的方法。
3. 关于 方法签名（Method Signature）详见 [java-method-signature-return-type](https://www.baeldung.com/java-method-signature-return-type)
4. 1. 定义：
      1. 类成员：在Java中，类成员是使用 `static` 关键字声明的成员，包括静态字段和静态方法。这些成员与类本身相关，而不是与类的实例相关。
      2. 实例成员：实例成员是在类中声明的非静态字段和方法，它们与类的实例相关联。
   2. 初始化：
      1. 类成员：类成员可以在类加载时初始化，通常在类的静态初始化块中或直接在类的定义中进行初始化。
      2. 实例成员：实例成员通常在类的构造函数中初始化，当创建类的实例时，会为每个实例创建一个新的实例成员副本。
   3. 使用：
      1. 类成员：类成员可以通过类名直接访问，而无需创建类的实例。它们适用于表示与整个类相关的信息，如共享数据或类方法。例如，`ClassName.staticMember`。
      2. 实例成员：实例成员需要通过类的实例来访问。它们通常用于表示每个对象特有的属性和方法。例如，`objectName.instanceMember`，其中 `objectName` 是类的实例。
5. 在Java中，异常（`Exception`）是一种表示程序运行时发生问题或错误的机制。异常用于处理各种问题，包括但不限于以下情况：
   - 运行时错误，如除零错误（`ArithmeticException`）。
   - 文件不存在或无法访问（`FileNotFoundException、IOException`）。
   - 空指针引用（`NullPointerException`）。
   - 数组越界（`ArrayIndexOutOfBoundsException`）。
   - 类型转换错误（`ClassCastException`）。
   - 用户输入无效数据，如格式错误（`NumberFormatException`）。
   
   异常提供了一种结构化的方式来处理这些问题，以防止程序崩溃或产生不可控制的结果。在Java中，异常被表示为类的对象，它们属于异常类的层次结构。最顶层的异常类是 `java.lang.Throwable`，它有两个主要子类：`java.lang.Exception`（表示可捕获的异常）和 `java.lang.Error`（表示不可恢复的错误）

   异常（`Exception`）又分为非运行时异常 和 运行时异常。
   - 运行时异常：RuntimeException 类或它的子类，这些类的异常特点是：即使没有使用 try 和 catch 捕获，Java 自己也能捕获，并且编译通过，（但运行时会发生异常使得程序运行终止）
   - 非运行时异常：必须捕获，否则编译错误，也就是说，必须处理编译时异常，将异常进行捕捉，转化为运行时异常等
   
   1. `throws` 是一个关键字，用于在方法声明中指定可能会抛出的异常。当一个方法可能会抛出非运行时异常时，它必须在方法头部使用 `throws` 关键字声明这些异常。这告诉调用者该方法可能引发指定类型的异常。调用该方法的代码必须要么处理这些异常，要么将它们继续抛给上层调用者。
   2. `throw` 是一个关键字，用于在程序中显式引发异常。当程序检测到某种问题时，可以使用throw关键字来创建并抛出一个异常对象。这个异常对象必须是 `Throwable` 的子类（通常是 `Exception` 的子类），并且它会被传递给调用栈，直到找到相应的异常处理代码。
6. 对象 `"Zhang"` 和 `new String("Zhang")` 地址不一样，但是 `"Zhang"` 和 `"Zhang"` 地址相同
   ![](https://telegraph-image-5ms.pages.dev/file/5bf5f014413479b823202.png)
7. - [ ] TODO
8. **子类父类可以用同名的字段，两个分开，对哪个操作取决于调用哪个类中的方法**
   
   **可用 `实例名.classVariable` 访问这个实例的静态类型中的类变量，但是这样不推荐**
   1. `Test.main` 结果：（注意上面几句话和动态方法选择即可）
      ```shell
      in int Base 11
      in float Base 10.0
      in float SubBase 0.0
      in float Base 5.0
      in int Base 21
      in float Base 12.0
      i = 21 f = 5.0
      i = 5 f = 0.0
      ```
   2. 删去有 `// ------------(*)` 注释的一行后无法成功编译，因为这样会导致 `SubBase` 构造器在第一行自动调用 `super()`，而 `Base` 没有无参构造器
   3. 把类 `SubBase` 和 `Base` 放到不同的包里，不能编译成功。
      
      如果加上 `import` 或者用全名表示，如 `foo.Base` 和 `bar.SubBase` 也无法编译通过，因为 `Test` 类无法访问 `protected` 变量
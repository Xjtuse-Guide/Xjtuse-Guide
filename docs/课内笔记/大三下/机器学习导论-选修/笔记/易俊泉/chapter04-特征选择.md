[TOC]

# 第四课——特征选择

![image-20220323212719038](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871116.png)

### 特征选择动机

维数灾难：**当维数增大时，空间数据会变得更稀疏，这将导致bias和variance的增加，最后影响模型的预测效果。**

对当前学习任务有用的特征称为“相关特征”：所以从众多特征中选择有用的一些特征来进行学习

过拟合：当样本数目小于特征维数时，容易造成过拟合。通过特征选择，可使模型泛化性能好、计算高效、鲁棒可解释

### 特征选择方法概述

:one: 任务无关方法（过滤式方法）：先过滤再训练模型

![image-20220323153224504](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871117.png)

:two: 任务相关方法（包裹式方法）：从众多特征中选取子集，然后使用模型评估特征子集

![image-20220323153420531](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871118.png)

:three: 自动化方法（嵌入式方法）：选择与学习融为一体，模型中暗含了子集选择

![image-20220323153610725](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871120.png)

### 过滤式选择（Filter method）

计算代价通常很低，计算速度较快

是特征选择的general框架，与学习器无关（learner-agnostic）

是一个预处理步骤

![image-20220323155021834](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871122.png)

#### 单变量过滤

**单变量**（Univariate）过滤方法：**Signal-to-noise ratio （S2N）**

一个**“好”**的特征：需要有明显的划分度——均值之间有明显的gap

![image-20220323153849565](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871123.png)
$$
S2N=\frac{|\mu^+-\mu^-|}{\sigma^++\sigma^-}
$$
**单变量过滤方法一些情况下可能失效**：需要综合多个特征

![image-20220323154238320](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871125.png)

#### 多变量过滤

**多变量**（ Multivariate ）过滤方法：Relief

> 给定训练集$\{(x_1,y_1),...,(x_n,y_n)\}$
>
> :one: 对每个样本xi，在同类样本中赵最近邻$x_{i,hit}$；在异类样本中寻找最近邻$x_{i,miss}$
>
> :two: 计算对应于属性j的统计量
> $$
> \delta^j = \sum_i-diff(x_i^j,x^j_{i,hit})^2+diff(x_i^j,x^j_{i,miss})^2
> $$
> :three: 若$\delta^j$大于阈值$\tau$，选择属性j；或者指定一个k值，选择统计量最大的前k 个特征
>
> 距离是结合多维的特征
>
> ![image-20220323154929587](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871127.png)

### 包裹式选择（Wrapper method）

Wrapper  methods：使用学习器的性能作为评价准则

特征选择结果因学习器不同而不同，选择的特征子集是为学习器“量身定做”

从学习器性能来看，包裹式特征选择方法比过滤式方法好；但是特征选择过程中需多次训练学习器，因此**计算开销大**。

两个关键问题：

> :a:  Search 搜索特征子集的方法;
>
> :b:  Assessment 评估特征子集优劣的方法
>

寻找最优特征子集是一个NP难问题

:one: 使用启发式方法寻找近似候选最优子集

> - 前向选择（Forward Selection）：从空集开始，每次**增加一个最优**特征
>
>   ![image-20220323155931127](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871130.png)
>
>   算法复杂度：$p+(p-1)+...+1=\frac{p(p+1)}{2}$ ， 𝑝 为属性的个数
>
> - 后向消除(Backward Elimination)：从全集开始，每次**去掉一个最差**特征
>
>   ![image-20220323160056186](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871133.png)
>
>   算法复杂度：$p+(p-1)+...+1=\frac{p(p+1)}{2}$ ， 𝑝 为属性的个数

:two: 使用验证集或交叉验证方法选择最优子集。

> 1. 将数据划分成训练、验证和测试三部分
> 2. 对每一个特征子集，使用训练集训练模型
> 3. 挑选在验证集上表现最好的特征子集
> 4. 在测试集上进行测试

### :apple: 嵌入式选择（Embedded method）:apple: 

#### 正则化

在训练过程中隐式进行特征选择，模型只训练一次

只对权重正则化，不对偏置正则化

最常见的嵌入式方法：L1-正则化，  L2-正则化，以及L1和L2 混合正则化

> :one: L1-正则化
>
> ![image-20220323160758429](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871140.png)
>
> :two: L2-正则化
>
> ![image-20220323160805774](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871142.png)
>
> :three: L1-L2混合正则化
>
> ![image-20220323160812011](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871144.png)

#### 线性回归模型说明

给定训练数据集$\{(x_1,y_1),..,(x_n,y_n)\}$，并假设$\sum^n_{i=1}x_i=0$（做了中心化处理），考虑最简单的线性回归模型

> 中心化：$\overline{x}=\frac{1}{n}\sum^n_{i=1}x_i\qquad x_i'=x_i-\overline{x}$

![image-20220323161244515](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871146.png)

其中$\pmb\beta 为权重向量，\beta_0为偏置向量$

![image-20220323174420570](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871148.png)

当使用正规方程求解时，得到

![image-20220323161751063](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871151.png)

证明如下：
$$
\begin{flalign}
&设C=\sum_{i=1}^n(y_i-\beta^Tx_i)^2-2\beta_0\sum_{i=1}^n(y_i-\beta^Tx_i)+n\beta_0^2&&\\
&则\frac{\partial C}{\partial \beta_0}=-2\sum^n_{i=1}y_i+2\pmb{\beta}\sum_{i=1}^nx_i+2n\beta_0=0\\
&由于x_i已经中心化处理过，所以\beta_0=\frac{1}{n}\sum_{i=1}^ny_i\\
&由于\pmb{X}=\begin{bmatrix}
\pmb x_1^T\\...\\
\pmb x_n^T
\end{bmatrix}\\
&\frac{\partial C}{\partial \pmb{\beta}}=\frac{\partial ||y-\pmb X\pmb \beta||^2}{\partial \pmb{\beta}}\\
&用之前求解正规方程的方法即可得到解
\end{flalign}
$$


当$n\ll p$时，很容易导致解病态、陷入过拟合

为了缓解过拟合，为误差函数增加惩罚项

![image-20220323164602681](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871152.png)

##### <mark>L2正则化——岭回归</mark>

当q=2时，即使用L2范数正则化（称为ridge regression，岭回归）
$$
C=||X\pmb \beta -y||^2+\lambda||\pmb \beta||^2
$$
（正规方程法）解为
$$
\pmb{\beta}=(\pmb X^T\pmb X+\lambda \pmb I)^{-1}\pmb X^Ty
$$

> $$
> \begin{flalign}
> &C=|| X\beta -y||^2+\lambda||\pmb \beta||^2\\
> &\quad=(X\beta -y)^T(X\beta -y)+\lambda\beta^T\beta\\
> &\quad=(\beta^TX^T-y^T)(X\beta -y)+\lambda\beta^T\beta\\
> &\quad=\beta^TX^T X\beta-y^TX\beta -\beta^T X^Ty+y^Ty+\lambda\beta^T\beta\\
> &利用矩阵求导公式\\
> &\frac{\partial x^TBx}{\partial x}=(B+B^T)x\\
> &\frac{\partial x^Ta}{\partial x}=\frac{\partial a^Tx}{\partial x}=a\\
> &可得到\frac{\partial C}{\partial\beta}=2X^TX\beta-2X^Ty+2\lambda\beta=0\\
> &可得到\beta=(X^TX+\lambda I)^{-1}X^Ty
> \end{flalign}
> $$
>

岭回归等价于

![image-20220323164822746](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871155.png)

上式更加明显的表示出了𝜷的约束条件。可以证明 𝑡  和𝜆  之间 存在一一对应关系

直观对比线性回归和岭回归，可以看到<mark>参数进行了缩减</mark>

> 这样能使噪声Δx对实际的β影响较小
> $$
> \beta(x+\Delta x)=\beta x+\beta\Delta x
> $$
> 

![image-20220323203625787](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871158.png)

q 取不同值时，正则化项的等值线

![image-20220323204213598](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871162.png)

##### L1正则化——Lasso回归

L1- 正则化（Least Absolute  Shrinkage and  Selection  Operator, Lasso回归）

![image-20220323204333074](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/qshell/image-20220323204333074.png)

与其等价的拉格朗日表达形式

![image-20220323204404123](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/qshell/image-20220323204404123.png)

L1约束使得解关于 𝒚  非线性，而且不能像岭回归那样可以得到封闭解。\

Lasso回归:

以一个特例进行说明

<img src="https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/qshell/image-20220323210833285.png" alt="image-20220323210833285" style="zoom:80%;float:left" />

<img src="https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/qshell/image-20220323210953272.png" alt="image-20220323210953272" style="zoom:80%;float:left" />

> 比如，如果原本线性回归的$\beta_j=\frac{\lambda}{4}$，则利用L1正则化使$\beta_j=0$
>
> 比如，如果原本线性回归的$\beta_j=\lambda$，则利用L1正则化使$\beta_j=\frac{\lambda}{2}$
>
> 比如，如果原本线性回归的$\beta_j=-\lambda$，则利用L1正则化使$\beta_j=-\frac{\lambda}{2}$
>
> 向中间的0靠拢
>
> 这样能使权重矩阵中在$(-\frac{\lambda}{2},\frac{\lambda}{2})$的$\beta$置为0，从而达到<mark>特征选择的作用</mark>
>
> 以上说明，L1正则化模型是一种嵌入式特征选择方法，将学习器和特征选择融为一体

#### 总结

𝑳𝒒正则化是实现嵌入式特征选择的常用方法

<img src="https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/qshell/image-20220323212527957.png" alt="image-20220323212527957" style="zoom:67%;" />

对于一般的学习任务，不希望权重过大

> 如果权重过大，导致微小的特征变化引起较大的预测变化
>
>  倾向于零权重，从而消除与任务无关的特征



### 参考资料

[1]庞善民.西安交通大学机器学习导论2022春PPT

[2]周志华.机器学习.北京:清华大学出版社,2016

[3\][怎样理解 Curse of Dimensionality（维数灾难）?](https://www.zhihu.com/question/27836140)


[TOC]

# 第六课——贝叶斯分类器

![image-20220324114543495](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871392.png)

## 一、知识准备

### 贝叶斯公式

针对两个随机变量，联合概率分布具有两种分解形式
$$
P(x,y)=P(x|y)P(y)=P(y|x)P(x)
$$
因此，利用上式得到贝叶斯公式

$$
P(c|x)=\frac{P(x|c)P(c)}{P(x)}
$$

通过贝叶斯公式得到贝叶斯决策理论基本思想：

1️⃣ 已知**类条件概率**密度参数表达式$P(x|c)$和**先验概率**$P(c)$

2️⃣ 利用贝叶斯公式转换成**后验概率**

3️⃣ 根据后验概率大小进行决策分类

> **先验概率（prior probability）：**指根据以往经验和分析。在实验或采样前就可以得到的概率。
>
> **后验概率（posterior probability）：**指某件事已经发生，想要计算这件事发生的原因是由某个因素引起的概率。
>
> **类条件概率密度**是，假定x是一个连续随机变量，其分布取决于类别状态，表示成p(x|ω)的形式，这就是“类条件概率密度”函数，即**类别状态为ω时的x的**[概率密度函数](https://baike.baidu.com/item/概率密度函数/5021996)（有时也称为状态条件概率密度）。

### 贝叶斯决策基础

贝叶斯分类决策利用概率对数据进行建模，从而基于**贝叶斯定理**给出分类预测的不确定性

将特征向量$x=(x_1,...,x_p)^T$类别标签𝑐𝑗作为**随机变量**

给定样本𝒙,基于条件（后验）概率$P(c_i|x)$计算将样本𝒙分类为𝑐𝑖所产生的期望损失
$$
R(c_i|\pmb x= \sum_{j=1}^L\lambda_{ij}P(c_j|\pmb x)
$$
其中,$\lambda_{ij}$是将一个真实标记为$c_j$的样本误分类为$c_i$所产生的损失

贝叶斯判定准则要求 <mark>期望损失达到最小 </mark>。
$$
h^*(x)=\text{argmin}\ R(c|x)
$$
称$h^*(x)$为贝叶斯最优分类器

进一步，若目标是最小化分类错误率，则

![image-20220321171559820](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871394.png)

期望损失可以写成
$$
R(c_i|x)=P(c_1|x)+...+P(c_{i-1}|x)+P(c_{i+1}|x)+...+P(c_{L}|x)=1-P(c_i|x)
$$
于是，对每个样本，选择使**后验概率最大的类别标记**
$$
c_{MAP}=\underset{c_j\in C}{\text{argmax}}\ P(c_j|x_1,x_2,...,x_p)
$$

## 二、MAP分类准则

估计后验概率𝑃(𝑐|𝑥)的方法主要有两种策略：

1️⃣ **判别式模型**：通过对𝑃(𝑐|𝑥)直接建模预测
![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871395.png)

逻辑回归：
$$
P(c|x;\theta)=(f_\theta(x))^c(1-f_\theta(x))^{1-c}\\
c\in{0,1}\ f_{\theta}(x)=\frac{1}{1+e^{-\theta^Tx}}
$$
**直接对条件概率建模，不关心背后的数据分布**$P(x,c)$

2️⃣ **生成式模型**：使用贝叶斯推理预测，即假定类条件概率具有某种确定的概率分布

![image-20220321171808451](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871396.png)

先对联合概率分布𝑃(𝑥,𝑐)建模，再通过贝叶斯公式计算后验概率𝑃(𝑐|𝑥)

![image-20220420162438848](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871397.png)

先对联合概率分布 𝑃(𝑥, 𝑐) 建模，再通过贝叶斯公式计算后验概率 𝑃( 𝑐| 𝑥)

GANs：适用于娱乐行业

## 三、贝叶斯分类算法

### 一般生成式贝叶斯分类器

#### 公式说明

基于贝叶斯公式估计后验概率：

![image-20220321172252379](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871398.png)

使用最大后验概率准则给出类标签

![image-20220321172306382](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871399.png)

#### 举例说明

例子：今天我们可以打网球吗？

训练示例集如下

![image-20220420164325967](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871401.png)

如果给一个新样本：X = (天气  = 晴, 气温  = 冷, 湿度  = 高, 风  = 有)，想知道是否可以打网球？

依据大数定律，利用样本出现频率估计先验概率

> 在试验不变的条件下，重复试验多次，随机事件的频率近似于它的概率。偶然中包含着某种必然。

![image-20220420164601250](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871402.png)

其次，估计类条件概率

![image-20220420164825761](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871403.png)

根据样本出现频率估计条件概率。但由于样本数远小于随机向量的可能取值数目，估计值通常不可靠

> 例如：$P(多云，热，高，无|Yes)=\frac{1}{9}\qquad P(多云，热，高，无|Yes)=\frac{0}{5}$
>
> <mark>未观测到≠出现概率为0</mark>

**训练过程**

**获得先验概率**
$$
P(X=Yes)=\frac{9}{14}\qquad P(C=No)=\frac{5}{14}
$$
**得到类条件概率表**

![image-20220420165625019](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871404.png)

**测试阶段**

给定测试样本：X = (天气 = 晴, 气温 = 冷, 湿度 = 高, 风 = 有)， 通过查找条件概率表，可以得到
$$
P(X|Yes)P(C=Yes)=\frac{0}{9}\times =\frac{9}{14}=0\\
P(X|No)P(C=No)=\frac{0}{5}\times =\frac{5}{14}=0\\
$$
由此，基于贝叶斯公式:
$$
P(Yes|X)=0\qquad P(No|X)=0
$$
<mark>打和不打都是0，效果不好！</mark>

### 朴素贝叶斯分类器

#### 公式说明

朴素贝叶斯分类：对已知类别，**假设所有属性相互独立**（属性条件独立性假设）

![image-20220321173421760](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871406.png)

因此朴素贝叶斯的分类公式为：

![image-20220321173455253](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871407.png)

在训练时，朴素贝叶斯为每个属性估计条件概率$P(x_i|c_j)$

假设样本的𝑝个属性都有𝑑种可能取值，则共需要估计𝑑𝑝个条件概率

> 朴素贝叶斯的朴素体现在其对各个条件的独立性假设上，加上独立假设后，大大减少了参数的假设空间：从$d^p$降到了𝑑𝑝。

#### 举例说明

例子：今天我们可以打网球吗？

训练示例集如下

![image-20220420164325967](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871401.png)

如果给一个新样本：X = (天气  = 晴, 气温  = 冷, 湿度  = 高, 风  = 有)，想知道是否可以打网球？

**需要估计**

> 先验$P(C=c_j)$
>
> 每个属性的条件概率$P(x_i|c_j)$

使用样本出现的概率
$$
\hat{P}(c_j)=\frac{N(C=c_j)}{N}\\
\hat{P}(x_i|c_j)=\frac{N(X_i=x_i,C=c_j)}{N(C=c_j)}
$$
对于打网球问题，有

先验概率：
$$
P(C=Yes)=9/14\qquad P(C=No)=5/14
$$
条件概率$P(X_i|C_j)$

![image-20220420203005417](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871412.png)

测试步骤

> :one: 给定新样本：X = (天气 = 晴, 气温 = 冷, 湿度 = 高, 风 = 有)
>
> :two: 查先验和条件概率表
> $$
> P(C=Yes)=9/14\qquad P(C=No)=5/14
> $$
> ![image-20220420203149604](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871414.png)
>
> :three: 计算后验概率
>
> ![image-20220420203315992](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871415.png)
>
> :four: 因为P(Yes|x)<P(No|x)，根据MAP准则，预测为"不打网球"

#### 避免0概率问题

若某个属性值在训练集中没有与某个类同时出现过，则基于频率的概率估计将为零

不合理：仅仅因为事件之前没有发生过，并不意味着它不会发生，为避免这一情况，**需要对概率值进行平滑**

解决方案：**使用拉普拉斯校正**
$$
\hat{P}(c_j)=\frac{N(C=c_j)+1}{N+|C|}\\
\hat{P}(x_i|c_j)=\frac{N(X_i=x_i,C=c_j)+1}{N(C=c_j)+|X_i|}\\
|C|\rightarrow 类的个数\qquad |X_i|\rightarrow 属性的取值数目
$$
例如：

![image-20220420203712736](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871416.png)
$$
P(X_1=多云|C=No)=\frac{0+1}{5+3}=\frac{1}{8}
$$
避免了因训练样本不足而导致的概率估值为0的问题。

### 高斯朴素贝叶斯分类器

#### 高斯分布

一维的高斯概率密度函数

$$
N(x|\mu,\sigma^2) = \frac{1}{(2\pi\sigma^2)^{1/2}}exp\{-\frac{1}{2\sigma^2}(x-\mu)^2\}
$$

多维的高斯概率密度函数

$$
N(\pmb{x}|\pmb{\mu},\pmb{\Sigma})=\frac{1}{(2\pi)^{p/2}}\frac{1}{|\pmb\Sigma|^{1/2}}exp\{-\frac{1}{2}(\pmb x-\pmb\mu)^T\pmb\Sigma^{-1}(\pmb x-\pmb\mu)\}
$$

Σ是协方差矩阵


#### 高斯分布参数估计

一维 Gaussian 情况下：均值和方差的极大似然估计值分别是样本的均值及样本的方差
$$
\mu=\frac{1}{n}\sum_{i=1}^n x_i\qquad \sigma^2=\frac{1}{n}\sum_{i=1}^n(x_i-\mu)^2(有偏估计，无偏估计是\frac{1}{n+1})
$$
多维  Gaussian 情况下，均值和协方差矩阵的估计值分别为

$$
\mu=\frac{1}{n}\sum_{i=1}^n x_i\qquad \Sigma^2=\frac{1}{n}\sum_{i=1}^n(x_i-\mu)(x_i-\mu)^T\\
\Sigma 是一个p\times p的矩阵
$$

#### 高斯贝叶斯分类器

$$
\underset{C}{\text{argmax}}P(C|X)=\underset{C}{\text{argmax}}P(X,C)=\underset{C}{\text{argmax}}P(X|C)P(C)
$$

假设**类条件概率服从高斯分布**

$$
P(X_1,X_2,...,X_P|C)=N(\pmb{x}|\pmb{\mu},\pmb{\Sigma})=\frac{1}{(2\pi)^{p/2}}\frac{1}{|\pmb\Sigma|^{1/2}}exp\{-\frac{1}{2}(\pmb x-\pmb\mu)^T\pmb\Sigma^{-1}(\pmb x-\pmb\mu)\}
$$

#### 高斯朴素贝叶斯分类器
![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871417.png)


朴素贝叶斯假设

$$
P(X_1,X_2,...,X_P|C)=P(X_1|C)P(X_2|C)...P(X_P|C)
$$

针对密度，利用一维高斯分布，估计一下好瓜和坏瓜的高斯分布

针对含糖量，利用一维高斯分布，估计一下好瓜和坏瓜的高斯分布
![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871419.png)


<mark>**训练过程** </mark>

1️⃣ 训练阶段

对于$X=(x_1,x_2,...,x_p)_{1:N}，C=\{c_1,c_2,...,c_L\}$，估计先验：$P(C=c_j)$，以及$p\times L$个条件正态分布
![在这里插入图片描述](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871420.png)

其中使用极大似然估计参数、

$$
\mu_{ij}=\frac{1}{N(C=c_j)}\sum_{x_i\in c_j}x_i\quad \sigma_{ij}^2=\frac{1}{N(C=c_j)}\sum_{x_i\in c_j}(x_i-\mu_{ij})^2
$$
2️⃣ 测试阶段

对于于新样本$X'=(x_1',x_2',...,x_p')$使用所有的正态分布计算类条件概率密度，基于MAP 准则进行分类
$$
\underset{c_j\in C}{\text{argmax}}\prod_{i=1}^p P(x_i'|c_j)P(c_j)
$$

#### 使用朴素高斯的必要性

使需要估计的参数量减少：$O(p^2)\rightarrow O(p)$

**非朴素**：

$$
P(X_1,X_2,...,X_P|C)=N(\pmb{x}|\pmb{\mu},\pmb{\Sigma})=\frac{1}{(2\pi)^{p/2}}\frac{1}{|\pmb\Sigma|^{1/2}}exp\{-\frac{1}{2}(\pmb x-\pmb\mu)^T\pmb\Sigma^{-1}(\pmb x-\pmb\mu)\}
$$

共有 $L×(p+p× (p+1)/2)$个参数

**朴素**

每一类的协方差矩阵都是对角阵，共有L× (p+p)个参数

#### 高斯贝叶斯决策面

> 如果输入的数据是一个$\pmb L$维空间特征，考虑一个$\pmb M$分类问题，那么分类器将会把这个$\pmb L$维空间的特征点分为i个区域$\pmb M$。每个区域显然就属于一个类别，如果输入一个点$\pmb x$落在第$\pmb i$个区域，那么$\pmb x$就属于第$\pmb i$类。分割成这些区域的边界就称为**决策面**。

基于MAP准则进行分类

![image-20220324110035600](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871422.png)

$\pi _k$为第k类的先验概率

决策边界对应后验概率临界值（指数形式用log比较简单）
$$
P(c_k|x)=P(c_l|x)\Rightarrow \log P(c_k|x)-\log P(c_l|x)=0\\
\log \frac{P(C_k|X)}{P(C_l|X)}=\log (\frac{P(X|C_k)}{P(X|C_l)}\frac{P(C_k)}{P(C_l)})=\log \frac{P(X|C_k)}{P(X|C_l)}+\log \frac{P(C_k)}{P(C_l)}\\
其中：\log P(x|c_k)=\frac{1}{2}(x-\mu_k)^T\Sigma_k^{-1}(x-\mu_k)-\log |\Sigma_k|^{\frac{1}{2}}
$$
因此

![image-20220420212512425](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871423.png)

决策边界二次：  Quadratic Discriminant Analysis, QDA

特殊情况：每类的协方差矩阵均相同,不同类的高斯分布可以通过互相平移得到

![image-20220324111926987](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871425.png)

上式简化成

![image-20220420213301363](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871426.png)

决策边界：$x^Ta+b=0\Rightarrow 线性决策$

#### LDA——会考

通过假设每一类具有的相同协方差矩阵，得到一种经典的线性学习方法：**线性判别分析**（Linear Discriminant Analysis, LDA）。

共有L×p + p× (p+1)/2 个参数

LDA拟合精度虽然可能不如一般的高斯函数准确 但大幅减少了参数量

##### 参数估计

先验：$\hat P(C=c_i)=\frac{N(C=c_j)}{N}$

第j个高斯分布的均值$\mu_j=\frac{1}{N(C=c_j)}\sum_{X\in c_j}X$

<mark>**高斯分布的协方差矩阵**</mark>：对每个类别计算样本协方差矩阵，然后把所有类别的样本协方差矩阵相加

> 所有的类共享一个协方差矩阵

$$
\Sigma =\frac{1}{N}\sum_{c_j\in C}\sum_{X\in c_j}(X-\mu_j)(X-\mu_j)^T
$$

LDA决策面为：

![image-20220420220342925](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871428.png)

其中定义
$$
a_0=\log\frac{\pi_1}{\pi_2}-\frac{1}{2}(\mu_1+\mu_2)^T\Sigma^{-1}(\mu_1-\mu_2)\\
(a_1,a_2,...,a_p)^T=\Sigma^{-1}(\mu_1-\mu_2)
$$
若$a_0+\sum_{i=1}^pa_jx_j>0$，将x的标签置为c1，否则置为c2

> ![image-20220420220736387](https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/img14/1695871429.png)

#### 高斯朴素贝叶斯决策面

![image-20220324114058911](https://img-blog.csdnimg.cn/img_convert/9b9e819b0e6b274e4b2af966669099b6.png)

如
$$
\Sigma_{好瓜}=\begin{pmatrix}
\sigma_{11}^2\quad 0\\
0\quad \sigma_{12}^2
\end{pmatrix}\quad
\Sigma_{坏瓜}=\begin{pmatrix}
\sigma_{21}^2\quad 0\\
0\quad \sigma_{22}^2
\end{pmatrix}
$$
因为Σ𝑘  ≠ Σ𝑗 ，所以**高斯朴素贝叶斯的决策面仍然是非线性的（二次）**



### 总结

:one: 估计类条件概率$P(X_1,...,X_p|C)$使用属性独立假设
$$
P(X_1,X_2,...,X_p|C)=P(X_1|C)P(X_2|C)...P(X_P|C)
$$

:two: 朴素贝叶斯显著降低了计算开销

:three: 朴素贝叶斯不仅可以处理离散属性，也可以处理连续属性

:four: 对于一般的高斯贝叶斯分类器（  QDA ）以及朴素高斯贝 叶斯分类器，分类决策面是二次的。

:five: 当$\Sigma_k=\Sigma,\forall k$,, QDA退化成具有线性决策面的LDA

## 四、K-NN 分类算法

机器学习中的分类算法大致分为以下三种

:one: 判别式：直接估计一个决策边界

例如：逻辑回归，支持向量机

:two: 生成式：建立一个生成式统计模型

例如：朴素贝叶斯分类器

:three: 基于实例的分类器：没有模型

例如：K-近邻 （K-nearest neighbors）
![在这里插入图片描述](https://img-blog.csdnimg.cn/9400cc5d44c44183a4e8422979157733.png)



### K-近邻分类器

训练偷懒，测试废时

**分类原理**

对一个未知样本进行分类：

> :one: 计算未知样本与标记样本的距离(最废时)
>
> :two: 确定k个近邻（超参，不鲁棒）
>
> :three: 使用近邻样本的标签确定目标的标签：例如，**将其划分到k个样本中出现最频繁的类**

![image-20220420221948914](https://img-blog.csdnimg.cn/img_convert/579dc5f2a1635c855a6e98c164469af5.png)

KNN算法本身简单有效，它是一种lazy- learning算法

分类器**不需要使用训练集进行训练， 训练时间复杂度为0**

KNN分类的计算复杂度和训练集中的训练样本的数目成正比，也就是说，如果训练集中样本总数为n,那么KNN的分类时间复 杂度为0(n)

> 假如有N个样本，而且每个样本的特征为D维的向量。那对于一个目标样本的预测，需要的时间复杂度是多少？
>
> 首先对于任何一个目标样本，为了做预测需要循环所有的训练样本，这个复杂度为O(N)。另外，当我们计算两个样本之间距离的时候，这个复杂度就依赖于样本的特征维度，复杂度为O(D)。把循环样本的过程看做是外层循环，计算样本之间距离看作是内层循环，所以总的复杂度为它俩的乘积，也就是O(N*D)。

### K-NN回归

当目标输出是连续值时，预测是k个最接近的训练样本的均值

![image-20220324115637533](https://img-blog.csdnimg.cn/img_convert/259444cff5e7ad39d8f39c9e0347ead8.png)

## 参考资料

[1]庞善民.西安交通大学机器学习导论2022春PPT

[2]周志华.机器学习.北京:清华大学出版社,2016

[3\][贝叶斯三之决策函数和决策面](https://zhuanlan.zhihu.com/p/34079681)

[4\][KNN复杂度分析及KD树](https://blog.csdn.net/weixin_43117447/article/details/101516007)
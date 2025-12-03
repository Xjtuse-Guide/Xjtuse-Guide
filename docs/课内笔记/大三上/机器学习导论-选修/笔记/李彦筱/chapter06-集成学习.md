# 第六章——集成学习

## 集成学习的基本概念

之前我们学习过的监督学习方法（无论是判别式的还是生成式的）都希望通过一个分类器将问题解决好。比如手写数字识别神经网络的实现中，我们就只训练了单个神经网络，通过其输出直接判断输入的类别。

集成学习的动机就是：一些情况下，直接建立一个高性能的分类器是很困难的。如果能找到一系列性能较差的分类器，并把它们集成起来的话，也许就能得到更好的分类器。

集成学习，就是一种把输入**送入多个学习器，再通过某种办法把学习的结果集成起来的办法**。其中，每一个学习器被称为“弱学习器”。

集成学习的结构如下：先产生一组个体学习器，然后再使用某种策略将其结合起来：

![image-20250610143810243](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBZGidg6Q-HQjhToaMkcrr0MtrDsafAALJFQACqw3wVCvUL9t-ByA1NgQ.png)

但是，我们的数据集通常只有一份，如何从这个单份的数据集中训练多个学习器，才能让每个个体学习器的参数不同（否则就没有意义了）呢？有两种方式：

通过重采样构造不同的训练集，或者通过重加权构造不同的训练集。

> 重加权是指：在学习时，不拿出所有的样本给学习器学习，可能只选择部分样本传递给学习器。

我们要求，个体学习器需要达到一定的精度（具有一定水平），且需要多样化（互不相同）。如果不满足这两个条件的话，可能存在如下的问题：

![image-20250610143925324](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBZWidg6d9F_n71oTFAY_0ZiKw-UFMAALKFQACqw3wVLZsYD7hPHheNgQ.png)

a 图中学习器既具有多样性（都适用于不同的测试用例），还具有精度（对大部分输入都是对的），因此集成可以提升性能；b 图中学习器没有差异，导致集成后没有更好的效果；c 图中每个学习器的精度都不好，虽然具有多样性，但错误较多，集成的结果更糟。

要获得好的集成，个体学习器应该“好而不同”，即个体学习器不能太坏，要有一定的“准确性”；并且要有多样性，即学习器间具有差异。

**个体学习器越精确、差异越大，集成越好**。

> 扩展：训练集样本数量不同导致的问题。
>
> 比如在做动物分类时，我的训练集可能包含大量猫和狗的数据，但稀有物种（比如熊猫、企鹅）的样本数量会很少。这样训练出来的分类器的分类面可能存在偏置，即对于训练集大的类别（猫狗）分类效果好，而对于稀有物种的分类效果不好。
>
> 解决这一问题的两个方法为：降采样和过采样。
>
> 过采样是指对于样本较少的类，使用 AI 或者其他算法合成手段手工“制造”一些样本，以得到一个各类样本数量均衡的类。
>
> 降采样是指对于样本较多的类，在训练时只使用小部分数据。
>
> 一般我们偏向于使用过采样而非降采样。因为降采样会导致原先样本多、分类效果好的类也变的不好。
>
> 还有一种方法是“分类加权”，即在损失函数中做点修改，如果模型对样本少的类识别错误，则通过引入系数加大惩罚力度（让损失函数更大）
>
> 这个扩展说明了，重采样和重加权等数据预处理方法不仅仅适用于集成学习，也可以用于其他领域。

### 集成有效性

考虑二分类问题 $y\in\{-1, +1\}$ 和真实函数 𝑓，假定基分类器的错误率为 𝜖 ,即对每个基分类器 ℎ𝑖：
$$
P(h_i(x)\ne f(x))=\epsilon
$$
假设我们通过简单投票法结合 T 个分类器，即将所有分类器结果求和，和大于 0 认为是 +1 类，小于 0 认为是 -1 类，那么：
$$
H(x)=sign(\sum_{i=1}^Th_i(x))
$$
集成分类器出错的概率如下：

![image-20250610145351879](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBZmidg6lyDS5ZrJsiF8g6I6nUSxUAA8sVAAKrDfBU9r50D0lIi702BA.png)

可以看到，分类错误率随着 T 的增加而下降，也就是基分类器越多，那么出错概率越小……真的吗？

事实上，基分类器过多时，基分类器之间的个体差异越来越难获得，导致基分类器之间不满足“多样性”的要求，可能反而导致分类结果变差。

### 集成方法分类

![image-20250610145421825](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBZ2idg63htMcqdCmm049MN3frVptEAALMFQACqw3wVITWQF522GcJNgQ.png)

串行化方法中，每个后生成的学习器都会受前面学习器的影响。后生成的学习器可能被要求提高前面学习器没能正确分类的样本的权重。

左侧 wn 表示样本的权重，am 表示每个分类器的权重。

并行化算法中，学习器之间没有相互影响，通过投票方式得出分类结果。

## Boosting 算法

Boosting 算法工作机制

- 首先给每一个训练样例赋予相同的权重，训练第一个基分类器并用它来对训练集进行测试;

- 对于那些分类错误的测试样例提高其权重，用调整后的带权训练集训练第二个基分类器;

- 重复上述过程直到最后得到一个足够好的学习器。

- 最终对基学习器进行加权结合得到集成学习器

![image-20250610145838919](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBaGidg7CI5LoAASrmHzLjPsetCL3F5gACzRUAAqsN8FRF69nGMjoP_DYE.png)

图中，$a_m$ 表示每个分类器对于最终结果的权重（会计算得到），$w_n^{(m)}$ 表示学习第 m 个分类器时所有的权重。

Boost 算法的主要代表是 AdaBoost：

### Adaboost

AdaBoost 算法步骤

1. 初始化每个训练样本的权重 𝑤𝑛：首先给每一个训练样例赋予相同的权重 𝑤𝑛(1) = 1/𝑁

2. 训练 1..M 共计 M 个分类器：每一轮训练时分为 a,b,c 三步：

   ![image-20250610150421758](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBaWidg7LHhHaG-HH53TdJekrTZmTVAALOFQACqw3wVFWPJdX6F3jSNgQ.png)

   其中，$\alpha_m$（每个分类器的权重）通过当前分类器分类错误率计算而得。如果要求 $\alpha_m$ >0，就需要 $1-\epsilon_m>\epsilon_m$，即错误率 < 1/2。

   I 函数的性质如下：如果 I(a) 中，a=0，那么 I(a)=0；如果 a!=0，那么 I(a)=1。

   c 步骤中，如果样本分错，那么指示函数 $I$ 的值为 1，其权重会乘以 $e^{\alpha_m}$ 而增加；如果样本分对，那么指示函数 $I$ 的值为 0，其权重会乘以 $e^0=1$ 保持不变。最后，所有样本的权重会经过归一化因子 $Z_m$ 进行缩放，以确保所有样本的权重之和为 1。因此，分类正确的样本权重值会相对减小，分类错误的样本权重值会增加。

3. 通过每个分类器及分类器的权重，得到输入的分类结果：
   $$
   H_M(x)=sign(\sum_{m=1}^Ma_mh_m(x))
   $$
   仍然通过把各个分类器加权求和的方式进行投票，从而得到分类结果。

ppt 14-21 页有此算法的直观展示。

AdaBoost 保证分类器多样化的方法就是重新计算样本权重：每次把被分类错误的样本的权重增加。从而让每次训练出的分类器都和上次不同。

### 一个例子

给定下表所示的训练数据。假设弱分类器由 𝑥 < 𝑣 或 𝑥 > 𝑣产生，其阈值 𝑣 使该分类器在训练数据集上分类误差最低。使用 AdaBoost 算法学习一个强分类器。

> 题干的意思是说，每个分类器在分类时只有一个参数：阈值 v，只能按照 x<v/x>v 来做分类。而我们每次寻找参数 v 时，都需要保证此参数 v 能够让此分类器的误差相比其他阈值 v 的分类器最小。
>
> 每个分类器可以自由规定哪侧属于哪一类，比如既可以规定 x>2 时 y=1，也可以规定 x<2 时 y=1，只要能够让错误率最低就行。

训练数据如下：

| 序号 | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| x    | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    |
| y    | 1    | 1    | 1    | -1   | -1   | -1   | 1    | 1    | 1    | -1   |

![image-20250610151754349](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBamidg7RCguZ9fF2xQoB26pVw2L_7AALPFQACqw3wVI3TNZ2Js2u4NgQ.png)

可以看出，第一次分类时，我们需要在跳变的数据之间分类，比如 2、3 之间，6、7 之间和 8、9 之间。我们就取中点 2.5, 5.5, 8.5 作为具体的分割阈值了（实际上取一个 2、3 之间的任何数都可以）。

第一次分类时，取 2.5 和 8.5 都仅仅会导致 3 个数字分错（即错误率 0.3 达到最低），因此按 2.5/8.5 分类都可以，我们取阈值为 2.5。

![image-20250610152214328](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBa2idg7fj2ojsquxvu30zuEvmK0RBAALQFQACqw3wVJgRa_zx0-deNgQ.png)

注意每次分类后 b 步需要计算分类器的权重，c 步需要更新每个样本的权重。分类错误的样本的权重会增加。

![image-20250610153128661](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBbGidg7jfXBD0ztVIQm-KPrGT4su0AALRFQACqw3wVLxE6kYtcHdENgQ.png)

![image-20250610153141955](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBbWidg7tprdNPX7ivt-YjaxSro3aRAALSFQACqw3wVDu67nBCqVpZNgQ.png)

小规律：

- $\epsilon_1>\epsilon_2>\epsilon_3$
- $\alpha_1<\alpha_2<\alpha_3$，分类器的权重单调递增，即分类器在逐渐变好。

每次构建分类器时，由于错误率计算时考虑了样本的权重，因此更倾向于将权重大的样本分到正确的类别。

![image-20250610153356381](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBbmidg75MHE082jLJAAGZvs56FdPsNQAC0xUAAqsN8FQYmcZ8ZjB0CTYE.png)

对于每个样本，都有两个分类器将其分对，一个分类器将其分错；而通过集成，十个样本的分类结果最终都是正确的。

### AdaBoost 正确性的证明

AdaBoost 实际上使用的是指数损失函数：
$$
E=\sum_{n=1}^Nexp(-y_nH_m(x_n))
$$
$y_n$ 为样本的真实标签，$H_m(x_n)$ 是当前分类器得到的分类结果，二者相乘后的 e 次幂作为误差。

其中：$H_m(x)=sign(\frac{1}{2}\sum_{l=1}^m a_l h_l(x))$，即分类器预测输出就是每个子分类器输出乘权重再求和。

因此，需要求得基分类器 ℎ𝑙，及系数 𝛼𝑙 （l=1,2,3,...,m）使得𝐸 达到最小。

但问题求解难度过大，降低难度。固定 ℎ1, … , ℎ𝑚−1 和 𝛼1, … , 𝛼𝑚−1 ，只优化当前步骤的 ℎ𝑚 和 𝛼𝑚。

由于
$$
H=\frac{1}{2}\sum_{l=1}^m a_l h_l(x)=\frac{1}{2}\sum_{i=1}^{M-1}a_ih_i(x)+\frac{1}{2}a_mh_m(x)=H_{m-1}+\frac{1}{2}a_mh_m(x)
$$
因此：
$$
E=\sum_{i=1}^{N}exp(-y_iH_m(x_i))=\sum_{i=1}^Nexp{\{-y_iH_{m-1}(x)-y_n\frac{1}{2}a_mh_m(x_n)\}}\\=\sum_{n=1}^Nw_n^{(m)}\times exp{\{(-\frac{1}{2}a_my_nh_m(x_n)\}}
$$
即记 $exp(-y_iH_{m-1})=w_n^{(m)}$。

我们接下来讨论两种情况：$y_n=h_m(x_n)$（即预测输出和实际标签相同）和 $y_n\ne h_m(x_n)$。

> 由于标签和预测输出都是 1/-1，因此预测对时必定有二者乘积为 1，预测错误时有二者乘积为 -1

$$
E=\sum_{n=1}^Nw_n^{(m)}\times exp{\{(-\frac{1}{2}a_my_nh_m(x_n)\}}\\=\sum_{n\in T}w_n^{(m)}exp{\{-\frac{1}{2}a_m\}}+\sum_{n\in F}w_n^{(m)}exp{\{\frac{1}{2}a_m\}}
$$

即分类正确（$n\in T$）时 ，exp 内部只剩下 $-\frac{1}{2}a_m$；错误时，只剩下 $\frac{1}{2}a_m$，因为 $y_nh_m(x_n)$ 就只可能是 1（正确）或者 -1（错误）。接下来推导得到：
$$
E=e^{-\frac{1}{2}a_m}[\sum_{n\in T}w_n^{(m)}+\sum_{n\in F}w_n^{(m)}]+[e^{\frac{1}{2}a_m}-e^{-\frac{1}{2}a_m}]\sum_{n\in F}w_n^{(m)}
$$
这个变换中，幻想出了一项 $\sum_{n\in F}w_n^{(m)}e^{-\frac{1}{2}a_m}$，将其和旧表达式的第一项合并后构成了新表达式的第一项；后面第二项中把这个幻想的内容又减回来了。

然后，我们可以将第一项里面的两个内容合并，得到 $\sum_{n=1}^Nw_n^{(m)}$，第二项中可以把后半部分内容改一改形式，得到最终结果为：
$$
E=e^{-\frac{1}{2}a_m}\sum_{n=1}^Nw_n^{(m)}+[e^{\frac{1}{2}a_m}-e^{-\frac{1}{2}a_m}]\sum_{n=1}^Nw_n^{(m)}I(h_m(x_n)\ne y_n)
$$
这也是 ppt 上的结果。

AdaBoost 的 a 步是最小化 hm，即通过最小化这个加权误差函数来拟合基分类器：

具体来说，是最小化了最后面这部分（$\sum_{n=1}^Nw_n^{(m)}I(h_m(x_n)\ne y_n)$)
$$
h_m^*=argmin_{h_m}\sum_{n=1}^Nw_n^{(m)}I(h_m(x_n)\ne y_n)
$$
b 步中，我们需要计算 am 的值。通过将误差函数关于 am 的偏导数求最小，其实就可以得到之前给出的公式：
$$
\frac{\partial{E}}{\partial{a_m}}=0=-\frac{1}{2}e^{-\frac{1}{2}a_m}\sum_{n\in T}w_n^{(m)}+\frac{1}{2}e^{\frac{1}{2}a_m}\sum_{n\in F}w_n^{(m)}
$$
将分类正确和错误的项移到等式两侧：
$$
e^{-\frac{1}{2}a_m}\sum_{n\in T}w_n^{(m)}=e^{\frac{1}{2}a_m}\sum_{n\in F}w_n^{(m)}
$$
两边同时乘以 $e^{\frac{1}{2}a_m}$，得到：
$$
\sum_{n\in T}w_n^{(m)}=e^{a_m}\sum_{n\in F}w_n^{(m)}
$$
由于 $\sum_{n\in T}w_n^{(m)} = \sum_{n=1}^N w_n^{(m)} - \sum_{n\in F}w_n^{(m)}$，并且错误率 $\epsilon_m = \frac{\sum_{n\in F}w_n^{(m)}}{\sum_{n=1}^N w_n^{(m)}}$，我们可以推导出：
$$
e^{a_m} = \frac{\sum_{n\in T}w_n^{(m)}}{\sum_{n\in F}w_n^{(m)}} = \frac{1-\epsilon_m}{\epsilon_m}
$$
可以解出：
$$
a_m=ln\frac{1-\epsilon_m}{\epsilon_m}
$$
这说明了之前给出的公式是正确的。

### Boosting 算法总结

Adaboost 的核心思想：“关注”被错分的样本，“器重”性能好的弱分类器

怎么实现？

- 不同的训练集→调整样本权重

- “关注” →增加错分样本权重

- “器重”→增加分类错误率低的分类器权重

预测：将弱分类器联合起来，使用加权的投票机制分类。让分类效果好的基分类器具有较大的权重，而分类效果差的分类器具有较小的权重。

## Bagging 算法

Bagging 基本思想：对训练集**有放回**地抽取训练样例，为每一个基本分类器都构造出一个跟训练集相当大小但各不相同的训练集，从而训练出不同的基本分类器；该算法是基于对训练集进行处理的集成方法中最简单、最直观的一种。

> 有放回的抽取是为了让所有生成的训练集都是相互独立的，互不干扰。

1. 从大小为N的原始数据集D中独立随机地抽取 N’个数据(N’<N)，形成一个自助数据集。

2. 重复上述过程，产生出多个独立的自助数据集；
3. 利用每个自助数据集训练出一个分类器
4. 最终的分类结果由这些“分量分类器”各自的判别结果投票决定

![image-20250610161654534](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBb2idg8EpL_y1mT9RF3fdipE83xSbAALUFQACqw3wVEXlLTEVtIitNgQ.png)

分类预测：投票。选择票数最多的。如果两个类收到同样票数，可以**随机选择一个**

回归预测：取所有分类器输出的均值。

Bagging 的特点

- 基础分类器变化越大，集成性能越好

- 集成决策树的效果较好
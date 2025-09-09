# 概率 PCA

之前我们从判别式的观点看待 PCA，现在我们从生成式的观点看待 PCA。

## 隐变量

假设隐变量 Z 服从正态分布 N(0, I)，z 可以生成真正的观测数据 x：
$$
x=wz+\mu+\epsilon
$$
其中 $\epsilon$ 为噪声，$\epsilon$ 服从正态分布 N(0, $\sigma^2 I$)
$$
P(x|z) =N(x|Wz+\mu,\sigma^2I)
$$
x 的值由隐变量 z 和噪声 $\epsilon$ （$\sigma^2I$ 这部分，即高斯分布公式中的方差）共同控制，其中 x 的均值是 z 的线性函数（Wz+u），通过 pxk 矩阵 W 和 p 维向量 $\mu$ 决定。

通过 P(z) 和 P(x|z)，我们可以得到：
$$
P(x)=\int p(x|z)p(z)dz
$$
![image-20250609201328118](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBcGidhPHaXiKnxyEmZLk4IpJdAvF6AALWFQACqw3wVO13uD6iUE3DNgQ.png)

左侧图片表示 P(z) 是一个一维的高斯分布，选择了一个 z 值；中间图片中选择了一个 P(x|z) 的值，多次采样，积分即可得到右侧的 p(x)。

可以看出（虽然很难证明），边缘概率 P(x) 仍然是一个高斯分布，它的均值就是 $\mu$，协方差矩阵为 $C=WW^T+\sigma^2I$，即 P(x)~$N(\mu, WW^T+\sigma^2I)$

利用观测样本集合 $X={x_i}$，估计出参数集合 θ={μ,W,$σ^2$} 的值之后，使用贝叶斯公式
$$
P(z|x)=\frac{P(z)\times P(x|z)}{P(x)}
$$
得出：

![image-20250609201825629](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBcWidhPOfhuos1XDIAQtG_FQb2dBOAALXFQACqw3wVE9HAo5sr3nJNgQ.png)

最后，降维结果通过条件概率 P(z│x) 的期望给出：
$$
z_i=M^{-1}W^T(x_i-\mu)
$$
上图中，M=$W^TW+\sigma^2I$ 和 C=$WW^T+\sigma^2I$ 相比很相似。事实上，我们可以证明 $C^{-1}=\sigma^{-2}[I-WM^{-1}W^T]$。

> 这个结论在证明 P(z|x) 等于后面那串东西时有用，不过既然不要求掌握证明，那么这个结论也是没用的）

我们可以看出，我们需要对参数 $\mu$，$\sigma^2$ 和 w 做极大似然估计，然后就可以根据它们的值先计算 $M^{-1}$，再求解出 $z_i$ 了。

### 估计 $\mu$

![image-20250609204211894](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBcmidhPZArimfFhU1fTpzep_UaZvRAALYFQACqw3wVL_Q3VcH6PPONgQ.png)

我们可以看出，假设输入样本为 X={xi}，那么：
$$
\mu=\frac{1}{N}\sum_{n=1}^Nx_n
$$
即 $\mu$ 就是所有输入样本的均值。

### 估计 w

![image-20250609204826480](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBc2idhPjdAfSerGWFc-1R2MO0noRsAALZFQACqw3wVLD3QGEPXKTtNgQ.png)

其中我们用到了：
$$
a^Tb=Tr(ab^T)
$$

> Tr 指矩阵的迹

在使用时，取 a=$(x_n-\mu)^TC^{-1}$，b=$(x_n-\mu)$（可能有错）

![image-20250609205353096](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBdGidhPtnd3fEauXO7lnhD16_vGouAALaFQACqw3wVMK3gk-dwSqSNgQ.png)

![image-20250609205413766](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBdWidhP3j_-DDCcE5AV_HPFnds3FnAALbFQACqw3wVHtl2pUOi6pcNgQ.png)

ML 是指极大似然估计匹配（Maximize Likelihood），$\sigma^2_{ML}$ 的值为 k+1...p 维度的平方差。在标准 PCA 中，我们只留下了最大 k 个特征值对应的特征向量维度；这里说明，我们在概率 PCA 中定义的噪声恰好就是标准 PCA 中我们扔掉的那些维度（k+1...p 维）。

### 具体算法步骤

![image-20250609205803036](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBdmidhQABUJGyhYLa7jKhpIVYsa-x8gAC3BUAAqsN8FT74meC8lUUrjYE.png)

这一页一定要会。

$z_i$ 其实就是 $M^{-1}W^T(x_i-\mu)$，只不过把矩阵 M 的定义直接代入进去了。

## EM 算法

PCA 中，EM 算法的隐变量是 z，参数 $\theta$ 就是 $\mu$， $\sigma^2$ 和 w。

![image-20250609211313338](/Users/liyanxiao/Downloads/软件工程经济学打印/./chapter08-概率 PCA.assets/image-20250609211313338.png)

第二行：利用了公式 P(X, Z) = P(x|z) \* P(z)。

> P(x|z) 和 P(z) 的定义在下面列出来了，看起来很复杂是因为二者都服从正态分布，这里把正态分布的整个分布函数写出来了，看起来很难，其实就是正态分布的概率密度函数。

**要求：至少要记住四个公式**。（即 w, $\mu$，$\sigma^2$ 和 zi 的计算公式）

最终推导结果：

![image-20250609212337442](https://telegraph-image-5ms.pages.dev/file/BQACAgUAAyEGAASIfjD1AAIBd2idhQRyWtow9VNQwMWtKLel1rStAALdFQACqw3wVILjpaO9Atv7NgQ.png)

即 E 步和 M 步都只需要一个公式，轮流更新 E 和 W。注意开始时需要通过上方公式初始化 Wnew。
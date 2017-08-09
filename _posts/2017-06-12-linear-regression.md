---
layout: post
title: 线性回归(Linear Regression)
categories:
- MachineLearning
---

## 1. 摘要

线性回归（Linear Regression）是一种线性模型，试图通过样本（训练样本）属性的线性组合得到预测函数，以尽可能准确预测新样本的输出。线性回归模型需要训练样本，因此一该模型为基础的机器学习（Machine Learning）被分类为有监督学习（Supervised Learning）。

线性回归，以线性函数表示预测函数（Hypothesis），以最小化代价函数（Cost Function）为目标，利用训练样本通过梯度下降法（Gradient Descent），当然也有其他方法，求得预测函数的的参数，进而得到预测函数。所得预测函数对新样本进行预测，得到预测结果。

通常情况，代价函数为最小二乘代价函数，为什么使用该代价函数，可以用概率中的极大似然估计方法来解释。

原始的线性回归是 Parametric Algorithm，其参数数目固定，由样本特征数目确定。我们还会讲到 Locally weighted linear regression，它是一种 Non-parametric Algorithm，其权重数目随训练样本数目增加而增加，并不固定。

Keywords：Linear Model, Hypothesis, Supervised Learning, LMS, Gradient Descent, Parametric Algorithm, Non-parametric Algorithm, Cost Function

## 2. 介绍

我们有一个房价的数据集(m个样本)：

|$$x^{i}$$| 住房面积（平方米）$$x_1$$ | 居室数目 $$x_2$$ | 房价（百万RMB）$$y^{i}$$ |
|---| :------------- | :------------- | --- |
| $$x^{1}$$ | 80  | 3 | 299 |
| $$x^{2}$$ | 100 | 2 | 411 |
| $$x^{3}$$ | 120 | 3 | 434 |
| $$x^{4}$$ | 145 | 3 | 499 |
| $$\vdots$$ | $$\vdots$$ | $$\vdots$$  | $$\vdots$$ |

让我们来用符号表示每个样本：

- $$x^{i}$$ 表示样本中的第i个样本, 总样本数为n
- $$x^{i}_{j}$$ 表示第i个样本的第j属性（特征），如住房面积，居室数目，总特征个数为n，此例n=2。
- $$y_{i}$$ 表示第i个样本对应的真实（目标值），上面的例子中是房价。

有监督学习的流程：训练集-->学习算法-->预测函数或映射函数 $$h$$（hypothesis），喂给预测函数$$h$$一个新的样本，h就吐出一个预测结果（$$y_{prediction}$$），就是对应一个映射$$X \rightarrow Y$$，学习算法的预测精度就看这个预测结果与真实值$$y$$之间的差距程度。

这里如果样本真实值（比如房价）是连续的，那么这个学习问题就是回归问题（regression problem）；如果真实值是离散的，那么这个学习问题就是分类问题（classification problem）.

上面的数据集的真实房价值是连续的，因此根据房价的数据集来预测房价这个问题是个回归问题。预测房价这个问题的关键就在于我们如何确定预测函数（hypothesis）。我们以简单的线性函数来表示：

$$h_{\theta}(x) = \theta_{0} + \theta_{1}x_{1} + \theta_{2}x_{2}$$

其中$$\theta_{i}$$是预测函数（映射函数）的参数（parameters，也称为权重 weights）。简化表示的话，我们可以令$$x_{0}=1$$,则有：

$$ h(x) = \sum_{j=0}^{n} \theta_{j}x_{j} = \Theta^{T}x$$

其中，$$\Theta = \begin{bmatrix} \theta_0 \\ \theta_1 \\ \vdots \\ \theta_j \end{bmatrix}, x = \begin{bmatrix} x_0 \\ x_1 \\ \vdots \\ x_j\end{bmatrix}$$

问题来了，如何根据训练样本集来确定预测函数的参数$$\theta$$？ 我们的目标是使得$$h(x^{i})$$尽可能接近$$y_{i}$$. 我们定义**代价函数**(式2-1)：

$${J(\theta) = \frac{1}{2} \sum_{i=1}^{m}(h_{\theta}(x^i)-y^i)^2} \tag{2-1}$$.  

这是一个最小二乘代价函数。

以上给出普通最小二乘法回归模型（ordinary least square regression model）。

现在我们的任务就是最小化代价函数$$J(\theta)$$，从而得到预测函数参数$$\theta$$.

### 2.1 LMS (Least Mean Squares) Algorithm

> LMS update rule , Widsow-Hoff learning rule

先初始化$$\theta$$，赋予初始值，然后慢慢改变$$\theta$$以让$$J(\theta)$$尽可能小，知道收敛到一定值，此时我们也就找到参数$$\theta$$。

以梯度下降法（gradient descent algorithm）为例，首先初始化参数$$\theta$$，然后不断重复下面的迭代公式：

$$\theta_{j} := \theta_{j} - \alpha \frac{\partial}{\partial\theta_{j}} J(\theta)$$

其中$$j = 0, 1, ..., n$$. $$\alpha$$ 称为学习因子（learning rate）。

对于一个训练样本$$(x,y)$$, 其

$$ \begin{align} \frac{\partial}{\partial \theta_j} J(\theta) &= \frac{\partial}{\partial \theta_j} \frac{1}{2} (h_{\theta}(x)-y)^2 \\ &= (h_{\theta}(x)-y) \cdot \frac{\partial}{\partial \theta_j}(h_{\theta}(x)-y) \\ &= (h_{\theta}(x)-y) \cdot \frac{\partial}{\partial \theta_j} (\sum_{i=0}^{n} \theta_i x_i - y) \\ &= (h_{\theta}(x) - y) x_j \end{align} $$

所以，对于单个训练样本， $$\theta_j := \theta_j + \alpha (y^i - h_{\theta}(x^i))x_j^i$$. 这就是 LMS（Least mean squares update rule）迭代规则, 也称为 Widrow-Hoff learning rule。 观察更新公式，我们可以发现：

1. 更新幅度 和 $$\alpha$$ 学习因子 以及 误差项 $$(y^i - h_{\theta}(x^i)$$有关，成比例关系；
2. 学习因子影响迭代更新
3. 误差项也影响迭代步数

**Batch Gradien Descent**

那么对于具有m个样本的训练集，若预测函数参数的LMS迭代算法为：

对于每个j按式 {  

$$\theta_j := \theta_j + \alpha \sum_{i=1}^{m}(y^i-h_{\theta}(x^i))x_j^i$$

}
重复迭代，直到收敛。

其中，$$j=0, 1, ..., n$$。推导类似，只有把代价函数$$J(\theta)$$**式(2-1)**。

这种迭代方式称为 **batch gradien descent(BGD)**（批量梯度下降法）。

**Stochastic Gradient Descent**

另外一种迭代更新方式为：

```
Loop {
  for i = 1 to m, {
```

$$\theta_j := \theta_j + \alpha (y^i - h_{\theta}(x^i))x_j^i, (for \ every \ j)$$

```
  }
}
```

此方法称为随机梯度下降（**stochastic gradient descent(SGD)** or **incremental gradient descent**）

**BGD 和 SGD 的区别**

1. BGD 每一步参数更新是在整个样本集之上，而SGD是在一个样本集上，更新参数。
2. 通常 SGD 比 BGD 更快得到参数$$\theta$$，使得代价函数最小，但SGD可能不收敛，在最小值附近振荡，但其也接近真实最小值。
4. BGD 也容易陷入局部最小区域。
3. 因此数据集非常大时，经常采用SGD。

### 2.2 The normal equations

梯度下降法是最小化代价函数$$J$$的方法。我们也可以使用求导的方式，使得$$\triangledown_{\theta}J(\theta)=0$$而得到参数$$\theta$$.

这里我们先用矩阵形式来表示代价函数。

训练集：

$$X= \begin{bmatrix} 1 & x_1^1 &x_2^1 & \cdots & x_n^1 \\ 1 & x_1^2 &x_2^2 & \cdots & x_n^2 \\
\vdots & \vdots & \vdots & \cdots & \vdots \\
1 & x_1^m & x_2^m & \cdots & x_n^m \end{bmatrix}_{m \cdot (n+1)}$$

参数矩阵：

$$\theta = \begin{bmatrix} \theta_0 \\ \theta_1 \\ \vdots \\ \theta_n \end{bmatrix}_{(n+1) \cdot 1}$$

目标值：

$$y=\begin{bmatrix} y^1 \\ y^2 \\ \vdots \\ y^m \end{bmatrix}$$

因为$$h_{\theta}(x^i) = (x^i)^T\theta$$,就有 $$X\theta-y=\begin{bmatrix} h_{\theta}(x^1) - y^1 \\ \vdots \\ h_{\theta}(x^m) - y^m \end{bmatrix}$$，再根据向量内积得

$$\begin{align} \frac{1}{2} (X\theta-y)^T(X\theta-y) &= \frac{1}{2} \sum_{i=1}^{m}(h_{\theta}(x^i)-y^i)^2 \\ &= J(\theta) \end{align}$$

最后对参数求偏导可以得到（具体推导过程省略，可参考[文献1][1]）

$$\triangledown_{\theta}J(\theta) = X^TX\theta - X^Ty$$

要是代价函数最小，上面的导数必须为0，就得到 **normal equations**：$$X^TX\theta = X^Ty$$，从而可以求得

$$\theta = (X^TX)^{-1}X^Ty$$

这里有个前提就是矩阵$$X^TX$$可逆，只要矩阵X中各列向量线性独立，就可以满足。也就是样本集中样本属性（特征）是线性独立的。

这里我们还可以使用矩阵正交投影的方法来证明。如下：

已知矩阵$$X,y$$， 我们的目标是找到参数$$\theta$$使$$X\theta = y$$，这里最理想的，然后现实很残酷，我们不一定能找不到参数满足上面理想的等式。但我们能找到的参数满足

$$X\theta \rightarrow y$$即$$X\theta$$近似$$y$$，也就是存在一定误差，得到误差向量

$$E=X\theta - y$$

从矩阵正交角度理解（可参考[文献2][2]），该误差向量垂直于$$X$$中所有的列向量，也就得到

$$X^TE=0 \rightarrow X^T(X\theta-y)=0 \rightarrow X^TX\theta = X^Ty$$

若$$X$$中的列向量线性独立，那么就可得到

$$\theta = (X^TX)^{-1}X^Ty$$

用矩阵方式来证明更容易。

### 2.3 Locally weighted linear regression

样本特征的选择对算法的学习性能至关重要。

> Locally weighted linear regression(LWR) algorithm which, assuming there is sufficient training data, makes the choice of features less critical.

LWR算法减弱算法性能对样本特征的敏感性。具体实现就是：

1. 求取$$\theta$$, 使得  $$\sum_i w^i(y^i - \theta^T x^i)^2$$ 最小化。
2. 得到预测值: $$\theta^T x$$.

和原始的线性回归算法，LWR在代价函数中为每个样本增加了对应权重（weights，正数）$$w^i$$, 其大小决定最小二乘误差的代价函数中的影响程度。标准的选择是：

$$w^i = e^{(-\frac{(x^i - x)^2}{2\tau^2})}$$

这里的$$x$$是我们特定一个点（at which we're trying to evaluate x），$$\tau$$为 bandwidth。 可以看出，预测样本与训练样本差距越小时，权重接近1，相反，权重就越小。

因此，LWR对每个需要训练样本都需要计算权重，训练样本数越多，则权重数目跟着增多。LWR是“non-parametric algorithm”的一种。

## 3. Taxonomy

以线性模型为基础，线性回归算法是有监督学习算法中的一种。（模型，算法好混乱。）


## 4. Inspiration or Interpretation

为什么代价函数选择公式(2-1)的形式？ 可用概率方面进入，来解释，使用最大似然估计来解释为什么选择该代价函数。具体可参见[文献1-Probabilistic interpretation][1]的讲解。

## 5. Metaphor

梯度下降法类似爬山坡，一步步下山，找山谷最低点。

## 6. Strategy

最小二乘回归模型最小化代价函数来得到预测函数的参数。

## Procedure

## Heuristics

## Code Listing

## Reference

1. [cs229-notes1.dvi - cs229-notes1.pdf](http://cs229.stanford.edu/notes/cs229-notes1.pdf)  
2. [线性代数:正交 · Anifacc](https://anifacc.github.io/math/linearalgebra/2017/05/17/intro2linear-algebra-c04-orthogonality/)

---

```
Beta 1.0
@Anifacc  
2017-06-12 (1.0 - 2.2)
```

---

[1]:  http://cs229.stanford.edu/notes/cs229-notes1.pdf
[2]:  https://anifacc.github.io/math/linearalgebra/2017/05/17/intro2linear-algebra-c04-orthogonality/

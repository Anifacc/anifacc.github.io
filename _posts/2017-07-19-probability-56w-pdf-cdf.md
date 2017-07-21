---
layout: post
title: 顽想学概率:概率密度函数与连续概率分布
categories:
- Math
- Probability
---

顽想学概率第5周下半部分和第六周主要讲了概率密度函数与常见的连续概率分布。

- 概率密度函数(Probability Density Function-PDF)
- 连续概率分布(Continuous Probability Distribution)：
  - Uniform 概率分布（连续）
  - Exponential 概率分布
  - Erlang 概率分布
  - Normal 概率分布

---

## 1. 概率密度函数

离散变量有概率质量函数PMF表示某个时间发生的概率，那么对于连续变量还能继续用PMF嘛，答案是否定。对于连续事物，我们要看的关键是密度。一根均匀圆棍子有密度，我们的概率对应的也可以有密度！对于一个随机变量X而言，其**概率密度PDF**为：

$$\begin{align}
f_X(x) &= \lim_{\triangle x \rightarrow 0} \frac{P(x \leq X \leq x+\triangle x)}{\triangle x}  \\
       &= \lim_{\triangle x \rightarrow 0} \frac{F_X(x+\triangle x)-F_X(x)}{\triangle x} \\
       &= F^{'}_X(x)
\end{align}$$

可以看出：累积分布函数 $$F_X(x)$$ 与PDF的之间的关系。

$$CDF\ F_X(x) \rightleftarrows_{\int_{-\infty}^{x}}^{\frac{d}{dx}} PDF \ f_x(x)$$

接下来，将PDF与概率连结起来。

$$\begin{align}
P(a < X \leq b) &= F_X(b) - F_X(a) \\
    &= \int_{-\infty}^bf_X(x)dx - \int_{-\infty}^af_X(x)dx  \\
    &= \int_a^b f_X(x)dx
\end{align}$$

概率密度函数PDF的性质：

- PDF: $$f_X(x) = F^{'}_X(x)$$
- CDF: $$F_X(x) = \int_{-\infty}^{x}f_x(u)du$$
- 概率：$$P(a\leq X \leq b) = \int_{a}^{b}f_X(x)dx$$
- 概率为1：$$\int_{-\infty}^{\infty}f_X(x)dx=1$$
- PDF>0: $$f_X(x) > 0$$

## 2.连续概率分布

### Uniform 概率分布（连续均匀分布）

观察：722路公交车每20钟一班，灵芝随意出发到公交站，灵芝需等候公交车的时间为X。X~UNIF(0,20)

| PDF | CDF     |
| :------------- | :------------- |
| $$f_X(x)=\begin{cases}\frac{1}{b-a} & a \leq x \leq b \\ 0 & \text{otherwise}\end{cases}$$      | $$\begin{align}F_X(x) &= \int_{-\infty}^{x}f_X(u)du \\ &= \begin{cases} 0 & x \leq a \\ \frac{x-a}{b-a} & a < x \leq b \\ 1 & x > b\end{cases} \end{align}$$ |

### Exponential 概率分布（指数分布）

| PDF | CDF     |
| :------------- | :------------- |
| $$f_X(x)=\begin{cases}\lambda e^{-\lambda x} & x\geq 0 \\ 0 & \text{otherwise}\end{cases}$$      | - If $$x \geq 0$$$$:\begin{align}F_X(x) &= \int_{-\infty}^{x}f_X(u)du \\ &= \int_0^x \lambda e^{-\lambda u}  du \\ &= -\int_0^x e^{-\lambda u}d(-\lambda u) \\ &= -[e^{-\lambda u}]_0^x \\ &= 1 - e^{-\lambda x}\end{align}$$, elif:$$F_X(x)=0$$|

其中$$\lambda > 0$$是该分布的一个参数，被成为rate paratemer.即每单位时间发生该事件的次数[^1]。随机变量X 服从指数分布的，可写作 **X~Exponential(lambda)**

指数分布带有失忆的性质（memoryless），常被用来处理具有类似性质的事情，比如：

- 灵芝早晨出门化妆所需的时间
- 小雷打王者荣耀所花的时间

### Erlang 概率分布

**X~Erlang(n,$$\lambda$$)** 也称为Gamma distribution. 常被用于 model 一件有多个关卡事情的总时间，而每个关卡所需时间都是随机的

- 关卡数：n
- 每个关卡所需时间的概率分布为 指数分布$$Exponential(\lambda)$$
- 例：大电动过三关所需时间 $$Erlang(3,\lambda)$$
- 例：写完5科作业所需时间$$Erlang(5,\lambda)$$

| PDF | CDF     |
| :------------- | :------------- |
| $$f_X(x)=\begin{cases}\frac{1}{(n-1)!}\lambda^n x^{n-1} e^{-\lambda x} ,& x\geq 0 \\ 0 , & \text{otherwise}\end{cases}$$ | $$F_X(x) =\begin{cases}1 - \sum_{k=0}^{n-1}\frac{(\lambda x)^k}{k!} e^{-\lambda x} ,& x\geq 0 \\ 0 , & \text{otherwise}\end{cases}$$ |

### Normal 正态分布

> 又名 Gaussian 高斯分布

$$X-Gaussian(\mu, \sigma), X-N(\mu, \sigma)$$

其概率密度函数PDF:

$$f_X(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

- CDF:
  - 难计算，积分算不出来！
  - 用数值积分法建表？也难，不同的参数值$$\mu, \sigma$$会造就不同的正态分布PDF，每个都要建立一个表，不值。
- 解决？
  - 找一组特别的$$\mu, \sigma$$，针对这组的CDF建表，然后其他参数的与这个特别组建立联系。
- 特别组：就是标准正态分布(Standard Normal Distribution) $$Z \thicksim N(0,1)$$

其PDF：

$$f_Z(z)=\frac{1}{\sqrt{2\pi}}e^{-\frac{z^2}{2}}$$

其CDF：

$$\Phi(z)=\int_{-\infty}^{z}\frac{1}{\sqrt{2\pi}}e^{-\frac{u^2}{2}}$$

标准正态分布性质：

1. 利用对称性: $$\Phi(-z)=1-\Phi(z)$$
2. 任意参数下的CDF: $$X\thicksim N(\mu, \sigma^2), \frac{X-\mu}{\sigma} \thicksim N(0, 1),F_X(x) = \Phi(\frac{x-\mu}{\sigma})$$,

---

## Ref

[^1]: [指数分布 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E6%8C%87%E6%95%B0%E5%88%86%E5%B8%83)

---

```
@Anifacc
2017-07-20 Beta 1.0
```

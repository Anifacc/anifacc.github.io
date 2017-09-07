---
layout: post
title: LFD第二章笔记:Bias-Variance-Learning-Curve
categories:
- MachineLearning
- LearningFromData
---

从书本的泛化误差[VC 分析](https://anifacc.github.io/machinelearning/learningfromdata/2017/08/31/lfd-ch02-generalization-bound-interpretion-test-set/), 我们了解假设集 $$\cal H$$ 的选择既要考虑在训练集上与目标函数 $$f$$ 相近---$$E_{in}$$ 要小, 又要考虑其泛化能力, 在输入空间中的其他数据上的识别或预测性能要好 --- $$E_{out}$$ 要小.

现实中, 我们不可能找到一个假设集中正好只含有目标函数. 这太理想, 比中500万的彩票还难. (哈, 趁早放弃, 踏实学习. 学过概率的都不会去买彩票, 这是理性, 有时候感性一下, 买张彩票, 相信自己能中, 简直痴心妄想.)  因为现实中的目标函数未知, 只能从"采集"到的数据中分析窥探其一二. 实际学习中, 我们通过训练确定的一个好的假设, 既要接近目标函数, 又要在其他数据上"奏效".

我们可利用 VC泛化边界来理解上面的"对立协调(trade-off)"情况: 如果假设集 $$\cal H$$ 太简单, 在训练集上的效果就差 $$E_{in}$$ 大; 如果假设集 $$\cal H$$ 太复杂, 则泛化能力不好, $$E_{out}$$ 大.

还有另一种方式来考察. 这就涉及本节需要讲述的内容:

- Bias and Variance 偏差与方差
- The Learning Curve 学习曲线

---

## 1.Bias and Variance

首先是 bias-variance 分析, 将 out-of-sample error (误差平方) 分解.

$$E_{out}(g^{(D)}) = \Bbb E_D \lbrack \Bbb E_x \lbrack \lgroup g^{(D)}(x) - f(x) \rgroup ^2\rbrack \rbrack$$

其中 $$g^{(D)}$$ 表示算法基于数据集(训练集) $$\cal D$$ 得到的最终假设; $$\Bbb E_x$$ 表示: 输入空间 $$\cal X$$ 数据 $$x$$, 学习得到最终假设在数据 $$x$$ 上的结果 $$g^{(D)}(x)$$ 与目标函数 $$f(x)$$ 误差平方的期望值. 这容易理解. 关键是下面的处理得到 bias 和 variance.

$$\begin{align}
\Bbb E_D \lbrack E_{out}(g^{(D)})\rbrack &= \Bbb E_D \left[ {\Bbb E_x \left[ \lgroup g^{(D)}(x) - f(x) \rgroup ^2\right]} \right] \\
  &= \Bbb E_x \left[ {\Bbb E_D \left[ \lgroup g^{(D)}(x) - f(x) \rgroup ^2\right]} \right] \\
  &= \Bbb E_x \left[ \Bbb E_D \lbrack g^{(D)}(x)^2 \rbrack - 2 \Bbb E_D \lbrack g^{(D)}(x) \rbrack f(x)  + f(x)^2 \right] \\
  &= \Bbb E_x \left[ \Bbb E_D \lbrack g^{(D)}(x)^2 \rbrack - 2 \bar g(x) f(x)  + f(x)^2 \right], where \ \Bbb E_D \lbrack g^{(D)}(x) \rbrack = \bar g(x) \\
  &= \Bbb E_x \left[ \Bbb E_D \lbrack g^{(D)}(x)^2 \rbrack - \bar g(x)^2 + \bar g(x)^2 - 2 \bar g(x) f(x)  + f(x)^2 \right] \\
  &= \Bbb E_x \left[ \Bbb E_D \lbrack (g^{(D)}(x) - \bar g(x))^2 \rbrack + (\bar g(x) - f(x))^2  \right]
\end{align}$$

其中 $$\Bbb E_D \lbrack g^{(D)}(x) \rbrack = \bar g(x)$$, 从数据集D下的得到的假设 $$g^{(D)}$$ 期望值以"均值函数"表示(大数定理是趋近的). 也可以这么理解: 有 K 个数据集 $$D_1, D_2, ..., D_K$$, 在这些数据集下, 我们得到最终的假设分别为 $$g_1, g_2, ..., g_K$$, 那么可令

$$\bar g(x) \approx \frac{1}{K} \sum_{k=1}^{K}g_k(x)$$

即 K 个数据集上得到的假设的平均值, 约等于期望值(大数定理).

本质上来讲, $$g(x)$$ 是个随机变量, 其随机性来自于数据集 D 的随机性; $$\bar g(x)$$ 就是这个随机变量的期望值 ( x 固定). 对于 数据集 D 而言, $$\bar g(x)$$ 是个常数.

**Bias**: 上式出现 Bias, 其定义为:

$$bias(x) = (\bar g(x) - f(x))^2$$

**Variance** 定义为

$$var(x) = \Bbb E_D \left[ (g^{(D)}(x) - \bar g(x))^2 \right]$$

所以有

$$\begin{align}
\Bbb E_D \lbrack E_{out}(g^{(D)})\rbrack &= \Bbb E_x \left[ bias(x) + var(x)\right] \\
  &= \ bias + \ var
\end{align}$$

---

## 2.The Learning Curve

---

## 3.Sum

---

## 参考

1. [Learning From Data - A Short Course](http://www.amlbook.com/support.html#_echapters) Chapter 2 Training VS Testing

## ChangeLog

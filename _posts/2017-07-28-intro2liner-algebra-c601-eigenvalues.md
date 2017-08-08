---
layout: post
title: 线性代数:特征值
categories:
- Math
- LinearAlgebra
---

大学时期，学习特征值特性向量问题，单纯是为学习，记忆和考试。都不知道矩阵的特征值和特征向量具体解决什么问题，或者说是哪一类问题。读过 Gilbert Strang 的 Introduction to liner algebra 第4版讲解之后，结合振动基础中模态分析问题，这才明白过来，特征值特征向量的用处非同小可。

本文内容主要是阅读后的笔记。

## 1.特征值

线性方程$$Ax=b$$对应的一类问题是稳态问题（steady state problems）。特征值解决的问题来自于动态领域（dynamic problems）：$$du/dt=Au$$的解随着时间的改变而变化，这类问题，我们就不能直接通过消元来求解，而需要使用矩阵特征值:

$$Ax=\lambda x$$. 其中$$\lambda$$为矩阵A的特征值。

如果只知道矩阵A，那么怎么求得$$A^{100}x$$？一个个矩阵慢慢乘下去？这个方法真的便捷么？假如现在我们知道矩阵的特征值，那么我们来看看$$A^{100}x$$会不会很好求解？$$A^{100}x=\lambda ^ {100} x$$. 这样是不是看上去变得容易和简洁。（注意这里的前提：$$x$$为矩阵A的特征向量。）

现在将$$Ax=\lambda x$$做下变换，得到$$(A-\lambda I)x =0$$, 假如$$x=\vec 0$$，这个等式恒成立，在这里排除这种情况。若$$x\neq \vec 0$$,只有$$\det (A-\lambda I)=0$$时，等式才成立，$$x$$在矩阵$$A-\lambda I$$的*零空间*中。

如此，通过矩阵行列式$$\det (A-\lambda I)=0$$，我们可以取得矩阵A的特征值，同时还可以求得特征值所对应的特征向量。

比如对应一个2x2的矩阵A，我们得到两个特征值$$\lambda_1, \lambda_2$$, 通过方程$$(A-\lambda_1I)x_1=0$$,我们可以求得特征值$$\lambda_1$$对应的特征向量$$x_1$$；那么另外一个特征值$$\lambda_2$$对应的特征向量$$x_2$$求解也类似。

**举个例子,案例1**：

> 马尔科夫矩阵(Markov matrix) $$A = \begin{bmatrix}0.8 & 0.3 \\ 0.2 & 0.7\end{bmatrix}$$的两个特征值分别为$$\lambda_1=1, \lambda_2=\frac{1}{2}$$.

$$\det(A-\lambda I)=0$$ 为 $$\begin{vmatrix} 0.8 - \lambda & 0.3 \\ 0.2 & 0.7-\lambda\end{vmatrix}=\lambda^2 - \frac{3}{2}\lambda+\frac{1}{2}=(\lambda-1)(\lambda -\frac{1}{2})$$


对于特征值$$\lambda_1=1$$,
$$(A-I)x_1=0$$，解得特征向量$$x_1=\begin{bmatrix}0.6 \\ 0.4\end{bmatrix}$$.

对于特征值$$\lambda_2=\frac{1}{2}$$.
$$(A-\frac{1}{2}I)x_2=0$$,解得特征向量$$x_2=\begin{bmatrix}1 \\ -1\end{bmatrix}$$

得到特征值和特征向量，因此

$$Ax_1=x_1, \ x_1$$经过矩阵变换后的向量方向不变。
$$Ax_2=\frac{1}{2}x_2, \ x_2$$经过矩阵变换后的向量方向没改变。如下图所示：

![eigenvalues](https://dn-jeremiahzhang.qbox.me/image/math/linearalgebra/c06s01_eignvalues.JPG)

也就是说，矩阵A的特征向量$$x$$，在经过矩阵A变换后得到向量$$Ax$$方向与变换前$$x$$的方向相同（或相反）。那么反过来，我们想想，如果不是特征向量的其他向量，那么经过矩阵A变换后的向量方向如何呢？还是相同或相反呢？答案是：方向改变了。若方向不改变，那么这个向量就是特征向量啦。但是我们可以通过特征向量来表示这些不是特征向量的向量，也就是说，这些特征向量是一组基。（思考下：这个具有一般性么？对于所有的方块矩阵都如此么？）继续上面例子的讨论。

矩阵A的第一列列向量可用特征向量表示，如：

$$\begin{bmatrix}0.8 \\ 0.2\end{bmatrix}=x_1 + (0.2)x_2 = \begin{bmatrix}0.6 \\ 0.4\end{bmatrix} + \begin{bmatrix}0.2 \\ -0.2\end{bmatrix}$$.

矩阵A乘以该列向量：

$$A\begin{bmatrix}0.8 \\ 0.2\end{bmatrix}=Ax_1 + 0.2Ax_2=x_1+(0.2)\frac{1}{2}x_2=\begin{bmatrix}0.7 \\ 0.3\end{bmatrix}$$.

知晓矩阵A的特征值和特征向量，当我们乘以矩阵A的时候，形式非常简介$$Ax=\lambda x$$。当多次相乘时，类似。

$$A^{99}\begin{bmatrix}0.8 \\0.2\end{bmatrix} = x_1 + (0.2)(\frac{1}{2})^{99}x_2 = x_1 + \begin{bmatrix}very \\small \\ vector \end{bmatrix}\rightarrow x_1$$.

$$\lambda_1 = 1$$, 特征向量$$x_1$$经过n次矩阵相乘后，最后保持不变，是“稳态值”；  
$$\lambda_2 = 0.5$$, 特征向量$$x_2$$ 经过n次矩阵相乘后，最后慢慢"消亡"。  
矩阵A的幂次越大，上式的值越接近"稳态"。

**案例2：**

> 投影矩阵$$P=\begin{bmatrix}0.5 & 0.5 \\ 0.5 & 0.5\end{bmatrix}$$的特征值分别为$$\lambda_1 = 1, \lambda_2 = 0$$.   

> 特征向量分别为$$x_1=\begin{bmatrix}1 \\1\end{bmatrix}, x_2 =\begin{bmatrix}1 \\-1 \end{bmatrix}$$

> $$Px_1=x_1(steady)$$, $$Px_2=0(nullspace)$$.  

上面的投影矩阵即是：（1）马尔科夫矩阵（Markov matrices）；（2）奇异矩阵（singular matrices 行列式为0）；（3）对称矩阵（symmetric matrices）。其特征值和特征向量特征：

1. P的每一列和为1，所以$$\lambda=1$$是一个特征值。
2. P是 **奇异矩阵** ，因此$$\lambda = 0$$是一个特征值。
3. P是 **对称矩阵** ，因此其特征向量 **(1,1)** 和 **(1,-1)** 相互垂直。

> Sum: 求nxn矩阵的特征值和特征向量步骤：

1. 计算行列式：$$\det(A-\lambda I)$$
2. 通过 $$\det(A-\lambda I)=0$$，求解多项式的根，得到特征值$$\lambda$$.
3. 求解$$(A-\lambda I)x=0$$得到特征向量$$x$$.

## 线索

如果知道一个nxn矩阵A，那么从这个矩阵中，我们可以得到关于特征值的那些信息呢？

1. 矩阵行列式$$\det A$$ 等于其所有特征值的乘积；
2. 矩阵A对角线元素的和（矩阵的迹trace）= 所有特征值的和。

矩阵特征值在复数域，与在实数域类似。

---

```
@Anifacc
2017-07-28 beta 1.0  
```

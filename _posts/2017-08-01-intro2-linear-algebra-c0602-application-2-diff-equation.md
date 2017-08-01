---
layout: post
title: 线性代数:特征值特征向量应用微分方程
categories:
- Math
- Linear Algebra
---

矩阵特征值特征向量简直是把利剑，应用相当广泛。现在就介绍应用于微分方程。将常系数微分方程转化到线性代数领域求解。这部分内容算是振动分析的数学基础。

本文内容是参考文献[^1]的学习笔记.主要内容：

- du/dt=Au 一阶常系数微分方程
- 二阶常系数微分方程
- 2x2矩阵的稳定性
- 矩阵的指数

## 1.du/dt=Au 一阶常系数微分方程

还记得微积分中如何求解一阶常系数微分方程（du/dt=u）的么？

$$\frac{du}{dt}=\lambda u, solutions \ u(t)=Ce^{\lambda t}$$

根据初始条件t=0时的值u(0)，我们可得到u(t).

这是简单的1x1问题，如果进入nxn的线性代数领域，对于n个一阶线性方程组（标量u就变为向量$$\boldsymbol u$$），该如何解决？

$$n \ equations \frac{d \boldsymbol u}{dt}=A \boldsymbol u, starting \ from \ the vector \ \boldsymbol u(0) at t=0$$

前提：线性微分方程（线性的哦）。

这里我们利用矩阵特征值和特征向量来解线性方程组。

$$Use \ \boldsymbol u = e^{\lambda t}\boldsymbol x \ when \ \boldsymbol {Ax}=\lambda \boldsymbol x , \ \frac{d \boldsymbol u}{dt}=\lambda e^{\lambda t}\boldsymbol x \ agrees \ with \ \boldsymbol{Au} = Ae^{\lambda t} \boldsymbol x$$

其中$$\lambda , x$$ 分别为矩阵A的特征值和特征向量。

**例1**：已知$$\boldsymbol u(0) = \begin{bmatrix} 4 \\ 2\end{bmatrix}$$, 求解 $$d \boldsymbol u / dt = A \boldsymbol u =\begin{bmatrix}0 & 1 \\ 1 & 0 \end{bmatrix}\boldsymbol u$$

矩阵A的特征值分别为1和-1，对应的特征向量分别为(1,1)和（1,-1）. 那么一阶微分方程组的解为：

$$u_{1}(t)=e^{\lambda_1 t}x_1=e^{t}\begin{bmatrix} 1 \\ 1\end{bmatrix}, u_2(t)=e^{\lambda_2 t}x_2=e^{-t}\begin{bmatrix}1 \\ -1\end{bmatrix}$$.

观察发现：$$\boldsymbol u$$也是特征向量，满足$$Au_1=u_1, Au_2=-u_2$$.如此：$$du_1/dt=u_1=Au_1, du_2/dt = -u_2=Au_2$$.

我们可以得到通解：

$$u(t)=Cu_1 + Du_2=\begin{bmatrix}
Ce^t + De^{-t} \\
Ce^t - De^{-t}
\end{bmatrix}$$

根据初始条件$$u_0$$，我们可以得到参数C和D的值分别为：

$$C\begin{bmatrix}
1 \\ 1
\end{bmatrix} +
D \begin{bmatrix}
1 \\ -1
\end{bmatrix} =
\begin{bmatrix}
4 \\2
\end{bmatrix} \Rightarrow C=3, D=1.$$

有没有发现这个过程和[线性代数:矩阵对角化 ](https://anifacc.github.io/math/linear%20algebra/2017/07/31/intro2-linear-algebra-c0602-diagonalizing-matrix/)中提到的解$$u_k = Au_k$$类似。**求解过程分为三步**：

1. u(0) 用矩阵A的特征向量（线性独立）来表示$$\boldsymbol u(0)=c_1\boldsymbol x_1 + \cdots + c_n\boldsymbol x_n$$;
2. 每个特征向量乘以$$e^{\lambda_i t}$$;
3. u(t)的解为$$e^{\lambda t}\boldsymbol x$$的组合：$$\boldsymbol u(t)=c_1e^{\lambda_1 t}\boldsymbol x_1 + \cdots + e^{\lambda_n t}\boldsymbol x_n$$

**备注**：以上没有考虑矩阵特征值相同的情形。

## 二阶常系数微分方程

对于二阶常系数微分方程：

$$my{''} + by' + ky = 0$$

在振动基础中是最常见的公式。利用线性代数来解特别方便。

经过变化：

$$\begin{cases}
dy/dt = y' \\
dy'/dt = -ky - by'
\end{cases} \Rightarrow
\frac{d}{dt}
\begin{bmatrix}
y \\ y'
\end{bmatrix} =
\begin{bmatrix}
0 & 1 \\ -k & -b
\end{bmatrix}
\begin{bmatrix}
y \\ y'
\end{bmatrix}$$

看，我们的二阶常系数微分方程变为一阶矩阵形式：$$d\boldsymbol u/dt = A\boldsymbol u$$.

下面的解法就是利用上面求解一阶方程组的方法来求解。

求矩阵A的特征值：

$$A-\lambda I=\begin{bmatrix}
-\lambda & 1 \\ -k & -b-\lambda
\end{bmatrix}, \det(A-\lambda I)=0 \rightarrow \lambda^2+b\lambda + k=0$$

可得到特征值分别记为$$\lambda_1, \lambda_2$$, 其特征向量为

$$x_1 = \begin{bmatrix}1 \\ \lambda_1 \end{bmatrix}, x_2 =  \begin{bmatrix}1 \\ \lambda_2 \end{bmatrix}$$

解为：

$$u(t)=c_1 e^{\lambda_1 t}\begin{bmatrix}1 \\ \lambda_1 \end{bmatrix}+ c_2 e^{\lambda_2 t}\begin{bmatrix}1 \\ \lambda_2 \end{bmatrix}$$

如果有初始条件的话，就可以求出参数。

## 2x2矩阵的稳定性

> For the solution of du/dt = Au, there is a fundamental question. Does the solutionapproach u = 0 as t--->+ oo? Is the problem stable, by dissipating energy?

求得解u(t)在时间t趋于无穷时，u是否也趋于0。也就是系统是否稳定。系统的稳定有赖于矩阵A。
可以从上面的案例中的解看出，只要指数中的$$\lambda$$ 为负值，那么时间t趋于无穷大时，u就趋于0。

**稳定性**：

> A is **stable** and $$u(t) \rightarrow 0 $$ 当A所有特征值为负数。 2x2 的矩阵$$A=\begin{bmatrix} a & b \\ c & d \end{bmatrix} $$必须满足：

> - 矩阵的迹小于0， trace = a+d = $$\lambda_1 + \lambda_2 < 0$$
> - 矩阵行列式大于0，$$\lambda_1 \lambda_2 > 0$$ 。

## 矩阵的指数

---

[^1]:   G. Strang, Introduction to Linear Algebra(4th edition)

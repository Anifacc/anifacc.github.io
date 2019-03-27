---
layout: post
title: 线性代数:矩阵对角化
categories:
- Math
- LinearAlgebra
---

矩阵特征值和特征向量是线性代数中的一个重点内容。我们之前学习如何计算一个矩阵的特征值和特征向量，这里我们利用矩阵的特征值和特征向量对矩阵进行对角化处理。

本文内容是参考文献[^1]的学习笔记.

- 1.矩阵对角化
- 2.应用: 斐波那契数列
- 3.矩阵的幂
- 4.非对角化的矩阵
- 5.矩阵AB和A+B的特征值

## 1.矩阵对角化

通过矩阵的特征值和特征向量，我们就容易得到矩阵的幂；只要我们适当利用特征向量，我们就可以将矩阵转换为对角矩阵。

**矩阵的对角化定义**：

> 假设一个 nxn 的矩阵A，它的n个特征向量$$x_1, x_2 , \cdots, x_n$$线性独立.将这些特征向量作为矩阵的每一列元素，组成 **特征向量矩阵S(eigenvector matrix)**，那么$$S^{-1}AS=\Lambda$$, 其中$$\Lambda$$为 **特征值矩阵(eigenvalue matrix)**:
> $$S^{-1}AS = \Lambda=\begin{bmatrix} \lambda_1 & \ & \ \\ \ & \ddots & \ \\
\ & \ & \lambda_n  \end{bmatrix}$$.

这样矩阵A就被对角化啦。从矩阵对角化定义中，可看出对角化的关键点(前提)：矩阵A是方块矩阵(nxn), 其 **所有n个特征向量线性独立**，这样组成的特征向量矩阵S肯定可逆，并将矩阵A对角化为特征值矩阵$$\Lambda$$。（这里思考：如果矩阵的所有特征向量线性独立，那么他的所有特征值是否不存在重复值呢或者说是其所有特征值各不相同呢？）

证明：

矩阵A的特征值和特征向量分别为$$\lambda_1, x_1; \cdots; \lambda_n, x_n$$, 特征向量矩阵为$$S=\begin{bmatrix}x_1 & x_2 & \cdots & x_n\end{bmatrix}$$。

那么，

$$AS=A\begin{bmatrix}x_1 & x_2 & \cdots & x_n\end{bmatrix}=\begin{bmatrix}\lambda_1x_1 & \lambda_2x_2 & \cdots & \lambda_nx_n\end{bmatrix}$$.

而$$\begin{bmatrix}\lambda_1x_1 & \lambda_2x_2 & \cdots & \lambda_nx_n\end{bmatrix} = \begin{bmatrix} x_1 & x_2 & \cdots & x_n\end{bmatrix} \begin{bmatrix} \lambda_1 & \ & \ \\ \ & \ddots & \ \\
\ & \ & \lambda_n  \end{bmatrix}=S \Lambda$$

所以：$$AS=S\Lambda \rightarrow S^{-1}AS=\Lambda \rightarrow A=S\Lambda S^{-1}$$, (因为特征向量矩阵S中的所有列向量线性独立，S可逆。)

啊哈！**矩阵的特征值和特征向量可用于矩阵对角化**，是谁发现的？这人真厉害。

既然矩阵A可以对角化，那么A的幂次就容易求得：$$A^n = S \Lambda^n S^{-1}$$

**备注1：** 假如矩阵A所有特征值各不相同，那么矩阵A的所有特征向量线性独立。 **任何一个没有重复特征值的矩阵都可以对角化。**  
**备注2：** 特征向量$$\boldsymbol x$$乘以任何非零常数，$$Ax=\lambda x$$仍然成立。   
**备注3：** 在特征向量矩阵S中的特征向量顺序与特征值矩阵$$\Lambda$$中特征值一一对应。  
**备注4：** 存在相同特征值的矩阵不能对角化。（相同的特征值对应相同的特征向量，S矩阵就不可逆）。

**重点：** 矩阵的可逆性与矩阵能否对角化关系:
  - **矩阵可逆性与其特征值有关**（=0或!=0）
  - **矩阵对角化与矩阵的特征向量有关，特征向量线性独立，则矩阵可对角化**。

例子，不可对角化矩阵：$$A=\begin{bmatrix}1 & -1 \\ 1 & -1\end{bmatrix}, B=\begin{bmatrix}0 & 1 \\ 0 & 0\end{bmatrix}$$.

矩阵A不可逆，它不能被对角化（其特征值都为0）。
矩阵B可逆，但它也不能被对角化（其特征值都为0）.

**那么什么样的矩阵可以对角化呢**？

1. 特征向量线性独立的矩阵
2. 对应：n个不同特征值所对应的特征向量线性独立，那么就可以对角化矩阵。

试想 **如何证明特征值不同，其对应的特征向量线性独立。**

矩阵的幂：$$A^k=S \Lambda ^ k S^{-1}=S\begin{bmatrix} \lambda_1^k & & \\ & \ddots & \\ & & \lambda_n^k\end{bmatrix}S^{-1}$$.

问题：什么情况下，$$k \rightarrow \infty, A^k \rightarrow zero \ matrix$$？（ALL $$\lvert \lambda \rvert < 1$$）.

## 2.应用：斐波拉契数列

> 斐波拉契数列：0，1，1，2，3，5，8，13，...

即 $$F_{k+2} = F_{k+1} + F_k$$，如何求得$$F_{100}$$


换一个思维方式，用矩阵和向量形式表示：

$$Let \ u_k =\begin{bmatrix}
F_{k+1} \\ F_k\end{bmatrix}, then
\begin{cases}
F_{k+2} = F_{k+1} + F_k \\
F_{k+1} = F_{k+1}
\end{cases}
\rightarrow \ u_{k+1} =
\begin{bmatrix}
1 & 1 \\
1 & 0
\end{bmatrix} u_k$$

$$ u_{100} =
\begin{bmatrix} F_{101} \\ F_{100}\end{bmatrix}
= A^{100} u_0
= A^{100} \begin{bmatrix} 1 \\ 0 \end{bmatrix} $$

求A的幂次，对角化矩阵A。

1. 首先求得特征值和特征向量，看能否对角化？
2. 矩阵A可对角化就进行对角化。

**求特征值，特征向量**

$$A-\lambda I =
\begin{bmatrix}
1 - \lambda & 1 \\
1 & -\lambda
\end{bmatrix} \rightarrow \det(A-\lambda I)=\lambda^2-\lambda-1$$

特征值和特征向量：

$$\lambda_{1} = \frac{1+\sqrt 5}{2} \thickapprox 1.618, x_1 = (\lambda_1, 1)$$  
$$\lambda_2=\frac{1-\sqrt 5}{2} \thickapprox -0.618, x_2=(\lambda_2, 1
)$$

$$u_0=
\begin{bmatrix}
1 \\ 0
\end{bmatrix} =
\frac{1}{\lambda_1-\lambda_2}(
  \begin{bmatrix}
  \lambda_1 \\ 1
  \end{bmatrix} -
  \begin{bmatrix}
  \lambda_2 \\ 1
  \end{bmatrix}
  ) =
  \frac{\boldsymbol x_1 - \boldsymbol x_2}{\lambda_1 - \lambda_2}$$

因此，

$$u_{100} = A^{100}u_0 = \frac{\lambda_1^{100}x_1 - \lambda_2^{100} x_2}{\lambda_1 - \lambda_2}$$

则，

$$F_{100}=\frac{1}{\sqrt 5}[(\frac{1+\sqrt 5}{2})^{100} - (\frac{1-\sqrt 5}{2})^{100}] \approx 3.54 \cdot 10^{20}$$

## 3.矩阵的幂

矩阵A的幂：

$$A^k u_0 =(S \Lambda S^{-1})\cdots(S \Lambda S^{-1})u_0 = S \Lambda^k S^{-1} u_0$$

$$S \Lambda^k S^{-1} u_0$$ 可分解成三步来理解特征值如何作用：

1. 将$$u_0$$用线性独立的特征向量表示 $$c_1x_1 + \cdots +c_nx_n$$. 可得 $$\boldsymbol c = S^{-1} u_0$$;
2. $$(\lambda_i)^k$$乘以每个特征向量$$x_i$$，$$(\lambda_i)^k x_i$$.  即$$x_i$$前的系数为$$\Lambda^k \boldsymbol c=\Lambda^k S^{-1} u_0$$
3. 将$$c_i(\lambda_i)^k x_i$$叠加求和得到 $$u_k=A^k u_0$$. 即$$S \Lambda^k \boldsymbol c = S s\Lambda^k S^{-1} u_0$$.

$$A^k u_0$$主要还是利用矩阵特征值和特征向量定义特性。

## 4.矩阵AB和A+B的特征值

矩阵AB和A+B的特征值，不要想当然以为就是A和B矩阵的特征值的简单乘积和和（前提它们的特征向量是否相同，相同则可，不相同，则不同）。

> 交换矩阵(Commuting matrices) 共享特征向量。假如A和B都能对角化，当且仅当AB=BA时，A和B共享特征向量（特征向量相同）。

---

```
@Anifacc
2017-07-31 beta 1.0
```

[^1]:   G. Strang, Introduction to Linear Algebra(4th edition)

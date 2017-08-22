---
layout: post
title: 线性代数:对称矩阵
categories:
- Math
- LinearAlgebra
---

本文内容是阅读文献[^1]的学习笔记.主要内容：

- 对称矩阵: $$P = P^T$$
- 对称矩阵的特征向量: 相互垂直的单位向量.(重要理论, 应用广, 比如模态分析)

---

## 1.起点

因为第6章内容本身就是将特征值和特征向量, 那么就关注对称矩阵的特征值和特征向量.

$$Ax=\lambda x$$

若A为对称矩阵, 那么其特征值和特征向量有什么特性, 或有没有与一般矩阵不同之处或特别之处. 要不然我们就不用去研究.

在矩阵对角化中, A矩阵可对角化可表示成: $$A = S \Lambda S^{-1}$$, 其中$$S$$为A的特征向量所组成的特征向量矩阵. 从这个形式来看, 是不是有点对称的意味? 那么我们来看看其A的转置. $$A^T = (S^{-1})^T \Lambda S^T$$.

若$$A = A^T$$, 再加上 $$(S^{-1})^T = (S^T)^{-1}$$

则有
$$\begin{align}
S \Lambda S^{-1} &= (S^{-1})^T \Lambda S^T \\
    &= (S^T)^{-1} \Lambda S^T \\
    & \Rightarrow \\
\Lambda &= S^{-1} (S^T)^{-1} \Lambda S^T S \\
        &= (S^T S)^{-1} \Lambda (S^T S) \\
        & \Rightarrow \\
(S^T S) &= I
\end{align}$$

这就表明对称矩阵特征向量的正交性.

关于对称矩阵的关键点:

- 对称矩阵只有实数特征值.
- 其特征向量互相正交.

 对称矩阵的特征向量矩阵$$S$$可转变为正交矩阵$$Q: Q^{-1} = Q^T$$

 在这里对阵矩阵的特征向量矩阵S只需要进行单位化就能得到标准正交化矩阵.因为S本身具有正交性.

 **spectral theorem(谱定理)**:

 任意对称矩阵A可写成为因式分解形式: $$A=Q \Lambda Q^T$$,

 其中$$\Lambda$$是由A的特征值组成的对角矩阵, 而$$Q$$为A的特征向量矩阵$$S$$经过单位化后的标准正交矩阵.

 **对称对角化Symmetric diagonalization**: $$A = Q \Lambda Q^{-1} = Q \Lambda Q^T, \ with \ Q^{-1} = Q^T$$

 上面的定理是数学中的 谱定理 spectral theorem 和几何与物理中的主轴定理 principle axis theorem.

 从谱定理中可以看出: A的对称性, 那么如何证明任意一个特征矩阵只有实数特征值和对称矩阵的特征向量正交呢?

书中使用三步来证明:

1. By an example, showing real $$\lambda's$$ in $$\Lambda$$ and orthonormal x's in $$Q$$.
2. By a proof of those facts when no eigenvalues are repeated.
3. By a proof that allows repeated eigenvalues (at the end of this section)

先给个案例来看看, 然后在进行证明.

例1: $$A=\begin{bmatrix} 1 & 2 \\ 2 & 4\end{bmatrix}$$

其特征值和特征向量

$$\lambda = 0, x_1 = (2, -1)^T$$  

$$\lambda = 5, x_2 = (1, 2)^T$$

$$Q = \frac{1}{\sqrt 5}[x_1, x_2] = \frac{1}{\sqrt 5} \begin{bmatrix} 2 & 1 \\ -1 & 2 \end{bmatrix}$$

$$Q^T = Q^{-1}, Q^{-1}AQ=\begin{bmatrix} 0 & 0 \\ 0 & 5 \end{bmatrix} = \Lambda$$

> **Real Eigenvalues: all the eigenvalues of a real symmetric matrix are real.**

**实对称矩阵的所有特征值都为实数.**

证明: 逆向思维, 假设存在复数特征值.

A 是实数矩阵, 假设: $$Ax = \lambda x, \lambda = a + b i$$, a, b都是实数, 其共轭为: $$\bar \lambda = a - b i$$. 同样, $$x$$ 也可能存在复数值, 其共轭为: $$\bar x$$.  现在我们取$$Ax$$的共轭, 有

$$\begin{align}
Ax = \lambda x & \rightarrow \bar{Ax} = \bar {\lambda x} \\
& \rightarrow A \bar x =  \bar \lambda \bar x
\end{align}$$

取转置: $${\bar x}^T A = {\bar x}^T \bar \lambda$$

上面两式一个左乘$${\bar x}^T$$, 一个右乘$$x$$, 得到:

$${\bar x}^T A x = {\bar x}^T \lambda x$$

$${\bar x}^T A x = {\bar x}^T \bar \lambda x$$

得到:

$${\bar x}^T \lambda x = {\bar x}^T \bar \lambda x$$

而 $${\bar x}^T x = \|x_1\|^2 + \|x_2\|^2 + \cdots \neq 0$$, 所以 $$\lambda = \bar \lambda$$, 得证 对称矩阵的特征值为实数.

特征向量$$x$$来自于$$(A - \lambda I) x = 0$$, 则可得到$$x$$也为实数向量. 关键是他们还是相互正交的.

> **Orthogonal Eigenvectors: Eigenvectors of a real symmetric matrix (when they correspond to different engivalue's are always perpendicular.**

**对称矩阵不同特征值对应的特征向量正交.**

证明: 假设$$Ax =\lambda_1 x, Ay = \lambda_2 y, \lambda_1 \neq \lambda_2$$

$$A^T = A$$

$$\lambda_1 x^T y = (\lambda_1 x)^T y = (Ax)^T y = x^T A^T y = x^T A y = x^T \lambda_2 y$$

等式左边等于右边, 两特征值又不相等, 则只有$$x^T y = 0$$ 的情况成立, 得证.

有趣:  

$$A = Q \Lambda Q^T =
\begin{bmatrix} x_1 & x_2 \end{bmatrix}
\begin{bmatrix} \lambda_1 & \\ & \lambda_2\end{bmatrix}
\begin{bmatrix} x_1^T \\ x_2^T\end{bmatrix}$$

$$A = \lambda_1 x_1 x_1^T + \lambda_2 x_2 x_2^T$$

推演到nxn的对称矩阵中:

$$A = \lambda_1 P_1 + \cdots \lambda_n P_n$$

其中 $$\lambda_i$$ 为特征值, $$P_i$$为特征空间投影.

## 2. 实数矩阵的复特征值


[^1]:   G. Strang, Introduction to Linear Algebra(4th edition)

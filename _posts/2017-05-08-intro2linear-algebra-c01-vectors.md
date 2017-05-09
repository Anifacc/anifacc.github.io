---
layout: post
title: 线性代数:向量-矩阵
categories:
- Math
- Linear Algebra
---

The contents are from chapter 1 of Introduction to Linear Algebra, Book of Gilbert Strang, editon 4th.

Review of the key ideas.

- Vectors & Linear Combinations
- Lengths and Dot products
- Matrices

# 1 Vectors & Linear Combinations #

1. A vector $$v$$ in 2-dimensional space has two components $$v_1$$ and $$v_2$$.
2. $$v + w = (v_1 + w_1, v_2 + w_2)$$ and $$cv = (cv_1, cv_2)$$ are found a component at a time.
3. A linear combination of three vectors $$u$$ and $$v$$ and $$w$$ is $$cu + dv + ew$$.
4. Take *all* linear combinations of $$u$$, or $$u$$ and $$v$$, or $$u, v, w$$. In 3-dimensions, those combinations typically fill a line, then a plane, and the whole space $$R^3$$.

# 2 Lengths and Dot products #

1. The dot product $$v \cdot w$$ multiplies each component $$v_i$$ by $$w_i$$ and adds all $$v_iw_i$$
2. The length $$\parallel v \parallel$$ of a vector is the square root of $$v \cdot v$$.
3. $$ u = \frac{v}{\parallel v \parallel} $$ is a *unit vector*. Its length is 1.
4. The dot product is $$v \cdot w = 0$$ when vectors $$v $$ and $$w$$ are perpendicular.
5. The cosine of $$\theta$$ (the angle between any nonzero $$v$$ and $$w$$) never exeeds 1: $$\cos\theta = \frac{v \cdot w}{\parallel v \parallel \parallel w \parallel}$$, **Schwarz inequality** $$\mid v \cdot w \mid \leq \parallel v \parallel \parallel w \parallel}$$.
6. Triangle inequality $$\parallel v + w \parallel \leq \parallel v \parallel + \parallel w \parallel$$.

# 3 Matrices #

1. **Matrix times vector:** $$Ax=$$ combination of the columns of A.
2. The solution to $$Ax=b$$ is $$x=A^{-1}b$$, when $$A$$ is an invertible matrix.
3. The difference matrix $$A$$ is inverted by the sum matrix $$S=A^{-1}$$.
4. The cyclic matrix $$C$$ has no inverse. Its three columns lie in the same plane. Those dependent columns add to the zero vector. $$Cx=0$$ has many solutions.

# Important notes

矩阵最基础的向量. 书中一开始就介绍向量的基本知识, 从而引导出矩阵内容. 这里要明白:

- 矩阵乘以向量, 从向量角度来理解.
- 矩阵是否可逆? 观察矩阵内各列向量是否独立.将矩阵的可逆性转换到向量的独立与否.
  - **Difference matrix** A :  $$\begin{bmatrix} 1 & 0 & 0 \\ -1 $ 1 & 0 \\ 0 & -1 & 1 \end{bmatrix}$$
  - Dot products with rows: $$Ax = \begin{bmatrix} 1 & 0 & 0 \\ -1 $ 1 & 0 \\ 0 & -1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} (1, 0, 0) \cdot (x_1, x_2, x_3) \\ (-1, 1, 0) \cdot (x_1, x_2, x_3) \\ (0, -1, 1) \cdot (x_1, x_2, x_3) \end{bmatrix}$$. 可逆其列向量互相独立.
  - **Cyclic Differences** $$Cx=\begin{bmatrix} 1 & 0 & -1 \\ -1 $ 1 & 0 \\ 0 & -1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} x_1 - x_3 \\ x_2 - x_1 \\ x_3 - x_2 \end{bmatrix} = b$$ **Cyclic difference matrix** $$C$$ 是不可逆的, 其列向量不独立. 其中一个列向量可以由另外两个列向量线性表示.
- Independence and Dependence: 独立与不独立.
  - $$u, v, w$$ are **independent**. No combination except $$0u+0v+0w=0$$ gives $$b=0$$
  - $$u, v, w^{1}$$ are **dependent**. Other combinations(specifically $$u + v + w^{1}$$) give $$b=0$$.
  - Note: 向量是否独立, 可以判断矩阵A的可逆性：
    - 矩阵A所有列向量互相独立, 那么矩阵A可逆(**invertible matrix**).
    - 矩阵A所有列向量不互相独立, 那么矩阵A不可逆(**singular matrix**).

向量角度理解矩阵, 更让人理解矩阵.

```
@Anifacc
2017-05-09
```

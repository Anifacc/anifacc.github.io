---
layout: post
title: 线性代数:线性方程
categories:
- Math
- LinearAlgebra
---

The review of the key ideas are from chapter 2 of Introduction to Linear Algebra, Book of Gilbert Strang, editon 4th.

- Vectors and linear equations
- The idea of elimination
- Elimination using Matrices
- Rules for matrix operations
- Inverse Matrices
- Elimination = Factorization:A=LU
- Transposes and Permutations

---

# 1.Vectors and linear equations #

1. The basic operations on vectors are multiplication $$cv$$ and vector addition $$v+w$$.
2. Together those operations give linear combinations $$cv + dw$$.
3. Matrix-vector multiplication $$Ax$$ can be computed by dot products, a row at a time. But $$Ax$$ should be understood as a combination of the columns of $$A$$.
4. **Column picture**: $$Ax=b$$ asks for a combination of columns to produce $$b$$.
5. **Row picture**: Each equation  in $$Ax = b$$ gives a line ($$n=2$$) or a plane($$n=3$$) or a "hyperplane"($$n>3$$). They intersect at the solution or solutions, if any.

# 2.The idea of elimination #

我仍然记得大学时学习线性代数, 课本是直接从 Gaussian elimination 讲起的.

```
Pivot = first nonzero in the row that does the elimination  
Multiplier = (entry to eliminate) divide by (pivot)
```

**Zero is never allowed as a pivot!**    
**Failure: for $$n$$ equations we do not get $$n$$ pivots**   
Elimination leads to an equation **$$0\neq0$$(no solution)** or **$$0=0$$(many solutions)**  
**Success comes with $$n$$ pivots. But we may have to exchange the $$n$$ equations.**

1. A linear system ($$Ax=b$$) becomes upper triangular ($$Ux=c$$) after elimination.
2. We subtract $$l_{ij}$$ times equation $$j$$ from equation $$i$$, to make the ($$(i, j)$$) entry zero.
3. The multiplier is $$l_{ij} = \frac{entry\ to\ eliminate\ in\ row\ i}{pivot\ in\ row\ j}$$. Pivots can not be zero!
4. A zero in the pivot position can be repaired if there is a nonzero below it.
5. The upper triangular system is solved by back substitution (starting at the bottom).
6. When breakdown is permanent, the system has no solution or infinitely many.

# 3.Elimination using Matrices #

上面的消元是按着步骤一步步执行下去的, 消元最后的结果是 1)有唯一解, 2)无数解, 3)无解. 我们也可以使用矩阵来进行消元.

**Identity matrix**: 单位矩阵$$I = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\0 & 0 & 1 \end{bmatrix}$$

**Elimination matrix or elementary matrix**: 消元矩阵 $$E_{31}=\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\-l & 0 & 1 \end{bmatrix}$$. 我们可以用消元矩阵左乘矩阵$$A$$, 将矩阵$$A$$中的第3行第1列的元素消为0.

**矩阵相乘**: $$AB = A \begin{bmatrix} b_1 & b_2 & b_3\end{bmatrix} = \begin{bmatrix} Ab_1 & Ab_2 & Ab_3\end{bmatrix}$$.

**Exchange matrix(Permutation matrix)** 置换矩阵 $$P_{23}=\begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}$$, exchanges row 2 with row 3.(左乘情况). 其他置换, 类似.

1. 从 row-pictures 来理解线性方程组 $$Ax=b$$. 其中: **$$Ax$$ is a combination of the columns of A.** 矩阵$$A$$的第i行写成列矩阵形式: $$[a_{i1}, a_{i2}, \cdots , a_{in}]$$, $$x^T=[x_1, x_2, \cdots, x_n]$$. 那么$$Ax$$中的任意一个元素可表示为: $$a_{i1}x_1 + a_{i2}x_2 + \cdots + a_{in}x_n, == \sum_{j=1}^{n}a_{ij}x_j$$.
2. Identity matrix = $$I$$, elimination matrix = $$E_{ij}$$ using $$l_{ij}$$, exchange matrix = $$P_{ij}$$.
3. Multiplying $$Ax=b$$ by $$E_{21}$$ subtracts a multiple $$l_{21}$$ of equation 1 from equation 2. The number $$-l{21}$$ is the $$(2,1)$$ entry of the elimination matrix $$E_{21}$$.
4. For the augmented matrix $$\begin{bmatrix} A & b\end{bmatrix}$$, the elimination step gives $$\begin{bmatrix} E_{21}A & E_{21}b \end{bmatrix}$$.
5. When $$A$$ multiplies any matrix $$B$$, it multiplies each column of $$B$$ separately.(可以将矩阵$$B$$看作为一个个列向量组成的矩阵, 这样就类似$$Ax$$.)

# 4.Rules for matrix operations #

1. The $$(i,j)$$ entry of $$AB$$ is (row i of $$A$$)·(column j of $$B$$).
2. An $$m \cdot n$$ matrix times an $$n \cdot p$$ matrix uses $$mnp$$ separate multiplication.
3. $$A(BC) = (AB)C$$(surprisingly important).
4. $$AB$$ is also the sum of these matrices: (column $$j of A$$) times (row $$j of B$$).
5. Block multiplication is allowed when the block shapes match correctly.
6. Block elimination produces the **Schur complement** $$D - CA^{-1}B$$.

在矩阵乘以向量的基础之上理解矩阵乘法就简单咯.

# 5.Inverse Matrices #

1. The inverse matrix gives $$AA^{-1}=I$$ and $$A^{-1}A=I$$.
2. $$A$$is inversible if and only if it has n pivots(row exchanges allowed).
3. If $$Ax=0$$ for a nonzero vector $$x$$, then $$A$$ has no inverse.
4. The inverse of $$AB$$ is the reverse product $$B^{-1}A^{-1}$$. And $$(ABC)^{-1} = C^{-1}B^{-1}A^{-1}$$.
5. The Gauss-Jordan method solves $$AA^{-1}=I$$ to find the $$n$$ columns of $$A^{-1}$$. The augmented matrix $$\begin{bmatrix} A & I \end{bmatrix}$$ is row-reduced to $$\begin{bmatrix} I & A^{-1} \end{bmatrix}$$.

三角矩阵(上, 下)只要对角线上存在0, 那么这个矩阵就不可逆.

# 6.Elimination = Factorization:A=LU #

LU分解:

Special pattern $$A =\begin{bmatrix}1 & 1 & 0 & 0 \\ 1 & 2 & 1 & 0 \\ 0 & 1 & 2 & 1 \\ 0 & 0 & 1 & 2\end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1\end{bmatrix}\begin{bmatrix} 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 1\end{bmatrix}$$.

```
When a row of A starts with zeros, so does that row of L.  
When a column of A starts with zeros, so does that column of U.
```

$$A=LU$$分解中, 上三角矩阵$$U$$中对角线上的元素对应$$A$$消元后的主元(pivots), 另外$$U$$可以继续分解为:$$U=DU_1$$, 对角阵和上三角矩阵乘积.($$A=LDU$$.)

1. Gaussian elimination (with no row exchanges) factors $$A$$ into $$L \cdot U$$.
2. The lower triangular $$L$$ contains the number $$l_{ij}$$ that multiply pivot rows, going from $$A$$ to $$U$$. The product $$LU$$ adds those rows back to recover $$A$$.
3. On the right side we solve $$Lc=b$$ (forward) and $$Ux=c$$ (backward).
4. **Factor**: there are $$\frac{1}{3}(n^3-n)$$ multiplications and subtractions on the left side.
5. **solve**: There are $$n^2$$ multiplications and subtractions on the right side.
6. For a band matrix, change $$\frac{1}{3}n^3$$ to $$nw^2$$ and change $$n^2$$ to $$2wn$$.

# 7.Transposes and Permutations #

矩阵转置:

> Sum $$(A + B)^T = A^T + B^T$$  
> Product $$(AB)^T = B^T A^T$$  
> Inverse $$(A^{-1})^T=(A^T)^{-1}$$

1. The transpose puts the rows of $$A$$ into the columns of $$A^T$$. Then $$A^{T}_{ij}=A_{ji}$$
2. The transpose of $$AB$$ is $$B^T A^T$$. $$(A^{-1})^{T}=(A^{T})^{-1}$$.
3. The dot product is $$x \cdot y = x^T y$$. Then $$(Ax)^T y$$ equals the dot product $$x^T(A^T y)$$.
4. When $$A$$ is symmetric ($$A^T=A$$), its $$LDU$$ Factorization is symmetic: $$A=LDL^{T}$$.
5. A permutation matrix $$P$$ has a 1 in each row and column, and $$P^T=R^{-1}$$.
6. There are $$n!$$ permutation matrices of size n. *Half even, half odd*.
7. If $$A$$ is invertible then a permutation $$P$$ will reorder its rows for $$PA=LU$$.

---
```
@anifacc
2017-05-10
```

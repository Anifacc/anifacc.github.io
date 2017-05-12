---
layout: post
title: 线性代数:向量空间-子空间
categories:
- Math
- Linear Algebra
---

The review of the key ideas are from chapter 3 of Introduction to Linear Algebra, Book of Gilbert Strang, editon 4th.

1. Spaces of vectors
2. The nullspace of A: solving $$Ax=0$$.
3. The rank and the row reduced form
4. The complete solution to $$Ax=b$$
5. Independence, Basis, and Dimension
6. Dimension of the Four Subspaces

---

# 1.Spaces of vectors #

## 1.0 Key ideas

1. $$R^n$$ contains all column vectors with $$n$$ real components.
2. $$M$$(2 by 2 matrices) and $$F$$(functions) and $$Z$$(zero vector alone) are vector spaces.
3. A subspace containing $$v$$ and $$w$$ must contain all their combinations $$cv\ + dw$$.
4. The combinations of the columns of $$A$$ form the *column space* $$C(A)$$. Then the column space is "spanned" by the columns(由列向量线性组合而成的空间 then spanned.).
5. $$Ax=b$$ has a solution exactly when $$b$$ is in the column space of $$A$$.

## 1.1 Spaces of Vectors

> **DEFINITION** The space $$R^n$$ consists all column vectors $$v$$ with n components. (The components of $$v$$ are real(R) numbers.)

In the definition of a *vector space*, vector addition $$x+y$$ and scalar multiplication $$cx$$ must obey the following eight rules:

1. $$x + y = y + x$$
2. $$x + (y + z) = (x + y) + z$$
3. There is a unique "zero vector" such that $$x + 0 = x$$ for all $$x$$(0 is zero vector)
4. For each $$x$$ there is a unique vector $$-x$$ that $$x + (-x) = 0$$
5. 1 times $$x$$ equals $$x$$
6. $$(c_1c_2)x=c_1(c_2x)$$
7. $$c(x + y) = cx + cy$$
8. $$(c_1 + c_2)x = c_1x + c_2x$$

上面8条规则离不开的是向量的加法和数乘(其中 $$c$$ 是系数, $$x,y$$是向量空间中的向量).所有向量空间必须满足以上8项规则. 最基本的还是向量加法和数乘. 向量空间中的向量作以上加法和数乘后所得到的向量必定在向量空间内.若不满足8规,这不是向量空间.

符号|含义
---|---
$$M$$|The vector space of *all real 2 by 2 matrices*
$$F$$|The vector space of *all real functions* $$f(x)$$
$$Z$$|The vector space that consists only of *a zero vector*

## 1.2 Subspaces

> **DEFINITION** A subspace of a vector space is a set of vectors(including 0) that satisfies two requirements: If $$v$$ and $$w$$ are vectors in the subspace and $$c$$ is an scalar, then  
> 1. $$v+w$$ is in the subspace.  
> 2. $$cv$$ is in the subspace.

已经确定一个向量空间之后(8规满足), 子空间的判定只需要上面两个规则.

In short, **all linear combinations stay in the subspace**.

- Facts:
  1. **Every subspace contain the zero vector.**
  2. **Lines through the origin are also subspaces.**

> A subspace containing $$v$$ and $$w$$ must contain all linear combinations $$cv + dw$$.

## 1.3 The Column Space of A

Remember: **$$Ax$$ is a combination of the columns of $$A$$**. So **to sovle $$Ax=b$$ is to express $$b$$ as a combination of the columns.** The right side $$b$$ has to be in the column space produce by $$A$$ on the left side, or no solution.

> **DEFINITION**: The *column space* consists of *all linear combinations of the columns*. The combinations are all possibble vectors $$Ax$$. They fill the column space $$C(A)$$.

看, 从向量空间和线性组合理解线性方程组$$Ax=b$$, 是不是更容易理解啦! 想要方程有解, 那么**$$b$$必须在$$A$$的列向量空间中.**

---

# 2.The nullspace of A: solving $$Ax=0$$. #

## 2.0 Key ideas

1. The nullspace $$N(A)$$ is a subspace of $$R^{n}$$. It contains all solutions to $$Ax=0$$.
2. Elimination produces an echelon matrix $$U$$, and then a row reduced $$R$$, with pivot columns and free columns.
3. Every free column of $$U$$ or $$R$$ leads to a special solution. The free variable equals 1 and the other free variables equals 0. Back substitution solves $$Ax=0$$.
4. The complete solution to $$Ax=0$$ is a combination of the special solutions.
5. If $$n > m$$ then $$A$$ has at least one column without pivots, giving a special solution. So there are nonzero vectors $$x$$ in the nullspace of this rectangular $$A$$.

## 2.1 Nullspace of $$Ax=0$$

> The nullspace of $$A$$ consists of all solutions to $$Ax=0$$. These vectors $$x$$ are in $$R^n$$. The nullspace containing all solution of $$Ax=0$$ is denoted by $$N(A)$$.

> The nullspace consists of all combinations of the special solutions.

> The **free components** correspond to columns without pivots. The special choice(one or zero) is only for the free variables.

我们来看看下面三个矩阵:

$$A = \begin{bmatrix} 1 & 2 \\ 3 & 8 \end{bmatrix}, B = \begin{bmatrix}A \\ 2A \end{bmatrix} = \begin{bmatrix}1 & 2 \\ 3 & 8 \\ 2 & 4 \\ 6 & 16\end{bmatrix}, C = \begin{bmatrix} A \\ 2A \end{bmatrix}= \begin{bmatrix} 1 & 2 & 2 & 4 \\ 3 & 8 & 6 & 16 \end{bmatrix}.$$

对他们消元:

$$A \Rightarrow \begin{bmatrix} 1 & 2 \\ 0 & 2 \end{bmatrix}$$,
$$C \Rightarrow U = \begin{bmatrix} 1 & 2 & 2 & 4 \\ 0 & 2 & 0 & 4 \end{bmatrix} \Rightarrow R = \begin{bmatrix} 1 & 0 & 2 & 0 \\ 0 & 1 & 0 & 2 \end{bmatrix}$$, C消元之后, 前两列为 **pivot columns**, 后两列为 **free columns**. 那么特解 special solution 就容易得到啦. 怎么得到, 自己去想(自由变量分别设为1,0等).

Once we have the special solutions, we have the whole nullspace.

## 2.2 Echelon Matrices

$$ U = \begin{bmatrix} p & x & x & x & x & x & x \\0 & p & x & x & x & x & x \\0 & 0 & 0 & 0 & 0 & p & x \\0 & 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix}$$.

> Three pivot variables $$x_1, x_2, x_6$$.    
> Four free variables $$x_3, x_4, x_5, x_7$$.   
> Four special solutions in $$N(U)$$  

$$A$$ is $$m$$ by $$n$$ matrix. If $$n>m$$, there must be free variables, then, equation $$Ax=0$$ must have nonzero vectors in its nullspace.

## 2.3 The Reduced Row Echelon Matrix R

$$ U = \begin{bmatrix} 1 & 1 & 2 & 3 \\ 0 & 0 & 4 & 4 \\ 0 & 0 & 0 & 0 \end{bmatrix} \Rightarrow R=rref(A) = \begin{bmatrix}
1 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0\end{bmatrix}$$.

---

# 3.The rank and the row reduced form #

## 3.0 Key ideas

1. The rank $$r$$ of $$A$$ is the number of pivots(which are 1's in $$R=rref(A)$$).
2. The $$r$$ pivot columns of $$A$$ and $$R$$ are in the same list *pivcol*.
3. Those $$r$$ pivot columns are not combinations of earlier columns.
4. The $$n-r$$ free columns are combinations of earlier columns(pivot columns).
5. Those combinations (using $$-F$$ taken from $$R$$) give the $$n-r$$ special solutions to $$Ax=0$$ and $$Rx=0$$. They are the $$n-r$$ columns of the nullspace matrix $$N$$.

## 3.1 Rank and the row reduced form

> **DEFINITION**: The rank of $$A$$ is the number of pivots. This number is $$r$$.

**Every "free column" is a combination of earlier pivot columns**.

Example:

$$A = \begin{bmatrix}1 & 1 & 2 & 4 \\ 1 & 2 & 2 & 5 \\ 1 & 3 & 2 & 6\end{bmatrix} \Rightarrow U = \begin{bmatrix} 1 & 1 & 2 & 4 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 0 & 0\end{bmatrix} \Rightarrow R = \begin{bmatrix} 1 & 0 & 2 & 3 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

"Pivot column": 有主元 pivot 的那一列.

**Rank one matrix**:

$$A = \begin{bmatrix} 1 & 3 & 10 \\ 2 & 6 & 20 \\ 3 & 9 & 30 \end{bmatrix} \Rightarrow R = \begin{bmatrix} 1 & 3 & 10 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$$.

Pivot row [1 3 10]  
Pivot variable $$x_1$$    
Free variables $$x_2, x_3$$  
special solutions: $$ s_1 = \begin{bmatrix} -3 \\ 1 \\ 0 \end{bmatrix}, s_2 = \begin{bmatrix} -10 \\ 0 \\ 1 \end{bmatrix}$$.

**The rank $$r$$ is the "dimension" of the column space.**  So the number $$n-r$$ is the "dimension" of the Nullspace of $$A$$.

---

## 3.2 The Pivot Columns  

**The pivot columns are not combinations of earlier columns**. The free columns are combinations of earlier columns. These combinations are the special solutions.

## 3.3 The Special Solutions

> $$Ax=0$$ has $$r$$ pivots and $$n-r$$ free variables: $$n$$ columns minus $$r$$ pivot columns. The nullspace matrix $$N$$ contains the $$n-r$$ special solutions. Then $$AN=0$$.

> $$Ax=0$$ has $$r$$ independent equations so it has $$n-r$$ independent solutions.

# 4.The complete solution to $$Ax=b$$ #
# 5.Independence, Basis, and Dimension #
# 6.Dimension of the Four Subspaces #

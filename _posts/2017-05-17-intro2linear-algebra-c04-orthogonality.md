---
layout: post
title: 线性代数:向量空间-子空间
categories:
- Math
- Linear Algebra
---

The review of the key ideas are from chapter 4 of Introduction to Linear Algebra, Book of Gilbert Strang, editon 4th.

1. Orthogonality of the Four Subspaces
2. Projections
3. Least Square Approximations
4. Orthogonal Bases and Gram-Schmidt

# 1. Orthogonality of the Four Subspaces #

## 1.0 Key ideas

1. Subspaces $$\bf V$$ and $$\bf W$$ are orthogonal if every $$v$$ in $$\bf V$$ is orthogonal to every $$w$$ in $$\bf W$$.
2. $$\bf V , \bf W$$ are "orthogonal complements" if $$\bf W$$ contains all vectors perpendicular to $$\bf V$$(and vice versa). Inside $$R^n$$, the dimensions of complements $$\bf V$$ and $$\bf W$$ add to $$n$$.
3. The nullspace $$N(A)$$ and the row space $$C(A^T)$$ are orthogonal complements, from $$Ax=0$$. Similarly $$N(A^T)$$ and $$C(A)$$ are orthogonal complements.
4. Any $$n$$ independent vectors in $$R^n$$ will span $$R^n$$.
5. Every $$x$$ in $$R^n$$ has s nullspace component $$x_n$$ and a row space component $$x_r$$.

## 1.1 Introduction

**Orthogonal vectors** $$v^T w = 0$$ and $$\parallel v \parallel ^2 + \parallel w \parallel ^2 = \parallel v + w \parallel ^2$$.

$$Ax$$:

- At the first level: this is only numbers
- At the second level: a combination of column vectors
- At the third level: subspaces

**The row space is perpendicular to the nullspace of $$A$$**: $$Ax=0$$.  

**The column space is perpendicular to the nullspace of $$A^T$$**: $$A^Tx=0$$, the row space of $$A^T$$ is the column space of $$A$$. When $$b$$ is outside the column space -- when we want to solve $$Ax=b$$ and can't do it -- then this nullspace of $$A^T$$ comes into its own. It contains the error $$e=b-Ax$$ in the "least-squares" solution.

**DEFINITION** Two subspaces $$V, W$$ of a vector space are orthogonal if every vector $$v$$ in $$V$$ is perpendicular to every vector $$w$$ in $$W$$.

> **Orthogonal subspaces** $$v^T w = 0 $$ for all $$v$$ in $$V$$ and all $$w$$ in $$W$$.

**The row space $$C(A^T)$$ and nullspace $$N(A)$$ are orthogonal subspaces inside $$R^n$$**.

**The left nullspace $$N(A^T)$$ and the column space $$C(A)$$ are orthogonal in $$R^m$$.**

## 1.2 Orthogonal Complements

**DEFINITION** The **orthogonal complement** of a subspace $$V$$ contains every vector that is perpendicular to $$V$$. This orthogonal subspace is denoted by $$V^{\perp}$$ ("$$V$$ perp").

![orthogonal](https://dn-jeremiahzhang.qbox.me/image/math/orthogonal.JPG)

|**Fundamental Theorem of Linear Algebra, Part 2**|
| --- |
|**$$N(A)$$ is the orthogonal complement of the row space $$C(A^T)$$(in $$R^T$$)**|
|*$$N(A^T)$$ is the orthogonal complement of the column space $$C(A)$$ (in $$R^m$$) **|

Part 1 gave the dimensions of the subpaces. Part 2 gives the 90° angles between them.

![orthogonal2](https://dn-jeremiahzhang.qbox.me/image/math/orthogonal2.JPG)

## 1.3 Combining Bases from Subspaces

> Any n independent vectors in $$R^n$$ must span $$R^N$$. So they are a basis.
> Any n vectors that span $$R^n$$ must be independent. So they are a basis.

$$A_{n,n}$$:

> If the n columns of $$A$$ are independent, they span $$R^n$$. So $$Ax=b$$ is solvable.
> If the n columns span $$R^n$$, they are independent. So $$Ax=b$$ has only one solution.

怎么就觉得上面的叙述是一样的, 看不出多大差异, 那么到底有没有差别呢?

---

# 2. Projections #
# 3. Least Square Approximations #
# 4. Orthogonal Bases and Gram-Schmidt #

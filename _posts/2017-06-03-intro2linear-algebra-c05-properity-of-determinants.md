---
layout: post
title: 线性代数:行列式性质
categories:
- Math
- Linear Algebra
---

The contents are from chapter 5 section 1 of Introduction to Linear Algebra, Book of Gilbert Strang, edition 4th.

- The properties of determinants

## 1.Key ideas

1. The determinant is defined by $$\det I = 1$$, sign reversal, and linearity in each row.
2. After elimination $$\det A$$ is $$\pm$$(product of the pivots).
3. The determinant is zero exactly when A is not invertible.
4. Two remarkable properties are $$\det{AB}=(\det A)(\det B)$$ and $$\det{A^T}=\det A$$.

## 2.Introduction

The determinant of an n by n matrix can be found in three ways:

- **pivot formula**: multiply the n pivots(times 1 or -1)
- **"big" formula**: add up n! terms(times 1 or -1)
- **cofactor formula**: combine n smaller determinants(times 1 or -1)

Let me show a simple example to get the determinant of matrix A.

$$A=\begin{bmatrix} a & b \\ c & d\end{bmatrix}, \det A = ad - bc, A^{-1} = \frac{1}{detA} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$

*The determinant changes sign when tow rows (or two columns) are exchanged*.

Row and column are equal.

Applications：

1. Determinants give $$A^{-1}$$ and $$A^{-1}b$$(this formula is called **Cramer's Rule**).
2. When the edges of a box are the rows of A, the **volume** is $$\mid \det A \mid$$.
3. For n special numbers $$\lambda$$, called **eigenvalues**, the determinants of $$A - \lambda I$$ is zero. This is a truly important application and it fills Chapter 6.

## 3.The properties of the determinant

1. $$\det I = 1$$
2. The determinant changes sign when two rows are changed(sign reversal).交换行，行列式值符号改变。（列也是一样）
3. **Key**：The determinant is a linear function of each row separately.
  - a. $$\begin{vmatrix} ta & tb \\ c & d \end{vmatrix} = t \begin{vmatrix} a & b \\ c & d\end{vmatrix}$$
  - b. $$\begin{vmatrix} a+a' & b+b' \\ c & d\end{vmatrix} = \begin{vmatrix} a & b \\ c & d\end{vmatrix} + \begin{vmatrix} a' & b' \\ c & d\end{vmatrix}$$
4. If two rows of A are equal, then $$\det A = 0$$.(两行相等, 行列式为0)
5. **Key**: Subtracting a multiple of one row from another row leaves $$\det A $$ unchanged.
  - Using rule 3 + 4 to prove this.
  - Example: $$\begin{vmatrix} a & b \\ c-la & d-lb \end{vmatrix} = \begin{vmatrix} a & b \\ c & d\end{vmatrix}$$.
6. A matrix with a row of zeros has $$\det A = 0$$ 一行全为0, 则行列式为0.
7. If A is triangular then $$\det A = a_{11}a_{22} \cdots a_{nn} =$$ product of diagonal entries.
  - ex: $$\begin{vmatrix} a & b \\ 0 & d \end{vmatrix} = ad, \begin{vmatrix} a & 0 \\ c & d \end{vmatrix} = ad$$.
8. If A is singular then $$\det A = 0$$. If A is invertible then $$\det A \neq 0$$.
9. $$\det{AB} = \det A \det B$$.
  - ex: $$\begin{vmatrix} a & b \\ c & d \end{vmatrix} \begin{vmatrix} p & q \\ r & s \end{vmatrix} = \begin{vmatrix} ap+br & aq+bs \\ cp+dr & cq+ds \end{vmatrix}$$.
10. $$\det{A^T} = \det A$$.
  - Prove:
    - 分解:$$A=LU$$, 其中$$L$$为下三角矩阵, $$U$$为上三角矩阵.
    - $$A^T=U^T L^T$$
    - $$\mid U^T \mid \mid L \mid = \mid L \mid \mid U \mid$$.

注: 1-8 为行列式自身的性质, 知道这些可以推导性质.

---

```
@Anifacc
2017-06-03
```

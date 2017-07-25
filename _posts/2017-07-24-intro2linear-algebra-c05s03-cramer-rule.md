---
layout: post
title: 线性代数:克莱姆法则-逆矩阵和体积
categories:
- Math
- Linear Algebra
---

The contents are from chapter 5 section 3 of Introduction to Linear Algebra, Book of Gilbert Strang, edition 4th.

5.3节内容主要关于克莱姆法则Cramer's Rule，在克莱姆法则基础上求解矩阵的逆矩阵；以及矩阵的应用-利用矩阵求解三角形的面积与平行六面体（3-dimension box）的体积；最后介绍向量叉乘（cross product），向量三重积（triple product）与矩阵行列式、体之间的关系。

- 克莱姆法则与逆矩阵
- 三角形的面积
- 向量叉乘
- 三重积=行列式=体积

## 1.克莱姆法则与逆矩阵

记得大学时候，克莱姆法则直接记住就可以使用了，然而也不知道如何推导出克莱姆法则。Gilbert Strang 的这本教材，讲解克莱夫法则的由来。我们一起来看看。

从前面的章节中，我们知道可使用消元法来解线性方程组$$Ax=b$$，如果矩阵A的逆矩阵存在，我们也可以通过其逆矩阵$$A^{-1}$$来解线性方程组。另外一种方法就是使用克莱姆法则，那么如何使用克莱姆法则解线性方程组呢？

关键之处在于此：

$$\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{bmatrix}
\begin{bmatrix}
x_1 & 0 & 0 \\
x_2 & 1 & 0 \\
x_3 & 0 & 1
\end{bmatrix} =
\begin{bmatrix}
b_1 & a_{12} & a_{13} \\
b_2 & a_{22} & a_{23} \\
b_3 & a_{32} & a_{33}
\end{bmatrix} = B_1$$

使用行列式的性质9，有

$$(\det A)(x_1) = \det B_1,\ or \ , x_1=\frac{\det {B_1}}{\det A}$$

这样就求出x中的一个值$$x_1$$.

按照上面的想法，我们可以得到$$x_2$$:

$$\begin{bmatrix}
\boldsymbol{a_1} & \boldsymbol{a_2} & \boldsymbol{a_3}
\end{bmatrix}
\begin{bmatrix}
1 & x_1 & 0 \\
0 & x_2 & 0 \\
0 & x_3 & 1
\end{bmatrix} =
\begin{bmatrix}
\boldsymbol{a_1} & \boldsymbol b & \boldsymbol{a_3}
\end{bmatrix} = B_2$$

对上面的矩阵求行列式得$$(\det A)(x_2)=\det{B_2}$$.

同样的方式，可得到$$x_3$$的表达式。

这样就得到**克莱姆法则**：

如果矩阵A的行列式不为0，可利用一下式子求解线性方程组$$\boldsymbol{Ax=b}$$：

$$x_1 = \frac{\det{B_1}}{\det A}, x_2 = \frac{\det{B_2}}{\det A}, \cdots, x_n = \frac{\det{B_n}}{\det A}$$.

其中矩阵$$B_j$$为用向量$$b$$取代系数矩阵A中的第j列后的矩阵。

根据克莱姆法则，我们可使用该法则计算一个矩阵的逆矩阵，前提是该矩阵存在逆矩阵。以3x3的矩阵A为例。

根据逆矩阵定义：$$AA^{-1}=I$$，可拆解该式为三个线性方程组：

$$\boldsymbol{Ax_1}=\begin{bmatrix}1 \\ 0 \\ 0 \end{bmatrix},
\boldsymbol{Ax_2}=\begin{bmatrix}0 \\ 1 \\ 0 \end{bmatrix}, \boldsymbol{A_3}=\begin{bmatrix}0 \\ 0 \\ 1\end{bmatrix}.$$

这样我们根据克莱姆法则，计算得到$$x_1,x_2,x_3$$三个向量，这三个向量组成A的逆矩阵$$A^{-1}=\begin{bmatrix} x_1 & x_2 & x_3 \end{bmatrix}$$.

其中向量的各个元素可通过克莱姆法则求得。比如向量$$x_1$$的各元素计算可按照上面克莱姆法则。

$$\det B_1=
\begin{vmatrix}
1 & a_{12} & a_{13} \\
0 & a_{22} & a_{23} \\
0 & a_{32} & a_{33}
\end{vmatrix} = C_{11}$$,

$$\det B_2 =
\begin{vmatrix}
a_{11} & 1 & a_{13} \\
a_{21} & 0 & a_{23} \\
a_{31} & 0 & a_{33}
\end{vmatrix} = C_{12}$$,

$$\det B_3 =
\begin{vmatrix}
a_{11} & a_{12} & 1 \\
a_{21} & a_{22} & 0 \\
a_{31} & a_{32} & 0
\end{vmatrix} = C_{13}$$.

那么逆矩阵$$A^{-1}$$第一列元素（即向量$$x_1$$的元素）分别为；

$$(A^{-1})_{11} = \frac{C_{11}}{\det A}, (A^{-1})_{21} = \frac{C_{12}}{\det A}, (A^{-1})_{31} = \frac{C_{13}}{\det A}$$.

依次类推，按克莱姆法则计算**A逆矩阵的公式**为：

$$(A^{-1})_{ij}=\frac{C_{ji}}{\det A}, \ and \ A^{-1} = \frac{C^T}{\det A}$$.

将上面公式展开进一步观察：

$$\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{bmatrix}
\begin{bmatrix}
C_{11} & C_{21} & a_{31} \\
C_{12} & C_{22} & C_{32} \\
C_{13} & C_{23} & C_{33}
\end{bmatrix} =
\begin{bmatrix}
\det A & 0 & 0 \\
0 & \det A & 0 \\
0 & 0 & \det A
\end{bmatrix}$$.

根据行列式的计算方法，我们可以看出该公式成立。

上式等式右边对角线上的元素为A的行列式，通过 如下公式得到：

$$a_{11}C_{11}+a_{12}C_{12}+a_{13}C_{13}=\det A$$

对于非对角线上的元素，我们可以看出：

$$a_{21}C_{11}+a_{22}C_{12}+a_{23}C_{13}=0$$.

为什么上式为0，如果我们将矩阵A的第一列全部换成A的第二行元素，因为有两行元素相同，所以其行列式为0。

---

## 2.三角形的面积

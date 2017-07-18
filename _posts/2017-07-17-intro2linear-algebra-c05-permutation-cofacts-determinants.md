---
layout: post
title: 线性代数:行列式计算方法
categories:
- Math
- Linear Algebra
---

The contents are from chapter 5 section 2 of Introduction to Linear Algebra, Book of Gilbert Strang, edition 4th.

5.2节内容主要是求解行列式的三种方法：

- 主元求解行列式（The pivot formula）
- 主公式求解行列式（The big formula for determinants）  
- 代数余子式求解行列式（Determinant by Cofactors）

课本内容一步步引导，因为之前学过线性代数，这部分内容不难看懂。

# 0. 主要内容回顾

1. 矩阵A，没有经过行变换，其行列式为主元乘积，$$\det A=(product \ of \ pivots)$$。在左上三角矩阵中，$$\det A_k =(product \ of \ the \ first \ k \ pivots)$$，也就是说，前k行和k列组成的矩阵$$A_k$$，其行列式为前k个主元的乘积。  
2. 大公式中的每一项都使用矩阵中的每一行，每一列，且没有重复项。n!个项中一半的符号为正，一半符号为负。  
3. 矩阵A的代数余子式$$C_{ij}$$为$$(-1)^{i+j}$$乘上去掉矩阵A第i行第j列后矩阵的行列式，
4. 当矩阵的某一行或某一列出现0的数目多时，只需计算少数几个代数余子式就能得到矩阵行列式。

## 1. 主元求行列式

> 例1

$$A = \begin{bmatrix}
0 & 0 & 1 \\
0 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix},
PA = \begin{bmatrix}
4 & 5 & 6 \\
0 & 2 & 3 \\
0 & 0 & 1
\end{bmatrix},
\det A = -(4)(2)(1)$$

将矩阵A的第一行和第一列互换，则得到矩阵 PA，A的行列式值$$(-1)^{i} * 主元乘积$$，其中i为行变换次数。因为置换矩阵（Permutation Matrix）$$P = \begin{bmatrix}
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0
\end{bmatrix}$$, 其行列式为(-1).

$$\begin{align}
\det (PA) &= 4*2*1 = 8  \\
          &=(\det P)(\det A) \\
          &= \begin{vmatrix}
              0 & 0 & 1 \\
              0 & 1 & 0 \\
              1 & 0 & 0
              \end{vmatrix}
              \begin{vmatrix}
              0 & 0 & 1 \\
              0 & 2 & 3 \\
              4 & 5 & 6
              \end{vmatrix} \\
          &= (-1)(\det A)
\end{align}$$,

因此可以得到$$\det A = -(4)(2)(1) = -8$$

> 例 2: -1,2,-1 矩阵 A

$$A=\begin{bmatrix}
2  & -1 & ~     & ~     & ~ \\
-1 & 2  & -1    & ~     & ~ \\
~  & -1 & 2     & \cdot & ~ \\
~  & ~  & \cdot & \cdot & -1 \\
~  & ~  & ~     & -1    & 2  
\end{bmatrix} =LU=
\begin{bmatrix}
1            &              &       &                & \\
-\frac{1}{2} & 1            &       &                & \\
             & -\frac{2}{3} & 1     &                & \\
             &              & \cdot & \cdot          & \\
             &              &       & -\frac{n-1}{n} & 1
\end{bmatrix}
\begin{bmatrix}
2 & -1 & & & \\
  & \frac{3}{2} & -1 & & \\
  &             & \frac{4}{3} & -1 & \\
  &             &             & \cdot & \cdot \\
  &             &             &       & \frac{n+1}{n}
\end{bmatrix}$$

$$\det A = 1(2)(\frac{3}{2})(\frac{4}{3}\cdots\frac{n+1}{n}) = n+1$$

上三角矩阵U的主元来自于A矩阵的左上角子矩阵[2]。前k个主元来自矩阵A的(kxk)左上三角子矩阵$$A_k$$。其行列式$$\det A_k = d_1 d_2 \cdots d_k$$。也就是说-1,2,-1矩阵A=LU中，U的主元可通过下面的方式求得：

$$d_k = \frac{d_1 d_2 \cdots d_k}{d_1 d_2 \cdots d_{k-1}}=\frac{\det A_k}{\det A_{k-1}}$$.

## 2. 主公式求解行列式（Big Formula）

如何得到求一个矩阵行列式？有一种方法是采用主公式（Big Formula）。这个公式如何得来，书本讲解到位。从简单出发，慢慢推演。

先来看看矩阵A：

$$A=\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}$$,
$$[a \ b] = [a \ 0] + [0 \ b]$$,
$$[c \ d] = [c \ 0] + [0 \ d]$$,
$$\begin{align}
\det A &= \begin{vmatrix}
            a+0 & 0+b \\
            c & d
          \end{vmatrix} \\
       &= \begin{vmatrix}
            a & 0 \\
            c & d
          \end{vmatrix} +
          \begin{vmatrix}
            0 & b \\
            c & d
          \end{vmatrix} \\
       &= \begin{vmatrix}
            a   & 0 \\
            c+0 & 0+d
          \end{vmatrix} +
          \begin{vmatrix}
            0 & b \\
            c+0 & 0+d
          \end{vmatrix} \\
       &= \begin{vmatrix}
            a & 0 \\
            c & 0
          \end{vmatrix} +
          \begin{vmatrix}
            a & 0 \\
            0 & d
          \end{vmatrix} +
          \begin{vmatrix}
            0 & b \\
            c & 0
          \end{vmatrix}+
          \begin{vmatrix}
            0 & b \\
            0 & d
          \end{vmatrix}
\end{align}$$

这样A的行列式就分解为$$2^2=4$$个行列式，但这里有两个行列式中都存在一列元素全为0（第1个和第4个行列式），这两个行列式值为0。那么就剩下$$2!=2$$个行列式：

$$\begin{align}
\det A &= \begin{vmatrix}
            a & 0 \\
            0 & d \\
          \end{vmatrix} +
          \begin{vmatrix}
          0 & b \\
          c & 0
          \end{vmatrix} \\
       &= ad \begin{vmatrix}
              1 & 0 \\
              0 & 1
              \end{vmatrix}
              +
          bc \begin{vmatrix}
              0 & 1 \\
              1 & 0
              \end{vmatrix} \\
       &= ad - bc
\end{align}$$

对于3x3的矩阵A的行列式,按上面的方式，展开求解行列式，展开项个数为$$3^3=27$$个，其中存在某一列都为0的行列式，这些行列式值为0，最后就剩下$$3!=6$$个行列式，如下所示。

$$\begin{align}
\det A &= \begin{vmatrix}
            a_{11} & a_{12} & a_{13} \\
            a_{21} & a_{22} & a_{23} \\
            a_{31} & a_{32} & a_{33}
          \end{vmatrix} \\
       &= \begin{vmatrix}
            a_{11} &  &  \\
             & a_{22} &  \\
             &  & a_{33}
          \end{vmatrix} +
          \begin{vmatrix}
             & a_{12} &  \\
             &  & a_{23} \\
            a_{31} &  &
          \end{vmatrix} +  
          \begin{vmatrix}
             &  & a_{13} \\
            a_{21} &  &  \\
             & a_{32} &
          \end{vmatrix} \\
        &+\begin{vmatrix}
            a_{11} &  &  \\
             &  & a_{23} \\
             & a_{32} &
          \end{vmatrix} +
          \begin{vmatrix}
               & a_{12} &  \\
              a_{21} &  &  \\
               &  & a_{33}
          \end{vmatrix} +
          \begin{vmatrix}
               &  & a_{13} \\
               & a_{22} &  \\
              a_{31} &  &
          \end{vmatrix}                 
\end{align}$$

上面等式右边六个行列式中的列的数目分别为

- (1,2,3)：基准顺序
- (2,3,1)：需要经过两次(偶数次)列变换变为(1,2,3)，(行列式符号为+)
- (3,1,2)：需要经过两次(偶数次)列变换变为(1,2,3)，(行列式符号为+)
- (1,3,2)：需要经过1次(奇数次)列变换变为(1,2,3)，(行列式符号为-)
- (2,1,3)：需要经过1次(奇数次)列变换变为(1,2,3)，(行列式符号为-)
- (3,2,1)：需要经过1次(奇数次)列变换变为(1,2,3)，(行列式符号为-)

所以可以得到；

$$\begin{align}
\det A &= a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32} \\
      &+ (-1)a_{11}a_{23}a_{32} + (-1)a_{12}a_{21}a_{33} + (-1)a_{13}a_{22}a_{31}
\end{align}$$

那么nxn的矩阵A，A的行列式为n!个分解行列式的和。

$$\det A = \sum(-1)^p a_{1\alpha}a_{2\beta}\cdots a_{n\omega} = Big~Formula$$

其中，p为$$(\alpha, \beta, \cdots, \omega)$$变为(1,2,3, ...,n)所需进行的列变换的次数。

## 3. 代数余子式求矩阵行列式

通过矩阵的代数余子式（cofacts）来计算矩阵行列式，本质和上一节主公式求解行列式相同。上一节是将矩阵的行列式拆解为多个简单的行列式，而这一节的方法类似，将矩阵行列式拆解，只是拆解方法不一样，我们且来看一个3x3矩阵的行列式拆解。

$$\begin{align}
\det A &= \begin{vmatrix}
            a_{11} & a_{12} & a_{13} \\
            a_{21} & a_{22} & a_{23} \\
            a_{31} & a_{32} & a_{33}
          \end{vmatrix} \\
       &= \begin{vmatrix}
            a_{11} & & \\
            & a_{22} & a_{23} \\
            & a_{32} & a_{33}
          \end{vmatrix} +
          \begin{vmatrix}
            & a_{12} & \\
            a_{21} & & a_{23} \\
            a_{31} & & a_{33}
          \end{vmatrix} +
          \begin{vmatrix}
            &  & a_{13}\\
            a_{21} & a_{22} & \\
            a_{31} & a_{32} &
          \end{vmatrix} \\
       &= a_{11}(-1)^{1+1}\begin{vmatrix}
                  a_{22} & a_{23} \\
                  a_{32} & a_{33}
                  \end{vmatrix} +
          a_{12}(-1)^{1+2} \begin{vmatrix}
          a_{21} & a_{23} \\
          a_{31} & a_{33}
          \end{vmatrix} +
          a_{13}(-1)^{1+3} \begin{vmatrix}
          a_{21} & a_{22} \\
          a_{31} & a_{32}
          \end{vmatrix}
\end{align}$$

我们可以看到，将矩阵A的第一行中每个元素单独提取出来（比如元素$$a_{1j}$$），分别去掉其所在行和列（去掉第一行第j列），那么就剩下一个2x2的子矩阵$$M_{1j}$$(上式中的2x2的行列式所对应的矩阵)，定义第一行元素对应的代数余子式为

$$C_{1j} = (-1)^{1+j} \det M_{1j}$$

那么任意矩阵A的行列式可以用代数余子式形式表示：

$$\det A = a_{11}C_{11} + a_{12}C_{12} + \cdots + a_{1n}C_{1n}$$

我们选取的是第一行，我们也可以选取矩阵中的任意一行或一列来计算矩阵的行列式。比如提取第i行，则代数余子式为：

$$C_{ij} = (-1)^{i+j} \det M_{ij}$$

行列式表示为：

$$\det A = a_{i1}C_{i1} + a_{i2}C_{i2} + \cdots + a_{in}C_{in}$$

同样，我们可以提取第j列，则代数余子式表示为：
$$C_{ij} = (-1)^{i+j} \det M_{ij}$$

行列式表示为：

$$\det A = a_{1j}C_{1j} + a_{2j}C_{2j} + \cdots + a_{nj}C_{nj}$$

代数余子式表示行列式，并求取行列式挺容易理解吧。

---

```
@Anifacc
2017-07-18 Beta 1.0
```

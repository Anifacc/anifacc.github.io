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

## 二阶常系数微分方程
## 2x2矩阵的稳定性
## 矩阵的指数

---

[^1]:   G. Strang, Introduction to Linear Algebra(4th edition)

---
layout: post
title: 顽想学概率一-4w-随机变数-累积分布函数-概率质量函数
categories:
- Math
- Probability
---

顽想学概率一 第四周的主题:

- 随机变数（Random Variable, R.V.）
- 累积分布函数（Cumulative Distribution Function, CDF）
- 概率质量函数（Probability Mass Funcion, PMF）

开始讲师就讲到:

> 练习是为了思考，而非为了得到正确答案，面对未知的世界，我们要有解决未知问题的勇气，信心和能力。

---

## 1.随机变数

- 定义：
  - 用来把实验结果（outcome）数字化的表示方式
- 目的：
  - 让概率的推导更数学、更简明
- 表示：
  - 通常用大写的英文字母表示：**X**
- 本质：
  - 随机变数X是一种函数，喂X吃一个outcome，就吐出一个对应的数字。$$X: S \rightarrow R$$
- 类型：
  - 离散
  - 连续

## 2.累积分布函数

- 定义：
  - 对任意一个随机变数X，定义其CDF为函数：$$F_X{x}=P(X\leqx)$$
- 用途：
  - 1 计算X落在某范围内的机率例如$$P(a < X \leq b) = F_X(b) - F_X(a)$$

离散随机变数之CDF：

$$ F_X(x^+) = F_X(x) $$  
$$ F_X(x^-) = F_X(x) - P(X=x) $$  

连续随机变数之CDF：

$$ F_X(x^-)=F_X(x)=F_X(x^+) $$  

共同性质：

$$ F_X(-\infty) = 0 $$   
$$ F_X(\infty) = 1 $$   
$$ 0 \leq F_X(x) \leq 1 $$  

## 3.概率质量函数

- 定义：
  - 对于任一个整数值的离散随机变数 **X**， 定义其PMF为函数$$ p_X(x)=P(X=x) $$
- PMF和CDF关系
  - PMF --> CDF : ex, $$ F_X(x) = \sum_{n=-\infty}^{\mid x \mid}p_X(n) $$
  - CDF --> PMF : ex, $$ P_X(x) = F_X(x^+) - F_X(x^-)


  概率分布（Probability Distribution）

  > 任何一个PMF(或是PDF)都称为是一种**机率分布**（将总和为1的机率分布在点上之故）。

---

```
@Anifacc
2017-06-02
```

---
layout: post
title: 顽想学概率一-5w-离散概率分布
categories:
- Math
- Probability
---

顽想学概率一 第五周的主题:

- 离散概率分布

---

## 离散概率分布

1. 阿宅告白：成功机率为0.3，不成功誓不休。 问到第5次才告白成功之机率？
2. 孙文革命：成功机率为0.1，不成功誓不休。问到第11次才成功之机率？
3. 六脉神剑：那纠缠狂妈宝废物段誉每次要打出六脉神剑，打的出来的机率为0.1。他在10次才打出六脉神剑的机率？

> 实验中出现某结果机率已知，重复操作实验至该结果出现为止。在意某结果是在第几次实验才首次出现
--->Geometric 概率分布

阿宅告白：成功机率为 p，不成功誓不休。 问到第X次才告白成功. $$X=x$$的机率?

机率：$$ (1-p)^{x-1}p $$

| PMF | CDF    |
| :------------- | :------------- |
| $$ p_X(x)= \begin{cases} (1-p)^{x-1} \cdot p & x =1, 2, 3, \cdots \\  0 & otherwise \end{cases} $$ |   $$ \begin{align} F_X(x) &= \sum_{n=-\infty}^{\lvert x \rvert}p_X(n) \\ &= \begin{cases} \sum_{n=1}^{\lvert x \rvert} (1-p)^{n-1}p = p \cdot \frac{1-(1-p)^{\mid x \mid}}{1-(1-p)} & x \geq 1 \\ 0 & x < 1 \end{cases} \\ &= \begin{cases} 1-(1-p)^{\mid x \mid} & x \geq 1 \\ 0 & otherwise \end{cases} \end{align} $$ |

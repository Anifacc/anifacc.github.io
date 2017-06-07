---
layout: post
title: 顽想学概率一-5w-离散概率分布
categories:
- Math
- Probability
---

顽想学概率一 第五周的主题:

- 离散概率分布 Probability Distribution
  - Bernoulli 伯努利分布
  - Binomial 二项分布
  - Uniform 均匀分布
  - Geometric 几何分布
  - Pascal 帕斯卡分布
  - Possion 泊松分布

---

## 离散概率分布

### Bernoulli 伯努利分布

观察：

1. 丢丢硬币：非正即反，正面机率：0.5
2. 宅男告白：非成即败，成功机率：0.7

> 1次实验，2种结果。在意某结果是否发生 ---> Bernoulli 机率分布

1次试验，试验成功机率为p，X表示成功次数。**X~Bernoulli( p )**

| PMF | CDF     |
| :------------- | :------------- |
| $$p_X(x) = \begin{cases} p & x = 1 \\ 1-p & x = 0 \\ 0 & otherwise \end{cases}$$       | $$F_X(x) = sum_{n=-\infty}^{\mid x \mid}p_X(n) = \begin{cases} 0 & x<0 \\ 1-p & 0 \leq x < 1 \\ 1 & x \geq 1 \end{cases}$$|

### Binomial 二项分布

观察：

1. 丢丢硬币：丢10次，8次为正面的概率？
2. 阿宅鼓起勇气搭讪10人，若每次搭讪成功的机率为0.6，10次成功8次的机率为？

> 作n次实验，1个机率，在意n次实验出现某结果k次的机率 --> Binomial 机率分布

n次伯努利试验，每次试验成功机率为p，做n次试验，X表示成功次数。 **X~BIN(n, p)**

| PMF | CDF|
| :------------- | :------------- |
| $$\begin{align} p_X(x) &= P(X=x) \\ &= \binom{n}{x}p^x(1-p)^{n-x} \end{align}$$      | \begin{align} F_X(x) &= \sum_{m=-\infty}^{\mid x \mid}p_X(m) \\ &= \sum_{m=-\infty}^{\mid x \mid} \binom{n}{m}p^m(1-p)^{n-m} \end{align}$$ |


### Uniform 均匀分布

观察：

1. 丢公平骰：1到6点各点数出现 *机会均等*
2. 狡兔三窟：出现在窟1，2，3 *机会均等*

> 1次试验，n种结果，各结果出现概率均等。 在意某个结果发生与否 ---> Uniform 概率分布

一次试验，X 等于a，a+1，...，b 的概率均等。 **X~UNIF(a, b)**

| PMF | CDF     |
| :------------- | :------------- |
| $$ p_X(x) = \begin{cases} \frac{1}{b-a+1} & x = a, a+1, \cdots, b \\ 0 & otherwise \end{cases}$$      | $$ \begin{align} F_X(x) &= \sum_{n=-\infty}{\mid x \mid}p_X(x) \\ &= \begin{cases} 0 & x < a \\ \frac{\mid x \mid - a + 1}{b-a+1} & a \leq x < b \\ 1 & x \geq b \end{cases}  \end{align}$$       |

### Geometric 几何分布

观察：

1. 阿宅告白：成功机率为0.3，不成功誓不休。 问到第5次才告白成功之机率？
2. 孙文革命：成功机率为0.1，不成功誓不休。问到第11次才成功之机率？
3. 六脉神剑：那纠缠狂妈宝废物段誉每次要打出六脉神剑，打的出来的机率为0.1。他在10次才打出六脉神剑的机率？

> 实验中出现某结果机率已知，重复操作实验至该结果出现为止。在意某结果是在第几次实验才首次出现
--->Geometric 概率分布

阿宅告白：成功机率为 p，不成功誓不休。 问到第X次才告白成功. $$X=x$$的机率?

机率：$$(1-p)^{x-1}p$$

| PMF | CDF    |
| :------------- | :------------- |
| $$p_X(x)= \begin{cases} (1-p)^{x-1} \cdot p & x =1, 2, 3, \cdots \\  0 & otherwise \end{cases}$$ |   $$\begin{align} F_X(x) &= \sum_{n=-\infty}^{\lvert x \rvert}p_X(n) \\ &= \begin{cases} \sum_{n=1}^{\lvert x \rvert} (1-p)^{n-1}p = p \cdot \frac{1-(1-p)^{\mid x \mid}}{1-(1-p)} & x \geq 1 \\ 0 & x < 1 \end{cases} \\ &= \begin{cases} 1-(1-p)^{\mid x \mid} & x \geq 1 \\ 0 & otherwise \end{cases} \end{align}$$ |

- Pascal 帕斯卡分布
- Possion 泊松分布

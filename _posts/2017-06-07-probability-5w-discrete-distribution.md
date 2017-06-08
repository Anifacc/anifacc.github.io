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
| $$p_X(x) = \begin{cases} p & x = 1 \\ 1-p & x = 0 \\ 0 & otherwise \end{cases}$$       | $$F_X(x) = \sum_{n=-\infty}^{\mid x \mid}p_X(n) = \begin{cases} 0 & x<0 \\ 1-p & 0 \leq x < 1 \\ 1 & x \geq 1 \end{cases}$$|

### Binomial 二项分布

观察：

1. 丢丢硬币：丢10次，8次为正面的概率？
2. 阿宅鼓起勇气搭讪10人，若每次搭讪成功的机率为0.6，10次成功8次的机率为？

> 作n次实验，1个机率，在意n次实验出现某结果k次的机率 --> Binomial 机率分布

n次伯努利试验，每次试验成功机率为p，做n次试验，X表示成功次数。 **X~BIN(n, p)**

| PMF | CDF|
| :------------- | :------------- |
| $$\begin{align} p_X(x) &= P(X=x) \\ &= \binom{n}{x}p^x(1-p)^{n-x} \end{align}$$      | $$\begin{align} F_X(x) &= \sum_{m=-\infty}^{\mid x \mid}p_X(m) \\ &= \sum_{m=-\infty}^{\mid x \mid} \binom{n}{m}p^m(1-p)^{n-m} \end{align}$$ |


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

### Pascal 帕斯卡分布

观察：

1. 六脉神剑：妈宝废物段誉每次打成功5次六脉神剑便功力耗尽。若每次打出来的概率为0.1，请问他在第9次时刚刚好功力耗尽的概率？
2. 自尊阿宅：阿宅邀约女店员失败的机率为0.9，若邀约失败达4次，阿宅便会自有损而放弃追求（这样能找到女朋友么！！！）。请问阿宅第7次邀约时决定放弃追求的概率？

> 实验中出现某结果的概率已知，重复操作实验直到该结果出现第k次结束。在意到底在第几次实验才结束 ---> Pascal 概率分布

对于段誉六脉神剑的情况：

- 第9次肯定是打出来的
- 前8次中有4次打出来，4次没打出来。那么这个的情况有 $$\binom{8}{4}$$
- 总概率为：$$\binom{8}{4}·0.9^4·0.1^5$$

一般化六脉神剑：妈宝废物段誉每次打成功k次六脉神剑便功力耗尽。若每次打出来的概率为p，请问他在第X次时刚刚好功力耗尽, $$X=x$$的概率？ **X~Pascal(k, p)**

- 第$$x$$次肯定打出来，而且是第$$k$$次打出来
- 前 $$x-1$$ 次中，有 $$k-1$$ 次打成功($$p^{k-1}$$)，$$(x-1)-(k-1)=(x-k)$$次没打成功$$(1-p)^{x-k}$$，发生的次数：$$\binom{x-1}{k-1}$$
- 总的概率: $$\binom{x-1}{k-1}·(1-p)^{x-k}·p^{k}$$

| PMF | CDF     |
| :------------- | :------------- |
| $$p_X(x)=\begin{cases} \binom{x-1}{k-1}·(1-p)^{x-k}·p^{k} &, x=k, k+1, \cdot \\ 0 & , otherwise \end{cases}$$      | $$\begin{align} F_X(x) &= P(X \leq x) \\ &= P(第k次成功在第x次以前发生) \\ &= P(在x次实验中 \geq k次成功) \\ &= P(Y \geq k), Y~BIN(x,p) \end{align}$$ |

> Pascal 又称为： Negative Binomial.


### Possion 泊松分布

观察:

1. 转角夜宵：在晚上平均每小时会有10人来跟转角哥买夜宵。问摆摊5小时有60人光顾之机率？
2. 费雯被嘘：费雯兄po文后，平均每分钟会有5人嘘之。问发文后二十分钟变成XX (100 嘘)之机率？

> 某结果出现之平均速率（rate:次数/时间）已知。问持续观察某时间长度后，看到该结果出现풌次之机率？ --> Poisson 机率分布

已知某事发生速率为每单位时间$$\lambda$$次，观察时间为T时间单位。X 为该观察时间内发生该事的总次数。 **$$X~POI(\lambda T)$$** --> $$\mu=\lambda T, X~POI(\mu) \Rightarrow P_X(x) = e^{-\mu}\frac{\mu^x}{x!}$$

| PMF | CDF    |
| :------------- | :------------- |
| $$p_X(x)=P(X=x)=e^{-\lambda T}\cdot \frac{(\lambda T)^{x}}{x!}$$ | $$\begin{align} F_X(x) &= \sum_{n=-\infty}{\mid x \mid}p_X(x) \\ &= \begin{cases} \sum_{n=-\infty}{\mid x \mid}e^{-\mu}\frac{\mu^n}{n!} & , x = 0, 1, 2, ... \\ 0 & , otherwise \end{cases}\end{align}$$ |

---

```
@Anifacc
2017-06-08
```

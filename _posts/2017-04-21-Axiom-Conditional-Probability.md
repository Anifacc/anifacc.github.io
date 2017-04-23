---
layout: post
title: 顽想学概率一-2w-极简公理-条件概率
categories:
- Math
---

coursera 台大 顽想学概率 一 第二周的主要内容是

- 概率的三个公理（神圣三公理）
- 条件概率

课程首先Beson反思自己的学习方式, 我自己的学习历程和Beson反省内容差不多, 大学考试成绩是很好, 但知识掌握的牢固程度又如何呢...?总之就是基础还是不牢固.

---

# 1 神圣3公理

## 公理Axiom:

> a statement or proposition that is regarded as being established, accepted, or self-evidently true.

- 不能被证明.
- 非常基本的性质.

> 公理1: 对任意事件A而言, $$P(A) \geq 0$$.

也就是任意事件发生的可能性都大于等于0, 要么不发生, 要么就有一定的可能性发生. 如果 P(A) = 1. 则事件A肯定发生.

> 公理2: $$P(S) = 1$$

对于整个样本空间, 其概率为1. 样本空间是概率实验所有可能结果的集合, 其概率之和肯定为1啦.

> 公理3: 
> 事件 $$A_1$$, $$A_2$$, ... 互斥, 
> $$ \Rightarrow P(A_1 \cup A_2 \cup A_3 \cup \cdots) $$
> $$ = P(A_1) + P(A_2) + P(A_3) + \cdots $$

事件A,B互斥有点类似*不是A死,就是B亡*, A发生则B不可能发生啦. 在集合里面就是 $$ A \cap B = \phi $$. AB是没有交集哒. 所以*公理3搭起了集合运算与概率运算的桥梁!*

**概率就这3个最基本的性质-公理, 其他性质都可以由这3个公理证明得到**.

## 衍生性质

1 若 $$ E = \{o_1, o_2, ..., o_n\} $$, 则 $$ P(E) = P(\{o_1\}) + P(\{o_2\}) + \cdots + P(\{o_n\}) $$

证明:

> $$ E = \{o_1\} \cup \{o_2\} \cup \cdots \cup \{o_n\} $$    
> 因 $$ \{o_1\}, \{o_2\}, \cdots \{o_n\} $$ 互斥    
> $$ \Rightarrow P(E) = P(E) = P({o_1}) + P({o_2}) + \cdots + P({o_n}) $$ (公理3)   

2 $$ P(\phi) = 0 $$: 不能可能事件(空集)发生的概率为0.

证明:

> because: $$ S \cup \phi = S $$, $$ S \cup \phi = \phi $$      
> $$ \Rightarrow S $$ 与 $$ \phi $$ 互斥    
> $$ \Rightarrow P(s) = P(S \cup \phi) = P(S) + P(\phi) $$  (公理3)    
> $$ \Rightarrow P(\phi) = 0 $$    

3 $$ P(A) = 1 - P(A^{c}) $$

证明:

> because: $$ A \cap A^{c} = \phi, A \cup A^{c} = S $$ 即 他俩互斥   
> $$ \Rightarrow 1 = P(S) = P(A \cup A^{c}) = P(A) + P(A^{c}) $$ (公理2 和 公理3)   
> $$ \Rightarrow P(A) = 1 - P(A^{c}) $$   

4 $$ P(A) = P(A-B) + P(A \cap B) $$

证明: 

> because: $$ (A-B) $$ 和 $$ A \cap B $$ 互斥, $$ A = (A-B) \cup (A \cap B) $$   
> $$ \Rightarrow P(A) = P((A-B) \cup (A \cap B)) $$   
> $$ \Rightarrow P(A) = P(A-B) + P(A \cap B) $$ (公理3)   

5 $$ P(A \cup B) = P(A) +P(B) - P(A \cap B) $$

证:

> $$ A \cup B = (A-B) \cup (A \cap B) \cup (B-A) $$    
> $$ \Rightarrow P(A \cup B) = P(A) - P(A \cap B) + P(B) $$ 使用公理3 和 上面的性质4  

6  切面包定理: if $$ C_1, C_2, \cdots, C_n $$ 互斥, 且 $$ C_1 \cup C_2 \cup \cdots \cup C_n = S $$, then 对任意事件 A: $$ P(A) = P(A \cap C_1) + P(A \cap C_2) + \cdots + (A \cap C_n) $$

证明:

> {1}  若 $$ C_1, C_2, \cdots, C_n $$ 互斥, 
> $$ \Rightarrow (A \cap C_1), (A \cap C_2), \cdots, (A \cap C_n) $$ 也互斥
> {2} 又 $$ C_1 \cup C_2 \cup \cdots \cup C_n = S $$
> $$ \Rightarrow (A \cap C_1) \cup (A \cap C_2) \cup \cdots \cup (A \cap C_n) = A $$
> {1} + {2} $$ \Rightarrow P(A) = P(A \cap C_1) + P(A \cap C_2) + \cdots + (A \cap C_n) $$

7 若 $$ A \subset B $$ then $$ P(A) \leq P(B) $$   

> 因为 $$ A \subset B \Rightarrow B = A \cup (B-A)$$
> 而 $$ A, (B-A) $$ 互斥
> $$ \Rightarrow P(B) = P(A) + P(B-A) \geq P(A) $$ (公理3 和 公理1)
> $$ \Rightarrow P(A) \leq P(B) $$

8 Boole's 不等式: 对于任意n个事件 $$ A_1, A_2, \cdots, A_n $$ 而言, $$ P(\cup_{i=1}^n A_i) \leq \sum_{i=1}^n P(A_{i}) $$

可以用归纳法, 先从 $$ A_1, A_2 $$两个开始证, 比如:

> 对于任意两个事件 $$ A_1, A_2 $$, 他们有可能互斥(交集为空集), 也有可能交集不为空集   
>   - 若互斥 $$ \Rightarrow P(A_1 \cup A_2) = P(A_1) + P(A_2) $$ 公理3
>   - 若有交集 $$ \Rightarrow P(A_1 \cup A_2) = P(A_1) + P(A_2) - P(A_1 \cap A_2) $$ 
> $$ \Rightarrow P(A_1 \cup A_2) \leq P(A_1) + P(A_2) $$ (公理1)

那么对于任意3个事件, $$ A_1, A_2, A_3 $$, 也类似, 可以将 $$ A_1, A_2 $$ 看作为一个事件, 那么证明就如上面的... 4,5,..., n个事件类似推导, 最后证明得到

> $$ P(\cup_{i=1}^n A_i) \leq \sum_{i=1}^n P(A_{i}) $$

9 Bonferroini's 不等式: 对于任意n个事件 $$ A_1, A_2, \cdots, A_n $$ 而言, $$ P(\cap_{i=1}^n A_i) \geq 1 - \sum_{i=1}^n P(A_{i}^c) $$

我们还是从任意两个事件 $$ A_1, A_2 $$来证明.

> 由上面衍生的性质 5 $$ P(A \cup B) = P(A) +P(B) - P(A \cap B) $$, 
> 即 $$ P(A_1 \cup A_2) = P(A_1) +P(A_2) - P(A_1 \cap A_2) $$
> $$ \Rightarrow P(A_1 \cap A_2) = P(A_1) +P(A_2) - P(A_1 \cup A_2) $$
> 由性质3. $$ P(A) = 1 - P(A^{c})$$
> $$ \Rightarrow P(A_1 \cap A_2) = 1 - P(A_{1}^{c}) + 1 - P(A_{2}^{c}) - P(A_1 \cup A_2) $$ 
> $$ \Rightarrow P(A_1 \cap A_2) = 1 - (P(A_{1}^{c})+P(A_{2}^{c}) + 1 - P(A_1 \cup A_2)$$
> 由公理2 可知 $$ 1 - P(A_1 \cup A_2) \geq 0 $$
> 所以有 $$ P(A_1 \cap A_2) \geq 1 - (P(A_{1}^{c})+P(A_{2}^{c}) $$ 得证

还是想上面一样, 任意3个事件, 将前两个事件并为一个事件, 与第三个事件如同上面一样证明.这样归纳证明即可.

---

# 2 条件概率

条件概率就是在一定条件Y下, 事件发生的概率$$ P(X \mid Y) $$.

## 条件概率性质

还是可以从公理得到

1. $$ P(X \mid Y) = \frac{P(X \cap Y) \geq 0 }{P(Y) \geq 0} \geq 0 $$   
2. $$ P(Y \mid Y) = 1 $$   
3. A, B互斥 $$ \Rightarrow P(A \cup B \mid Y) = P(A \mid Y) + P(B \mid Y) $$   

还有就是 Total Probability Law 和 Bayes Law.

> Total Probability Law: 

若 $$ C_1, C_2, ..., C_n $$ 互斥且 $$C_1 \cup C_2 \cup \cdots \cup C_n = S $$, 则对任意事件A, 有:   
$$ P(A) = P(A \mid C_1)P(C_1) + P(A \mid C_2)P(C_2) + \cdots + P(A \mid C_n)P(C_n) $$

证明和上面的切面包定理类似, 只不过换为条件概率而已.

> Baye's Rule

若 $$ C_1, C_2, ..., C_n $$ 互斥且 $$C_1 \cup C_2 \cup \cdots \cup C_n = S $$, 则对任意事件A, 有:

$$ P(C_j \mid A) = \frac{P(A \mid C_j)P(C_j)}{P(A \mid C_1)P(C_1) + P(A \mid C_2)P(C_2) + \cdots + P(A \mid C_n)P(C_n)} $$

---

# end

- 公理的意义
- 概率3公理
- 条件概率

---

```
@Anifacc
2017-04-21
```
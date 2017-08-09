---
layout: post
title: 初探决策树-ID3
categories:
- MachineLearning
---

本文是阅读 J.R.Quinlan 1986 论文后的简单笔记记录。

论文摘要：

论文介绍学习系统中TDIDT家族中的算法，详细介绍ID3方法（一种归纳方法），以及在噪声和不完全信息下ID3的处理方法，最后介绍归纳算法的核心方面内容并依次提出可能的改进方法。

详细阅读了TDIDT算法家族，并ID3方法。噪声和不完全信息下ID3处理方法，通读，暂时对不完全信息下的处理方法不理解。

- 为什么按论文中的方式计算期望值？

---

## The TDIDT family of learning system

Three principle dimensions along which machine learning systems can be classified.

- (根本学习策略) the underlying learning strategies used;
- (知识表达) the representation of knowledge acquired by the system; and
- (应用领域) the application domain of the system

The TDIDT(Top-Down Induction of Decision Trees) family tree:

- CLS(1963)
  - ID3(1979)
    - ASSISTANT(1984)
    - ACLS(1981)
      - Expert-Ease(1983)
      - EX-TRAN(1984)
      - RuleMaster(1984)

## The induction task

**丈母娘初选女婿**。一位母亲钱某为女儿小王选对象，赵某对其女婿（对象Object）的要求包括：

- 学历: {本科，研究生}
- 房子：{有(True)，无(False)}
- 年薪: {20w，30w+}.

某一天，小王在她母亲钱某的强烈要求下和某男小李（研究生毕业，无房，年薪20w）相亲，当然母亲钱某也在场。小李来到相亲地点（媒婆家），和母女两见面。见面后

```
...
钱某： 小李啊，大学里学什么专业呀？有么读研究生？
小李： 学的计算机，在xx大学读了计算机专业的研究生。
...

钱某：现在工作年薪多少？
小李：20w
....

钱某：小伙子，有房么？
小李: 阿姨，你好，我没有房子？（刚说完，钱某一脸鄙夷）
...
```

最后，很遗憾，小王相亲失败，小李未通过小王母亲钱某的初步考核。多次相亲之后，可得到一组数据集如下（其中P代表通过，N代表未通过）：

| No  | Attr:学历 | Attr:房子 | Attr:年薪 | Class：首轮通过 |
| :--| -------   | -------- | ---------- | -------- |
| 1 | 本科 | 无 | 20w | N |
| 2 | 本科 | 无 | 30w+ | N |
| 3 | 本科 | 有 | 20w | N |
| 4 | 本科 | 有 | 30w+ | N |
| 5 | 研究生 | 无 | 20w | N |
| 6 | 研究生 | 无 | 30w+ | N |
| 7 | 研究生 | 有 | 20w | N |
| 8 | 研究生 | 有 | 30w+ | P |

我们假设只有两类：P（Positive）表示首轮通过；N（Negative）表示首轮未通过。该数据集中的数据，属性和类别都已经知晓，可用于作为训练集。

在机器学习中，所谓的训练集就是那些已经知道属性（Attribution）和类别（Class）的对象（Object）。从训练集中学习得到分类准则（classification rule）是归纳的任务（induction task）。因此首先要考虑对象属性提供的信息是否充足（能否准确反应出对象的类别特质）即信息完备与否。

决策树（decision trees）其实就是一种分类准则（classification rule）。上面的丈母娘挑女婿的案例（当然这个训练集数目很小，仅仅为了举例方便），可以用决策树进行分类，其图解如下：

![decision-trees-diag](https://dn-learnml.qbox.me/image/ai/decision-trees-examples.jpg)

对对象分类，我们从“树根”开始。最上层的“房子”（属性）是决策树的根（root），其下的分支（branch）为“房子”对应的属性值{有, 无}。在{有}这个属性值下，有“年薪”这个属性作为分支节点另外再产生分支，直到得到最底层的叶子（P or N）；另外{无}属性值下，直接得到叶子（N）。

如果通过训练集训练，得到如上图所示的决策树，那么再来一个新对象（新样本），喂给这个决策树，就可以吐出一个outcome（P or N）。

这样，小王妈妈钱某可以利用这个决策树初选女婿啦，只要知道那些相亲对象的基本信息（属性）就能得到结果。这是一个简单的决策树案例（也是个特例），对于初选女婿这个案例，可以有多种决策树。

只要对象属性信息完备，就可能得到许多分类正确的决策树。树根不同，分支节点不同，决策树就不同。两个决策树之间，在训练集上的分类准确性相同的话，似乎更简单的那个更容易捕捉问题的内在结构<sup>[^1]</sup>。

根据训练集我们可以得到决策树，关键还是要看训练得出的决策树在新样本上的分类准确性（预测准确性）。

## ID3

接着上面的例子🌰，通过训练集训练得到多个决策树，我们可以从中选择最简单的一个决策树去解决分类问题。如果决策树数目很多，怎么办？可以采用ID3<sup>[^1]</sup>算法。如果训练集中样本数目非常多，属性也非常多，ID3无需太多计算就能得到合理且良好的决策树。该算法缺点就是可能忽视更好的决策树。

**ID3的基本原理**: 从训练集中随机划分出一个子集，称其为window，从这个window中训练得到决策树（该决策树能正确分类window中的所有样本）；接下来，该决策树用于其他不在window中的训练样本的分类。如果对剩余样本全部分类正确，则表明该决策树在训练集上分类都正确，程序结束；如果对剩余样本的分类有错误，将出现分类错误的训练样本纳入window中，重复上面的步骤，直到程序可以结束。

决策树的结构如下：

```
- 训练集中随机产生的子集C(P类个数为p，N类个数为n)
  + 根据属性 A 判别归纳：
    + 样本中属性值为 A_1 的划分为数据集 C_1（其中类别为P，N的个数为p_1, n_1）
    + 样本中属性值为 A_2 的划分为数据集 C_2（其中类别为P，N的个数为p_2, n_2）
    + 样本中属性值为 A_3 的划分为数据集 C_3（其中类别为P，N的个数为p_3, n_3）
    + ...
    + 样本中属性值为 A_w 的划分为数据集 C_w（其中类别为P，N的个数为p_w, n_w）

- 对 C_1, C_2, ... , C_w 重复上述操作（使用其他属性 B,C,D...），直到得到决策树的树叶（完成决策树生产）
```

决策树的结构如上所描述，但是那么问题来了，如何从随机生成的window（随机产生的训练样本子集）中生成决策树？ID3采用以信息为基础的方法，这个方法依赖两个假设：

1. 任何一个正确的决策树会以类别P, N在子集C中的所占比例为概率对对象进行分类。即一个对象或样本判别为P类的概率为：$$\frac{p}{p+n}$$, 判别为N类的概率为：$$\frac{n}{p+n}$$
2. 决策树对样本分类，最终返回值为一个类别（比如 P或N）。我们可以认为决策树是类别（ P,N）的来源，则得到类别所需的期望信息量（expected information）以下式表示：
$$I(p,n) = -\frac{p}{p+n}\log_2\frac{p}{p+n} - \frac{n}{p+n}\log_2\frac{n}{p+n}$$

根据上面的决策树结构，以属性A为决策树的根，根据其属性值{$$A_1, A_2, ..., A_w$$}将集合C划分为{$$C_1, C_2, ..., C_w$$}，则在子集$$C_i$$基础上构建子决策树所需的期望信息量（分支所需期望信息量）为$$I(p_i, n_i)$$，$$p_i, n_i$$分别为子集$$C_i$$中P类和N类的样本数目.

则属性A为根的决策树的期望信息量为分支所需期望信息量的加权值：

$$E(A) = \sum_{i=1}^{w} \frac{p_i+n_1}{p+n}I(p_i,n_i)$$

最后得到属性A的信息增益（Information gained by branching A）为  

$$gain(A)=I(p,n) - E(A)$$

选择最大信息增益值对应的那个属性作为分支节点。ID3会检查所有属性，选择最大gain值对应的那个属性来形成决策树。这样一层层生成决策树分支，直到结束。

让我们继续以**丈母娘初选女婿**为例子。表中的数据集为集合C(P类样本数为1，N类样本书为7), 则

$$I(p,n) = -\frac{1}{8}\log_2\frac{1}{8} - \frac{7}{8}\log_2\frac{7}{8}=0.544 \ bits$$

若以属性“房子”为根节点，如下图所示。
![decision-trees-diag](https://dn-learnml.qbox.me/image/ai/decision-trees-examples.jpg)

属性值{有}将集合C划分为一个子集$$C_1$$，其中P类样本数目为1($$p_1=1$$)，N类样本数目为3($$n_1=3$$),$$I(p_1,n_1)=0.811$$

属性值为{无}将集合C划分为一个子集$$C_2$$，其中P类样本数目为1($$p_2=0$$)，N类样本数目为3($$n_2=4$$）,$$I(p_2,n_2)=0$$。

这样我们就可以得到

$$\begin{align}
E(房子) &= \frac{4}{8}I(p_1,n_1) + \frac{4}{8}I(p_2,n_2) \\
        &= 0.406 \ bits
\end{align}$$

最后得到属性“房子”的信息增益为  

$$gain(房子)=0.544 - E(房子) = 0.138 \ bits$$

对于其他属性也可以进行相同的分析，得到：

$$ gain(学历) = 0.138 \ bits $$
$$ gain(年薪) = 0.138 \ bits $$

这里的例子是个特例，只是为举例而已。 因为三个属性对应的gain值相等，我就选择属性“房子”作为根节点。因为子集$$C_2$$中只有4个N类别的样本，即得到树叶（N）；另外一个分支({有})划分的子集$$C_1$$中包含1个P类和3个N类的样本，我们就得继续确定下一层决策树的根（从整体来看是分支节点），方法同上。只是我们要去除属性“房子”，因为我们已经选择该属性作为上一层决策树的根了。那么我们还剩下“学历”和“年薪”这两个属性，此时集合C变为子集$$C_1$$，按照上面的方法计算两属性对应的gain值，选择最大gain值对应的那个属性作为该层分支节点的根。在上面的决策树图中，我选择属性“年薪”作为决策树的根（这一层gain(年薪)和gain(学历)值是一样的）。这样一层层下去，可得到上方图形中整一个决策树。

上面的特例只是为了举个例子，具体可参考文献1。


## C4.5

- [C4.5: programs for machine learning](http://dl.acm.org/citation.cfm?id=152181)

```
@Anifacc
2017-06-21 09:22:04
```

[^1]: [Induction of Decision Trees](http://dl.acm.org/citation.cfm?id=637969)
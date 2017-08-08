---
layout: post
title: Python深度学习实战02-Keras构建一个神经网络
categories:
- Deep Learning
- Machine Learning
- Python
---

第一次使用python进行深度学习实战，使用Keras构建一个简单的多层感知器神经网络[^1]。让我们直入主题。

## 实战流程

- 加载数据
- 模型定义
- 模型编译
- 模型拟合
- 模型评估

## 1.加载数据

数据来源[^2]：[UCI Machine Learning Repository: Pima Indians Diabetes Data Set](http://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes)，数据直接使用url抓取，可参考文章[^3].

> Pima Indians Dataset

- 特征8个
    - 怀孕次数 Number of times pregnant
    - 口服葡萄糖耐量试验中2小时的血糖浓度 Plasma glucose concentration a 2 hours in an oral glucose tolerance test.
    - 舒张压 Diastolic blood pressure (mm Hg)
    - 肱三头肌皮肤褶皱厚度 Triceps skin fold thickness (mm)
    - 两个小时血清胰岛素 2-Hour serum insulin (mu U/ml)
    - 体质指数 BMI-Body mass index
    - 糖尿病血系功能 Diabetes pedigree function
    - 年龄（岁）  Age (years)
- 标签1个
    - 类别：5年内糖尿病发病（1代表发病，0为不发病）Class, onset of diabetes within five years

> It describes patient medical record data for Pima Indians and whether they had an
onset of diabetes within five years.

所以数据集中每个数据有8个属性（或特征），一个类别（或标签，1代表5年内发病，0表示5年内不发病）

若所有预测为不发病（0），则准确率为65.1%，因为数据集中，类别为0的数目为500，类别为1的数目为268，总个数为768. 数据加载代码如下

```
# 加载数据集 和 相关库
from keras.models import Sequential
from keras.layers import Dense

import numpy as np

import urllib

# 使用url来获取 diabetes dataset
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"

# 下载文件
raw_data = urllib.urlopen(url)

# 下载CSV文件 保存为 numpy matrix 格式
dataset = np.loadtxt(raw_data, delimiter=",")

# 数据特征与标签分开
X = dataset[:, 0:8]
y = dataset[:, 8]

# 随机数设置，便于产生相同的随机数
seed = 42
np.random.seed(seed)
```
## 2.模型定义

Keras中的神经网络模型是一层层网络模型。通过建立`Sequential`模型，设置参数，以构建我们想要的神经网络模型。在这里我们建立4层感知器神经网络模型。

- 第一层：输入层，神经元个数=数据集样本特征个数；
- 第二层：第一个中间隐含层，神经元个数设为12
- 第三层：第二个中间隐含层，神经元个数为8
- 第四层：输出层，神经元个数为1

其中输入层和输出层神经元个数可以通过训练样本的特征和类别来确定。中间隐含层层数以及隐含层神经元个数（节点）确定是神经网络拓扑结构确定中的一个难点。我们可以通过人为确定，也可以通过一些算法来确定隐含层层数以及节点数，这里暂且不深入。

神经元拓扑结构确定后，需要确定层与层间的激活函数，这个也需要选择。这里中间层的激活函数选用`rectifier activation function`[^4], 输出层的激活函数选用 `sigmoid function`[^5].

最后，前一层到下一层过程中的神经网络权重初始化选择使用 `uniform 分布`[^6]，`Keras`中默认权重初始化范围为0-0.05。

模型定义的代码如下：

```
# 创建模型
model = Sequential()

# 总4层神经网络
# 输入层 和 第一个隐含层 模型参数设置
# Dense calss 用来定义 完全连接层 的神经网络
# 其中
# - 参数：12 是第一个隐含层的神经元个数，即12个神经元
# - 参数 input_dim=8 表示输入层神经元个数为8
# - 参数 init='uniform' 表示输入层到第一个隐含层之间的权重w初始化方式为uniform分布（keras中的默认权重初始化范围为0-0.05）
# - 参数 activation 表示所使用的激活函数，‘relu’表示使用的是 rectifier activation function
#                   ‘sigmoid’ 表示所使用的是 sigmoid activation function
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))

# 第二个隐藏层模型参数设置: 8个神经元，权重初始方式为uniform分布形式，激活函数为 rectifier
model.add(Dense(8, init='uniform', activation='relu'))

# 第三层输出层模型参数设置：1个神经元输出，权重初始化方式：uniform，激活函数：sigmoid
model.add(Dense(1, init='uniform', activation='sigmoid'))
```

## 3.模型编译


定义好模型，我们就需要编译。 我们可以使用便捷数字处理库 under the covers （the so-called backend 后端）[^1]，如Theano 或 TensorFlow. 这些后端库会自动选择最佳方式去训练神经网络并进行预测。

编译时，我们必须定义其他一些属性以便神经网络的训练。神经网络训练就是解决问题的一组最佳参数。

需要定义的属性：

- *loss function* 损失函数：用于评估神经网络的权重。下面使用 logarithmic loss
- *optimizer* 优化器：用于搜索神经网络权重的方法，方法为： gradient descent algorithm: adam[^7]
- *metrics* 度量： 以什么方式来度量训练后神经网络的效果呢？这里可以设置。 用预测的准确性 accuracy 来度量神经网络训练效果。

代码如下：

```
# 编译模型
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
```

## 4.模型拟合

定义好模型，编译好模型，我们就需要拟合模型（fit model）。

参数：

- 模型训练迭代次数 `nb_epoch`
- 更新一次神经网络权重时使用的训练样本数目 `batch_size`

代码如下：

```
# Fit the model
model.fit(X, y, nb_epoch=150, batch_size=10)
```

## 5.模型评估

我们在整个数据集上训练好神经网络，此时我们在相同的数据集上评估网络的性能，即看看训练集上的模型准确性（训练准确率）。但是我们不知道在其他新的样本上网络的性能（泛化能力），怎么办呢？我们可将整个数据集划分为训练集和测试集。用训练集来训练模型，用测试集来评估模型在测试集上的性能（分类or预测准确率）。目前，我们只看模型在整个数据集上的预测准确率。

代码如下：

```
# Evaluate the model
# 在整个数据集（同时也是训练集）上评估模型性能
scores = model.evaluate(X, y)
print("{0}: {1:.2f}%".format(model.metrics_names[1], scores[1]*100))
```

结果为：

```
 32/768 [>.............................] - ETA: 0s
 acc: 78.39%
```

从结果中，我们看出所建立的神经网络模型在整个数据集上，预测或分类的准确率为78.39%。

## END

是不是很简单？用`Keras`创建一个极简神经网络模型，还能用于预测，是不是很好玩呢？我是觉得非常有趣。整个实战的Jupyter Notebook内容可在[Jupyter Notebook Viewer-DLWP-02-Diabetes](https://nbviewer.jupyter.org/github/JeremiahZhang/gopython/blob/master/AI/deep-learning-with-python/ch7-pima-indians-diabetes-nn.ipynb)查看


---

## ChangeLog

```
@anifacc
2017-08-08 Beta 1.0
```

[^1]:   [Deep Learning With Python](https://machinelearningmastery.com/deep-learning-with-python/)
[^2]:   [UCI Machine Learning Repository: Pima Indians Diabetes Data Set](http://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes)
[^3]:   [Introduction to Machine Learning with Python and Scikit-Learn](https://kukuruku.co/post/introduction-to-machine-learning-with-python-andscikit-learn/)
[^4]:   [Rectifier (neural networks) - Wikipedia](https://en.wikipedia.org/wiki/Rectifier_(neural_networks))
[^5]:   [Sigmoid function - Wikipedia](https://en.wikipedia.org/wiki/Sigmoid_function)
[^6]:   [Uniform distribution (continuous) - Wikipedia](https://en.wikipedia.org/wiki/Uniform_distribution_(continuous))
[^7]:   [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980)

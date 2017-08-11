---
layout: post
title: Python深度学习实战04-Keras和Scikit-learn结合解决机器学习问题
categories:
- DeepLearning
- MachineLearning
- Python
---

在上一个实战[Python深度学习实战03-模型性能评估](https://anifacc.github.io/deeplearning/machinelearning/python/2017/08/09/dlwp-setimate-model-performance/)中，我们学会使用'Scikit-learn'中的K-fold交叉验证来评估神经网络模型的性能。

这一次，我们可以通过`Keras`和`Scikit-learn`，一起解决一般性的机器学习问题。让我们开始吧。

内容包括：

Keras 模型和Python Scikit-Learn Library 结合，学习如何

- 如何将Keras模型和 scikit-learn 库结合
- 利用scikit-learn 库中的交叉验证(cross validation)来评估 Keras 模型
- 利用scikit-learn 库中的格点搜索(grid search)调节Keras模型超参数

---

## 1.前言

在Python中，Keras是用于深度学习的库，虽然受欢迎，但是Keras只关注深度学习。Keras追求极简，只关注我们快速使用、定义并建立深度学习模型。

Scikit-learn 是Python的另一个库，建立在用于有效数值计算的SciPy基础之上，常用于机器学习。

Keras中为深度学习模型能在scikit-learn中用于分类和回归提供了便捷的封装器（Wrapper），如`KearsClassifier`wrapper（用于在Keras中建立的神经网络分类器）。

---

# 2.利用交叉验证评估模型

在实战03中，我们知道如何评估算法性能，让我们再来看看，这次如何使用。

> 代码如下：

```
# 通过sklearn交叉验证评估用于糖尿病预测的神经网络模型
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier

from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score

import numpy as np

import urllib

# 函数用于建立模型，KerasClassifier需要的函数
def create_model():
    # 建立模型
    model = Sequential()
    model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
    model.add(Dense(8, init='uniform', activation='relu'))
    model.add(Dense(1, init='uniform', activation='sigmoid'))
    # 编译模型
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# 随机数设置，便于产生相同的随机数
seed = 42
np.random.seed(seed)

# 加载数据

# 使用url来获取 diabetes dataset
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
# 打开文件
raw_data = urllib.urlopen(url)
# 下载CSV文件 保存为np matrix格式
dataset = np.loadtxt(raw_data, delimiter=',')
# 数据特征与标签分开
X = dataset[:, 0:8]
y = dataset[:, 8]

# 建立模型
model = KerasClassifier(build_fn=create_model, nb_epoch=150, batch_size=10, verbose=0)

# 利用10-fold 交叉验证建立的模型
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(model, X, y, cv=kfold)
print("accuracy: {0} %".format(results.mean()*100))
```

> 结果

```
accuracy: 67.0454549068 %
```

对比上一篇[Python深度学习实战03-模型性能评估](https://anifacc.github.io/deeplearning/machinelearning/python/2017/08/09/dlwp-setimate-model-performance/)中的交叉验证，这里的更加快捷。

---

## 3.格点搜索调节深度学习模型参数

从上面我们知道`Keras`中就配有与`scikit-learn`库结合使用的功能（封装包，wrapper），如`KerasClassifier`,和`scikit-learn`结合使用，这个非常棒。另外我们还可以使用`scikit-learn`中的`grid search`来找到较佳的神经网络参数，不过这些参数仅包括：

- Optimizers：用于搜索神经网络权重的优化器
- Initializers: 初始化神经网络权重的方法
- Epochs：模型训练时迭代次数
- Batch_Size：用于更新网络权重的样本数目。

在这里，我们没有 search 神经网络的拓扑结构参数：网络层数，中间隐含层神经元（节点）个数。神经网络拓扑结构确定是一个难点。

下面的代码展示了利用`scikit-learn`格点搜索技术调节深度学习模型的参数。

利用 `GridSearchCV` 功能，我们可以看到神经网络可调节参数为：

```
optimizers = ['rmsprop', 'adam']
init = ['glorot_uniform', 'normal', 'uniform']
epochs = np.array([50, 100, 150])
batches = np.array([5, 10, 20])
```

这样就有`2x3x3x3=54`中不同参数的神经网络。如果数据集量非常大，那么search起来，计算时间相对样本量小的长很多。

> 代码

```
# 通过sklearn 格点搜索来调节 用于糖尿病预测神经网络模型的参数
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier

from sklearn.model_selection import GridSearchCV

import numpy as np

import urllib

# 函数用于建立模型，KerasClassifier需要的函数
## 选择rmsprop优化器，初始化权重方式为 glorot_uniform
def create_model(optimizer='rmsprop', init='glorot_uniform'):
    # 创建模型
    model = Sequential()
    model.add(Dense(12, input_dim=8, init=init, activation='relu'))
    model.add(Dense(8, init=init, activation='relu'))
    model.add(Dense(1, init=init, activation='sigmoid'))
    # 编译模型
    model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    return model

# 随机数设置，便于产生相同的随机数
seed = 7
np.random.seed(seed)

# 加载数据
## 使用url来获取 diabetes dataset
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
## 打开数据文件
raw_data = urllib.urlopen(url)
## 下载数据文件 保存为np matrix格式
dataset = np.loadtxt(raw_data, delimiter=',')
## 将数据特征与标签分开
X = dataset[:, 0:8]
Y = dataset[:, 8]

# 创建模型
model = KerasClassifier(build_fn=create_model, verbose=0)
# 格点搜索的步数，batch 样本数和优化器 参数设置
optimizers = ['rmsprop', 'adam']
init = ['glorot_uniform', 'normal', 'uniform']
epochs = np.array([50, 100, 150])
batches = np.array([5, 10, 20])
param_grid = dict(optimizer=optimizers, nb_epoch=epochs, batch_size=batches, init=init)
grid = GridSearchCV(estimator=model, param_grid=param_grid)
grid_result = grid.fit(X, Y)

# 结果显示
print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))

for params, mean_score, scores in grid_result.grid_scores_:
    print("%f (%f) with: %r" % (scores.mean(), scores.std(), params))
```

> 结果（部分）

```
Best: 0.697917 using {'init': 'normal', 'optimizer': 'adam', 'nb_epoch': 150, 'batch_size': 5}
0.636719 (0.024910) with: {'init': 'glorot_uniform', 'optimizer': 'rmsprop', 'nb_epoch': 50, 'batch_size': 5}
0.665365 (0.021236) with: {'init': 'glorot_uniform', 'optimizer': 'adam', 'nb_epoch': 50, 'batch_size': 5}
0.643229 (0.030647) with: {'init': 'glorot_uniform', 'optimizer': 'rmsprop', 'nb_epoch': 100, 'batch_size': 5}
...
```

> Best: 0.697917 using {'init': 'normal', 'optimizer': 'adam', 'nb_epoch': 150, 'batch_size': 5}

最好的分类结果约为 69.79%。其使用的参数设置，如上所示。

---

## 4.Sum

这一次实战中，我们简单了解了

- 如何将Keras模型和 scikit-learn 库结合
- 利用scikit-learn 库中的交叉验证(cross validation)来评估 Keras 模型
- 利用scikit-learn 库中的格点搜索(grid search)调节Keras模型超参数

代码具体运行结果参见 [Jupyter Notebook ch9](https://nbviewer.jupyter.org/github/JeremiahZhang/gopython/blob/master/AI/deep-learning-with-python/ch9-keras-model-with-sklearn-general-ML.ipynb)。

---

## 5.申明

本文实战是参考[Deep Learning With Python](https://machinelearningmastery.com/deep-learning-with-python/)一书后的笔记记录。

涉及内容版权归原作者[Jason Brownlee](http://machinelearningmastery.com/about/)所有。

---

## ChangeLog

```
@Anifacc  
2017-08-11 Beta 1.0
```

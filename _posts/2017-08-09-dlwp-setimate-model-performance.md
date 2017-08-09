---
layout: post
title: Python深度学习实战03-模型性能评估
categories:
- DeepLearning
- MachineLearning
- Python
---

在[Python深度学习实战02-Keras构建一个神经网络](https://anifacc.github.io/deeplearning/machinelearning/python/2017/08/08/Pima-Indians-NN-practicing/)中我们建立了第一个深度学习算法。现在我们要考虑如何评估算法（模型）性能。

设计和配置深度学习模型时，我们需要做很多决策。我们可以直接使用他人的网络模型和对应的改进版本。其实，我们可以根据实际数据自己进行尝试并评估算法，这是最好方法。这就需要我们确定：神经网络层数、神经元个数及类型；在此基础上，我们还要选择损失函数（loss function），激活函数（activation functions），优化程序（optimization procedure）和迭代次数（number of epochs）。

深度学习通常处理数据量非常大的问题，数据集中有成千上万的样本。所以我们需要一个鲁棒性测试工具，让我们能在这些不可见的数据中评估不同配置的算法的性能，并进行比较，以确定选用哪种（参数）配置比较好[^1]。

数据集样本数目非常多，若我们在这个数据集上进行算法评估，那么所消耗时间必定比数据量少的多。若我们可以通过其中的一些样本进行算法评估，同样可以确定算法配置，这样所消耗时间缩减，这想必极好。

---

## 1.划分数据

数据集样本数目越大和模型越复杂，训练算法的时间就越长。我们通常将数据集划分为训练集和测试集或训练集和验证集(validation datasets）。`Keras`中，我们可以使用两种方法来评估深度学习算法：

- 自动划分验证数据集
- 手动划分验证数据集

### 1.1 自动划分验证数据集

`Keras`可以从训练集中划分出一部分数据作为验证集，并在每一次迭代中，在这些验证集上评估模型的性能。那我们能怎么做呢？在模型拟合时的`fit() function`中设置`validation_split`参数。参见下面的代码，我们还是使用[Python深度学习实战02-Keras构建一个神经网络](https://anifacc.github.io/deeplearning/machinelearning/python/2017/08/08/Pima-Indians-NN-practicing/)中所使用的Diabetes Data Set。其中参数`validation_split=0.33`表示`Keras`将训练集中的33%样本划分为验证集，这部分验证集在每一次迭代中评估算法性能。

运行下面的代码，我们可以看到每一步迭代的结果，其中包括算法在训练集上的损失函数值、准确率以及在验证集上的损失函数值、准确率。

代码：

```
# 多层感知器 自动划分数据集
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
Y = dataset[:, 8]

# 随机数设置，便于产生相同的随机数
seed = 42
np.random.seed(seed)

# 创建模型
model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))
# 编译模型
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# 拟合模型
model.fit(X, Y, validation_split=0.33, nb_epoch=150, batch_size=10)
```

一部分结果：

```
Epoch 147/150
514/514 [==============================] - 0s - loss: 0.5179 - acc: 0.7607 - val_loss: 0.5648 - val_acc: 0.7126
Epoch 148/150
514/514 [==============================] - 0s - loss: 0.5324 - acc: 0.7451 - val_loss: 0.5824 - val_acc: 0.7087
Epoch 149/150
514/514 [==============================] - 0s - loss: 0.5154 - acc: 0.7490 - val_loss: 0.5727 - val_acc: 0.7008
Epoch 150/150
514/514 [==============================] - 0s - loss: 0.5121 - acc: 0.7646 - val_loss: 0.5837 - val_acc: 0.6890
```

### 1.2 手动划分验证数据集

从上面的代码中，我们观察到在模型拟合时，通过设置`fit()`函数中的参数可以自动从训练集划分出验证集。还有另一种方法，就是在模型创建之前，我们人为手动划分好训练集和验证集，参看下面的代码。通过调用 `sklearn` 模型选择中的 `train_test_split` 功能，我们同样可以将整个数据集划分为一定比例的训练集（67%）和验证集（或33%测试集）。运行代码，我们同样可以看到每一步迭代的结果，其中包括算法在训练集上的损失函数值、准确率以及在验证集上的损失函数值、准确率。

代码：

```
# 多层感知器 手动划分数据集
from keras.models import Sequential
from keras.layers import Dense

from sklearn.model_selection import train_test_split

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
Y = dataset[:, 8]

# 随机数设置，便于产生相同的随机数
seed = 42
np.random.seed(seed)

# 手动设置才整个数据集中划分出训练集和验证集（或测试集）
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=seed)

# 创建模型
model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))
# 编译模型
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# 拟合模型
model.fit(X_train, y_train, validation_data=(X_test, y_test), nb_epoch=150, batch_size=10)
```

一部分结果：

```
Epoch 147/150
514/514 [==============================] - 0s - loss: 0.4519 - acc: 0.7821 - val_loss: 0.5510 - val_acc: 0.7362
Epoch 148/150
514/514 [==============================] - 0s - loss: 0.4582 - acc: 0.7879 - val_loss: 0.5638 - val_acc: 0.7559
Epoch 149/150
514/514 [==============================] - 0s - loss: 0.4557 - acc: 0.7665 - val_loss: 0.5500 - val_acc: 0.7480
Epoch 150/150
514/514 [==============================] - 0s - loss: 0.4480 - acc: 0.7938 - val_loss: 0.5475 - val_acc: 0.7441
```

---

## 2.K-fold 交叉验证

机器学习算法评估的黄金准则就是：**K-fold交叉验证**（k-fold cross validation）。K-fold交叉验证方法[^2]将数据集划分为k个大小相似的互斥子集后，在每一个子集都尽可能保持数据分布的一致性，即从D中通过分层采样得到。然后，每一次用一个子集作为测试集，剩下的k-1个子集的并集作为训练集，直到每一个子集都做过测试集为止。这样我们就得到k组训练集和测试集，从而就能进行k次训练和测试，最后取这k个测试结果的平均值作为交叉验证结果。

然而，交叉验证通常不用于评估深度学习模型，因为它计算成本大。一般常用的k值为5或10，这样每一次就要构建5次或10次模型，然后得到平均值。不过呢，如果咱们的数据量不大，或者咱们的计算资源充足，k-fold交叉验证可以很好评估算法性能，如下面代码中的`for loop`所示。在下面的代码中，我们选择用 `scikit-learn` Python机器学习库中的`StratifiedKfold`类（分层Kfold）进行10-fold交叉验证。分层采样的意思是算法划分子集中的每一个类别的样本数目均衡。具体参见下面代码示例。

代码：

```
# 多层感知器 手动划分数据集
from keras.models import Sequential
from keras.layers import Dense

from sklearn.model_selection import StratifiedKFold

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
Y = dataset[:, 8]

# 随机数设置，便于产生相同的随机数
seed = 42
np.random.seed(seed)

# 定义 K-fold 交叉验证 参数
kfold= StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)

# Cross validation 交叉验证结果
cvscores = []

for train, test in kfold.split(X, Y):
    # 创建模型
    model = Sequential()
    model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
    model.add(Dense(8, init='uniform', activation='relu'))
    model.add(Dense(1, init='uniform', activation='sigmoid'))
    # 编译模型
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # 拟合模型
    model.fit(X[train], Y[train], nb_epoch=150, batch_size=10, verbose=0)
    # 评估模型
    scores = model.evaluate(X[test], Y[test], verbose=0)
    print("%s: %s %.2f%%" % (model.metrics_names[1], ':', scores[1]*100))
    cvscores.append(scores[1]*100)

print("The average score: %.2f%% (+/- %.2f%%)" % (np.mean(cvscores), np.std(cvscores)))
```

结果：

```
acc: : 63.64%
acc: : 77.92%
acc: : 74.03%
acc: : 75.32%
acc: : 67.53%
acc: : 75.32%
acc: : 74.03%
acc: : 77.92%
acc: : 76.32%
acc: : 71.05%
The average score: 73.31% (+/- 4.39%)
```

---

## End

现在我们已经知道如何评估模型性能，可以通过三种方式：

- 自动划分验证集
- 人为划分验证集
- K-fold 交叉验证

最常用的是第三种：交叉验证。然而在深度学习中，K-fold交叉验证的使用时，需要考虑计算成本和时间。具体的代码参见[Jupyter Notebook DLWP-CH8-Evaluate-Performance-of-Model](https://nbviewer.jupyter.org/github/JeremiahZhang/gopython/blob/master/AI/deep-learning-with-python/ch8-evaluate-performance-dl-model.ipynb)。

## Ref

- [Model (functional API) - Keras Documentation](https://keras.io/models/model/)

## ChangeLog

```
@Anifacc
2017-08-09 Beta 1.0
```

[^1]:   [Deep Learning With Python](https://machinelearningmastery.com/deep-learning-with-python/)
[^2]:   [《机器学习》 周志华 Amazon](https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/dp/B01ARKEV1G)

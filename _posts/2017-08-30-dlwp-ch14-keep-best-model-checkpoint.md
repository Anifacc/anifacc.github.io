---
layout: post
title: Python深度学习实战09-保存训练的最佳模型
categories:
- DeepLearning
- MachineLearning
- Python
---

深度学习模型花费时间大多很长, 如果一次训练过程意外中断, 那么后续时间再跑就浪费很多时间. 这一次练习中, 我们利用 Keras checkpoint 深度学习模型在训练过程模型, 我的理解是检查训练过程, 将好的模型保存下来. 如果训练过程意外中断, 那么我们可以加载最近一次的文件, 继续进行训练, 这样以前运行过的就可以忽略.

那么如何 checkpoint 呢, 通过练习来了解.

- 数据: Pima diabete 数据
- 神经网络拓扑结构: 8-12-8-1

## 1.效果提升检查

> 如果神经网络在训练过程中, 其训练效果有所提升, 则将该次模型训练参数保存下来.

`代码`:

```
# -*- coding: utf-8 -*-
# Checkpoint NN model imporvements

from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint

import numpy as np

import urllib

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
raw_data = urllib.urlopen(url)
dataset = np.loadtxt(raw_data, delimiter=",")

X = dataset[:, 0:8]
y = dataset[:, 8]

seed = 42
np.random.seed(seed)

# create model
model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))
# compile
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# checkpoint
filepath = "weights-improvement-{epoch:02d}-{val_acc:.2f}.hdf5"
# 中途训练效果提升, 则将文件保存, 每提升一次, 保存一次
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True,
                            mode='max')
callbacks_list = [checkpoint]
# Fit
model.fit(X, y, validation_split=0.33, nb_epoch=150, batch_size=10,
         callbacks=callbacks_list, verbose=0)
```

`部分结果`:

```
Epoch 00139: val_acc did not improve
Epoch 00140: val_acc improved from 0.70472 to 0.71654, saving model to weights-improvement-140-0.72.hdf5
Epoch 00141: val_acc did not improve
Epoch 00142: val_acc did not improve
Epoch 00143: val_acc did not improve
Epoch 00144: val_acc did not improve
Epoch 00145: val_acc did not improve
Epoch 00146: val_acc did not improve
Epoch 00147: val_acc did not improve
Epoch 00148: val_acc did not improve
Epoch 00149: val_acc did not improve
```

在运行程序的本地文件夹下, 我们会发现许多性能提升时, 程序自动保存的 hdf5 文件.

---

## 2.检查最好模型

> 检查训练过程中训练效果最好的那个模型.

`代码`:

```
# -*- coding: utf-8 -*-
# # checkpoint the weights for the best model on validation accuracy
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint

import numpy as np

import urllib

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
raw_data = urllib.urlopen(url)
dataset = np.loadtxt(raw_data, delimiter=",")

X = dataset[:, 0:8]
y = dataset[:, 8]

seed = 42
np.random.seed(seed)

# create model
model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))
# compile
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# checkpoint
filepath='weights.best.hdf5'
# 有一次提升, 则覆盖一次.
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True,
                            mode='max')
callbacks_list = [checkpoint]
# fit
model.fit(X, y, validation_split=0.33, nb_epoch=150, batch_size=10,
         callbacks=callbacks_list, verbose=0)
```

`部分结果`:

```
df5
Epoch 00044: val_acc did not improve
Epoch 00045: val_acc improved from 0.69685 to 0.69685, saving model to weights.best.hdf5
Epoch 00046: val_acc did not improve
Epoch 00047: val_acc did not improve
Epoch 00048: val_acc did not improve
Epoch 00049: val_acc improved from 0.69685 to 0.70472, saving model to weights.best.hdf5
...
Epoch 00140: val_acc improved from 0.70472 to 0.71654, saving model to weights.best.hdf5
Epoch 00141: val_acc did not improve
Epoch 00142: val_acc did not improve
Epoch 00143: val_acc did not improve
Epoch 00144: val_acc did not improve
Epoch 00145: val_acc did not improve
Epoch 00146: val_acc did not improve
Epoch 00147: val_acc did not improve
Epoch 00148: val_acc did not improve
Epoch 00149: val_acc did not improve
```

文件 `weights.best.hdf5` 将第140迭代时的模型权重保存.

---

## 3.加载保存模型

上面我们将训练过程中最好的模型保存下来, 如果训练有中断, 那么我们可以直接采用本次模型.

`代码`:

```
# -*- coding: utf-8 -*-
# Load and use weights from a checkpoint
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint

import numpy as np

import urllib

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
raw_data = urllib.urlopen(url)
dataset = np.loadtxt(raw_data, delimiter=",")

X = dataset[:, 0:8]
y = dataset[:, 8]

seed = 42
np.random.seed(seed)

# create model
model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))

# load weights 加载模型权重
model.load_weights('weights.best.hdf5')
# compile 编译
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print('Created model and loaded weights from hdf5 file')

# estimate
scores = model.evaluate(X, y, verbose=0)
print("{0}: {1:.2f}%".format(model.metrics_names[1], scores[1]*100))
```

`结果`:

```
Created model and loaded weights from hdf5 file
acc: 74.74%
```

---

## 4.Sum

本次练习如何将神经网络模型训练过程中, 训练效果最好的模型参数保存下来, 为以后的时候准备, 以备意外发生, 节省时间, 提高效率.

---

## 申明

本文实战是参考[Deep Learning With Python](https://machinelearningmastery.com/deep-learning-with-python/)一书后的笔记记录。

涉及内容版权归原作者[Jason Brownlee](http://machinelearningmastery.com/about/)所有。

## 用时

```
代码实现: 0: 28
阅读与记录: 0: 50
总: 1: 18
@Anifacc
2017-08-30
```

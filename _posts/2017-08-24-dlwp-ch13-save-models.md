---
layout: post
title: Python深度学习实战08-保存模型与权重
categories:
- DeepLearning
- MachineLearning
- Python
---

本次练习将已经训练好的神经网络模型保存至本地磁盘, 如果未来仍需使用, 则可以直接读取调用. 因为训练深度学习不易, 不要不保存, 要不然以后再次需要模型, 则又要花好多时间成本去训练.

本次所用是[Python深度学习实战02-Keras构建一个神经网络 · Anifacc](https://anifacc.github.io/deeplearning/machinelearning/python/2017/08/08/Pima-Indians-NN-practicing/)中的神经网络模型, 我们可以(1)将Keras神经网络模型结构保存为JSON文件,并读取;或者将Keras神经网络模型结构保存为YAML文件,并读取;(2)将模型却总保存为HDF5格式文件,并读取.

让我们开始吧:

## 1.HDF5

我们需要安装 Python 包 `h5py`, 这样我们就可以将文件保存为 HDF5(hierarchical data format) 格式文件, 该格式文件用来保存大型实数阵列, 对于存储神经网络模型参数极佳. 下面, 我们会将网络权重保存为 HDF5 格式文件, 并在以后读取.

因为使用的anaconda, 所以 conda list 发现已经安装到该包, 无需再次安装.

## 2.选择一:JSON

将网络模型保存为JSON格式. `Keras.model` 中自带 `to_json()`(转化为json文件)函数, 和 `model_from_json()`(读取模型json文件函数), 同时, `Keras` 模型自带`save_weights()` 和 `load_weights()` 函数保存模型权重和加载模型权重.

代码实现如下:
```
# -*- coding: utf-8 -*-

# MLP for json, hdf5
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

import os

import numpy as np

import urllib

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
raw_data = urllib.urlopen(url)
dataset = np.loadtxt(raw_data, delimiter=",")

X = dataset[:, 0:8]
y = dataset[:, 8]

seed = 42
np.random.seed(seed)

# Create model
model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(X, y, nb_epoch=150, batch_size=10, verbose=0)

# Evaluate the model
scores = model.evaluate(X, y)
print("{0}: {1:.2f}%".format(model.metrics_names[1], scores[1]*100))

# Here is the Point
# save model: JSON
model_json = model.to_json()
with open('model.json', 'w') as json_file:
    json_file.write(model_json)

# save weights: HDF5
model.save_weights("model.h5")
print("Save model to disk")

# later when you want to use the model
# load json and creat model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# load weight into new model
loaded_model.load_weights('model.h5')
print("Loaded model from disk, OK")

# Evaluate loaded model on test data
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
score = loaded_model.evaluate(X, y, verbose=0)

print("{0}: {1:.2f}%".format(loaded_model.metrics_names[1], scores[1]*100))
```

结果:

`32/768 [>.............................] - ETA: 0sacc: 78.39%`      
`Save model to disk`    
`Loaded model from disk, OK`   
`acc: 78.39%`

## 2.选择二:YAML

除了将模型保存为JSON格式, 我们也可以保存为YAML格式, 并读取.

代码如下:
```
# -*- coding: utf-8 -*-

# MLP for json, hdf5
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_yaml

import os

import numpy as np

import urllib

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
raw_data = urllib.urlopen(url)
dataset = np.loadtxt(raw_data, delimiter=",")

X = dataset[:, 0:8]
y = dataset[:, 8]

seed = 42
np.random.seed(seed)

# Create model
model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(X, y, nb_epoch=150, batch_size=10, verbose=0)

# Evaluate the model
scores = model.evaluate(X, y)
print("{0}: {1:.2f}%".format(model.metrics_names[1], scores[1]*100))

# Here is the Point
# save model to YAML
model_yaml = model.to_yaml()

with open('model.yaml', 'w') as yaml_file:
    yaml_file.write(model_yaml)

# save weights to hdf5
model.save_weights('model1.h5')
print("Save model to disk")

# later...
# Load YAML to create model
yaml_file = open('model.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()

loaded_model = model_from_yaml(loaded_model_yaml)

# load weights
loaded_model.load_weights('model1.h5')
print("loaded model from disk")

# evaluate loaded model on test data
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
score = loaded_model.evaluate(X, y, verbose=0)

print("{0}: {1:.2f}%".format(loaded_model.metrics_names[1], scores[1]*100))
```

结果:
`Save model to disk`
`loaded model from disk`
`acc: 78.39%`

---

## Sum

到这里, 我们学会将训练好的模型分别保存为JSON和YAML格式文件, 并将权重保存为HDF5格式文件.

## 申明

本文实战是参考[Deep Learning With Python](https://machinelearningmastery.com/deep-learning-with-python/)一书后的笔记记录。

涉及内容版权归原作者[Jason Brownlee](http://machinelearningmastery.com/about/)所有。

---

## 用时

```
代码实现: 0: 45
记录: 0: 25
总: 1:10
@Anifacc
2017-08-24
```

---
layout: post
title: Python深度学习实战10-模型训练历史
categories:
- DeepLearning
- MachineLearning
- Python
---
深度学习模型训练过程如何可视化, 或者说如何可视化模型训练时模型准确率等模型性能数据随时间变化程度. 本次实战就是让我们知道:

- 查看训练历史数据
- 绘制模型训练时, 模型在训练集和验证集上的准确率(in-sample-error, validation-error 可参考 learning from data 一书)随时间(迭代步数)变化的曲线.
- 绘制模型训练时, 模型在训练集和验证集上的代价函数随时间变化的曲线.

## 1.Model Training History

模型训练时的历史数据, 可以通过 `model.fit()` 返回的 `history` 对象获取. 比如, 在建立模型和编译模型之后, 我们进行模型拟合.

```
# 训练历史 图形化
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 随机数设定
seed = 7
np.random.seed(seed)

# 加载数据
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
df = pd.read_csv(url, header=None)
dataset = df.values

X = dataset[:, 0:8]
Y = dataset[:, 8]

# 创建神经网络模型 12-8-1
model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))

# 编译模型
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 模型拟合
history = model.fit(X, Y, validation_split=0.33, nb_epoch=150, batch_size=10, verbose=0)

# 列出历史数据
print(history.history.keys()) # 可查看 history 对象中有哪些历史数据
```

output: `['acc', 'loss', 'val_acc', 'val_loss']`

从输出中, 我们可以看出, `history` 对象中存储了 `'acc', 'loss', 'val_acc', 'val_loss'` 4种数据.

- `acc`: 模型在训练集上准确率
- `loss`: 模型在训练集上的代价函数值
- `val_acc`: 模型在验证集上准确率
- `val_loss`: 模型在验证集上的代价函数值

## 2.训练历史数据可视化

我们知道训练历史数据, 那么就可以绘制与时间(迭代步数)的曲线图.

```
# 总: 准确性
plt.figure(1)
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model Accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()

#  总: 代价函数值
plt.figure(2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()
```

output:

![model_acc](https://dn-learnml.qbox.me/image/ai/dlwp_ch15_model_acc.png)

上图中的曲线分别为模型在训练集(train), 验证集(validation)上准确率随迭代步数变化的曲线. 我们可以看出, 模型训练未收敛, 其准确率可以进一步提升.

![model_loss](https://dn-learnml.qbox.me/image/ai/dlwp_ch15_model_loss.png)

上图中的曲线分别为模型在训练集(train), 验证集(validation)上的代价函数值随迭代步数变化的曲线. 我们可以看出, 模型训练未收敛, 代价函数值可以进一步降低.

从上面的变化曲线, 我们也可以看看模型是否 overfitting[validation 准确率或loss值是否出现明显拐点.]

## 3.Sum

我们通过简单的例子, 查看深度学习模型训练过程的数据, 并进行可视化, 可以帮助我们判断模型是否收敛, 是否出现 overfit 现象.

具体代码与结果, 请参见: [deep_learning_with_python chapter 15 code Viewer](https://nbviewer.jupyter.org/github/JeremiahZhang/gopython/blob/master/AI/deep-learning-with-python/ch_15_understand_model_behavior_during_train_by_plotting_history.ipynb)

---

## 申明

本文实战是参考[Deep Learning With Python](https://machinelearningmastery.com/deep-learning-with-python/)一书后的笔记记录。

涉及内容版权归原作者[Jason Brownlee](http://machinelearningmastery.com/about/)所有。

## 用时

```
代码实现: 0: 29
阅读与记录: 0: 56
总: 1: 25
@Anifacc
2017-09-26
```

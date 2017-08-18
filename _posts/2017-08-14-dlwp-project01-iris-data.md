---
layout: post
title: Python深度学习实战05-Iris鸢尾花分类
categories:
- DeepLearning
- MachineLearning
- Python
---

这是书中的一个项目练习，我们选用 [Iris Data Set](https://archive.ics.uci.edu/ml/datasets/Iris) 数据集，利用`Keras`建立神经网络模型用来解决多分类问题。

在这个项目中，我们可学会：

- 如何加载数据
- 如何准备多类别数据
- 如何评估Keras神经网络模型(scikti-learn)

---

## 1.Iris Flowers 数据集

我们在这个项目中使用 [Iris Data Set](https://archive.ics.uci.edu/ml/datasets/Iris)，这个数据集中的每个样本有4个特征，1个类别。该数据集[^1]中的样本类别数为3类，每类样本数目为50个，总共150个样本。

属性信息：

- 花萼长度 sepal length(cm)
- 花萼宽度 sepal width(cm)
- 花瓣长度 petal length(cm)
- 花瓣宽度 petal width(cm)
- 类别：
    - Iris Setosa
    - Iris Versicolour
    - Iris Virginica

样本特征数据是数值型的，而且单位都相同（厘米）。

我们建立神经网络模型，经过已知数据集的训练，得到合适的网络参数，进而预测未知类别的iris plant的类别。这是一个多分类问题（3分类）。我们期望神经网络的目标分类准确率在95%-97%范围之内。

---

## 2.Import Classes and Functions

导入需要使用的类和函数.

```
import numpy as np

import pandas as pd

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
```

---

## 3.Initialize Random Number Generator

随机数生成初始设置.

```
# 随机数参数设置
seed = 7
np.random.seed(seed)
```

---

## 4.Load dataset

加载数据.

```
# 加载数据
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
df = pd.read_csv(url, header=None)
dataset = df.values

# 样本特征和类别划分
X = dataset[:, 0:4].astype(float)
Y = dataset[:, 4]
```

## 5.Encode The output variable

因为数据类别不是数值型的, 我们需要对它们编码, 将它们变为数值型. 这里的数据类别有三类(Iris-setosa, Iris-versicolor, Iris-virginica), 我们可将其变为:(1, 0, 0), (0, 1, 0), (0, 0, 1).

```
# encode class values as interger
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert intergers to dummy variables(i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)
```

可参考:

参考：

- [sklearn.preprocessing.LabelEncoder — scikit-learn 0.19.0 documentation](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)
- [4.8. Transforming the prediction target (y) — scikit-learn 0.19.0 documentation](http://scikit-learn.org/stable/modules/preprocessing_targets.html#preprocessing-targets)
- [Utils - Keras Documentation](https://keras.io/utils/#to_categorical)

---

## 6.Define NN model

确定神经网络模型, 其拓扑结构为4-4-3.

```
# 定义基准模型
def baseline_model():
    # 创建模型
    model = Sequential()
    model.add(Dense(4, input_dim=4, init='normal', activation='relu'))
    model.add(Dense(3, init='normal', activation='sigmoid'))
    # 编译模型
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

estimator = KerasClassifier(build_fn=baseline_model, nb_epoch=200, batch_size=5, verbose=0)
```

## 7.Evaluate the model with k-fold cross validation

K-fold交叉验证评估模型性能.

```
# 交叉验证准备
kfold = KFold(n_splits=10, shuffle=True, random_state=seed)

# 结果
results = cross_val_score(estimator, X, dummy_y, cv=kfold)

print("Accuracy: {0:.2f}% ({1:.2f}%)".format(results.mean()*100, results.std()*100))
```

结果:

```
Accuracy: 46.67% (22.11%)
```

这个模型分类的准确率没有过50%, 性能不好.  

## Sum

在这个简单的项目中, 我们学会如何建立神经网络模型, 并使用K-fold交叉验证来评估模型性能.

这里, 因为神经网络具有随机性, 即使同样的数据训练同样的神经网络,也可能得到不同的结果.  

参考:

- [Embrace Randomness in Machine Learning - Machine Learning Mastery](http://machinelearningmastery.com/randomness-in-machine-learning/)

代码具体运行结果参见 [Jupyter Notebook Viewer ch10](https://nbviewer.jupyter.org/github/JeremiahZhang/gopython/blob/master/AI/deep-learning-with-python/ch10-p01-multiclass-classification-of-flower-species.ipynb).

## 申明

本文实战是参考[Deep Learning With Python](https://machinelearningmastery.com/deep-learning-with-python/)一书后的笔记记录。

涉及内容版权归原作者[Jason Brownlee](http://machinelearningmastery.com/about/)所有。

## ChangeLog

```
@anifacc
2017-08-18 beta 1.0
```

[^1]:    [iris data info](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names)

---
layout: post
title: Python深度学习实战07-波士顿房价
categories:
- DeepLearning
- MachineLearning
- Python
---

本项目将神经网络模型应用于波士顿房价线性回归问题中, 并评估模型.

- 目的: 建立和评估用于线性回归问题(波士顿房价)神经网络模型
- 过程:
    - 加载数据
    - 正则化数据(标准化)
    - 建立神经网络模型
    - 交叉验证
    - 调节网络参数

项目内容主要包括:

1. 使用原始数据训练一个基准神经网络模型(13-13-1),用交叉验证评估模型, 并作为基准.
2. 正则化(Standardize)原始数据, 并训练该基准神经网络模型, 交叉验证评估模型;
3. 调整神经网络模型拓扑结构为(13-13-6-1), 使用正则化数据训练该基准神经网络模型, 交叉验证评估模型;
4. 调整神经网络模型隐含层节点数目(13-20-1), 使用正则化数据训练该基准神经网络模型, 交叉验证评估模型.

让我们开始吧.

## 1. 波士顿房价数据集

- 数据来源: [housing_data](https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data)
- 数据说明: [housing_name](https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.names)
- 数据信息:
    - 主要关注: 关注波士顿郊区的房价。
    - 数据样本数目: 506个
    - 样本特征: 13个
    - 样本房价(MEDV): 1个
```
        1. CRIM      per capita crime rate by town
        2. ZN        proportion of residential land zoned for lots over 25,000 sq.ft.
        3. INDUS     proportion of non-retail business acres per town
        4. CHAS      Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
        5. NOX       nitric oxides concentration (parts per 10 million)
        6. RM        average number of rooms per dwelling
        7. AGE       proportion of owner-occupied units built prior to 1940
        8. DIS       weighted distances to five Boston employment centres
        9. RAD       index of accessibility to radial highways
        10. TAX      full-value property-tax rate per $10,000
        11. PTRATIO  pupil-teacher ratio by town
        12. B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
        13. LSTAT    % lower status of the population
        14. MEDV: Median value of owner-occupied homes in $1000's
```

---

## 2.建立神经网络模型基准

使用原始数据训练一个基准神经网络模型(13-13-1),用交叉验证评估模型, 并作为基准.

```
# 基准神经网络模型
import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# 数据加载
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data"
df = pd.read_csv(url, delim_whitespace=True, header=None)
dataset = df.values
# 样本特征和标签划分
X = dataset[:, 0:13]
Y = dataset[:, 13]

# 基准NN模型
def baseline_model():
    # 创建模型
    model = Sequential()
    model.add(Dense(13, input_dim=13, init='normal', activation='relu'))
    model.add(Dense(1, init='normal'))
    # 编译模型
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

# 随机数参数
seed = 7
np.random.seed(seed)
# 评估模型
reg = KerasRegressor(build_fn=baseline_model, nb_epoch=100, batch_size=5, verbose=0)
kfold = KFold(n_splits=10, random_state=seed)
results = cross_val_score(reg, X, Y, cv=kfold)
print("基准NN(MSE-均方根值): {0:.2f} ({1:.2f})".format(results.mean(), results.std()))
```

结果: `基准NN(MSE-均方根值): 55.88 (40.94)`

---

## 3.标准化数据训练基准NN模型

正则化(Standardize)原始数据, 并训练该基准神经网络模型, 交叉验证评估模型;

```
# 正则化数据集训练神经网络模型
import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# 数据加载
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data"
df = pd.read_csv(url, delim_whitespace=True, header=None)
dataset = df.values
# 样本特征和标签划分
X = dataset[:, 0:13]
Y = dataset[:, 13]

# 基准NN模型
def baseline_model():
    # 创建模型
    model = Sequential()
    model.add(Dense(13, input_dim=13, init='normal', activation='relu'))
    model.add(Dense(1, init='normal'))
    # 编译模型
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

# 随机数参数
seed = 7
np.random.seed(seed)
# 正则化数据训练, 评估模型
estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasRegressor(build_fn=baseline_model, nb_epoch=50,
                                       batch_size=5, verbose=0)))
pipeline = Pipeline(estimators)
kfold= KFold(n_splits=10, random_state=seed)
results_stand = cross_val_score(pipeline, X, Y, cv=kfold)
print("标准化数据NN模型(MSE): {0:.2f} ({1:.2f})".format(results_stand.mean(),
                                                results_stand.std()))
```

结果: `标准化数据NN模型(MSE): 51.47 (34.84)`

---

## 4. 调整神经网络拓扑结构

调整神经网络模型拓扑结构为(13-13-6-1), 使用正则化数据训练该基准神经网络模型, 交叉验证评估模型;

```
# 调整神经网络拓扑结构: 4层 13 - [13 - 6] - 1
import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# 数据加载
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data"
df = pd.read_csv(url, delim_whitespace=True, header=None)
dataset = df.values
# 样本特征和标签划分
X = dataset[:, 0:13]
Y = dataset[:, 13]

# 模型定义
def larger_model():
    # 创建模型
    model = Sequential()
    model.add(Dense(13, input_dim=13, init='normal', activation='relu'))
    model.add(Dense(6, init='normal', activation='relu'))
    model.add(Dense(1, init='normal'))
    # 编译模型
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

# 随机数
seed = 7
np.random.seed(seed)
# 标准化数据训练模型并评估
estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasRegressor(build_fn=larger_model, nb_epoch=50, batch_size=5,
                                        verbose=0)))
pipeline = Pipeline(estimators)
kfold = KFold(n_splits=10, random_state=seed)
results_larger_nn = cross_val_score(pipeline, X, Y, cv=kfold)
print("Larger NN MSE: {0:.2f} ({1:.2f})".format(results_larger_nn.mean(),
                                               results_larger_nn.std()))
```

结果: `Larger NN MSE: 37.98 (35.32)`

---

## 5. 调整隐含层节点数

调整神经网络模型隐含层节点数目(13-20-1), 使用正则化数据训练该基准神经网络模型, 交叉验证评估模型.

```
# 神经网络中间层节点数多的模型: wider = 13-20-1
import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# 数据加载
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data"
df = pd.read_csv(url, delim_whitespace=True, header=None)
dataset = df.values
# 样本特征和标签划分
X = dataset[:, 0:13]
Y = dataset[:, 13]

# 模型定义
def wider_model():
    # 创建模型
    model = Sequential()
    model.add(Dense(20, input_dim=13, init='normal', activation='relu'))
    model.add(Dense(1, init='normal'))
    # 编译模型
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

# 随机数
seed = 7
np.random.seed(seed)
# 正则化数据训练模型并评估
estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasRegressor(build_fn=wider_model, nb_epoch=100,
                                        batch_size=5, verbose=0)))
pipeline = Pipeline(estimators)
kfold = KFold(n_splits=10, random_state=seed)
results_wider = cross_val_score(pipeline, X, Y, cv=kfold)
print("Wider NN MSE: {0:.2f} ({1:.2f})".format(results_wider.mean(),
                                               results_wider.std()))
```

结果: `Wider NN MSE: 47.47 (39.22)`

---

## Sum

在这次项目中, 我们进行4次练习:

1. 使用原始数据训练一个基准神经网络模型(13-13-1),用交叉验证评估模型, 并作为基准.
2. 正则化(Standardize)原始数据, 并训练该基准神经网络模型, 交叉验证评估模型;
3. 调整神经网络模型拓扑结构为(13-13-6-1), 使用正则化数据训练该基准神经网络模型, 交叉验证评估模型;
4. 调整神经网络模型隐含层节点数目(13-20-1), 使用正则化数据训练该基准神经网络模型, 交叉验证评估模型.

我们可以比较每一次的模型评估结果, 均方根值大小, 来评估那个神经网络模型相对较好.

---

## 申明

本文实战是参考[Deep Learning With Python](https://machinelearningmastery.com/deep-learning-with-python/)一书后的笔记记录。

涉及内容版权归原作者[Jason Brownlee](http://machinelearningmastery.com/about/)所有。

---

## 用时

```
代码实现: 0: 46
记录: 0: 40
总: 1:26
@Anifacc
2017-08-22
```

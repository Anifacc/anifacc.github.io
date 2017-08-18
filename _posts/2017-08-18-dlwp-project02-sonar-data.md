---
layout: post
title: Python深度学习实战06-Sonar信号分类
categories:
- DeepLearning
- MachineLearning
- Python
---

本回合, 我们设计不同的神经网络模型, 对Sonar信号进行分类练习.

## 1.Sonar 数据集

来源: [Index of /ml/machine-learning-databases/undocumented/connectionist-bench/sonar](https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/?C=D;O=D)

数据描述: [sonar_names](https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.names)

两类sonar信号辨别:

- M: 表示从金属缸返回的声纳信号(bounced off a metal cylinder), 总 111 个样本
- R: 表示从圆柱形的岩石返回的声纳信号(bounced off a roughly cylindrical rock) 总97个样本

总样本数目为208, 样本特征数为60, 这60个特征都是 0.0-1.0 范围内的数值.

> A benefit of using this dataset is that it is a standard benchmark problem. This means that we have some idea of the expected skill of a good model. Using cross validation, a neural network should be able to achieve performance around 84% with an upper bound on accuracy for custom models at around 88%.

---

# 2.神经网络模型性能基准

先定一个基准, 三层神经网络, 拓扑结构为60-60-1.

```
# Baseline NN model performance
import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense
from keras. wrappers.scikit_learn import KerasClassifier

from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# 随机数设定
seed = 42
np.random.seed(seed)
# 加载数据
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"
df = pd.read_csv(url, header=None)
dataset = df.values
# 特征与类别
X = dataset[:, 0:60].astype(float)
Y = dataset[:, 60]
# 类别编码成数字形式 0 or 1
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)

# 创建神经网络模型
def creat_baseline():
    # 创建模型
    model = Sequential()
    # 中间层网络参数设定
    model.add(Dense(60, input_dim=60, init='normal', activation='relu'))#
    # 输出层网络参数设定
    model.add(Dense(1, init='normal', activation='sigmoid'))
    # 编译模型
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# 评估模型
estimator = KerasClassifier(build_fn=creat_baseline, nb_epoch=100, batch_size=5, verbose=0)
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(estimator, X, encoded_Y, cv=kfold)
print("Baseline: {0}% ({1}%)".format(results.mean()*100, results.std()*100))
```

结果:

```
Baseline: 76.0367974258% (7.84685282946%)
```

结果显示神经网络模型在unseen data上的准确率为76.03%.
我们单单设计一个三层的神经网络,准确率就达到70%以上. 如果我们改进下, 会出现怎样的结果.
下面我们来看看.

可参考:

1. [Scikit-learn API - Keras Documentation](https://keras.io/scikit-learn-api/)
2. [verbose: Model (functional API) - Keras Documentation](https://keras.io/models/model/)
3. [sklearn.model_selection.StratifiedKFold — scikit-learn 0.19.0 documentation](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html)
4. [Losses - Keras Documentation](https://keras.io/losses/)

---

## 3.数据处理

我们将数据特征正则化(standardize).数据特征的均值为0, 标准差为1.

> This is where the data is rescaled such that the mean value for each attribute is 0 and the standard deviation is 1.

```
# 两分类问题使用标准化数据
import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense
from keras. wrappers.scikit_learn import KerasClassifier

from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# 随机数设定
seed = 42
np.random.seed(seed)
# 加载数据
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"
df = pd.read_csv(url, header=None)
dataset = df.values
# 特征与类别
X = dataset[:, 0:60].astype(float)
Y = dataset[:, 60]
# 类别编码成数字
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)

# 模型函数
def creat_baseline():
    # 创建模型
    model = Sequential()
    model.add(Dense(60, input_dim=60, init='normal', activation='relu'))
    model.add(Dense(1, init='normal', activation='sigmoid'))
    # 编译模型
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# 评估模型
np.random.seed(seed)
estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasClassifier(build_fn=creat_baseline, nb_epoch=100,
                                        batch_size=5, verbose=0)))
# 封装在pipeline中
pipeline = Pipeline(estimators)
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(pipeline, X, encoded_Y, cv=kfold)
print("Standardized: {0}% ({1}%)".format(results.mean()*100, results.std()*100))
```

结果:```Standardized: 85.5887454477% (5.27619115623%)```

结果显示神经网络模型在unseen data上的准确率为85.59%.


可参考:

1. [sklearn.preprocessing.StandardScaler — scikit-learn 0.19.0 documentation](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)  
2. [sklearn.pipeline.Pipeline — scikit-learn 0.19.0 documentation](http://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)

## 4.改变神经网络层数和节点数

改变神经网络的拓扑结构, 来观察模型性能.

1. smaller, 建立一个小的神经网络模型, 三层: 60-30-1;
2. larger: 建立一个大的神经网络模型, 四层: 60-60-30-1.

```
# Smaller 神经网络模型 60-30-1
import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense
from keras. wrappers.scikit_learn import KerasClassifier

from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# 随机数设定
seed = 42
np.random.seed(seed)
# 加载数据
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"
df = pd.read_csv(url, header=None)
dataset = df.values
# 特征与类别
X = dataset[:, 0:60].astype(float)
Y = dataset[:, 60]
# 类别编码成数字
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)

# smaller_model
def creat_smaller():
    # 创建模型
    model = Sequential()
    model.add(Dense(30, input_dim=60, init='normal', activation='relu'))
    model.add(Dense(1, init='normal', activation='sigmoid'))
    # 编译模型
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

np.random.seed(seed)
estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasClassifier(build_fn=creat_smaller, nb_epoch=100,
                                         batch_size=5, verbose=0)))
pipeline = Pipeline(estimators)
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(pipeline, X, encoded_Y, cv=kfold)
print("Smaller: {0:.2f}% ({1:.2f}%)".format(results.mean()*100, results.std()*100))
```

结果:```Smaller: 81.30% (5.70%)```

Smaller网络模型与基准的网络模型baseline 相比, 它们的神经网络层数相同, 就中间隐含层节点数不同, 前者节点数为30, 后者节点数为60.

Smaller神经网络的结果为81.30%, 比baseline神经网络模型的85.59%低4.29%.

```
# Larger神经网络模型 60-60-30-1
import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense
from keras. wrappers.scikit_learn import KerasClassifier

from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# 随机数设定
seed = 42
np.random.seed(seed)
# 加载数据
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"
df = pd.read_csv(url, header=None)
dataset = df.values
# 特征与类别
X = dataset[:, 0:60].astype(float)
Y = dataset[:, 60]
# 类别编码成数字
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)

# larger_model
def creat_larger():
    # 创建模型
    model = Sequential()
    model.add(Dense(60, input_dim=60, init='normal', activation='relu'))
    model.add(Dense(30, init='normal', activation='relu'))
    model.add(Dense(1, init='normal', activation='sigmoid'))
    # 编译模型
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

np.random.seed(seed)
estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasClassifier(build_fn=creat_larger, nb_epoch=100,
                                         batch_size=5, verbose=0)))
pipeline = Pipeline(estimators)
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(pipeline, X, encoded_Y, cv=kfold)
print("Larger: {0:.2f}% ({1:.2f}%)".format(results.mean()*100, results.std()*100))
```

Larger网络模型(60-60-30-1)与基准的网络模型baseline(60-60-1)相比, 它们的神经网络层数不同,前者比后者多一层.

Larger神经网络的结果为88.49%, 比baseline神经网络模型的85.59% 高2.9%.

---

## Sum

在这个项目中, 我们建立多个不同拓扑结构的神经网络模型, 并标准化数据集, 使用k-fold交叉验证法评估模型性能.

具体代码参见: [Jupyter Notebook Viewer ch11](https://nbviewer.jupyter.org/github/JeremiahZhang/gopython/blob/master/AI/deep-learning-with-python/ch11-p02-binary-classification-sonar-returns.ipynb)

---

## 申明

本文实战是参考[Deep Learning With Python](https://machinelearningmastery.com/deep-learning-with-python/)一书后的笔记记录。

涉及内容版权归原作者[Jason Brownlee](http://machinelearningmastery.com/about/)所有。

## ChangeLog

```
@anifacc
2017-08-18 beta 1.0
```

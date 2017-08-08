---
layout: post
title: Python深度学习实战01-环境配置
categories:
- DeepLearning
- MachineLearning
- Python
---

某日搜索无人驾驶，发现 [MIT 6.S094: Deep Learning for Self-Driving Cars](http://selfdrivingcars.mit.edu/) 课程，看上去挺有趣的，就想以TOP-DOWN的方式来进入深度学习领域，不再以DOWN-TOP的方式。那么首先就从[Deep Learning With Python](https://machinelearningmastery.com/deep-learning-with-python/)一书开始。

开始Python深度学习之旅前，你需要一台电脑，最好有个GPU设备，没有也没关系，可以用亚马逊云的GPU。目前所用设备：带WIN10系统台式电脑一台，Linux Mint系统的Taptop一台。因为笔记本配置低，选择在带WIN10系统的台式电脑上进行深度学习实战。

WIN10 系统配置

```
- conda 4.3.23 (python2.x)
    - scipy: 0.19.1
    - numpy: 1.13.1
    - matplotlib: 2.0.2
    - pandas: 0.20.3
    - statsmodels: 0.8.0
    - sklearn: 0.18.2
- deep_learning_version
    theano: 0.9.0.dev
    Using Theano backend.
    keras: 2.0.6
```

- Anacoda：[Anaconda- Continuum](https://www.continuum.io/anaconda-overview) 下载安装，更新参考 Help 文档.
- Theano：安装参考[Windows Installation Instructions — Theano 0.9.0 documentation](http://deeplearning.net/software/theano/install_windows.html)
- Keras：安装参考[Keras Documentation](https://keras.io/#installation)

因为TensorFlow目前不支持Windows系统，所以在此忽略。具体系统的Python环境配置可参考[How to Setup a Python Environment for Machine Learning and Deep Learning with Anaconda - Machine Learning Mastery](http://machinelearningmastery.com/setup-python-environment-machine-learning-deep-learning-anaconda/)。

备注：
**Keras 默认以TensorFlow为后端，因此需要修改其json文件**。

```
修改 ~/.keras/keras.json 文件

{
    "epsilon": 1e-07,
    "floatx": "float32",
    "image_data_format": "channels_last",
    "backend": "theano"
}
```
---

```
@Anifacc
2017-08-08 Beta 1.0
```

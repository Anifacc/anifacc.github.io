---
layout: post
title: Python基础之安装Python(Win10)
categories:
- Coding
---
目錄 
* any list
{:toc}
人生客旅，我用Python。

## 1、缘起

入手一台新电脑作为工作电脑，系统 Win 10。 平常要用Python，需自行安装。 (PS：Linux 和 MacOS 系统自带 Python，无需安装即可使用。)

## 2、Python 版本选择

选择 Python 3.x，因为 2.x 2020 年就停更了。如今以及未来流行的必然是 Pyhon 3.x。

> The End Of Life date (EOL, sunset date) for Python 2.7 has been moved five years into the future, to 2020.

> Being the last of the 2.x series, 2.7 received bugfix support until 2020. Support officially stopped January 1 2020, and 2.7.18 code freeze occurred on January 1 2020, but the final release will occur after that date. ^[1][1]

## 3、Chocolatey

安装 [Chocolatey](https://chocolatey.org/why-chocolatey)（Win7+ 系统的社区系统软件包管理器），这样使用 Chocolatey 就在Windows 命令行内就直接可以安装软件（比如安装Python `choco install python -y`）。

按照官网[Installing Chocolatey](https://chocolatey.org/install)指导，安装 Chocolatey，步骤如下：

- 1 直接以管理员身份运行 Powershell。
- 2 直接复制代码到 Powershell 中，按下 Enter(回车)。 
- 3 等待片刻，提示安装成功
- 4 可在 Shell 中键入：`choco` 确认是否安装成功。

```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))`
```

chocolatey 支持的包可以在其[官网](https://chocolatey.org/packages)查阅.

![py_1](https://raw.githubusercontent.com/Anifacc/anifacc.github.io/master/images/py_1_install_chocolatey.png)

## 4、Python

安装完 Chocolatey，可以直接在 Powershell 中使用如下命令安装 Python，默认安装的是 3.x，如下图所示。

```
choco install python
```

![py_2](https://raw.githubusercontent.com/Anifacc/anifacc.github.io/master/images/py_2_install_py.JPG)

注意：需要在管理员权限下运行Powershell，之后在其中运行命令（choco）安装。

此外，还可以通过如下命令卸载 python、安装 git 或更新 packages：

```
choco uninstall python -y
choco install git -y
choco install python -y
choco upgrade all -y
```

## 5、Setuptools + Pip

> The two most crucial third-party Python packages are setuptools and pip, which let you download, install and uninstall any compliant Python software product with a single command. It also enables you to add this network installation capability to your own Python software with very little work.^[2][2]

Python 3.x 自带 [pip - The Python Package Installer](https://pip.pypa.io/en/stable/) 和 [Setuptools](https://github.com/pypa/setuptools)，更新 `pip` 和 `setuptools`:

```
python -m pip install -U pip   
python -m pip install -U setuptools
```

这样安装 python 的其他包就方便多了。

## 6、Pipenv & Virtual Environments

> A Virtual Environment is a tool to keep the dependencies required by different projects in separate places, by creating virtual Python environments for them. It solves the “Project X depends on version 1.x but, Project Y needs 4.x” dilemma, and keeps your global site-packages directory clean and manageable.^[2][2]

为不同的项目创建各自的虚拟环境，方便。 下面就安装 pipenv，用 pipenv 去创建 Virtual Environments。

首先，命令行安装 pipenv：

```
pip install --user pipenv
```

其次，设置环境变量：

将`C:\Users\Jeremy\AppData\Roaming\Python\Python36\Scripts`添加到系统环境变量中，如下图所示，将其上移后就可以使用.

![py_3](https://raw.githubusercontent.com/Anifacc/anifacc.github.io/master/images/py_3_install_pipenv.JPG)


**坑**：如果不设置环境变量，无法使用 pipenv 命令问题，引起的原因是 环境路径问题。 因为在安装的scipy 等数据法分析包的时候, 也出现类似问题。

```
python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
```

查阅日志，问题出在：`installed in 'C:\Users\Jeremy\AppData\Roaming\Python\Python36\Scripts' which is not on PATH.`

之后就可以根据 [使用 Pipenv 为项目安装需要的 Packages](https://docs.python-guide.org/dev/virtualenvs/#installing-packages-for-your-project)，比如安装 `requests` 包

```
cd myproject
pipenv install requests
```

![py_4](https://raw.githubusercontent.com/Anifacc/anifacc.github.io/master/images/py_4_using_pipenv.JPG)

创建 `main.py` 脚本:

```
import requests
response = requests.get('https://httpbin.org/ip')
print('Your IP is {0}'.format(response.json()['origin']))
```

使用`pipenv run`运行脚本：

```
pipenv run python main.py
```

显示：`Your IP is 8.8.8.8`。

这部本内容，初学者可以略过。

## Log

```
Jeremy.Anifacc 
2020-04-11
```

## 参考

1. https://www.linkedin.com/pulse/how-use-python-pipenv-mac-windows-mahmud-ahsan/
2. https://docs.python-guide.org/starting/install3/win/

---

[1]: https://www.python.org/dev/peps/pep-0373/#id2  
[2]: https://docs.python-guide.org/starting/install3/win/  
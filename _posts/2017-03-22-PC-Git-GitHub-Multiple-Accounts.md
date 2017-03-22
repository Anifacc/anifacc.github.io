---
layout: post
title: Github-多账户同时使用
categories:
- Martrix
---

# 缘起

安然想新建一个blog, 使用Github page, fork [班长yixuan的极客绿][1], 建立自己的blog [α2Ω][2]. 

现在问题是：

> 之前, 我的Laptop上ssh设置好我之前的github帐号JeremiahZhang, 现在我想如何在我的Laptop上设置好新建的github帐号Anifacc的ssh key.

# Action

## Step 1 - Generating a new SSH key

1. open Git bash, 路径 __~/.ssh__ 下运行命令行
2. 为 github账户 Anifacc 建立新的 ssh key, 在 git 中键入：

	$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

会显示：

	Enter a file in which to save the key (/c/Users/you/.ssh/id_rsa):[Press enter]

建立自己的id_rsa. 因为安然之前一个账户（JeremiahZhang）用的是默认的id_rsa，因此，我建立新的id_rsa_Anifacc. 因此键入的是

	Enter a file in which to save the key (/c/Users/you/.ssh/id_rsa):id_rsa_Anifacc

之后一路enter

## step 2 Adding your SSH key to the ssh-agent

1. Ensure the ssh-agent is running

	$ eval $(ssh-agent -s)

2. Add your SSH key to the ssh-agent.

	$ ssh-add ~/.ssh/id_rsa_Anifacc

## step 3 - Create a Config File

	touch ~/.ssh/config

建立 **config** 文档, 并编辑如下：

	# JeremiahZhang(zhangleisuda@gmail.com)
	  Host JeremiahZhang.github.com
	  HostName github.com
	  User git
	  IdentityFile ~/.ssh/id_rsa
	
	# Anifacc(zhangleisuda@foxmail.com)
	  Host Anifacc.github.com
	  HostName github.com
	  User git
	  IdentityFile ~/.ssh/id_rsa_Anifacc

其中 JeremiahZhang 是安然之前默认的账户, Anifacc 是安然建立博客新建的账户. 安然以后在Laptop上改好blog, 好直接推送到 Anifacc 账户上.

## step 4 Adding a new SSH key to your GitHub account

将 SSH key 添加到 Anifacc 账户上. 参考[Adding a new SSH key to your GitHub account - User Documentation][3].

	$ clip < ~/.ssh/id_rsa_Anifacc.pub

添加到Anifacc github账户的 **SSH and GPG keys** 中.

## step 5 try it

1. clone blog __anifacc.github.io__ repo
2. 为仓库添加 用户名和邮箱（在anifacc.github.io 路径下）

	$ git config user.name "two_name" ; git config user.email "two_email"

3. 开始写blog
4. push over

---

# reference 

1. [Generating a new SSH key and adding it to the ssh-agent - User Documentation](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/#adding-your-ssh-key-to-the-ssh-agent)
2. [git - Multiple github accounts on the same computer? - Stack Overflow](http://stackoverflow.com/questions/3860112/multiple-github-accounts-on-the-same-computer)
3. [Quick Tip: How to Work with GitHub and Multiple Accounts](https://code.tutsplus.com/tutorials/quick-tip-how-to-work-with-github-and-multiple-accounts--net-22574)
4. [一台电脑上的git同时使用两个github账户 - 小蒋不素小蒋 - 博客园](http://www.cnblogs.com/xjnotxj/p/5845574.html)

---

	beta 1.0  
	Anifacc  
	2017-03-22  

---

[1]:	https://github.com/YixuanFranco/yixuanfranco.github.io
[2]:	anifacc.github.io
[3]:	https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/
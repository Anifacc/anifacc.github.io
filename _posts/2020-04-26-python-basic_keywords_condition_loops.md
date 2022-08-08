---
layout: post
title: Python基础之基础语法
categories:
- Coding
---
目錄 
* any list
{:toc}
人生客旅，我用Python

## 前言

此文乃 [Crash Course on Python](https://www.coursera.org/learn/python-crash-course/home/welcome) 的一部分总结笔记。在 Python 3.8.2 完成代码运行。

## Python 内置函数与关键字

函数与关键字是编程语言语法的必要组成部分。

`print()` 为 Python 的内置函数，其他内置函数可以参考 [Built-in Functions](https://docs.python.org/3/library/functions.html)

Python 中的关键字如下：

```
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

如果编程时自己使用这些关键字作为变量，会报错。

```
# pass 是关键字，自己定义使用，会出错
>>> pass = "I passed the exam"
  File "<stdin>", line 1
    pass = "I passed the exam"
         ^
SyntaxError: invalid syntax
>>> pass =1
  File "<stdin>", line 1
    pass =1
         ^
SyntaxError: invalid syntax

# 需使用关键字以外的其他词
>>> str_1 = "I passed the exam"
>>> str_1
'I passed the exam'
>>> num_1 = 1
>>> num_1
1
```

## 数学运算

```
>>> 1 + 1
2
>>> 1 - 1
0
>>> 1 * 42
42
>>> 1 / 42
0.023809523809523808
>>> 2 ** 3
8
>>> 9 // 2
4
>>> 9 % 2
1
>>> 2 * 4 + 1
9
```

## 数据类型

```
# 字符串 string data
>>> "I love coding"
'I love coding'
>>> 'I love coding'
'I love coding'

# Number: integer
>>> 1
1
>>> 2
2
>>> 42
42

# Number: float
>>> 0.42
0.42
>>> 4.2
4.2
>>> 3.1415926
3.1415926

# 查看数据类型
>>> str1 = "I love coding"
>>> type(str1)
<class 'str'>

# 类型错误 TypeError
## 不同数据类型混用会报错, 如下
>>> 1 + "2"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 数据转换(隐性和显性转换)
显性: `str()`
隐性: ` 5 + 5.5`
>>> sum = 2048 + 4357 + 97658 + 125 + 8
>>> amount = 5
>>> average = sum/amount
>>> print("The average size is: " + str(average))
The average size is: 20839.2
```

## Functions 函数定义

在数学中`函数f`中对应输入值x的输出值符号表示为`f(x)`。 Python 中函数类似`f(x)`。

```
# 1) 函数定义 f(x) 
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km ## 返回值

my_trip_miles = 55

# 2) 调用函数
my_trip_km = convert_distance(my_trip_miles)

# 3) 输出结果
print("The distance in kilometers is " + str(my_trip_km))
```

## 条件句

### 比较运算

英文里面有条件句，比如 `if clause(条件), main clause(结果)`。 编程语言也是语言，也有条件句。其条件句中需要用到**比较运算符**(comparison operators)，比较运算符返回布尔值 True 或 False。

```
# 比较: 是否相等
>>> 0 == 0
True
>>> 42 == 8
False
>>> 'hello' == 'hello'
True

# 比较：不相等
>>> 0 != 0
False
>>> 42 != 8
True

# 比较: 大小
>>> 8 < 42
True
>>> 8 > 42
False
>>> 8 <= 8
True
>>> 8 >= 8
True

# 逻辑运算符
>>> 0 and 2
0
>>> -42 or 42
-42
>>> not 0
True
>>> not 1
False
>>> not True
False
>>> not False
True
>>> not -42
False
>>> -42 != False
True
>>> 0 == False
True
```

### if 语句

if statement 块:

```
if condition1:
	if-block
elif condition2:
	elif-block
else:
	else-block
```

示例：

```
>>> number = 11
>>> if number > 11:
...   print(0)
... elif number != 10:
...   print(1)
... elif number >= 20 or number < 12:
...   print(2)
... else:
...   print(3)
...
1
```

示例：

```
>>> def greeting(name):
...   if name == "Jeremy":
...     return "Welcome back Jeremy!"
...   else:
...     return "Hello there, " + name
...
>>> print(greeting("Jeremy"))
Welcome back Jeremy!
>>> print(greeting("Mark"))
Hello there, Mark
```

## 循环 Loops

`while` 和 `for` 都在循环中使用，不要与条件句`if`等混淆。

### while

```
# While 简例

>>> a = 0
>>> while a < 3:
...   print(a)
...   a += 1
...
0
1
2

# 寻找一个数的所有素数因子
>>> def print_prime_factors(number):
...   factor = 2                   # 从 2 开始，2 是素数
...   while factor <= number:      # [2, number] 的范围(在大于等于2，小于等于number范围内寻找
...     if number % factor == 0:   # 检查 factor 能否整除 number
...       print(factor)
...       number = number / factor # 如果 number 能被 factor 整除，那么在 [2, number/factor] 范围内继续寻找
...     else:                      # 如果不是，factor 加一
...       factor += 1
...   return "done"
...
>>> print_prime_factors(100)
2
2
5
5
'done'

# 计算一个数的所有除数之和（不包括它自身）
>>> def sum_divisors(n):
...   sum = 0
...   factor = 1
...   while factor < n:
...     if n % factor == 0:     # 判断是否是除数
...       sum = sum + factor
...       factor += 1
...     else:
...       factor += 1
...   return sum
...
>>> print(sum_divisors(6)) # 1+2+3
6
>>> print(sum_divisors(15)) # 1+3+5
9
```

### for

```
>>> for x in range(5):
...   print(x)
...
0
1
2
3
4

>>> for x in range(1, 5):
...   print(x)
...
1
2
3
4

>>> for x in range(1, 5, 2):
...   print(x)
...
1
3
```

### Break & Continue

- `break`： 在循环中，可以使用`break`关键字中断 while 和 for 循环
- `continue`: 可以使用 `continue` 关键字跳过当前迭代并继续下一个迭代

```
>>> for x in range(1, 10):
...   print(x)
...   if x >= 5:
...     break
...
1
2
3
4
5

>>> for val in "python":
...   if val == "h":
...     continue
...   print(val)
...
p
y
t
o
n
```

### Recursion(递归)

递归的基本结构:(GEB一书中大量描写递归)

```
def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)
```

计算[1,n]范围内所有正数之和：

```
>>> def sum_positive_numbers(n):
...   sum = n
...   if n > 0:
...     sum += sum_positive_numbers(n-1)
...   return sum
...
>>> print(sum_positive_numbers(5)) # 1+2+3+4+5
15
```

## 总结

本部分主要总结了 Python 基础语法，主要包括：

- 内置函数
- 内置关键字
- 数学运算
- 数据类型
- 函数
- 条件句
	- 比较运算
	- `if`
	- `elif`
	- `else`
- 循环
	- `for`
	- `while`
	- `break`
	- `continue`
	- 递归

## 参考

- [Crash Course on Python Coursera](https://www.coursera.org/learn/python-crash-course/home/welcome)
- [Learn Python in Y Minutes](https://learnxinyminutes.com/docs/python/)
- [Type Conversion in Python-Intellipaat](https://intellipaat.com/blog/tutorial/python-tutorial/type-conversion-in-python/)
- [List of Keywords in Python Programming](https://www.programiz.com/python-programming/keyword-list)
- [Python break and continue](https://www.programiz.com/python-programming/break-continue)
- [Python For Loop](https://www.scaler.com/topics/python/for-loop-in-python/)

## Log

```
@Jeremy.Anifacc
2020.05.01
```

---
layout: post
title: Python基础之基本数据结构
categories:
- Coding
---
目錄 
* any list
{:toc}
人生客旅, 我用Python.

## 前言

此文乃 [Crash Course on Python](https://www.coursera.org/learn/python-crash-course/home/welcome) 的一部分总结（Python基本结构）笔记。在 Python 3.8.2 完成代码运行。

- String
- Sequence: tuple & list
- Dictionary

## String

- string immutable(不可变)

```
# 创建 String
>>> new_string = "I love coding"
>>> new_string
'I love coding'
>>> new_string_2 = "人生客旅, 我用Python"
>>> new_string_2
'人生客旅, 我用Python'
```

### string operation

```
# String Indexing: 从string中提取某一个位置的字符
>>> new_string[0]
'I'
>>> new_string[1]
' '
>>> new_string[2]
'l'
>>> new_string[-1]
'g'
>>> new_string[-2]
'n'

# string 长度
>>> len(new_string)
13
# 字符串长度为 13 indexing 超出范围报错
>>> new_string[14]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range

# String Slicing: 从string中提取某一块区域内的字符
>>> new_string[0:6]
'I love'
>>> new_string[6:]
' coding'
>>> new_string[7:14]
'coding'
>>> new_string[:14]
'I love coding'
>>> new_string
'I love coding'

# if substring in string: 检查子字符串是否是字符串的一部分
>>> if "I" in new_string: print("yes")
...
yes
>>> "python" in new_string
False
>>> "coding" in new_string
True

# for character in string: 遍历字符串中的每个字符
>>> for i in new_string: print(i)
...
I

l
o
v
e

c
o
d
i
n
g
```

### String Methods

- 定位 `string.index(substring)`
- 大小写 `string.lower()` ; `string.upper()`
- 去除首/尾空格 `string.lstrip()` ; `string.rstrip()` ; `string.strip()`
- 计数 `string.count(substring)`
- 是否数字 `string.isnumeric()`
- 是否字母 `string.isalpha()`
- 分割返回为*list* `string.split()`; `string.split(delimiter)`
- 替换 `string.replace()`
- 插入 `delimiter.join(list_of_strings)`

```
# string.index() 定位
>>> new_string
'I love coding'
>>> new_string.index("I")
0
>>> new_string.index("love")
2
>>> new_string.index("coding")
7

# string.lower()/string.upper()
>>> new_string.lower()
'i love coding'
>>> new_string
'I love coding'
>>> new_string.upper()
'I LOVE CODING'
>>> new_string
'I love coding'

# string.lstrip() / string.rstrip() / string.strip()
>>> new_string = '    I love coding.    '
>>> new_string.lstrip()
'I love coding.    '
>>> new_string
'    I love coding.    '
>>> new_string.rstrip()
'    I love coding.'
>>> new_string
'    I love coding.    '
>>> new_string.strip()
'I love coding.'

# string.count(substring)
>>> new_string
'    I love coding.    '
>>> new_string.count("o")
2
>>> new_string.count("love")
1
>>> new_string.count("d")
1

# string.isnumeric()
>>> new_string
'    I love coding.    '
>>> new_string.isnumeric()
False
>>> new_string_2 = '2'
>>> new_string_2.isnumeric()
True

# string.isalpha()
>>> new_string = 'I love coding.'
>>> new_string
'I love coding.'
>>> new_string.isalpha()
False
>>> new_string_2 = 'ILoveCoding'
>>> new_string_2.isalpha()
True
>>> new_string_3 = 'I love Python'
>>> new_string_3.isalpha()
False

# string.split() / string.split(delimiter)
>>> new_string
'I love coding.'
>>> new_string.split()
['I', 'love', 'coding.']
>>> new_string_1 = "I,love,coding"
>>> new_string_1.split(",")
['I', 'love', 'coding']
>>> new_string_1.split()
['I,love,coding']
>>>

# string.replace(old, new)
>>> new_string
'I love coding.'
>>> new_string.replace("coding", "Python")
'I love Python.'

# delimiter.join(list of strings)
>>> new_string
'I love coding.'
>>> string_list = new_string.split()
>>> string_list
['I', 'love', 'coding.']
>>> ";".join(string_list)
'I;love;coding.'
>>> "!".join(string_list)
'I!love!coding.'
>>> "  X  ".join(string_list)
'I  X  love  X  coding.'
```

### string formatting

- `string.format()`

```
# 常用 { } .format(value)
>>> print("{} love coding".format("I"))
I love coding

>>> new_string = "I love {} coding."
>>> print(new_string.format("Python"))
I love Python coding.

# 其他 { } { } .format(value1, value2)
>>> print("{0} love {1} coding".format("I", "Python"))
I love Python coding
>>> print("{1} love {0} coding".format("I", "Python"))
Python love I coding
```

## Sequence(元组与列表)

- Sequence
	- Tuple(immutable 不可变)
	- List(mutable)
- Tuple 和 List 通用
	- `len(sequence)`
	- `for elem in sequence`
	- `if elem in sequence`
	- `sequence[i]`
	- `sequence[i:j]`
	- `for index, elem in enumerate(sequence)`
- List
	- `list[i] = x`
	- `list.append(x)`
	- `list.insert(i, x)`
	- `list.pop(i)`
	- `list.remove(x)`
	- `list.sort()`
	- `list.reverse()`
	- `list.clear()`
	- `list.copy()`
	- `list.extend(other_list)`
- List comprehension
	- `[expression for variable in sequence]`
	- `[expression for variable in sequence if condition]`

### Sequence General Operation 

```
# sequence general operation
## Tuple
>>> my_tuple = ("I", "love", "coding")
>>> my_tuple
('I', 'love', 'coding')
>>> len(my_tuple)
3
>>> my_tuple[1]
'love'
>>> my_tuple[2]
'coding'
>>> my_tuple[:2]
('I', 'love')
>>> my_tuple[2] = "Python"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

>>> for elem in my_tuple: print(elem)
...
I
love
coding
>>> if "coding" in my_tuple: print("coding is in it")
...
coding is in it
>>> for index, elem in enumerate(my_tuple): print("{0}'s index in my_tuple is: {1}".format(elem, index))
...
I's index in my_tuple is: 0
love's index in my_tuple is: 1
coding's index in my_tuple is: 2

## List 类似 只不过 List 的元素可替换，如下
>>> my_list = ["I", "love", "coding"]
>>> my_list[0]
'I'
>>> my_list[2]
'coding'
>>> my_list[0:2]
['I', 'love']
>>> my_list[2] = "Python"
>>> my_list[2]
'Python'
>>> my_list
['I', 'love', 'Python']
## 所以 list 是可变的 这里和 tuple 不同

>>> for elem in my_list: print(elem)
...
I
love
Python
>>> if "Python" in my_list: print("yes")
...
yes
>>> for index, elem in enumerate(my_list): print("{0}'s idx in my_list is: {1}.".format(elem, index))
...
I's idx in my_list is: 0.
love's idx in my_list is: 1.
Python's idx in my_list is: 2.
```

### List-specific operations and methods

```
>>> my_list
['I', 'love', 'Python']
>>> my_list.append("coding")
>>> my_list
['I', 'love', 'Python', 'coding']
>>> my_list.insert(1, "like")
>>> my_list
['I', 'like', 'love', 'Python', 'coding']
>>> my_list.pop(1)
'like'
>>> my_list
['I', 'love', 'Python', 'coding']
>>> my_list.append("I")
>>> my_list
['I', 'love', 'Python', 'coding', 'I']
>>> my_list.remove("I")
>>> my_list
['love', 'Python', 'coding', 'I']
>>> list.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: descriptor 'sort' of 'list' object needs an argument
>>> my_list.sort()
>>> my_list
['I', 'Python', 'coding', 'love']
>>> my_list.reverse()
>>> my_list()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable
>>> my_list
['love', 'coding', 'Python', 'I']
>>> my_list_copied = my_list.copy()
>>> my_list_copied
['love', 'coding', 'Python', 'I']
>>> my_list.clear()
>>> my_list
[]
>>> my_list.extend(my_list_copied)
>>> my_list
['love', 'coding', 'Python', 'I']
```

### List comprehension 列表推导式

范式：

```
# 1 基于给定序列(sequence)创建新列表(List[])。每个元素都是我给定表达式(my_expression)的结果。
[my_expression for my_variable in sequence] 

# 2 基于给定序列(sequence)创建新列表。每个元素都是我给定表达式(my_expression)的结果；只有在我的条件(my_condition)为真(True)时才添加元素。
[my_expression for my_variable im sequence if my_condition]
```

示例1, 将

`filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]`

变为

`newfilenames = [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]`

```
>>> filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
>>> newfilenames = [(x, x.replace(".hpp", ".h")) for x in filenames]
>>> print(newfilenames)
[('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]
```

示例2 Pig Lation 游戏：修改每个单词，将第一个字符移到结尾，并将“ay”追加到结尾。例如，python最终成为ythonpay。

```
>>> def pig_latin(text):
...   say = ""
...   words = text.split()
...   for word in words:
...     pig_latin = word[1:] + word[0] + "ay"
...     say = say + pig_latin + " "
...   return say
...
>>> print(pig_latin("hello how are you"))
ellohay owhay reaay ouyay
>>> print(pig_latin("Programming in Python is so fun"))
rogrammingPay niay ythonPay siay osay unfay
```

## Dictionary 字典

- 定义
	- `x = {key_1:value_1, key_2:value_2}`
- 使用
	- `len(dictionary)`
	- `for key in dictionary`
	- `for key, value in dictionary.items()`
	- `if key in dictionary`
	- `dictionary[key]`
	- `dictionary[key] = value`
	- `del dictionary[key]`
- 方法
	- `dict.get(key, default)`
	- `dict.keys()`
	- `dict.values()`
	- `dict.update(other_dictionary)`
	- `dict.clear()`

### 定义

```
>>> tel_dict = {"Jeremy":9366, "Sarah":8888}
>>> tel_dict
{'Jeremy': 9366, 'Sarah': 8888}
```

### 使用

```
>>> tel_dict
{'Jeremy': 9366, 'Sarah': 8888}
>>> len(tel_dict)
2
>>> for key in tel_dict: print(key)
...
Jeremy
Sarah

>>> for name in tel_dict: print(name)
...
Jeremy
Sarah

>>> for name,tel in tel_dict.items(): print(name, tel)
...
Jeremy 9366
Sarah 8888

>>> if "Jeremy" in tel_dict: print("Yes")
...
Yes

>>> tel_dict["Jeremy"]
9366
>>> tel_dict["Jeremy"] = 6666
>>> tel_dict["Jeremy"]
6666
>>> tel_dict["Moses"] = 0000
>>> tel_dict["Moses"]
0
>>> tel_dict
{'Jeremy': 6666, 'Sarah': 8888, 'Moses': 0}
>>> del tel_dict["Moses"]
>>> tel_dict
{'Jeremy': 6666, 'Sarah': 8888}
```

### 方法

```
>>> tel_dict
{'Jeremy': 9366, 'Sarah': 8888}
# dict.get(key, default)
>>> print("{}'s telephone number is {}".format("Jeremy", tel_dict.get("Jeremy")))
Jeremy's telephone number is 6666
>>> print("{}'s telephone number is {}".format("Mark", tel_dict.get("mark", "None")))
Mark's telephone number is None
# 字典中没有 Mark 的号码，因此，显示为 None（默认 default 设置）

# dict.keys() 和 dict.values()
>>> tel_dict.keys()
dict_keys(['Jeremy', 'Sarah'])
>>> for key in tel_dict.keys(): print(key)
...
Jeremy
Sarah
>>> type(tel_dict.keys())
<class 'dict_keys'>
>>> for value in tel_dict.values(): print(value)
...
6666
8888
>>> tel_dict.values()
dict_values([6666, 8888])

# dict.update(other_dictionary)
>>> new_dict = {"Jack": 1111, "John": 2222}
## new_dict 字典中的内容添加到 tel_dict 字典中
>>> tel_dict.update(new_dict)
>>> tel_dict
{'Jeremy': 6666, 'Sarah': 8888, 'Jack': 1111, 'John': 2222}

>>> new_dict_2 = {'John': 1122, 'Luke': 9999}
## new_dict_2 字典中的内容添加到 tel_dict 字典中，而且以最新的添加进入，比如 'John': 2222 变为 'John': 1122,
>>> tel_dict.update(new_dict_2)
>>> tel_dict
{'Jeremy': 6666, 'Sarah': 8888, 'Jack': 1111, 'John': 1122, 'Luke': 9999}
```

## 总结

本部分内容主要整理了 Python 中的基本数据结构包括 string, tuple, list, dictionary，并给出如何使用以及对应的方法。

知道了这些数据结构，如果要详细了解他们，可以直接在命令行中输入(以string为例)：`help(str)` 以及具体方法(`help(str.count))`查看，这样非常方便。

```
## help(<data_type>)
>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return key in self.
 | .................

## help(<method>)
>>> help(str.count) # string.count 方法介绍
Help on method_descriptor:

count(...)
    S.count(sub[, start[, end]]) -> int

    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.

>>> help(list.append) # list.append 方法介绍
Help on method_descriptor:

append(self, object, /)
    Append object to the end of the list.

>>> help(dict.update) # dictionary.update 方法介绍
Help on method_descriptor:

update(...)
    D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
    If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
    If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
    In either case, this is followed by: for k in F:  D[k] = F[k]
```

## 参考

- [Crash Course on Python Coursera](https://www.coursera.org/learn/python-crash-course/home/welcome)
- [Built-in Types — Python 3.8.3rc1 documentation](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python format() function - GeeksforGeeks](https://www.geeksforgeeks.org/python-format-function/)
- [5. Data Structures — Python 3.8.3rc1 documentation](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

## Log

```
@Jeremy.Anifacc
2020-05-03 2:51
```
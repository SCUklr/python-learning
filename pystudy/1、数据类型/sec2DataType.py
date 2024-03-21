# -*- coding = utf-8 -*-
# @Time : 2024/3/13 18:43
# @Author: Vast
# @File: sec2DataType.py
# @Software: PyCharm

"""
变量无需申明，但需赋值
"""

a = 1000
b = 114.514
c = "kkksama"

print(a, end="")
print(b)
print(c)

'''多变量赋值'''

d, e, f = 1, 2, 3
g = h = i = 1
print("多变量赋值：\n")
print("d = ", d)
print("e = ", e)
print("f = ", f)

print("g=h=i=", g, h, i)
'''
标准数据类型
Python3 中常见的数据类型有：

Number（数字）--int float bool complex
String（字符串）
Tuple（元组）

List（列表）
Set（集合）
Dictionary（字典）

bool（布尔类型）


Python3 的六个标准数据类型中：

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
此外还有一些高级的数据类型，如: 字节数组类型(bytes)。
'''

"""
>>> 5 + 4  # 加法
9
>>> 4.3 - 2 # 减法
2.3
>>> 3 * 7  # 乘法
21
>>> 2 / 4  # 除法，得到一个浮点数
0.5
>>> 2 // 4 # 除法，得到一个整数
0
>>> 17 % 3 # 取余 
2
>>> 2 ** 5 # 乘方
32"""

# !/usr/bin/python3

str1 = 'Runoob'  # 定义一个字符串变量

print(str1)  # 打印整个字符串
print(str1[0:-1])  # 打印字符串第一个到倒数第二个字符（不包含倒数第一个字符）
print(str1[0])  # 打印字符串的第一个字符
print("打印字符串第三到第五个字符:", str1[2:5])  # 打印字符串第三到第五个字符
print(str1[2:])  # 打印字符串从第三个字符开始到末尾
print(str1 * 2)  # 打印字符串两次
print(str1 + "TEST")  # 打印字符串和"TEST"拼接在一起(加号只能用于字符串)

"""
注意：

1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
2、字符串可以用+运算符连接在一起，用*运算符重复。
3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
4、Python中的字符串不能改变。
"""
"""
bool（布尔类型）
布尔类型即 True 或 False。

在 Python 中，True 和 False 都是关键字，表示布尔值。

布尔类型可以用来控制程序的流程，比如判断某个条件是否成立，或者在某个条件满足时执行某段代码。

布尔类型特点：

布尔类型只有两个值：True 和 False。

布尔类型可以和其他数据类型进行比较，比如数字、字符串等。在比较时，Python 会将 True 视为 1，False 视为 0。

布尔类型可以和逻辑运算符一起使用，包括 and、or 和 not。这些运算符可以用来组合多个布尔表达式，生成一个新的布尔值。

布尔类型也可以被转换成其他数据类型，比如整数、浮点数和字符串。在转换时，True 会被转换成 1，False 会被转换成 0。
"""
x = True
y = False
print("a=True,b=False;a交b:", x and y)
print(int(x))
print(float(y))
print(not x)
print("y的字符串形式：", str(y))

'''列表'''
list1 = ['abcd', 786, 2.23, 'runoob', 70.2]  # 定义一个列表
tinylist = [123, 'runoob']

print(list1)  # 打印整个列表
print(list1[0])  # 打印列表的第一个元素
print(list1[1:3])  # 打印列表第二到第三个元素
print(list1[2:])  # 打印列表从第三个元素开始到末尾
print(tinylist * 2)  # 打印tinylist列表两次
print(list1 + tinylist)  # 打印两个列表拼接在一起的结果

"""反转字符串"""


def reverseWords(input1):
    # 空格把单词分割为列表
    inputWords = input1.split(" ")
    # 从-1反向输出
    inputWords = inputWords[-1::-1]

    # 重组
    output = ' '.join(inputWords)

    return output


input = "I like you."
print(reverseWords(input))

##

"""
Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。

元组中的元素类型也可以不相同：
"""
tuple1 = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple1)  # 输出完整元组
print(tuple1[0])  # 输出元组的第一个元素
print(tuple1[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple1[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple1 + tinytuple)  # 连接元组

"""


Set（集合）{}
Python 中的集合（Set）是一种无序、可变的数据类型，用于存储唯一的元素。

集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。

在 Python 中，集合使用大括号 {} 表示，元素之间用逗号 , 分隔。

另外，也可以使用 set() 函数创建集合。

注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

创建格式：

parame = {value01,value02,...}
或者
set(value)
"""
sites = {1, 2, 3, 4, 5, 6, 7, 8, 9, 1}
print(sites)  # 重复元素自动去除

if 1 in sites:
    print("1在sites中")
else:
    print("没有1")

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)  # a 和 b 的差集

print(a | b)  # a 和 b 的并集

print(a & b)  # a 和 b 的交集

print(a ^ b)  # a 和 b 中不同时存在的元素

"""
Dictionary（字典）
字典（dictionary）是Python中另一个非常有用的内置数据类型。

列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的。
"""
# !/usr/bin/python3

dict = {'one': "1 - 菜鸟教程", 2: "2 - 菜鸟工具"}

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

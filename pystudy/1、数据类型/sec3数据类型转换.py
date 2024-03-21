# -*- coding = utf-8 -*-
# @Time : 2024/3/14 21:34
# @Author: Vast
# @File: sec3数据类型转换.py
# @Software: PyCharm

# type(num)显示数据类型
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("num_int 数据类型为:", type(num_int))
print("num_flo 数据类型为:", type(num_flo))

print("num_new 值为:", num_new)
print("num_new 数据类型为:", type(num_new))

"""
显式类型转换
在显式类型转换中，用户将对象的数据类型转换为所需的数据类型。 我们使用 int()、float()、str() 等预定义函数来执行显式类型转换。

int() 强制转换为整型：

实例
x = int(1)   # x 输出结果为 1
y = int(2.8) # y 输出结果为 2
z = int("3") # z 输出结果为 3
float() 强制转换为浮点型：

实例
x = float(1)     # x 输出结果为 1.0
y = float(2.8)   # y 输出结果为 2.8
z = float("3")   # z 输出结果为 3.0
w = float("4.2") # w 输出结果为 4.2
str() 强制转换为字符串类型：

实例
x = str("s1") # x 输出结果为 's1'
y = str(2)    # y 输出结果为 '2'
z = str(3.0)  # z 输出结果为 '3.0'
"""

a = int(1.1)
b = float(2)
c = str(345)
print(a, b, c)
print(type(a), type(b), type(c))

"""
以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。

3、函数	描述
int(x [,base]),将x转换为一个整数;float(x),将x转换到一个浮点数;complex(real [,imag]),;创建一个复数
str(x)
将对象 x 转换为字符串

repr(x)
将对象 x 转换为表达式字符串

eval(str)
用来计算在字符串中的有效Python表达式,并返回一个对象

tuple(s)
将序列 s 转换为一个元组

list(s)
将序列 s 转换为一个列表

set(s)
转换为可变集合

dict(d)
创建一个字典。d 必须是一个 (key, value)元组序列。

frozenset(s)
转换为不可变集合

chr(x)
将一个整数转换为一个字符

ord(x)
将一个字符转换为它的整数值

hex(x)
将一个整数转换为一个十六进制字符串

oct(x)
将一个整数转换为一个八进制字符串
"""
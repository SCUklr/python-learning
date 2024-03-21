# -*- coding = utf-8 -*-
# @Time : 2024/3/18 17:32
# @Author: Vast
# @File: 3.18 函数lambda.py
# @Software: PyCharm

# Python 使用 lambda 来创建匿名函数。
#
# 所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
#
# lambda 只是一个表达式，函数体比 def 简单很多。
# lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
# lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
# 虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，内联函数的目的是调用小函数时不占用栈内存从而减少函数调用的开销，提高代码的执行速度。

# 语法
# lambda 函数的语法只包含一个语句，如下：
#
# lambda [arg1 [,arg2,.....argn]]:expression
x = lambda a, b: a + b
print(x(5, 10))

sum = lambda a, b: a + b
print(f"10和20相加后的值为：{sum(10, 20)}")


# 我们可以将匿名函数封装在一个函数内，这样可以使用同样的代码来创建多个匿名函数。
#
# 以下实例将匿名函数封装在 myfunc 函数中，通过传入不同的参数来创建不同的匿名函数：

def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(f"111翻倍后：{mydoubler(111)}")
#
# return 语句
# return [表达式]
# 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的
# return 语句返回
# None。之前的例子都没有示范如何返回数值，以下实例演示了
# return 语句的用法：
#
# 实例(Python
# 3.0 +)
#
# # !/usr/bin/python3
#
# # 可写函数说明
# def sum(arg1, arg2):
#     # 返回2个参数的和."
#     total = arg1 + arg2
#     print("函数内 : ", total)
#     return total
#
#
# # 调用sum函数
# total = sum(10, 20)
# print("函数外 : ", total)
# 以上实例输出结果：
#
# 函数内: 30
# 函数外: 30
# 强制位置参数
# Python3
# .8
# 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。
#
# 在以下的例子中，形参
# a
# 和
# b
# 必须使用指定位置参数，c
# 或
# d
# 可以是位置形参或关键字形参，而
# e
# 和
# f
# 要求为关键字形参:
#
#
# def f(a, b, /, c, d, *, e, f):
#     print(a, b, c, d, e, f)
#
#
# 以下使用方法是正确的:
#
# f(10, 20, 30, d=40, e=50, f=60)
# 以下使用方法会发生错误:
#
# f(10, b=20, c=30, d=40, e=50, f=60)  # b 不能使用关键字参数的形式
# f(10, 20, 30, 40, 50, f=60)  # e 必须使用关键字参数的形式

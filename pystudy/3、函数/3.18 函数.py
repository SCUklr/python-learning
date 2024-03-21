# -*- coding = utf-8 -*-
# @Time : 2024/3/18 10:59
# @Author: Vast
# @File: 3.18 3、函数.py
# @Software: PyCharm

# Python3 3、函数
# 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
#
# 函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。
#
# 定义一个函数
# 你可以定义一个由自己想要功能的函数，以下是简单的规则：
#
# 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
# 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
# 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
# 函数内容以冒号 : 起始，并且缩进。
# return [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。

# 函数调用
def printme(str1):
    print(str1)
    return


printme("输出我自己")

"""
参数传递
在 python 中，类型属于对象，对象有不同类型的区分，变量是没有类型的：

a=[1,2,3]

a="Runoob"
以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。

可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。

可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：

不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。

可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
"""


# a=888这个a只是一个指针（装水的盆子），随时可以换水
def change(a):
    print(id(a))
    a = 114
    print(id(a))


# 在调用函数前后，形参和实参指向的是同一个对象（对象 id 相同），
# 在函数内部修改形参后，形参指向的是不同的 id。

b = 113  # 数字、字符串和元组是不可变类型
print(id(b))
change(b)
print(f"b = {b}") # 这里输出的b还是113


# 传可变对象实例
# 可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如：


def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print(f"函数内：{mylist}")


# 调用

mylist1 = [10, 20, 30]
changeme(mylist1)
print(fr"函数外：{mylist1}")


# 默认参数
# 调用函数时，如果没有传递参数，则会使用默认参数。
# 以下实例中如果没有传入 age 参数，则使用默认值：

def printinfo2(name, age=35):
    print(f"姓名：{name}， 年龄：{age}")


# 参数顺序无所谓
printinfo2(age=50, name='kkksama')
print("----------")
printinfo2(name='lll')


#
# 不定长参数
# 你可能需要一个函数能处理比当初声明时更多的参数。
# 这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。
# 基本语法如下：

def printinfo3(arg1, *v):
    """打印任何传入的参数"""
    print("输出")
    print(arg1)
    print(v)


# 调用函数
printinfo3(10, 20, 30)


# 还有一种就是参数带两个星号 **基本语法如下：
#
# def functionname([formal_args,] **var_args_dict ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]
# 加了两个星号 ** 的参数会以字典的形式导入。

# !/usr/bin/python3

# 可写函数说明
def printinfo4(arg1, **vardict):
    """打印任何传入的参数"""
    print("字典形式导入输出: ")
    print(arg1)
    print(vardict)


# # 调用printinfo 3、函数
# printinfo4(1, a=2, b=3)
# 声明函数时，参数中星号 * 可以单独出现，例如:
#
# def f(a,b,*,c):
#     return a+b+c
# 如果单独出现星号 *，则星号 * 后的参数必须用关键字传入：
#
# >>> def f(a,b,*,c):
# ...     return a+b+c
# ...
# >>> f(1,2,3)   # 报错
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: f() takes 2 positional arguments but 3 were given
# >>> f(1,2,c=3) # 正常
# 6
# >>>
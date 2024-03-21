# -*- coding = utf-8 -*-
# @Time : 2024/3/13 17:59
# @Author: Vast
# @File: sec1.py
# @Software: PyCharm

# 第一个注释
print(r"Hello, world!")

# 单行注释：Ctrl + / （Windows/Linux）或 Command + /（macOS）
# 多行注释：
# Ctrl + Shift + / （Windows/Linux）或 Command + Shift + /（macOS）
'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""

'''缩进'''
if True:
    print("True")
else:
    print("False")

# '''多行语句'''
#
# total1 = item_one + \
#          item_two + \
#          item_three
#
# '''在{}、[]、()多行语句不需要'''
# total2 = [item_three + item_four + item_five]

'''数字类型
int 2
bool True
float 1.14514
complex(复数) 1 + 2j'''

# 字符串
# Python 中单引号 ' 和双引号 " 使用完全相同。
# 使用三引号(''' 或 """)可以指定一个多行字符串。
# 转义符 \。
# 反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。 如 r"this is a line with \n" 则 \n 会显示，并不是换行。
# 按字面意义级联字符串，如 "this " "is " "string" 会被自动转换为 this is string。
# 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
# Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
# Python 中的字符串不能改变。
# Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]"""

str = '123456789'

print(str)
print(str[0: -1])  # 第一到倒数第二
print(str[0])
print(str[2:5])  # 第三到第六（不包含第六）
print(str[2])
print(str[1:5:2])  # 第二到第五 步长2
print(str + str)
print(str * 2)

print("-------")
print("Hello\nworld")
print(r"Hello\nworld")  # 只识别输出纯文本

'''
同一行显示多条语句
Python 可以在同一行中使用多条语句，语句之间使用分号 ; 分割，以下是一个简单的实例：

实例(Python 3.0+)
#!/usr/bin/python3
 
import sys; x = 'runoob'; sys.stdout.write(x + '\n') '''

# 不换行输出： 加end = ""
print("这是不换行输出", end="")
print(r"不换行输出2", end="")

'''
import 与 from...import
在 python 用 import 或者 from...import 来导入相应的模块。   '''

import sys  # 置于顶部

print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

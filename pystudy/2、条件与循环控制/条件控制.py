# -*- coding = utf-8 -*-
# @Time : 2024/3/16 11:14
# @Author: Vast
# @File: 条件控制.py
# @Software: PyCharm

"""
if 语句
Python中if语句的一般形式如下所示：

if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
如果 "condition_1" 为 True 将执行 "statement_block_1" 块语句
如果 "condition_1" 为False，将判断 "condition_2"
如果"condition_2" 为 True 将执行 "statement_block_2" 块语句
如果 "condition_2" 为False，将执行"statement_block_3"块语句
Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。

注意：

1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
3、在 Python 中没有 switch...case 语句，但在 Python3.10 版本添加了 match...case
"""
apple = 1
if apple:
    print("\napple!")
    print(apple)
    print(type(apple))

banana = 3
if banana >= 9:
    print("\nbanana1!")
elif 3 <= banana <= 8:
    print("\nbanana2!")
else:
    print("\nbanana3!")


def mind100(status):
    match status:
        case 1:
            return 100
        case 2:
            return 200
        case _:
            return 400


b = 2
print(mind100(b))


age = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print(fr"对应人类年龄: {human}")

# 退出提示
input("点击 enter 键退出")

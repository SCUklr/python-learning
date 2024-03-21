# -*- coding = utf-8 -*-
# @Time : 2024/3/19 11:11
# @Author: Vast
# @File: 2、2.2 input().py
# @Software: PyCharm

age = input("How old are you?\n")
print(age)  # Python将用户输入解读为字符串,字符串和数值没法比较
# print(age > 18)
# File "C:\Users\12279\PycharmProjects\pythonProject2\pystudy\2、条件与循环控制\2、2.2 input().py", line 9, in <module>
#     print(age > 18)
# TypeError: '>' not supported between instances of 'str' and 'int'
age = int(age)
print(age)
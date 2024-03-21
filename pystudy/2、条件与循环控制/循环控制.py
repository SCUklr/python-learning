# -*- coding = utf-8 -*-
# @Time : 2024/3/16 11:28
# @Author: Vast
# @File: 2、条件与循环控制.py
# @Software: PyCharm

# while

a = 0
while not a > 10:
    print(a)
    a += 1
else:
    print("a > 10 is already")
b = 0
counter = 1
while counter <= 100:
    b += counter  # b1=1,b2=1+2,b3=1+2+3
    counter += 1

print(fr"1到{counter - 1}之和为{b}")
# while - else
count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")

'''
for 语句
Python for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串。

for循环的一般格式如下：

for <variable> in <sequence>:
    <statements>
else:
    <statements>
'''
sites1 = ['baidu', 'ali', 'tencent']
for site in sites1:
    print(site, end='')

# !/usr/bin/python3

sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

# 结合 range() 和 len() 函数以遍历一个序列的索引,如下所示:
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

# break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。(彻底不循环)
# continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环（回到循环开头）

for i in range(1, 10, 2):
    if i > 6:
        break
    print(i)
print("i>6")

for i in range(1, 20, 3):
    if i == 16:
        continue
    print(i)

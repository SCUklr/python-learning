# -*- coding = utf-8 -*-
# @Time : 2024/3/16 16:04
# @Author: Vast
# @File: 例题：加一.py
# @Software: PyCharm
"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。
"""
"""
解题思路：1、从尾到头的循环遍历，尾的索引尾len(list)-1
2、如果最尾部的数字小于9就直接加1然后结束循环(return)输出结果
for i in range(len(list)-1, -1, -1):
    if list[i] < 9:
        list[i] += 1
        break
        
3、如果最尾部=9就变成0，然后继续循环到前面一个数再做类似判定
    else:
        list[i] = 0

4、全部都进位了就在索引为0的地方插入1
    if list[0] == 0:
        list.insert(0,1)
        return list

"""


def addOne(list):
    for i in range(len(list) - 1, -1, -1):
        if list[i] < 9:
            list[i] += 1
            break
        else:
            list[i] = 0

    if list[0] == 0:
        list.insert(0, 1)
    return list


a = [9]
addOne(a)
print(a)

b = [1, 1, 9]
print(addOne(b))

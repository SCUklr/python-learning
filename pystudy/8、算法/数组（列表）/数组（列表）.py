# -*- coding = utf-8 -*-
# @Time : 2024/3/16 15:05
# @Author: Vast
# @File: 数组（列表）.py
# @Software: PyCharm

"""
2.1 访问元素
访问数组中第 iii 个元素：

只需要检查 iii 的范围是否在合法的范围区间，即 0≤i≤len(nums)−10 \le i \le len(nums) - 10≤i≤len(nums)−1。超出范围的访问为非法访问。
当位置合法时，由给定下标得到元素的值。
"""


def listList(numlist, situation):
    if 0 <= situation <= len(numlist):
        print(numlist[situation])


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

listList(numbers, 4)

"""
2.2 查找元素
查找数组中元素值为 val的位置：

建立一个基于下标的循环，每次将 val 与当前数据元素 nums[i] 进行比较。
在找到元素的时候返回元素下标。
遍历完找不到时可以返回一个特殊值（例如 −1）。
"""


def find(list, num):
    for i in range(len(list)):
        if list[i] == num:
            print(f"List[{i}]的值为{num}")
    return -1


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = 2
find(list1, 2)

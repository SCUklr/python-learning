# -*- coding = utf-8 -*-
# @Time : 2024/3/16 21:33
# @Author: Vast
# @File: 排序大法好.py
# @Software: PyCharm

"""
冒泡排序
第 111 趟「冒泡」：对前 nnn 个元素执行「冒泡」，从而使第 111 个值最大的元素放置在正确位置上。
先将序列中第 111 个元素与第 222 个元素进行比较，如果前者大于后者，则两者交换位置，否则不交换。
然后将第 222 个元素与第 333 个元素比较，如果前者大于后者，则两者交换位置，否则不交换。
依次类推，直到第 n−1n - 1n−1 个元素与第 nnn 个元素比较（或交换）为止。
经过第 111 趟排序，使得 nnn 个元素中第 iii 个值最大元素被安置在第 nnn 个位置上。
第 222 趟「冒泡」：对前 n−1n - 1n−1 个元素执行「冒泡」，从而使第 222 个值最大的元素放置在正确位置上。
先将序列中第 111 个元素与第 222 个元素进行比较，若前者大于后者，则两者交换位置，否则不交换。
然后将第 222 个元素与第 333 个元素比较，若前者大于后者，则两者交换位置，否则不交换。
依次类推，直到对 n−2n - 2n−2 个元素与第 n−1n - 1n−1 个元素比较（或交换）为止。
经过第 222 趟排序，使得数组中第 222 个值最大元素被安置在第 nnn 个位置上。
依次类推，重复上述「冒泡」过程，直到某一趟排序过程中不出现元素交换位置的动作，则排序结束。
"""
list1 = [1, 2, 4, 1, 4, 2, 5, 7, 4, 7, 4, 7, 3, 2, 6, 4, 8, 6, 8, 9, 5, 2]
for i in range(0, len(list1) - 1):
    for j in range(0, len(list1) - 1 - i):
        if list1[j] > list1[j + 1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]
print("对list1冒泡排序后的结果为：", list1)

# 选择排序: 选择最小的往前移动
list2 = [1, 2, 3, 5, 2, 4, 8, 9, 0]
for i in range(0, len(list2) - 1):
    min_i = i  # 放置锚点
    for j in range(i + 1, len(list2)):
        if list2[j] < list2[min_i]:
            min_i = j # 重置最小锚点
    list2[i], list2[min_i] = list2[min_i], list2[i] # 在内部循环外面交换值
print(list2)

# -*- coding = utf-8 -*-
# @Time : 2024/3/16 15:21
# @Author: Vast
# @File: 增删.py
# @Software: PyCharm

# 尾部插入： append
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a.append(10)
print(a)

# 指定位置插入：insert
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b.insert(3, 10)
print(b)

# 2.4 改变元素
# 将数组中第 iii 个元素值改为 valvalval：
#
# 需要先检查 iii 的范围是否在合法的范围区间，即 0≤i≤len(nums)−10 \le i \le len(nums) - 10≤i≤len(nums)−1。
# 然后将第 iii 个元素值赋值为 valvalval。

c = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def change(nums, situ, changes):
    if situ in range(len(nums)):
        nums[situ] = changes


change(c, 2, 114)
print(c)

# 删除尾部数字： pop()（指定删除的位置）
d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d.pop()
print(d)

e = [1, 2, 3, 4, 5, 6, 7, 8, 9]
e.pop(0)
print(e)

# 移除指定数值目标：remove
f = [1, 2, 3, 4, 5, 6, 7, 8, 9]
f.remove(1)
print(f)
# -*- coding = utf-8 -*-
# @Time : 2024/3/21 15:36
# @Author: Vast
# @File: motorcycles.py
# @Software: PyCharm
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print(motorcycles[0].title())
# 修改列表元素
motorcycles[0] = 'ducati'
print(motorcycles[0].title())

# 末尾添加元素：append()
motorcycles.append('ducati')
print(motorcycles)

# 指定位置添加元素：insert(索引，元素值)
motorcycles.insert(0,'lifan')
print(motorcycles)

# del删除指定位置元素 del 列表(索引)
del motorcycles[0]
print(motorcycles)

# pop删除莫为元素或任意位置元素
motorcycles.pop()
motorcycles.pop(0)
print("删去首尾后的motorcycles列表：", motorcycles)

# 根据值删除(只删除碰到的第一个值) 列表.remove(值)
motorcycles.remove('suzuki')
print(f"删去suzuki之后：{motorcycles}")
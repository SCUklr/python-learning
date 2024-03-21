# -*- coding = utf-8 -*-
# @Time : 2024/3/21 15:45
# @Author: Vast
# @File: cars.py
# @Software: PyCharm

"""在Python中，`sorted()`和`.sort()`方法都可以用来对列表进行排序，但它们之间有几个关键的区别，这也解释了为什么`sorted()`的用法与`.sort()`不同：

1. **方法调用方式**：
   - `.sort()`是列表（list）的一个方法，因此它是通过在列表对象后使用点号（.）调用的，比如`cars.sort()`。这意味着`.sort()`只能用于列表。
   - `sorted()`是Python的一个内置函数，不是特定于列表的方法。因此，它是直接调用的，然后将想要排序的可迭代对象作为参数传入，比如`sorted(cars)`。这意味着`sorted()`不仅可以用于列表，还可以用于任何可迭代对象，如元组、字典和集合等。

2. **返回值**：
   - `.sort()`对列表进行原地排序，意味着它直接修改原列表，不返回任何值（准确地说，返回`None`）。
   - `sorted()`则返回一个新的列表，原列表不会被修改。这使得`sorted()`更加灵活，可以在不影响原列表的情况下获取排序结果。

3. **用法差异**：
   - 由于`.sort()`是列表的方法，所以不能以`cars.sorted()`的形式调用，因为这样的语法暗示`sorted()`是列表对象的一个方法，而不是一个独立的Python内置函数。

总结，`sorted()`和`.sort()`的设计有着明确的用途和目标差异，这就是为什么它们的调用方式不同。`sorted()`提供了更广泛的适用性和灵活性，而`.sort()`提供了对列表的原地排序功能。"""
# sorted()排序：sorted(list)临时排序
cars = ['audi', 'bmw', 'toyota', 'subaru']
print("Here's the original list: ")
print(cars)
print("Here's the sorted list")
print(sorted(cars))
print("Here's the original list: ")
print(cars)
# sort()排序：list.sort() 永久排序
cars.sort()
print(cars) # 首字母顺序
cars.sort(reverse=True) # 利用reverse=True倒序
print(cars)
# 反向打印 list.reverse()
cars.reverse()
print(cars)

# 确定列表长度： len(list)
print(len(cars))
# -*- coding = utf-8 -*-
# @Time : 2024/3/19 16:05
# @Author: Vast
# @File: 4.1 创建和使用类.py
# @Software: PyCharm
class Dog:  # 首字母大写指的是类class
    """一次模拟小狗的简单实验"""

    # 类里面的函数称为方法

    # __init__(两条下划线)是一个特殊方法，Python调用方法创建Dog实例时将自动传入实参self，该实参是一个指向实例本身的引用
    def __init__(self, name, age):
        """初始化name和age"""
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is not sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")


# 实例化
my_dog = Dog("w", 6)
# 这个时候my_dog具备Dog里面所有方法
your_dog = Dog("x", 7)

print(f"我的狗的信息：name：{my_dog.name}, age：{my_dog.age}")
my_dog.sit()
my_dog.roll_over()

your_dog.sit()
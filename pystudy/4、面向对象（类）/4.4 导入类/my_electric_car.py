# -*- coding = utf-8 -*-
# @Time : 2024/3/19 19:30
# @Author: Vast
# @File: my_electric_car.py
# @Software: PyCharm
# 一个模块存储多个类
from car import ElectricCar

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

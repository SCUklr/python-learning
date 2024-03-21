# -*- coding = utf-8 -*-
# @Time : 2024/3/19 19:26
# @Author: Vast
# @File: my_car.py
# @Software: PyCharm
from car import Car
#导入单个类
# 实例化Car
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
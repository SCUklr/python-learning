# -*- coding = utf-8 -*-
# @Time : 2024/3/19 19:37
# @Author: Vast
# @File: my_cars.py
# @Software: PyCharm

from car import Car,ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_telsa = ElectricCar('tesla', 'leaf', 2024)
print(my_telsa.get_descriptive_name())

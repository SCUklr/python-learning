# -*- coding = utf-8 -*-
# @Time : 2024/3/19 17:02
# @Author: Vast
# @File: 4.2 实用类和实例.py
# @Software: PyCharm

class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 不用通过形参定义，直接指定为默认值

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):  # 读取里程表
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mile):
        if mile >= self.odometer_reading:
            self.odometer_reading = mile
        else:
            print("You can't roll")

    def increment_odometer(self, miles_add):
        self.odometer_reading += miles_add


my_car = Car("Audi", 'a4', 2024)
print(my_car.get_descriptive_name())
# my_car.odometer_reading = 23  # 1、直接手动修改属性的值
my_car.update_odometer(23)  # 2、编写方法修改属性的值
my_car.read_odometer()
my_car.increment_odometer(114)  # 3、编写方法增加属性的值
my_car.read_odometer()

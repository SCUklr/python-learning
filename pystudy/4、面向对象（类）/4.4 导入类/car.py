# -*- coding = utf-8 -*-
# @Time : 2024/3/19 19:26
# @Author: Vast
# @File: car.py
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

    def increment_odometer(self, miles_add: object):
        self.odometer_reading += miles_add

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has {self.battery_size} battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles.")
# 创建一个电车子类
class ElectricCar(Car):
    def __init__(self, make, model, year):
        """初始化父类属性"""
        super().__init__(make, model, year)
        # 给子类初始化子类特有的属性
        self.battery = Battery()

    def describe_battery(self):
        print(f"This car has a {self.battery_size} battery.")
# -*- coding = utf-8 -*-
# @Time : 2024/3/19 23:39
# @Author: Vast
# @File: employee.py
# @Software: PyCharm
class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.annual_salary = annual_salary
        self.first_name = first_name
        self.last_name = last_name

    def give_raise(self, amount=5000):
        self.annual_salary += int(amount)

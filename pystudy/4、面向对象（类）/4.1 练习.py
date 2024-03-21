# -*- coding = utf-8 -*-
# @Time : 2024/3/19 16:33
# @Author: Vast
# @File: 4.1 练习.py
# @Software: PyCharm

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name} and the cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The restaurant is open now.")


restaurant1 = Restaurant("川菜馆", "川菜")
print(restaurant1.restaurant_name, restaurant1.cuisine_type)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant("东北菜馆", "东北菜")
restaurant2.describe_restaurant()


class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.number_served = 15

    def describe_user(self):
        print(f"用户信息如下：{self.first_name}，{self.last_name}，{self.age}，{self.gender}. ")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, i):
        self.number_served = self.number_served + int(i)


user1 = User("Lingran", "Kong", 20, "male")
user1.greet_user()
user1.describe_user()
print(f"有{user1.number_served}个人在本餐厅就餐过。")
user1.set_number_served(28)
print(f"传递新人数后，有{user1.number_served}个人在本餐厅就餐过。")
i_add = input("请输入今天增加的顾客数：")
user1.increment_number_served(i_add)
print(f"现在有{user1.number_served}个顾客在本餐厅就餐过。")

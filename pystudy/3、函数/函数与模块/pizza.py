# -*- coding = utf-8 -*-
# @Time : 2024/3/19 15:46
# @Author: Vast
# @File: pizza.py
# @Software: PyCharm
def make_pizza(size, *toppings):
    print(f"Making {size} inches pizza with the following toppings:")
    for t in toppings: print(f"-{t}")
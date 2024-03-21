# -*- coding = utf-8 -*-
# @Time : 2024/3/19 15:22
# @Author: Vast
# @File: 传递实参.py
# @Software: PyCharm

# 单星号创建元组（tuple）,打了星号就不限个数了
def pizza(*p):
    for pi in p:
        print(f"--{pi}")


pizza("a")
pizza('b', 'c', 'd')


# 结合位置实参和任意数量实参
def make_pizza(size, *toppings):
    print(fr"Making a {size}-inches pizza with the following toppings:")
    for t in toppings:
        print({t})


make_pizza(16, "cheese", "cheese")


# 任意数量关键字形参:**

def build_profile(first_name, last_name, **user_info):
    user_info["first_name"] = first_name
    user_info["last_name"] = last_name
    return user_info


user_profile = build_profile("lr","k",locations = 'cq', university = 'scu')
print(user_profile)
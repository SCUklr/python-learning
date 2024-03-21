# -*- coding = utf-8 -*-
# @Time : 2024/3/19 15:48
# @Author: Vast
# @File: making-pizzas.py
# @Software: PyCharm


import pizza
# 也可以只导入想用的函数，下面的方法改为make_pizza()
# from pizza import make_pizza

# 或者指定别名
# from pizza import make_pizza as mp,下面的方法改为mp.()
# 也可以给模块通过as指定别名, pizza->p
# 用星号导入模块所有函数：
# from modules import *
pizza.make_pizza(12, 'oranges')
pizza.make_pizza(16, 'mushrooms','cheese')
# -*- coding = utf-8 -*-
# @Time : 2024/3/19 15:01
# @Author: Vast
# @File: 3.19 函数与列表.py
# @Software: PyCharm

# 传递列表
# def greet_users(names):
#     for name in names:
#         msg = f'Hello, {name.title()}!'
#         print(msg)
#
#
# usernames = ['Alice', 'Bob']
# greet_users(usernames)
#
# # 修改列表
# unprinted_design = ['python', 'java', 'c']
# completed_design = []
#
# # 先打印所有未打印的设计
# while unprinted_design:
#     # 出栈
#     current_design = unprinted_design.pop()
#     print(f'Printing model:{current_design}')
#     # 移到新列表
#     completed_design.append(current_design)
#
# print("The printed designs are:")
# for design in completed_design:
#     print(design)
# 用函数来实现
def print_models(unprinted_models, completed_models):
    while unprinted_models:
        current_model = unprinted_models.pop()
        print(current_model)
        completed_models.append(current_model)
        for models in completed_models:
            print(f"已完成模型：{models}")


models1 = ['a', 'b', 'c']
models1_completed = []
print_models(models1, models1_completed)

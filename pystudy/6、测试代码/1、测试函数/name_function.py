# -*- coding = utf-8 -*-
# @Time : 2024/3/19 19:50
# @Author: Vast
# @File: name_function.py
# @Software: PyCharm
def get_formatted_name(first, last, middle=''):
    """生成规范格式的姓名"""
    if middle:
        full_name = f'{first} {middle} {last}'
    else:
        full_name = f'{first} {last}'
    return full_name.title()


name1 = get_formatted_name('lingran', 'kong')
print(name1)

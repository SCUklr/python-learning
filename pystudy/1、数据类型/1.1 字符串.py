# -*- coding = utf-8 -*-
# @Time : 2024/3/20 22:58
# @Author: Vast
# @File: 1.1 字符串.py
# @Software: PyCharm
"""What is String in python?"""

'''This is a string.'''

"""1.1.1 大小写"""
# title() 首字母大写
# upper() 全部大写
# lower() 全部小写
name = "kong lingran"
print(name.title())  # 输出Kong Lingran
print(name.upper())
print(name.lower())

"""1.1.2 在字符串中使用变量"""
first_name = "Lingran"
last_name = "kong"
full_name = f'{first_name} {last_name}'
print(full_name)

"""1.1.3-1.1.4 添加与删除空白"""
# \t 空四格
# \n 换行
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# lstrip() 删左边
# rstrip() 删右边
# strip() 两边都删
coding_language = " Python "
print(f"lstrip()删左边空白：{coding_language.lstrip()}")
print(f"strip()删右边空白：{coding_language.rstrip()}")

"""1.1.5 删除前缀"""
# removeprefix('删除内容')
baidu_url = "https://www.baidu.com"
print(baidu_url.removeprefix('https://'))
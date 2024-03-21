# -*- coding = utf-8 -*-
# @Time : 2024/3/19 19:53
# @Author: Vast
# @File: names.py
# @Software: PyCharm
from name_function import get_formatted_name

print("Enter 'q' at anytime to quit.")
while True:
    first = input("Enter your first name: ")
    if first == 'q':
        break
    last = input("Enter your last name:")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name:{formatted_name}")
# -*- coding = utf-8 -*-
# @Time : 2024/3/19 11:41
# @Author: Vast
# @File: 2、条件与循环控制-while.py
# @Software: PyCharm

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I'll repeat back to you:"
prompt += "\nEnter 'quit' to quit this program."
# 使用标志flag

message = ' '
active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

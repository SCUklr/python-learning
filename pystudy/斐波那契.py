# -*- coding = utf-8 -*-
# @Time : 2024/3/16 14:33
# @Author: Vast
# @File: 斐波那契.py
# @Software: PyCharm

a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b

counter = 0
sum1 = 0
for i in range(1, 10):
    counter += 1
    sum1 += counter
    print(f"第{i}次：counter = {counter}， sum = {sum1}")

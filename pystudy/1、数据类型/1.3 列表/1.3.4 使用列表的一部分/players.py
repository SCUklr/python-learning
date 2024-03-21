# -*- coding = utf-8 -*-
# @Time : 2024/3/21 19:37
# @Author: Vast
# @File: players.py
# @Software: PyCharm
# 切片
players = ['Charles', 'martina', 'michael','florence', 'eli']
print(players[:3])  # 输出索引为0、1、2的元素的列表
print(players[1:4])
print(players[2:])
print(players[-3:])  # 打印最后三位的名字

# 遍历切片
print(fr"There are 3 first players in the list: ")
for player in players[0:3]:print(player.title(), end=' ')


# -*- coding = utf-8 -*-
# @Time : 2024/3/19 13:17
# @Author: Vast
# @File: 练习8.7.py
# @Software: PyCharm
def make_album(singer, album_name, songs_numbers=None):
    if songs_numbers is None:
        album = {f"歌手：{singer}, 专辑名：{album_name}"}
    else:
        album = {f"歌手：{singer}, 专辑名：{album_name}, 包含歌曲数：{songs_numbers}"}
    return album


a1 = make_album("周杰伦", "夜的第七章")
a2 = make_album("周杰伦", "Mojito", 1)
print(a1)
print(a2)
while True:
    a = input("输入quit可以退出此操作。输入start开始本操作。")
    if a == "start":
        singer_input = input("输入歌手名:")
        album_input = input("输入专辑名:")
        print(make_album(singer_input, album_input))
    elif a == "quit":
        break
    else:
        print("输入类型错误，请重新输入。")
        continue

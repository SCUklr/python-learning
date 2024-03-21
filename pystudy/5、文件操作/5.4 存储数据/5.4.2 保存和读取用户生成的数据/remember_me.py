# -*- coding = utf-8 -*-
# @Time : 2024/3/21 11:46
# @Author: Vast
# @File: remember_me.py
# @Software: PyCharm
from pathlib import Path
import json

# username = input("What's your name?")

"""将收集到的数据写入username.json"""
path = Path('username.json')
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}")
else:
    username = input("What's your name? ")
    contents = json.dumps({username})
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")

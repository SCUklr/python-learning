# -*- coding = utf-8 -*-
# @Time : 2024/3/21 11:51
# @Author: Vast
# @File: greet_user.py
# @Software: PyCharm
from pathlib import Path
import json

path = Path('username.json')
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")
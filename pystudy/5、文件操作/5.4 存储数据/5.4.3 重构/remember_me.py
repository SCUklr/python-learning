from pathlib import Path

"""虽然代码能够正确运行，但还可以将其划分为一系列完成具体工作的函数来进行改进"""
from pathlib import Path
import json


def get_stored_user_name(path):
    """如果存储了用户名就获取它"""
    if path.exists():
        contents = path.read_text()
        # Assuming the username is stored as a plain string in JSON.
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    '''提示用户输入用户名'''
    username = input("What's your name? ")
    # 将用户名作为字符串存储在JSON中
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """问候用户并指出其名字"""
    path = Path('username.json')
    username = get_stored_user_name(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


greet_user()

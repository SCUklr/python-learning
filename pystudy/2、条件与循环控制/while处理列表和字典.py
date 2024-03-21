# -*- coding = utf-8 -*-
# @Time : 2024/3/19 12:53
# @Author: Vast
# @File: while处理列表和字典.py
# @Software: PyCharm

unconfirmed_users = ['Alice', 'Bob', 'Charlie']
confirmed_users = []

# 验证每个用户知道没有未经验证用户
while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print("Verifying user: ", current_users.title())
    confirmed_users.append(current_users)

print("\nThe confirmed users are: ", confirmed_users)

# 删除
a = ['a', 'a', 'b']
while 'a' in a:
    a.remove('a')
print(a)

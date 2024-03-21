# -*- coding = utf-8 -*-
# @Time : 2024/3/20 22:28
# @Author: Vast
# @File: 练习10.6.py
# @Software: PyCharm

print("请输入两个数：(输入'q'退出)")
while True:
    try:
        nums1 = input("请输入第一个数：")
        if nums1 != 'q':
            real_nums1 = int(nums1)
        else:
            break
        nums2 = input("请输入第二个数：")
        if nums2 != 'q':
            real_nums2 = int(nums2)
        else:
            break
        sum = real_nums1 + real_nums2
    except ValueError:
        print("您输入的不是数字")
    else:
        print(f'两数总和为{sum}')
"""更简化的方法是定义一个函数"""
# def get_number(prompt):
#     """从用户获取一个整数，如果输入非数字且不是'q'，则抛出异常。"""
#     user_input = input(prompt)
#     if user_input == 'q':
#         return 'q'
#     return int(user_input)  # 如果输入不是数字，这里会抛出 ValueError
#
# print("请输入两个数：(输入'q'退出)")
#
# while True:
#     try:
#         nums1 = get_number("请输入第一个数：")
#         if nums1 == 'q':
#             break
#         nums2 = get_number("请输入第二个数：")
#         if nums2 == 'q':
#             break
#         print(f'两数总和为{nums1 + nums2}')
#     except ValueError:
#         print("您输入的不是数字，请重新输入。")

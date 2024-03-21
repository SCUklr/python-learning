# -*- coding = utf-8 -*-
# @Time : 2024/3/19 22:30
# @Author: Vast
# @File: test_name_function.py
# @Software: PyCharm

# 测试文件和函数的名称必须以test开头
from name_function import get_formatted_name


def test_first_last_name():
    """能够正确处理像Janis Joplin这样的姓名吗？"""
    f_name = get_formatted_name('Janis', 'Jophin')
    assert f_name == "Janis Jophin"  # 断言就是生成满足特定的条件


def test_first_last_middle_name():
    """能正确处理Wolfgang Amadeus Mozart这样的姓名吗？"""
    f_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert f_name == "Wolfgang Amadeus Mozart"

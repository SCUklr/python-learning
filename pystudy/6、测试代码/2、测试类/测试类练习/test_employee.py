# -*- coding = utf-8 -*-
# @Time : 2024/3/19 23:42
# @Author: Vast
# @File: test_employee.py
# @Software: PyCharm
import pytest

from employee import Employee


@pytest.fixture
def employee():
    """创建一个共用的 Employee 实例作为夹具"""
    return Employee('Lingran', 'Kong', 50000)


def test_give_default_raise(employee):
    """测试默认增加年薪的情况"""
    employee.give_raise()
    assert employee.annual_salary == 55000


def test_give_custom_raise(employee):
    """测试自定义增加年薪的情况"""
    employee.give_raise(10000)
    assert employee.annual_salary == 60000

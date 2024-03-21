# -*- coding = utf-8 -*-
# @Time : 2024/3/19 22:44
# @Author: Vast
# @File: city_functions.py
# @Software: PyCharm
def city_country(city, country, population=''):
    """接受两个形参：一个城市名和一个国家名"""
    if population:
        string1 = f"{city}, {country} - population {population}".title()
    else:
        string1 = f"{city}, {country}".title()
    return string1


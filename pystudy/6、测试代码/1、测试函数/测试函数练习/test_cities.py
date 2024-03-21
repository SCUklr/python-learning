# -*- coding = utf-8 -*-
# @Time : 2024/3/19 22:47
# @Author: Vast
# @File: test_cities.py
# @Software: PyCharm
from city_functions import city_country


def test_city_country():
    f_city_country = city_country('santiago', 'chile')
    assert f_city_country == "Santiago, Chile"


def test_city_country_population():
    f_city_country_population = city_country('santiago', 'chile', 500000)
    assert f_city_country_population == "Santiago, Chile - Population 500000"

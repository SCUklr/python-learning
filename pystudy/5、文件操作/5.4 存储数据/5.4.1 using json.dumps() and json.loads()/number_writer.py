# -*- coding = utf-8 -*-
# @Time : 2024/3/21 11:25
# @Author: Vast
# @File: number_writer.py
# @Software: PyCharm
from pathlib import Path
import json
# json.dupm()接受实参 转化为JSON格式的数据
numbers = [2, 3, 5, 7, 11, 13]

path = Path("numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)
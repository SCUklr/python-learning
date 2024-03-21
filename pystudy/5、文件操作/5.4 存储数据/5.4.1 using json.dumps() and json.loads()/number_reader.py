# -*- coding = utf-8 -*-
# @Time : 2024/3/21 11:38
# @Author: Vast
# @File: number_reader.py
# @Software: PyCharm
from pathlib import Path
import json

path = Path("numbers.json")  # 确保读取前面写入的文件
contents = path.read_text()  # 使用read_text读取
numbers = json.loads(contents)  # 将读取的内容传递给json.loads()，这个函数把一个JSON格式的字符串作为参数并返回一个Python对象，赋值给numbers
print(numbers)
"""处理FileNotFoundError异常"""
from pathlib import Path

path = Path("Alice.txt")

try:
    contents = path.read_text(encoding='utf-8')

except FileNotFoundError:
    print(f"无{path}文件.")

else:
    """计算大概包括多少个单词"""
    words= contents.split() # 调用split()方法生成一个列表
    num_words = len(words)
    print(f"The file has {num_words} words.")

# Traceback (most recent call last):
#   File "c:\Users\12279\PycharmProjects\pythonProject2\pystudy\5、文件操作\5.3 异常\alice.py", line 5, in <module>
#     contents = path.read_text(encoding='utf-8')
#                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\12279\AppData\Local\Programs\Python\Python312\Lib\pathlib.py", line 1027, in read_text
#     with self.open(mode='r', encoding=encoding, errors=errors) as f:
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\12279\AppData\Local\Programs\Python\Python312\Lib\pathlib.py", line 1013, in open
#     return io.open(self, mode, buffering, encoding, errors, newline)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'Alice.txt'
# PS C:\Users\12279\PycharmProjects\pythonProject2>
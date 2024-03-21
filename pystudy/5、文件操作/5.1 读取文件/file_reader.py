from pathlib import Path

# path = Path(r'pystudy\5、文件操作\5.1 读取文件\pi_digits.txt') # 这是相对路径

path = Path(r'C:\Users\12279\PycharmProjects\pythonProject2\pystudy\5、文件操作\5.1 读取文件\pi_digits.txt') # 这是绝对路径

contents = path.read_text()

# contents = contents.rstrip() # 删除字符串末尾（右侧）的空白
# print(contents)


# 10.1.3 访问文件中的各行
# lines = contents.splitlines() # 将字符串转换为行
# for line in lines:
#     print(line)
# 简化代码

#10.1.4 使用文件的内容
pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip() # 除去每行左端的空格

print(pi_string)
length = len(pi_string)
print(fr"长度为:{length}")

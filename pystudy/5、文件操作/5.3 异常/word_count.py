from pathlib import Path


def count_words(path):
    try:
        contents = path.read_text(encoding='utf-8')

    except FileNotFoundError:
        print(f"无{path}文件.")

    else:
        """计算大概包括多少个单词"""
        words = contents.split()  # 调用split()方法生成一个列表
        num_words = len(words)
        print(f"The file has {num_words} words.")


path = Path("Alice.txt")
count_words(path)
file_names = ['Alice.txt', 'bob.txt', 'bob.txt', 'moby_dick.txt']
for filename in file_names:
    path = Path(filename)
    count_words(path)

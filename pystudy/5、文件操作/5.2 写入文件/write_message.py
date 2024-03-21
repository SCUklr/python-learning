from pathlib import Path

# 10.2 写入多行

contents = 'I love programming.\n'
contents += 'I love creating new games.\n'
contents += 'I also love working with data.\n'
# 10.1 写入一行
path = Path('programming.txt')
path.write_text(contents)
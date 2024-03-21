from pathlib import Path

while True:
    guest_name = input("请输入用户名：")
    path = Path("guest_book.txt")
    with path.open(mode='a') as file:
        file.write(guest_name + '\n')

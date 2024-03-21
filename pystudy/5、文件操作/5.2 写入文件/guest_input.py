from pathlib import Path
guest_name = input("请输入用户名：")

path = Path("guest.txt")
path.write_text(guest_name)
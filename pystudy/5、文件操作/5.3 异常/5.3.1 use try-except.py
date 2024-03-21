# 使用try_except代码块
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
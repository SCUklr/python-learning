"""使用异常避免崩溃"""

print("Give me two numbers, and I'll divide them.")
print("print 'q' to exit.")
      
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError: # 如果出现异常
        print("You can't divide by 0!")
    else: # 如果不出现异常
        print(answer)
# second_number如果输入0直接崩溃
#     First number: 1

# Second number: 0
# Traceback (most recent call last):
#   File "c:\Users\12279\PycharmProjects\pythonProject2\pystudy\5、文件操作\5.3 异常\5.3.3 division_calculator.py", line 13, in <module>
#     print(int(first_number)/int(second_number))
#           ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~
# ZeroDivisionError: division by zero
# PS C:\Users\12279\PycharmProjects\pythonProject2>
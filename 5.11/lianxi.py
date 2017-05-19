
import math

_username = "hell"
_password = "abc123"

for i in range(0,6):
    UserName = input("UserName:")
    PassWord = input("PassWord:")
    if UserName == "hell" and PassWord == "abc123":
        print("loginSuccess")
    else:
        print("loginFailed" ,i)
        if i == 2:
            print("程序锁定")
            break


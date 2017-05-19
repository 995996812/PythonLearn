name = "Alex Li"

print(name.capitalize()) #首字母大写
print(name.casefold()) #首字母小写
print(name.center(20,'-'))#占20个字符位
print(name.count("e",0,5))#
print(name.endswith("ae"))#以什么结束
# name = "alex \tli"
# print(name.expandtabs(20))#/t占20个字符

print(name.find('li'))#找到了返回位置,找不到返回-1
msg = "my name is{0}, and i am {1} years old"
print(msg.format("alex",22))#格式化字符串

print("ad".isalpha())#是不是字母
print("a3d".isalnum())#是不是阿拉伯数字和字母

print("2.0".isdecimal())#十进制
print("0".isdigit())#是不是数字
print("al_ex".islower())
print("al_ex".isupper())
print("3.1".isnumeric())
print(float("3.1"))
print("My Name Is Alex".istitle())
print(",".join("alex"))
print("|".join(["alex","jack","rain"]))

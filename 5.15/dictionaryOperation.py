
#
# names = {
#     "stu1101":"jack",
#     "stu1102":"hell",
#     "stu1103":"margin",
# }
#
# print(names["stu1101"])
#
# print(names.get("stu1101"))
#
# print(names.values())

# 字典排列通过hash实现的
# 散列  通过一些数学算法,使字符串生成一个唯一的数字
# 没一个key其实都被生成了一个对应的数字

# 为什么字典比列表快
'''
字典的查询是分段查询
'''
'''
字典的性:
1.无序
2.去重
3.查询效率高
'''

dictionary = {
    "a":"1",
    "b":"2",
    "c":"3"
}

for key in dictionary.items():
    print(key)

# n3 = dictionary.fromkeys(dictionary,[1,2,3])
#
# print(n3)
# #{'c': [1, 2, 3], 'a': [1, 2, 3], 'b': [1, 2, 3]}
#
# n3["a"][1] = 9
#
# print(n3)
#
# print(id(n3["a"]),id(n3["b"]))




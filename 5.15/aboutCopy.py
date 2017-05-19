import copy

dict = {
    "a":{
        "d":"4",
        "e":"5"
    },
    "b":"2",
    "c":"3"
}
newDict = dict.copy()
# newDict11 = copy.deepcopy(dict)

dict["c"] = "6"
dict["a"]["d"] = "7"

print(dict)
print(newDict)
# print(newDict11)
'''
第一层不会跟着变,第二层会跟着变 为什么?


# '''
# import copy
#
# credit_card = {
#     "name":"hell",
#     "acc":{
#         "id":2333,
#         "balance":900
#     }
# }
#
# credit_card2 = credit_card.copy()
# credit_card3 = copy.deepcopy(credit_card)
#
# credit_card2["name"] = "hell2"
# credit_card["acc"]["balance"] -= 300
# credit_card2["acc"]["balance"] -= 500
#
#
# print(credit_card)
# print(credit_card2)
# print(credit_card3)

product_list = [
    ["iPhone",7500],
    ["MacbookPro",13000],
    ["bike",999],
    ["pythonBook",66],
    ["coffee",31]
]

shopping_cart = []

salary = input("input your salary:")

if salary.isdigit():

    while True:
        for index,i in enumerate(product_list):
            print("%s.\t %s \t %s" %(index,i[0],i[1]))

        choice = input(">>>:")

        if choice.isdigit():
            choice = int(choice)
            if choice < len(product_list) and choice >= 0:
                product_item = product_list[choice]
                if salary >= product_item[1]:#买得起
                    salary -= product_item[1]
                    shopping_cart.append(product_item)
                    print("your shoppingCart product \033[32;1m%s\033[0m\
                    and your money \033[31;1m%s\033[0m" %(shopping_cart,salary))
                else:
                    print("can't afford to buy, your remain's salary \033[31;1m%s\033[0m" %(salary))
            else:
                print("without this goods")
        elif choice ==  "exit":
            total_cost = 0

            print("your have bought below products:")

            for i in shopping_cart:
                print(i[1])
                total_cost += i[1]

            print("total_cost:",total_cost)
            print("your current balance is",salary)
            break
else:
    print("工资不合法")

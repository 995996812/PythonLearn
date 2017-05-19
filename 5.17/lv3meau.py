meau = {
    "北京":{
        "海淀":{
            "五道口":{
                "soho":{},
                "网易":{},
                "google":{}
            },
            "中关村":{
                "爱奇艺":{},
                "汽车之家":{},
                "youku":{}
            },
            "上地":{
                "百度":{}
            },
        },
        "昌平":{
          "沙河":{
              "老男孩":{},
              "北航":{}
          },
            "天通苑":{},
            "回龙观":{},
        },
        "朝阳":{},
        "东城":{}
    },
    "上海":{
        "闵行":{
            "人民广场":{
                "炸鸡店":{}
            }
        },
        "闸北":{
            "火车站":{
                "携程":{}
            }
        }
    },
    "山东":{}

}

while True:
    for k in meau:
        print(k)
    choice = input(">>:").strip()
    if len(choice) == 0 : continue

    if choice in meau:
        while True:
            for k in meau[choice]:
                print(k)

            choice2 = input(">>:").strip()
            if len(choice2) == 0 : continue

            if choice2 in meau[choice]:
                while True:
                    for k in meau[choice][choice2]:
                        print(k)

                    choice3 = input(">>:").strip()
                    if len(choice3) == 0 : continue

                    if choice3 in meau[choice][choice2]:
                        while True:
                            for k in meau[choice][choice2][choice3]:
                                print(k)

                                choice4 = input(">>:").strip()

                            if len(choice4) == 0 : continue

                    elif choice3 == "b":
                        break
                    elif choice3 == "a":
                        exit("退出程序")
            elif choice2 == "b":
                break
            elif choice2 == "a":
                exit("退出程序")
    elif choice == "a":
        exit("退出程序")


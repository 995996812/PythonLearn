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

curren_layer = meau
p_layers = []

while True:
    for k in curren_layer:
        print(k)
    choice = input(">>:").strip()
    if len(choice) == 0 : continue

    if choice in curren_layer:
        p_layers.append(curren_layer)
        curren_layer = curren_layer[choice]
    elif choice == "b":
        if len(p_layers) > 0:
            curren_layer = p_layers.pop()
    elif choice == "a":
        break


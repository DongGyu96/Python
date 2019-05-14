def Check(list):
    for i in range(len(list)):
        if str(int(list[i]) + 1) in list:
            if str(int(list[i]) + 2) in list:
                if str(int(list[i]) + 3) in list:
                    return True
    return False


for i in range(6):
    dice = input("주사위 입력 : ")
    dice = dice.replace(" ", "")

    if Check(dice):
        print("YES")
    else:
        print("NO")
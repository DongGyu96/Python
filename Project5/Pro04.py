number = eval(input(""))
for k in range(number):
    list = input("")
    h, w, num = map(int, list.split(" "))
    x = 1
    y = 0
    while num > h:
        x += 1
        num = num - h
    y = num
    if x < 10:
        print(y, end="")
        print("0", end="")
        print(x)
    else:
        print(y, end="")
        print(x)
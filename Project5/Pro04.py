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
        result = str(y)  + "0"  + x
        print(result)
    else:
        result = str(y)  + x
        print(result)
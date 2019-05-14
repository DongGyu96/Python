count = eval(input(""))

def ToInt(list):
    size = len(list)
    num = 0
    if list[0] == "-":
        for i in range(1, len(list)):
            num += int(list[i]) * (10 ** (size - i - 1))
        num *= -1
    else:
        for i in range(len(list)):
            num += int(list[i]) * (10 ** (size - i - 1))
    return num

list = []
for i in range(count):
    list.append(input(""))

for i in range(count):
    first = []
    middle = None
    last = []
    result = []
    for j in range(0, len(list[i])):
        if list[i][j] == "+":
            middle = "+"
            for x in range(0, j - 1):
                first.append(list[i][x])
            for x in range(j + 2, len(list[i])):
                if list[i][x] == " ":
                    break
                else:
                    last.append(list[i][x])
        elif list[i][j] == "-" and list[i][j + 1] == " ":
            middle = "-"
            for x in range(0, j - 1):
                first.append(list[i][x])
            for x in range(j + 2, len(list[i])):
                if list[i][x] == " ":
                    break
                else:
                    last.append(list[i][x])
        elif list[i][j] == "*":
            middle = "*"
            for x in range(0, j - 1):
                first.append(list[i][x])
            for x in range(j + 2, len(list[i])):
                if list[i][x] == " ":
                    break
                else:
                    last.append(list[i][x])
        elif list[i][j] == "/":
            middle = "/"
            for x in range(0, j - 1):
                first.append(list[i][x])
            for x in range(j + 2, len(list[i])):
                if list[i][x] == " ":
                    break
                else:
                    last.append(list[i][x])
        elif list[i][j] == "=":
            for x in range(j+2, len(list[i])):
                result.append(list[i][x])
    if middle == "+":
        if ToInt(result) == ToInt(first) + ToInt(last):
            print("correct")
        else:
            print("wrong answer")
    elif middle == "-":
        if ToInt(result) == ToInt(first) - ToInt(last):
            print("correct")
        else:
            print("wrong answer")
    elif middle == "/":
        if ToInt(result) == ToInt(first) / ToInt(last):
            print("correct")
        else:
            print("wrong answer")
    elif middle == "*":
        if ToInt(result) == ToInt(first) * ToInt(last):
            print("correct")
        else:
            print("wrong answer")
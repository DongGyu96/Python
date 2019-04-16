list = []
def decimalToHex(value):
    global list
    if value == 0:
        return
    else:
        if value % 16 >= 10:
            list.append(chr(97 + (value % 16) - 10))
        else:
            list.append(value % 16)
        decimalToHex(value//16)

num = eval(input("숫자를 입력하세요 : "))
decimalToHex(num)
print("16진수 변환 : ", end = '')
for i in range(len(list) - 1, -1, -1):
    print(list[i], end='')
print()
print("실제 값과 비교 : ", hex(num))
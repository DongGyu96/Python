list = []
def decimalToBinary(value):
    global list
    if value == 0:
        return
    else:
        list.append(value % 2)
        decimalToBinary(value//2)

num = eval(input("숫자를 입력하세요 : "))
decimalToBinary(num)
print("이진수 변환 : ", end = '')
for i in range(len(list) - 1, -1, -1):
    print(list[i], end='')
print()
print("실제 값과 비교 : ", bin(num))
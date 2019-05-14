num = eval(input("숫자 입력 : "))

list = []

for i in range(1, 2000000):
    a = num * i
    a += i
    if a // num == a % num:
        list.append(a)

result = 0
for i in range(len(list)):
    result += list[i]
print(result)
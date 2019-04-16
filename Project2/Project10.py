def m(x):
    sum = 0
    for i in range(0, x + 1):
        sum += i / (i + 1)
    return sum

num = eval(input("i를 입력하세요 : "))
print("m(", num,") 의 값은 ", m(num), "입니다.")
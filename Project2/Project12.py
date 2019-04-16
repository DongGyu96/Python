def m(i):
    if i == 1:
        print("1")
        return 1
    else:
        print("1 /", i, "+ ", end = "")
        return (1 / i) + m(i-1)

num = eval(input("i의 값을 입력하세요 : "))
print("m(", num, ")의 값은", m(num))
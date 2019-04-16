def reverse(number):
    result = 0
    while(True):
        result += number % 10
        number = number // 10
        if number <= 0:
            return result
        result = result * 10

num = eval(input("정수를 입력하세요 : "))
print("reverse(", num,") :", reverse(num))
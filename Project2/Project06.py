def reverse(number):
    result = 0
    while(True):
        result += number % 10
        number = number // 10
        if number <= 0:
            return result
        result = result * 10

def isPalindrome(number):
    if number == reverse(number):
        return True
    else:
        return False

num = eval(input("정수를 입력하세요 : "))

if isPalindrome(num):
    print(num, "은 대칭수 입니다.")
else:
    print(num, "은 대칭수가 아닙니다.")
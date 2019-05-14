def reverse(number):
    result = 0
    while(True):
        result += number % 10
        number = number // 10
        if number <= 0:
            return result
        result = result * 10

def IsPrime(num):
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    if IsPalindrome(num):
        return True

def IsPalindrome(num):
    if num == reverse(num):
        return True
    else:
        return False

max = 100

list = []
num = 0

number = 2
while(True):
    if len(list) == max:
        break
    if IsPrime(number):
        list.append(number)
    number += 1

for i in range(max):
    if num == 10:
        print()
        num = 0
    print("{0:>5}".format(list[i]), end = "\t")
    num += 1
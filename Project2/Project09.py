def printChars(ch1, ch2, numberPerLine):
    count = 0
    for i in range(ord(ch1), ord(ch2) + 1):
        print(chr(i), end = ' ')
        count += 1
        if count == numberPerLine:
            count = 0
            print()

ch1 = input("시작이 되는 문자를 입력하시오 : ")
ch2 = input("끝이 되는 문자를 입력하시오 : ")
num = eval(input("한 행에 몇글자씩 출력하겠습니까 : "))
printChars(ch1,ch2,num)
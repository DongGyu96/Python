import math

for i in range(3):
    a, b, c = eval(input("a, b, c를 입력하세요 : "))
    if b ** 2 - (4 * a * c) > 0:
        result = ((-1 * b) + math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
        result2 = ((-1 * b) - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
        print("실근은 ", result, "과 ", result2, "입니다. ")
    elif b ** 2 - (4 * a * c) == 0:
        result = ((-1 * b) + math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
        print("실근은 ", result, "입니다. ")
    else:
        print("이 방정식은 실근이 존재하지 않습니다.")
def gcd(m,n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

n1, n2 = eval(input("숫자 2개를 입력하세요 : "))
if n1 > n2:
    print(n1, n2, "의 최대 공약수는 ", gcd(n1, n2), "입니다.")
else:
    print(n2, n1, "의 최대 공약수는 ", gcd(n2, n1), "입니다.")

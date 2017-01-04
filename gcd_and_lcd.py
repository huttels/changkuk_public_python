print("#"*50)
print("                oh shit!!!!!!!!!!!")
print("#"*50)
'''
최대공약수(gcd)
1.두 수를 입력받는다.
2. 각자 약수를 구한다.  미ㅏㅇ늘 ㅣㅁㄴ을 ㅏㅣ 시ㅣㅣㅣㅣㅣㅣㅣㅣ바ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㄹ
3.공통숫자를 뽑는다
4.곱한다.
'''
a = int(input("첫번째 숫자를 고르시오징어.:"))
b = int(input("두번째 숫자를 고르시오다리.:"))

def yaksu(a):
    c = int(a/2)
    d = [a]
    while c >= 1:
        if a % c == 0 :
            d.append(c)
            c = c-1
        else:
            c = c-1
    return d
# https://wikidocs.net/24   함수 안에서 선언된 변수의 효력 범위   ??????? 머여 ㅅㅂ
q =set(yaksu(a))
w =set(yaksu(b))

#최대공약수
e = list(q & w)
gcd = max(e)
'''
#최소공배수
def soinsu(a):
    p =[]
    l = 2
    while a != 1:
    if a%l == 0:
        p.append(l)
        n = a/l
    else :
        l = l+1

xx = soinsu(a)
yy = soinsu(b)
'''

n =2
p =1
while a/n >= 1 :
    if a%n == 0 and b%n ==0 :
        p = p*n
        a = a/n
        b = b/n
    else :
        n = n+1
        continue
p = int(p*a*b)

print("최대공약수는 {} 입니다".format(gcd))
print("최소공배수는 {}".format(p))









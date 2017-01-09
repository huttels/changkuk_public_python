a = int(input("2진법으로 만들 숫자를 입렬하시옹 : "))
b = []
while a/2 >= 1 :
    b.append(int(a)%int(2))    # 여기서 b.append(str(int(a)%int(2)))  왜 안됨요??
    a = a/2
b.append(1)                   # str(b) -> print("".join(b))왜 안됨요??

c=[]
for i in b:
    c.append(str(i))
c.reverse()
print("".join(c))

'''
http://blog.eairship.kr/285
초기화 ???
set.name =name 이 왜 초기화??
name값을 집어넣는거 아님???

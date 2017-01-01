import random


# answer = []
# b = [1,2,3]
#
# for a in b :
#     answer.append(random.randrange(0,10))
# answer = list(set(answer))
# while len(answer) != 3 :
#     answer.append(random.randrange(0,10))
#     answer = list(set(answer))

def ohyeah():
    answer = []

    for a in range(1,4):
        answer.append(random.randrange(1, 10))
    answer = list(set(answer))
    while len(answer) != 3:
        answer.append(random.randrange(1, 10))
        answer = list(set(answer))
    return answer


c = ohyeah()
'''
ck = 0
guess = []
while ck < 3 :
    ck = ck+1
    m = input("골라골라 :")
    m2 = int(m)
    guess.append(m2)
'''


def goguess():
    ck = 0
    guess = []
    while ck < 3:
        ck = ck + 1
        m = input("골라골라 :")
        m2 = int(m)
        guess.append(m2)
    return guess


# 너가 넣은 숫자 3개 와 지렸당
# 리스트 - 위치 확인(index) 함수
# 같은숫자있으면 볼
# 같은숫자에같은 위치면 스트랔




kk =0
d = []
while c != d:
    kk= kk+1
    pp = 0
    ap = 0
    d = goguess()
    for i in range(0,3):

        if c[i] == d[i]:
            pp = pp + 1

        elif c[i] in d:
            ap = ap + 1

    print("{}스트라이크{}볼 입니다".format(pp, ap))

print("축하합니다!!! {}턴만에 맞추셨습니다~~".format(kk))


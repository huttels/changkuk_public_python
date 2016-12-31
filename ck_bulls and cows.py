

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

def ohyeah() :
    answer = []
    b = [1, 2, 3]

    for a in b:
        answer.append(random.randrange(0, 10))
    answer = list(set(answer))
    while len(answer) != 3:
        answer.append(random.randrange(0, 10))
        answer = list(set(answer))
    return answer
c=ohyeah()
'''
ck = 0
guess = []
while ck < 3 :
    ck = ck+1
    m = input("골라골라 :")
    m2 = int(m)
    guess.append(m2)
'''
def goguess() :
    ck = 0
    guess = []
    while ck < 3:
        ck = ck + 1
        m = input("골라골라 :")
        m2 = int(m)
        guess.append(m2)
    return guess
d = goguess()

# 너가 넣은 숫자 3개 와 지렸당
#리스트 - 위치 확인(index) 함수
#같은숫자있으면 볼
#같은숫자에같은 위치면 스트랔
cj = 0
guess = []
while c != guess :
    goguess()
    if c[0] in guess :
        print("볼입니다")
    elif c[1] in guess :
        print()







# 숫자야구
import random

answer = []
number_array = list(range(1, 11))
random.shuffle(number_array)
# print(number_array)

for i in range(0, 3):
    answer.append(number_array[i])


def get_user_input():
    user_input = []
    while True:
        for i in range(1, 4):
            user_input.append(int(input("{}번째 숫자를 입력하세요 : ".format(i))))
        break
    return user_input


def get_game_result(answer, input):
    ball = 0
    strike = 0
    for i in range(0, 3):
        for j in range(0, 3):
            # print("compare {} and {}".format(answer[i], user_input[j]))
            if answer[i] == input[j]:
                if i == j:
                    strike += 1
                else:
                    ball += 1

    print("ball : {} , Strike : {}".format(ball, strike))
    if strike == 3:
        return True


while True:
    if get_game_result(answer, get_user_input()):
        print("게임이 끝났습니다!!")
        break

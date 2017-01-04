import random

answer = []
number_array = list(range(1, 11))
random.shuffle(number_array)
print(number_array)

answer = number_array[0:3]

print(answer)
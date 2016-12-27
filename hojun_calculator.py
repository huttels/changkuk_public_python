# 목표 결과물 예시
# Select operation.
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide
# Enter choice(1/2/3/4): 3
# Enter first number: 15
# Enter second number: 14
# 15 * 14 = 210


def calculator(first_number, second_number, index):
    switcher = {
        1: first_number + second_number,
        2: first_number - second_number,
        3: first_number * second_number,
        4: first_number / second_number
    }
    return switcher.get(index)


calculator_sign = {
    1: "+",
    2: "-",
    3: "*",
    4: "/"
}

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = int(input("Enter choice(1/2/3/4):"))
first_number = int(input("Enter first number:"))
second_number = int(input("Enter second number:"))
result = '{} {} {} = {}'.format(first_number, calculator_sign.get(choice), second_number, calculator(first_number, second_number,
                                                                                            choice))
print(result)
# print(first_number + calculator_sign.get(choice) + second_number + " = " + calculator(first_number, second_number,
#                                                                                       choice))

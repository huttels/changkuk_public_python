print("which one do you need?")
cal = int(input("1.add 2.subtract 3.multifly 4.devide : "))
first_number = int(input("first number : "))
second_number = int(input("second number : "))

if cal == 1:
    print(first_number + second_number)
elif cal == 2:
    print(first_number - second_number)
elif cal == 3:
    print(first_number * second_number)
elif cal == 4:
    print(first_number / second_number)

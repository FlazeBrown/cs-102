print("Введите первое и второе число")
first_num, second_num = int(input()), int(input())
print("Введите операцию")
operation = input()
if operation == "+":
    print(first_num + second_num)
elif operation == "-":
    print(first_num - second_num)
elif operation == "*":
    print(first_num * second_num)
elif operation == "/":
    if second_num != 0:
        print(first_num / second_num)
    else:
        print("На 0 делить нельзя!")
else:
    print("Неизвестная операция")

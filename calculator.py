"""Это калькулятор."""

first_operand = float(input("Введи первое число: "))
second_operand = float(input("Введи второе число: "))
operation = str(input("Введи операцию: "))

if operation == "+":
    result = first_operand + second_operand
    print(result)
elif operation == "-":
    result = first_operand - second_operand
    print(result)
elif operation == "*":
    result = first_operand * second_operand
    print(result)
elif operation == "/" and second_operand == 0:
    print("Деление на 0!")
elif operation == "/":
    result = first_operand / second_operand
    print(result)
elif operation == "mod" and second_operand == 0:
    print("Деление на 0!")
elif operation == "mod":
    result = first_operand % second_operand
    print(result)
elif operation == "pow":
    result = first_operand ** second_operand
    print(result)
elif operation == "div" and second_operand == 0:
    print("Деление на 0!")
else:
    result = first_operand // second_operand
    print(result)
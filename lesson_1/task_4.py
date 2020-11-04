# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num = int(input("Введите целое положительное число: "))

if num < 0:
    print("Вы ввели отрицательное число: ")
else:
    power = 1
    depth = 10
    max_digit = 0

    while num / depth > 1:

        digit = (num % depth) // (10 ** (power - 1))
        if digit > max_digit:
            max_digit = digit

        power = power + 1
        depth = 10 ** power

    print(f"Самая большая цифра в числе: {max_digit}")

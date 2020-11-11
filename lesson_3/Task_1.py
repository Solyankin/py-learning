# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Делитель равен нулю!")


print(f"Результат деления: {div(1, 1)}")
print(f"Результат деления на ноль: {div(1, 0)}")

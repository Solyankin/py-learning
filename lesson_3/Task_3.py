#  Реализовать функцию my_func(), которая принимает три позиционных аргумента,
#  и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    values = [a, b, c]
    min_value = min(values)
    values.remove(min_value)

    s = 0
    for num in values:
        s += num

    return s


print(my_func(1, -1, 2))
print(my_func(1, 1, 2))
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def calculate_salary(hours, rate, bonus):
    try:
        hours = float(hours)
        if hours < 0:
            raise ValueError()
    except ValueError:
        return f"Значение выработка в часах должно быть положительным числом. Вы ввели '{hours}'"

    try:
        rate = float(rate)
        if rate < 0:
            raise ValueError()
    except ValueError:
        return f"Значение ставки должно быть положительным числом. Вы ввели '{rate}'"

    try:
        bonus = float(bonus)
        if bonus < 0:
            raise ValueError()
    except ValueError:
        return f"Значение премии должно быть положительным числом. Вы ввели '{bonus}'"

    salary = hours * rate + bonus
    return round(salary, 2)


print(calculate_salary(argv[1], argv[2], argv[3]))

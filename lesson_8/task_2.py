# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.


class CustomZeroDivisionError(ZeroDivisionError):

    def __init__(self):
        super().__init__(self, self.__str__())

    def __str__(self):
        return "На ноль делить нельзя!"


a = int(input("Введите делимое: "))

while True:
    b = int(input("Введите делитель: "))

    if not b == 0:
        break
    else:
        print(CustomZeroDivisionError())

print(f"Результат деления {a} на {b} равен {a / b}")


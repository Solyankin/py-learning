#  Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
#  В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
#  должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
#  Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
#  Проверить работу полученной структуры на реальных данных.

class Date:

    def __init__(self, data):
        self.data = data
        self.day = None
        self.month = None
        self.year = None

    def __str__(self):
        return f"Raw: {self.data}, Day: {self.day}, Month: {self.month}, Year: {self.year}"

    @classmethod
    def convert_to_int(cls, date):
        date.day, date.month, date.year = map(int, date.data.split("-"))
        return date

    @staticmethod
    def validate(date):
        if any([e is None for e in [date.day, date.month]]):
            Date.convert_to_int(date)

        errors = []

        if date.day <= 0 or date.day > 31:
            errors.append(f"Day value ({date.day}) must be in range [1, 31]")

        if date.month <= 0 or date.month > 12:
            errors.append(f"Month value ({date.month}) must be in range [1, 12]")

        if date.year <= 0:
            errors.append(f"Year value ({date.year}) must be greater than 0")

        if len(errors) > 0:
            raise ValueError("\n".join(errors))


date_1 = Date.convert_to_int(Date("27-11-2020"))
print(date_1)
Date.validate(date_1)

Date.validate(Date("32-14-2020"))

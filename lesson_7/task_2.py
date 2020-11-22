# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и м.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        Clothes.__init__(self, "Пальто")
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size <= 0:
            raise ValueError("Размер должен быть положительным числом")
        self.__size = size

    def fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, height):
        Clothes.__init__(self, "Костюм")
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("Рост должен быть положительным числом")
        self.__height = height

    def fabric_consumption(self):
        return 2 * self.height + 0.3


print(Coat(173).fabric_consumption())
print(Suit(0).fabric_consumption())

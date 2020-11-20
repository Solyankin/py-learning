# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

def draw_by(stationery):
    print(f"{stationery.title} рисует")


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):

    def __init__(self):
        Stationery.__init__(self, "ручка")

    def draw(self):
        draw_by(self)


class Pencil(Stationery):

    def __init__(self):
        Stationery.__init__(self, "карандаш")

    def draw(self):
        draw_by(self)


class Handle(Stationery):

    def __init__(self):
        Stationery.__init__(self, "маркер")

    def draw(self):
        draw_by(self)


Pen().draw()
Pencil().draw()
Handle().draw()

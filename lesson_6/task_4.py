# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:

    def __init__(self, color, name, is_police):
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed = 0

    def go(self):
        print("Go")

    def stop(self):
        self.speed = 0
        print("Stop")

    def turn(self, direction):
        print(f"Turn {direction}")

    def increase_speed(self, value):
        self.speed += value
        self.show_speed()

    def decrease_speed(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0
        self.show_speed()
        if self.speed == 0:
            self.stop()

    def show_speed(self):
        print(f"Speed is {self.speed}")
        return self.speed


def warn_speed(threshold, value):
    if value > threshold:
        print(f"Attention! Speed {value} is too high!")


class TownCar(Car):

    def __init__(self, color, name):
        Car.__init__(self, color, name, is_police=False)

    def show_speed(self):
        warn_speed(60, super().show_speed())


class SportCar(Car):

    def __init__(self, color, name):
        Car.__init__(self, color, name, is_police=False)


class WorkCar(Car):

    def __init__(self, color, name):
        Car.__init__(self, color, name, is_police=False)

    def show_speed(self):
        warn_speed(40, super().show_speed())


class PoliceCar(Car):

    def __init__(self, color, name):
        Car.__init__(self, color, name, is_police=True)


car = TownCar("red", "zaparojez")

car.go()
car.increase_speed(10)
car.increase_speed(60)
car.turn("left")
car.turn("right")
car.decrease_speed(70)

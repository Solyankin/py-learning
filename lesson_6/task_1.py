# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from itertools import cycle
from time import sleep


class TrafficLight:
    __color = None

    def running(self):
        color_seq = ["Red", "Yellow", "Green", "Yellow"]  # Последовательность переключения цветов
        timing = {"Red": 7, "Yellow": 2, "Green": 5}  # тайминг для каждого цвета

        for color in cycle(color_seq):
            self.__color = color
            waiting = timing[color]
            print(f"{self.__color} (wait {waiting} sec)")
            sleep(waiting)
        #
        # [for i in range(len(self.__timing))]
        # for color in cycle(colors):
        #     self.__color = color


TrafficLight().running()

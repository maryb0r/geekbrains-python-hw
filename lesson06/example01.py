# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep

class TrafficLight:
    __color = None

    def __setcolor(self, color):
        self.__color = color
        print(self.__color)

    def running(self):
        try:
            while True:
                self.__setcolor("red")
                sleep(7)
                self.__setcolor("yellow")
                sleep(2)
                self.__setcolor("green")
                sleep(5)
        except KeyboardInterrupt:
            exit()

trafficlight = TrafficLight()
trafficlight.running()

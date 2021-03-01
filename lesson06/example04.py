# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    speed: int = 0
    color: str = None
    name: str = None
    is_police: bool = False
    def __init__(self, name, color):
        self.name = name
        self.color = color
        if self.is_police is True:
            print(f"{self.color} {self.name} is police")
        else:
            print(f"{self.color} {self.name} is not police")

    def show_speed(self):
        print(f"Speed of {self.color.lower()} {self.name} is {self.speed}")

    def go(self, speed):
        self.speed = speed
        print(f"{self.color} {self.name} is riding")

    def stop(self):
        self.speed = 0
        print(f"{self.color} {self.name} stopped")

    def turn(self, direction):
        print(f"{self.color} {self.name} turned {direction}")


class TownCar(Car):
    def show_speed(self):
        print(f"Speed of {self.color.lower()} {self.name} is {self.speed}")
        if self.speed > 60:
            print("Slow down, please!")


class WorkCar(Car):
    def show_speed(self):
        print(f"Speed of {self.color.lower()} {self.name} is {self.speed}")
        if self.speed > 40:
            print("Slow down, please!")


class PoliceCar(Car):
    is_police = True


vw = TownCar("VW", "White")
vw.show_speed()
vw.go(30)
vw.turn("left")
vw.go(100)
vw.show_speed()
vw.turn("right")
vw.go(40)
vw.stop()
print()
police = PoliceCar("police Toyota", "Silver")
police.go(30)
police.show_speed()
police.stop()
print()
kia = TownCar("Kia", "Brown")
kia.show_speed()
kia.go(40)
kia.turn("left")
kia.go(100)
kia.show_speed()
kia.turn("right")
kia.go(30)
kia.stop()

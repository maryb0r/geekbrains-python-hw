# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str = None
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Drawing by {self.title}")


class Pen(Stationery):
    def draw(self):
        print("Drawing by pen")


class Pencil(Stationery):
    def draw(self):
        print("Drawing by pencil")


class Handle(Stationery):
    def draw(self):
        print("Drawing by handle")


brush = Stationery("brush")
brush.draw()
pen = Pen("blue pen")
pen.draw()
pencil = Pencil("red pencil")
pencil.draw()
handle = Handle("violet handle")
handle.draw()

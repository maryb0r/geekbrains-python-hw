# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы
# и т.д.

from random import randint

class Matrix:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def __str__(self):
        string = ''
        for i in self.list1:
            string += str(i) + '\n'
        string += '\n'
        for i in self.list2:
            string += str(i) + '\n'
        return string

    def __add__(self):
        result = self.list1
        for i in range(0, len(self.list1)):
            for j in range(0, len(self.list1[i])):
                result[i][j] += self.list2[i][j]
        return Matrix(result, [])

x = 3
y = 3
a = Matrix([[randint(1, 100) for _ in range(0, y)] for _ in range(0, x)],
           [[randint(1, 100) for _ in range(0, y)] for _ in range(0, x)])
print(a)
print(a.__add__())

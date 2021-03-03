# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
# умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex:
    real: float = None
    imaginary: float = None
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return [self.real + other.real, self.imaginary + other.imaginary]

    def __mul__(self, other):
        return [self.real * other.real - self.imaginary * other.imaginary,
                self.real * other.imaginary + self.imaginary * other.real]


a = Complex(2, -2)
b = Complex(-1, -5)
print(a + b)
print(a * b)

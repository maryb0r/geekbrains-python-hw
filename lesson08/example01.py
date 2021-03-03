# Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    data: str = None
    def __init__(self, data):
        self.data = data

    @classmethod
    @staticmethod
    def convert_to_number(cls):
        return int(''.join(word for word in cls.data.split(sep='-')))

    @staticmethod
    def is_valid(cls):
        flag = True
        user_data = [word for word in cls.data.split(sep='-')]
        # print(user_data)
        if (int(user_data[0]) < 1 or int(user_data[0]) > 31) \
            or (int(user_data[1]) < 1 or int(user_data[1]) > 12) \
            or int(user_data[2]) < 0:
            flag = False
        if flag:
            return f"Data is valid"
        return f"Data is invalid"


print(Data.convert_to_number(Data("01-01-2021")))
print(Data.convert_to_number(Data("56-99-1234")))
print(Data.is_valid(Data("15-04-1992")))
print(Data.is_valid(Data("34-08-2077")))
print(Data.is_valid(Data("7-34-1234")))

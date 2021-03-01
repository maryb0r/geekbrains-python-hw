# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name: str = None
    surname: str = None
    position: str = None
    wage: int = None
    bonus: int = None
    _income = None
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def _set_income(self, wage, bonus):
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": self.wage, "bonus": self.bonus}

    def _get_income(self):
        return f"Total income = {sum(self._income.values())}, " \
               f"wage = {self._income['wage']}, " \
               f"bonus = {self._income['bonus']}"


class Position(Worker):

    def get_full_name(self):
        return f"Name: {self.name}, surname: {self.surname}, position: {self.position}"

    def get_total_income(self, wage, bonus):
        self._set_income(wage, bonus)
        return self._get_income()


employee = Position("Petr", "Petrov", "engineer")
print(employee.get_full_name())
print(employee.get_total_income(50000, 10000))

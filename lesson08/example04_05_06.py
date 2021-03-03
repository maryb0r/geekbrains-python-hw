# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

# Продолжить работу над заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class Electronics:
    name: str = None
    number: int = None
    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number

class Warehouse:
    __counter: int = 0
    __statistics: dict = {}
    limit: int = None
    unit: Electronics = None
    def __init__(self, limit: int):
        self.limit = limit

    def add_unit(self, unit: Electronics):
        self.unit = unit
        self.__statistics.setdefault(self.unit.name, 0)
        try:
            if self.__counter + self.unit.number < self.limit:
                self.__statistics[self.unit.name] += self.unit.number
                self.__counter += self.unit.number
                print(f"{self.unit.number} {self.unit.name.lower()}(s) are in the warehouse now")
            else:
                print(f"No free space in the warehouse for {self.unit.number} {self.unit.name.lower()}(s)")
        except TypeError:
            print("Enter the correct number")

    def give_unit(self, unit: Electronics):
        self.unit = unit
        self.__statistics.setdefault(self.unit.name, 0)
        try:
            if self.__statistics.get(self.unit.name) > self.unit.number:
                self.__statistics[self.unit.name] -= self.unit.number
                print(f"{self.unit.number} {self.unit.name.lower()}(s) shipped from the warehouse")
                self.__counter -= self.unit.number
            else:
                print(f"No {self.unit.number} {self.unit.name.lower()}(s) in the warehouse")
        except TypeError:
            print("Enter the correct number")

    def show_statistics(self):
        return f"Now in the warehouse: {self.__statistics}"

warehouse = Warehouse(50)

xerox = Electronics("Xerox", "10")
warehouse.add_unit(xerox)
scanner = Electronics("Scanner", 5)
warehouse.add_unit(scanner)
printer = Electronics("Printer", 5)
warehouse.add_unit(printer)
comp = Electronics("Computer", 20)
warehouse.add_unit(comp)
periph = Electronics("Periphery", 10)
warehouse.add_unit(periph)
print(warehouse.show_statistics())
xerox.number = 5
warehouse.give_unit(xerox)
scanner.number = 2
warehouse.give_unit(scanner)
monitor = Electronics("Monitor", 10)
warehouse.give_unit(monitor)
print(warehouse.show_statistics())

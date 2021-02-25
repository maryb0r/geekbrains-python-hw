# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

def salary_calc(employee_data):
    try:
        hours, rate, bonus = employee_data
        print(f"{(hours * rate) + bonus}")
    except ValueError:
        print("Invalid arguments")
        exit()

user_data = [int(argv[i]) for i in range(1, len(argv))]
salary_calc(user_data)

# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from random import randint
from sys import argv

def user_generator(start, stop, length):
    generated_list = []
    for i in range(0, length):
        generated_list.append(randint(start, stop))
    print(f"1st script from file example06_1.py. Generated list: {generated_list}")
    return generated_list

# user_generator(int(argv[1]), int(argv[2]), int(argv[3]))

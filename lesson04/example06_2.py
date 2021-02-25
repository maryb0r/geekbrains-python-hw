# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import cycle
from sys import argv
from example06_1 import user_generator

def list_iterator(user_list, count):
    print("2nd script from file example06_2.py. List of elements:")
    i = 0
    for element in cycle(user_list):
        if i > count:
            break
        i += 1
        print(element)

list_iterator(user_generator(int(argv[1]), int(argv[2]), int(argv[3])), int(argv[4]))

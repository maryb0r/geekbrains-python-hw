# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from random import randint
from functools import reduce

def multi(prev_num, num):
    return prev_num * num

number_list = []
for i in range(0, 10):
    num = randint(100, 1000)
    if num % 2 == 0:
        number_list.append(num)
print(f"Original list: {number_list}")
print(f"Result: {reduce(multi, number_list)}")

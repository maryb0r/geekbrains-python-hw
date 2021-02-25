# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from random import randint

number_list = []
for i in range(0, 15):
    number_list.append(randint(1, randint(1, 500)))
print(f"Original list: {number_list}")

new_list = []
for i in range(1, len(number_list)):
    if number_list[i] > number_list[i - 1]:
        new_list.append(number_list[i])
print(f"Filtered list: {new_list}")

# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

from random import randint

number_list = []
for i in range(0, 15):
    number_list.append(randint(1, randint(1, 50)))
print(f"Original list: {number_list}")

number_dict = {}
for x in number_list:
    number_dict.setdefault(x, 0)
    number_dict[x] += 1
print(f"Subtotal: {number_dict}")

print(f"Result: {list(key for key, value in number_dict.items() if value == 1)}")

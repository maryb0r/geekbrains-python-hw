# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Пример готовой структуры:
# [
#     (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
#     (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
#     (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
# ]

# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.

# Пример:
# {
# "название": ["компьютер", "принтер", "сканер"],
# "цена": [20000, 6000, 2000],
# "количество": [5, 2, 7],
# "ед": ["шт."]
# }

prod_dscr_type = {
    "Название": None,
    "Цена": None,
    "Количество": None,
    "Ед": None
}
print("\nДля выхода из программы введите номер товара 0\n")
total_struct = []
prod_struct = []
state_struct = {}
prod_num = 1
while prod_num > 0:
    prod_num = int(input("Введите номер товара >>> "))
    if prod_num == 0:
        continue
    temp_struct = prod_dscr_type.copy()
    for key, value in temp_struct.items():
        temp = input(f"{key} товара № {prod_num} >>> ")
        temp_struct[key] = temp
        state_struct.setdefault(key, []).append(temp)
    prod_struct.append(prod_num)
    prod_struct.append(temp_struct)
    total_struct.append(tuple(prod_struct))
    prod_struct.clear()
    print()
print(f"\nСписок введенных товаров:")
for element in total_struct:
    print(f"{element}")
print("\nСтатистика введенных товаров:")
for key, value in state_struct.items():
    print(f"{key}: {value}")

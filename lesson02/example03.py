# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

season_list = ['зима', 'весна', 'лето', 'осень']
season_dict = {
    'зима': [12, 1, 2],
    'весна': [3, 4, 5],
    'лето': [6, 7, 8],
    'осень': [9, 10, 11]
}

month = int((input("Введите месяц в виде целого числа от 1 до 12 >>> ")))

if month < 1 or month > 12:
    print("Номер месяца введен неверно!")
    exit()

print("Решение задачи с помощью list:")
if 3 <= month <= 5:
    print(f"Это {season_list[1]}")
elif 6 <= month <= 8:
    print(f"Это {season_list[2]}")
elif 9 <= month <= 11:
    print(f"Это {season_list[3]}")
else:
    print(f"Это {season_list[0]}")

print("Решение задачи с помощью dict:")
for key, value in season_dict.items():
    for element in value:
        if element == month:
            print(f"Это {key}")
            break

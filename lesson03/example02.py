# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

user_data_struct = {
    "Имя": None,
    "Фамилия": None,
    "Год рождения": None,
    "Город проживания": None,
    "email": None,
    "Телефон": None}

def set_user_data(name, surname, year, city, email, phone):
    print(
        f"Имя: {name}, "
        f"Фамилия: {surname}, "
        f"Год рождения: {year}, "
        f"Город проживания: {city}, "
        f"email: {email}, "
        f"Телефон {phone}"
    )

for key, value in user_data_struct.items():
    user_data_struct[key] = input(f"Введите поле {key} >>> ")
set_user_data(*user_data_struct.values())

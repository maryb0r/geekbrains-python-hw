# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(arg1, arg2):
    if arg2 == 0:
        return "Деление на ноль!"
    return f"{arg1} / {arg2} = {arg1 / arg2}"

try:
    user_arg1 = int(input("Введите целое делимое >>> "))
    user_arg2 = int(input("Введите целый делитель >>> "))
except ValueError:
    print("Введите целые числа")
print(div(user_arg1, user_arg2))

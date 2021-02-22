# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    arg_list = [arg1, arg2, arg3]
    arg_list.sort()
    print(f"{arg_list[1]} + {arg_list[2]} = {arg_list[1] + arg_list[2]}")

arg_list = [int(x) for x in input("Введите три целых числа через пробел >>> ").split()]
my_func(*arg_list)

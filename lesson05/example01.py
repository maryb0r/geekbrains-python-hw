# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("file01.txt", "w") as f_obj:
    line = None
    while line != '':
        line = input("Type your text >>> ")
        f_obj.write(f"{line}\n")

print()
with open("file01.txt", "r") as f_obj:
    print(f_obj.read())

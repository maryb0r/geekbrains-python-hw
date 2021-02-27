# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open("file03.txt", encoding="utf-8", mode="r") as f_obj:
    print(f_obj.read())

sum = 0
with open("file03.txt", encoding="utf-8", mode="r") as f_obj:
    for i, line in enumerate(f_obj.readlines(), start=1):
        if float(line.split()[1]) < 20000:
            print(f"Employee with payment less than 20000: {line.split()[0]}")
        sum += float(line.split()[1])
    print(f"Average salary: {sum / i}")

# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

line = ''
with open("file05.txt", "w") as f_write:
    for x in range(1, 10):
        line += f"{randint(1, 50)} "
    f_write.write(line)
    print(f"List = {line}")

with open("file05.txt", "r") as f_read:
    sum = 0
    for x in f_read.read().split():
        sum += int(x)
    print(f"Sum = {sum}")

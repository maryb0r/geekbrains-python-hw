# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

num_list = ["Один", "Два", "Три", "Четыре"]
with open("file04.txt", encoding="utf-8", mode="r") as f_read:
    with open("file04_new.txt", encoding="utf-8", mode="w") as f_write:
        for i, line in enumerate(f_read.readlines()):
            res_line = f"{num_list[i]} {line.split()[1]} {line.split()[2]}\n"
            f_write.writelines(res_line)

with open("file04.txt", encoding="utf-8", mode="r") as f1:
    print(f"Was:\n{f1.read()}")
with open("file04_new.txt", encoding="utf-8", mode="r") as f2:
    print(f"Now:\n{f2.read()}")

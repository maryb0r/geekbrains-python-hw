# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("file02.txt", encoding="utf-8", mode="r") as f_obj:
    for i, line in enumerate(f_obj.readlines(), start=1):
        print(f"Line {i} {len(line.split())} word(s): {line}")

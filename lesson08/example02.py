# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class ZeroDivision(Exception):
    def __init__(self, message):
        self.message = message

a = int(input("Enter dividend >>> "))
b = int(input("Enter divider >>> "))
try:
    if b == 0:
        raise ZeroDivision("Division by zero")
except ZeroDivision as message:
    print(message)
else:
    print(f"Result: {a / b}")

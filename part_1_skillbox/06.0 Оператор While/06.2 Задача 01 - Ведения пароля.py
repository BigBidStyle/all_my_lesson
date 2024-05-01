print("Задача № 1 -Введении пароля.")
password = int(input("Введите пароль: "))
while password != 1234:
    print("Пароль введен не верно!")
    password = int(input("Введите пароль: "))
print("Пароль верный! Добро пожаловать!")
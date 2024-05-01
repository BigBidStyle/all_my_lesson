print("Урок 10.2 Использование if во вложенных циклах.")
print("Задача № 1 - Матрица.")
size = int(input("Введите размер таблицы: "))
for row in range(1, size + 1):
    for col in range(1, size + 1):
        if row % 2 == 0:
            print(row, end = " ")
        else:
            print(col, end =  " ")
    print()
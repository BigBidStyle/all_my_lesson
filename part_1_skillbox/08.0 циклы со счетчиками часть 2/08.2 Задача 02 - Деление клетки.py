print("Теория - Задача № 2 - Деление клетки")
totalhours = int(input("Введите кол-во часов: "))
cells = 1
for hour in range (1, totalhours // 3 + 1):
    cells *= 2
    print("Прошло часов: ", hour * 3)
    print("Кол-во клеток: ", cells)
    print("Осталось часов: ", totalhours - hour * 3)
    print(" ")
print("Наблюдение завершено!")

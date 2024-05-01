print("Задача № 2 - Делаем дорогу.")
for row in range(20):
    for col in range(50):
        if row == 9:
            print('-', end = "")
        elif col == row + 29:
            print("\\", end = "")
        elif col == -row + 19:
            print("/", end = "")
        elif col == 24:
            print('|', end = "")
        else:
            print(" ", end = "")
    print()
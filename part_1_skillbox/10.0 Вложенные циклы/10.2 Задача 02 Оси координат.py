print("Задача № 2 - Оси координат.")
for row in range(20):
    for col in range(20):
        if row == 10:
            print(' - ', end="")
        elif col == 10:
            print('|', end="")
        else:
            print(" ", end="  ")
    print()

print("Введите расположение фигуры")
x = float(input("По горизонтали: "))
y = float(input("По вертикали: "))
if 0 < x < 0.8 and 0 < y < 0.8:
    xSquare = int(x * 10)
    ySquare = int(y * 10)
    print("Фигура находиться в клетке (", xSquare,",", ySquare, ")")
    popravka_x = round(float(xSquare / 10) + 0.05 - x, 3)
    popravka_y = round(float(ySquare / 10) + 0.05 - y, 3)
    print("Поправьте расположение фигуры на (",popravka_x, popravka_y,")")
else:
    print("\nКлетки с такой координатой не существует!!!\n")
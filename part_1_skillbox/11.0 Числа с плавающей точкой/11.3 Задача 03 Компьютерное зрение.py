while True:
    print("Введите местоположение фигуры")
    x = float(input("По горизонтали: "))
    y = float(input("По вертикали: "))
    if 0 < x < 0.8 and 0 < y < 0.8:
        xSquare = int(x * 10)
        ySquare = int(y * 10)
        print("\nФигура находиться в клетке (", xSquare, ySquare, ")\n")
    else:
        print("\nКлетки с такой координатой не существует!!!\n")
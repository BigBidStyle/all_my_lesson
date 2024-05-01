import math
choice = int(input("1 - расстояние до точки;\n"
                   "2 - расстояние между двумя точками: "))

def myDistance(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)
    print(distance)

def betweenDistance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(distance)


if choice == 1:
    x = float(input("Введите координату x: "))
    y = float(input("Введите координату y: "))
    myDistance(x, y)
elif choice == 2:
    x1 = float(input("Введите координату x1: "))
    y1 = float(input("Введите координату y1: "))
    x2 = float(input("Введите координату x2: "))
    y2 = float(input("Введите координату y2: "))
    betweenDistance(x1, y1, x2, y2)
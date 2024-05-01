print("\nУрок № 11.4 - Математические функции. Работа с модулем math")
print("Урок № 11.4 - Задача № 1 теория - Расположение танка.")
import math
distance = float(input("Введите расстояние до танка: "))
angle = float(input("Введите угол в градуса: "))
angle /= 57.2958
x = math.cos(angle) * distance
y = math.sin(angle) * distance
print("Координаты вражеского танка:", x,",", y)


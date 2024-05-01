# Задача 9. Уравнение
# Что нужно сделать
# Даны действительные коэффициенты a, b, c при этом a≠ 0 .
# Решите квадратное уравнение a∙x2+b∙x+c=0 и выведите все его корни.
# Если уравнение имеет два корня, выведите два корня в порядке возрастания,
# если один корень — выведите одно число, если нет корней — не выводите ничего

# Что оценивается
# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).

import math
a = int(input("Введите число а не равное 0: "))
while a == 0:
    a = int(input("Введите число а не равное 0: "))
b = int(input("Введите число в: "))
c = int(input("Введите число с: "))
discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
     x1 = round((-b + math.sqrt(discriminant)) / (2 * a), 2)
     x2 = round((-b - math.sqrt(discriminant)) / (2 * a), 2)
     if x1 < x2:
         print(f"Уравнение умеет два решения: \nx1 = {x1}\nx2 = {x2}")
     else:
         print(f"Уравнение умеет два решения: \nx2 = {x2}\nx1 = {x1}")
elif discriminant == 0:
     x1 = round(-b / (2 * a), 2)
     print(f"x = {x1}")


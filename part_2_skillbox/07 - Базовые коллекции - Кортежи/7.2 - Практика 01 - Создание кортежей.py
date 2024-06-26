# Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно.
# Также заполните второй кортеж числами от −5 до 0. Объедините два кортежа, создав тем
# самым третий кортеж. С помощью метода кортежа определите в нём количество нулей.
# Выведите на экран третий кортеж и количество нулей в нём.

import random

def create_random_tuple(a, b, n):
    return tuple([random.randint(a, b) for _ in range(n)])

first = create_random_tuple(0, 5, 10)                   # Создаем кортеж из рандомных чисел от 0 до 5 в кол-ве 10 шт.
second = create_random_tuple(-5, 0, 10)                 # Создаем кортеж из рандомных чисел от -5 до 5 в кол-ве 10 шт.
third = first + second                                  # Объединяем два кортежа.
nulls_count = third.count(0)                            # Считаем кол-во нулей в третьем кортеже.
print(first)
print(second)
print(third,"\n", nulls_count, " <-- Кол-во нулей в третем кортеже")

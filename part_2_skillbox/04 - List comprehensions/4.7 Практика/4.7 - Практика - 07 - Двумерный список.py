# Как мы говорили ранее, в программировании часто приходится писать код исходя из результата,
# который требует заказчик. В этот раз заказчику нужно получить вот такой двумерный список:

[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# Напишите программу, которая генерирует такой список и выводит его на экран. Используйте только list comprehensions.

import random
shift = int(input("Введите шаг: "))
number_elements = int(input("Введете кол-во массивов: "))
digit_elements = int(input("Введите кол-во элементов в массиве: "))


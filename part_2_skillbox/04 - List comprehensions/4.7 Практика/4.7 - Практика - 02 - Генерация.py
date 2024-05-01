# Пользователь вводит целое число N. Напишите программу,
# которая генерирует список из N чисел, на чётных местах в нём
# стоят единицы, а на нечётных — числа, равные остатку от деления
# своего номера на 5.

# Пример:
# Введите длину списка: 10
# Результат: [1, 1, 1, 3, 1, 0, 1, 2, 1, 4]

import random
number = int(input("Введите длину списка: "))
number_list = [random.randint(1, 100) for _ in range(number)]
print(number_list)

new_list = [(i // i if i in number_list[1::2] else i % 5) for i in number_list]
print(f"Результат: {new_list}")
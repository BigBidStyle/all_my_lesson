# Дан список из N целых случайных чисел (число от 0 до 2). 
# Напишите программу, которая выполняет «сжатие списка» — переставляет все нулевые 
# элементы в конец массива. При этом все ненулевые элементы располагаются в начале 
# массива в том же порядке. Затем все нули из списка удаляются.

# Пример:

# Количество чисел в списке: 10
# Список до сжатия: [0, 2, 1, 0, 0, 0, 1, 0, 2, 0]
# Список после сжатия: [2, 1, 1, 2]

import random
numbers = int(input("Введите кол-во чисел: "))

numbers_list = [random.randint(0, 2) for a in range(numbers)]
print(f"Список до сжатия: {numbers_list}")

new_list = [i for i in numbers_list if i != 0]
print(f"Список после сжатия: {new_list}")
# N палочек выставили в один ряд, пронумеровав их слева направо числами от 1 до N.
# Затем по этому ряду бросили K камней, при этом i-й камень сбил все палки с номерами
# от L_i до R_i включительно. Определите, какие палки остались стоять на месте.

# Напишите программу, которая получает на вход количество палок N и количество
# бросков K. Далее идёт K пар чисел Left_i, Right_i, при этом 1 ≤ Left_i ≤ Right_i ≤ N.

# Программа должна вывести последовательность из N символов, где j-й символ есть
# “I”, если j-я палка осталась стоять, или “.”, если j-я палка была сбита.

# Пример:
# Количество палок: 10
# Количество бросков: 3

# Бросок 1. Сбиты палки с номера 8
# по номер 10.

# Бросок 2. Сбиты палки с номера 2
# по номер 5.

# Бросок 3. Сбиты палки с номера 3
# по номер 6.

# Результат: I.....I...
import random
from itertools import groupby
n = int(input("Введите кол-во палок: "))
k = int(input("Введите кол-во бросков: "))
print("\n")

list_sticks = [i + 1 for i in range(n)]

result = []
for cast in range(k):
    left_i = random.randint(1, n)
    right_i = random.randint(left_i, n)
    print(f"Бросок {cast + 1}. Сбиты палки с номера {left_i} по номер {right_i}")
    result_1 = [result.append(i) for i in list_sticks if left_i <= i <= right_i]

# Сортируем и удаляем дублирующиеся элементы.
result.sort()
result = [el for el, _ in groupby(result)]

new_list = []
result_2 = [(new_list.append("I") if i not in result else new_list.append(".")) for i in list_sticks]
end_result = [print(i, end="") for i in new_list]

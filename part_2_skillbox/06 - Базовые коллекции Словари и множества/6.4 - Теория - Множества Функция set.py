# Убрать одинаковые числа.
import random
number_list = [random.randint(1, 4) for _ in range(10)]

# По факту закоментированный код не нужен!!! Результат одинг и тот же....
# new_list = []
# for i_num in number_list:
#     if i_num not in new_list:
#         new_list.append(i_num)
print(number_list)
# print(new_list)

unique = set(number_list)
print(unique, "\n")

# -----------------------------------
num_1 = {1, 2, 3, 4, 5}
num_2 = {4, 5, 6, 7, 8}
print(num_1.intersection(num_2))                                 # {4, 5}
# то же самое получиться если написать код вот так
print(num_1 & num_2)                                                # {4, 5}
print(num_1.union(num_2))                                         # {1, 2, 3, 4, 5, 6, 7, 8}
print(num_1.difference(num_2))                                   # {1, 2, 3}
print(num_1 - num_2)                                                # {1, 2, 3}
print(num_2 - num_1)                                                # {8, 6, 7}

# --------------------------
nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]
# Убираем повторяющиеся элементы.
nums_set_1 = set(nums_1) # {1, 2, 3, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 20, 21, 22, 24, 26, 27, 29}
nums_set_2 = set(nums_2) # {1, 5, 7, 8, 9, 11, 12, 13, 15, 16, 19, 21, 22, 23, 24, 29, 30}
# Затем удаляет минимальный элемент из каждого множества
nums_set_1.discard(min(nums_set_1))
nums_set_2.discard(min(nums_set_2))
# добавляем случайное число в диапазоне от 100 до 200.
nums_set_1.add(random.randint(100, 200))
nums_set_2.add(random.randint(100, 200))
# Вывести все элементы множеств (объединение).
print(nums_set_1 | nums_set_2)
# Вывести только общие элементы (пересечение).
print(nums_set_1 & nums_set_2)
# Вывести элементы, входящие в nums_2, но не входящие в nums_1.
print(nums_set_2 - nums_set_1)
from typing import List

my_nums: List[int] = [3, 1, 4, 1, 5, 9, 2, 6]
other_nums: List[int] = [2, 7, 1, 8, 2, 8, 1, 8]

result: List[int] = list(map(lambda x, y: x + y, my_nums, other_nums))
print(result)

print(list(map(lambda x, y: 1, [1, 2], [2, 3, 4])))
# -------------------------------------------------------------------------------------------------------------------- #
result_event: List[int] = list(filter(lambda x: x % 2 == 0, result))
print(result_event)

result = map(lambda num: num * 3, filter(lambda num: num % 2, my_nums))
print(list(result))

# -------------------------------------------------------------------------------------------------------------------- #
animals = ['cat', 'dog', 'cow'] # Нужно ['Сat', 'Вog', 'Сow']

# решение с map
new_animals_1 = list(map(lambda elem: elem.capitalize(), animals))

# решение с list comprehension
new_animals_2 = [elem.capitalize() for elem in animals]
# -------------------------------------------------------------------------------------------------------------------- #
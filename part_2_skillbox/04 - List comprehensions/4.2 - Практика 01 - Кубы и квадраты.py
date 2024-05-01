# Пользователь вводит числа A и B. Напишите программу,
# которая генерирует два списка: в первом лежат кубы чисел
# в диапазоне от А до В, во втором — квадраты чисел в этом же
# диапазоне. Выведите списки на экран. Для генерации используйте
# list comprehensions (как и в следующих задачах).

# Пример:
# Левая граница: 5
# Правая граница: 10

# Список кубов чисел в диапазоне от 5 до 10: [125, 216, 343, 512, 729, 1000]
# Список квадратов чисел в диапазоне от 5 до 10: [25, 36, 49, 64, 81, 100]

left_border = int(input("Левая граница: "))
right_border = int(input("Правая граница: "))

list_cube = [x ** 3 for x in range(left_border, right_border + 1)]
list_square = [x ** 2 for x in range(left_border, right_border + 1)]

print(f"Список кубов чисел в диапазоне от {left_border} до {right_border}: {list_cube}")
print(f"Список квадратов чисел в диапазоне от {left_border} до {right_border}: {list_square}")

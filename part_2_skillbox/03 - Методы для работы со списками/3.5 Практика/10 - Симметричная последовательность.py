# Последовательность чисел называется симметричной, если она одинаково читается как слева направо, т
# ак и справа налево. Например, следующие последовательности являются симметричными:

# 1 2 3 4 5 4 3 2 1
# 1 2 1 2 2 1 2 1

# Пользователь вводит последовательность из N чисел. Напишите программу, которая определяет,
# какое минимальное количество и каких чисел надо приписать в конец этой последовательности,
# чтобы она стала симметричной.

# Пример 1:
# Кол-во чисел: 5
# Число: 1
# Число: 2
# Число: 1
# Число: 2
# Число: 2

# Последовательность: [1, 2, 1, 2, 2]

# Нужно приписать чисел: 3
# Сами числа: [1, 2, 1]

# Пример 2:
# Кол-во чисел: 5
# Число: 1
# Число: 2
# Число: 3
# Число: 4
# Число: 5

# Последовательность: [1, 2, 3, 4, 5]

# Нужно приписать чисел: 4
# Сами числа: [4, 3, 2, 1]

numbers = int(input("Кол-во чисел: "))
numbers_list = []

for i in range(numbers):
    print(f"Число: ", end="")
    digit = int(input())
    numbers_list.append(digit)

print(f"Последовательность: {numbers_list}")

for i in range(numbers - 1):
    if numbers_list[i] != numbers_list[(i + 1)]:
        numbers_list.insert(numbers, numbers_list[i])

print(numbers_list)

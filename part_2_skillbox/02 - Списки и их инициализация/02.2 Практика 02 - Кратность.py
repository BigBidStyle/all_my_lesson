# Пользователь вводит список из N чисел и число K. Напишите код,
# выводящий на экран сумму индексов элементов списка, которые кратны K.

# Пример:
# Кол-во чисел в списке: 4
# Введите 1 число: 1
# Введите 2 число: 20
# Введите 3 число: 30
# Введите 4 число: 4

# Введите делитель: 10
# Индекс числа 20: 1
# Индекс числа 30: 2
# Сумма индексов: 3

number_count = int(input("Введите кол-во чисел: "))
number = []

for i in range(number_count):
    print(f"Введите {i + 1} число: ", end=" ")
    digit = int(input())
    number.append(digit)

summ = 0
divider = int(input("\nВведите делитель: "))
for i_number in range(number_count):
    if number[i_number] % divider == 0:
        print(f"Индекс числа {number[i_number]}: {i_number + 1}")
        summ += i_number + 1
print(f"Сумма индексов: {summ}")

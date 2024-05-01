print("Урок 8.2 Алгоритмические задачи со счётными циклами.")
print("Теория - Задача № 1")
n = int(input("Введите число: "))
for number in range(1, n // 2 + 1):
    number *= 2
    print(number, "в степени 3 =", number ** 3)
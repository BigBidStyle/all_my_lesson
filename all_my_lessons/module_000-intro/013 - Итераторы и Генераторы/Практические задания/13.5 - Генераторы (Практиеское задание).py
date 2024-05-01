# Задача 1. Бесконечный генератор
# По аналогии с бесконечным итератором из практики предыдущего урока, реализуйте свой счётчик-генератор, который также
# в цикле будет бесконечно выдавать значения.

# Дополнительно: преобразуйте (или напишите с нуля) итератор простых чисел в функцию-генератор.
# Мое решение
# def iterator():
#     counter = 0
#     while True:
#         yield counter  # <-- Выдать значение (Он замораживает функцию, со всеми значениями)
#         counter += 1
#
# my_iter = iterator()
# for i_elem in my_iter:
#     print(i_elem)
#
# def counter():
#     n = 0
#     while True:
#         n += 1
#         yield n

# Решение от skilBox ой это оказалось допюзаданием
def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


for i in get_prime_numbers(50):
    print(i, end='\t')
print()
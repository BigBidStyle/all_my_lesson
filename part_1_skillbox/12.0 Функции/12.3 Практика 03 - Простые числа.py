# Задача 3. Простые числа
# Пользователь вводит число N — количество чисел в последовательности.
# Напишите программу, которая проверяет, сколько из этих чисел являются простыми.
# Для проверки простоты числа реализуйте функцию isPrime.

def isPrime(N):
    count = 0
    for number in range(1, N + 1):
        isPrime = True
        for divider in range(2, number):
            if number % divider == 0:
                isPrime = False
                break
        else:
            count += 1
    print(f"В последовательности {count} простых чисел.")

N = int(input("Введите количество чисел в последовательности: "))
isPrime(N)




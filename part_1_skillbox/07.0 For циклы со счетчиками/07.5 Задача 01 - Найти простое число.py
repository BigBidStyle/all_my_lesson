print("Урок 7.5 Типовые алгоритмы со счётными циклами.")
print("Теория - Задача № 1 - найти простое число.")
number = int(input("Нипишите число: "))
isPrime = True
for divider in range(2, number):
    if number % divider == 0:
        isPrime = False
        break
if isPrime:
    print("Число простое")
else:
    print("Число составное")

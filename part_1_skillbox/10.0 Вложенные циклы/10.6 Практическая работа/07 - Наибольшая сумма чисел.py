# Задача 7. Наибольшая сумма цифр
# Что нужно сделать
# Пользователь вводит N чисел. Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.


summ = 0
maxNumber = 0
sumNumber = 0
for number in range(int(input("Введите кол-во чисел: "))):
    isPrime = True
    number = int(input("Введите число: "))
    for divider in range(2, number):
        if number % divider == 0:
            isPrime = False
            break
    if isPrime:
        if maxNumber < number:
            maxNumber = number
        while number != 0:
            summ = summ + number % 10
            number = number // 10
        if sumNumber < summ:
            sumNumber = summ
        summ = 0
print(f"\nМаксимально большое простое число: {maxNumber}")
print(f"Сумма всех цифр этого числа равно: {sumNumber}")





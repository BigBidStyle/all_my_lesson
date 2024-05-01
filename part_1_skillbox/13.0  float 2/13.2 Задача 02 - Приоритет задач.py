def numeral_count(number):
    if number < 0:
        print("Число отрицательное. Произошло обнуление.")
        return 0

    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count

firstTask = int(input("Введите первое число: "))
secondTask = int(input("Введите второе число: "))

firstNumeral = numeral_count(firstTask)
secondNumeral = numeral_count(secondTask)

if firstNumeral > secondNumeral:
    print("Цифр больше в первом числе.")
elif firstNumeral < secondNumeral:
    print("Цифр больше во вотором числе.")
else:
    print("Одинаковое число цифр.")

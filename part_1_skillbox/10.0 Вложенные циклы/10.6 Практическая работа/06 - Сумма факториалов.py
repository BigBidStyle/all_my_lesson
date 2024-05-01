summ = 0
factorial = 1
for number in range(1, int(input("Введите число n: ")) + 1):
    factorial *= number
    summ += factorial
print(f"Факториал введеного числа = {factorial}")
print(f"Сумма факториалов этого числа будет: {summ}")

print("Задача № 1 -Цикл-это сложно.")
number = int(input("Введите число: "))
summ = 0
while number > 0:
    summ += number
    print(number, " Какое число")
    number = int(input("Введите число: "))
print(summ)
# Задача 3. Апгрейд калькулятора
# Что нужно сделать

# Степан, как и большая часть населения планеты, для расчёта суммы и разности чисел
# использует калькулятор. Однако в работе ему нужно делать не только обычные действия
# вроде сложения и вычитания, а делать что-то вручную, он уже устал. Поэтому Степан
# решил немного расширить функционал своего калькулятора.

# Напишите программу, запрашивающую у пользователя число и действие, которое нужно
# с ним сделать: вывести сумму его цифр, максимальную или минимальную цифру. Каждое
# действие оформите в виде отдельной функции, а основную программу зациклите.

def menu():
    number = int(input("Введите число: "))
    choice = int(input("Выберите действие:\n"
                       "1 - Сумма цифр\n"
                       "2 - Максимальная цифра\n"
                       "3 - Минимальная цифра\n"
                       "Ваш вариант: "))
    if choice == 1:
        summ(number)
    elif choice == 2:
        maxDigit(number)
    elif choice == 3:
        minDigit(number)
    else:
        print("Ошибка Ввода!\n")
        menu()

# Находим сумму цифр.
def summ(number):
    count = 0
    for summ in range(0, number):
        count += summ
    print(f"Сумма всeх чисел равна {count}\n")
    menu()

# Находим максимальное число.
def maxDigit(number):
    maxNumber = number % 10
    while number > 0:
        number = number // 10
        if maxNumber < number % 10:
            maxNumber = number % 10
    print(f'Максимальная цифра в числе = {maxNumber}\n')
    menu()

# Находим минимальное число.
def minDigit(number):
    minNumber = number % 10
    while number > 0:
        number = number // 10
        if number == 0:
            break
        if minNumber > number % 10:
            minNumber = number % 10
    print(f'Минимальная цифра в числе равна {minNumber}\n')
    menu()

menu()

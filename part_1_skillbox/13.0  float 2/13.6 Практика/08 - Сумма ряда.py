# Что нужно сделать
# Пользователь вводит действительное число х и точность precision. Напишите программу,
# которая по числу х вычисляет сумму ряда в точности до precision.

# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001
# Введите x: 5
# Сумма ряда =  0.2836250150891709

# Что оценивается
# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# формат вывода соответствует примеру;
# вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием);

def row_summ(precision, x):
    row_summ = 0
    n = 0
    f = 1

    while abs(f) > precision:
        f = (- 1) ** n * (x ** (2 * n) / factorialN(2 * n))
        n += 1
        row_summ += f
    print(f'Сумма ряда = {row_summ}')


def factorialN(number):
    factorialN = 1
    for counter in range(2, number + 1):
        factorialN *= counter
    # print(f'Факториал числа {number} равен', factorialN)
    return factorialN


def main():
    while True:
        precision = float(input('Введите точность: '))
        if precision <= 0 or precision >= 1:
            print('Точность должна быть больше 0 и меньше 1. Введите еще раз!')
        else:
            break
    x = int(input('Введите дейcтвительное число x: '))

    row_summ(precision, x)


main()
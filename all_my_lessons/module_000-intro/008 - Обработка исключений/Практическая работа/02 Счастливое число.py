"""Что нужно сделать.
Напишите программу, которая запрашивает у пользователя число до тех пор, пока сумма запрашиваемых чисел не станет
больше либо равна 777. Каждое введённое число при этом дозаписывается в файл out_file.txt. Сделайте так, чтобы перед
дозаписью программа с вероятностью 1 к 13 выдавала пользователю случайное исключение и завершалась.

Пример 1.
Введите число: 10
Введите число: 500
Введите число: 200
Введите число: 67

Вы успешно выполнили условие для выхода из порочного цикла!

Содержимое файла out_file.txt:
10
500
200
67

Пример 2.
Введите число: 10
Введите число: 500
Вас постигла неудача!
Содержимое файла out_file.txt:
10
"""

import random
end_point = 777 # Нужное кол-во очков.
num_stop = random.randint(1, 13)    # Случайное число при котором будет вызываться исключение.
print(f'Случайное число: {num_stop} ')
count_numbers = 0   # Кол-во номеров.
sum_points = 0 # Кол-во набранных очков.

try:
    with open('out_file.txt', 'w', encoding='utf-8') as out_file:  # Открываем файл для записи в него введенных чисел.

        while count_numbers < num_stop and sum_points <= end_point:
            numbers = int(input('Введите число: '))  # Вводим число.
            count_numbers += 1  # Считаем количество чисел.
            try:
                if count_numbers < num_stop:
                    sum_points += numbers  # Считаем сумму введённых чисел.

                else:
                    raise Exception

            except Exception:
                print('Вас постигла неудача!')
                break

            try:
                if sum_points < end_point:
                    out_file.write(str(numbers) + '\n')  # Записываем результат в файл.
                else:
                    raise Exception

            except Exception:
                print('Вы успешно выполнили условие для выхода из порочного цикла!')
                break

finally:
    print('Содержимое файла out_file.txt: ')
    for i_line in open('out_file.txt', 'r', encoding='utf-8'):
        print(i_line, end='')





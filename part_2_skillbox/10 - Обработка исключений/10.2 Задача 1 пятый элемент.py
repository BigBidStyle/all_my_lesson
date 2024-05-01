"""Задача 1. Пятый элемент
В курсе по программированию студенту дали простую задачу: умножить константу (число 42) на пятый элемент строки,
введённой пользователем. Вот код студента:"""

# BRUCE_WILLIS = 42
#
# input_data = input('Введите строку: ')
# leeloo = int(input_data[4])
# result = BRUCE_WILLIS * leeloo
# print(f'- Leeloo Dallas! Multi-pass № {result}!')

print('Решение задачи № 1')
BRUCE_WILLIS = 42

try:
    input_data = input('Введите строку: ')
    result = BRUCE_WILLIS * int(input_data[4])
    print(f'Multi-pass № {result}!')

except IndexError as error:
    print(type(error), ': Мало введено чисел!')

except ValueError as error:
    print(type(error), ': Должны быть целые числа!')

except Exception as error:
    print(type(error), 'Есть еще ошибки...')




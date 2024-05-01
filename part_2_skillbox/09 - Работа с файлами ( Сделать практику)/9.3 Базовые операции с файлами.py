import os

# speakers_file = open('speakers.txt', 'r', encoding='utf-8') # 'r' <-- считать файл.
# data = speakers_file.read() # Открываем данные и записываем в переменную data.
# for i_line in speakers_file:
#     print(i_line, end='')   #(end='') <-- для того чтобы не создавал в конце \n и все строки выводились поочередно.
# speakers_file.close()   # Закрываем файл.

# Практическая работа по данному уроку.
# Задача 1. Результаты
# Одному программисту дали задачу для обработки неких результатов тестирования двух групп людей. Файл первой группы
# (group_1.txt) находится в папке task, файл второй группы (group_2.txt) — в папке Additional_info.

# Содержимое файла group_1.txt
# Бобровский Игорь 10
# Дронов Александр 20
# Жуков Виктор 30

# Содержимое файла group_2.txt
# Павленко Геннадий 20
# Щербаков Владимир 35
# Marley Bob 15

# На экран нужно было вывести сумму очков первой группы, затем разность очков опять же первой группы и напоследок —
# произведение очков уже второй группы.

# Программист оказался не очень опытным, писал код наобум и даже не стал его проверять. И оказалось, этот код просто
# не работает. Вот что он написал:

# file = open('E:\task\group_1.txt', 'read')
# summa = 0
# for i_line in file:
#     info = i_line.split()
#     summa += info[2]
# file = open('E:\task\group_1.txt', 'read')
# diff = 0
# for i_line in file:
#     info = i_line.split()
#     diff -= info[2]
# file_2 = open('E:\task\group_2.txt', 'read')
# compose = 0
# for i_line in file:
#     info = i_line.split()
#     compose *= info[2]
# print(summa)
# print(diff)
# print(compose)

# Исправьте код для решения поставленной задачи. Для проверки результата создайте необходимые папки
# (task, Additional_info, Dont touch me) на своём диске в соответствии с картинкой
# и также добавьте файлы group_1.txt и group_2.txt.
import os
print(f'Решение задачи 1')
file = open(os.path.join('task', 'group_1.txt'), 'r', encoding='utf-8')
file_2 = open(os.path.join('task', 'Additional_info', 'group_2.txt'), 'r', encoding='utf-8')

summa = 0
diff = 0
compose = 1

for i_line in file:
    info = i_line.split()
    if info:
        summa += int(info[2])
        diff -= int(info[2])

for i_line in file_2:
    info = i_line.split()
    if info:
        compose *= int(info[2])

print(summa)
print(diff)
print(compose)


# Задача 2. Поиск файла 2
# Как мы помним, скрипты — это просто куча строк текста, хоть они и понятны только программисту. Таким образом, с ними
# можно работать точно так же, как и с обычными текстовыми файлами.

# Используя функцию поиска файла из предыдущего урока, реализуйте программу, которая находит внутри указанного пути все
# файлы с искомым названием и выводит на экран текст одного из них (выбор можно сгенерировать случайно).

# Подсказка: можно использовать, например, список для сохранения найденного пути.
import random
# def find_file(cur_path, file_name):
#     all_paths = []   # Список всех найденных путей
#     # print(f'Переходим {cur_path}')
#     for i_elem in os.listdir(cur_path): # Перебираем папки искомого пути.
#         path = os.path.join(cur_path, i_elem)
#         # print(f'Просматриваем папку: {path}')
#         if file_name == i_elem:
#             all_paths.append(os.path.abspath(path))   # Добавляем в список найденный путь.
#         elif os.path.isdir(path):
#             result = find_file(path, file_name)
#             if result:
#                 all_paths.extend(result)
#
#     return all_paths
#
# def check_file_inside(path_to_file):
#     file = open(path_to_file, 'r', encoding='utf8')
#     for line in file:
#         print(line, end='')
#     file.close()
#
# # Указываем путь к директории, где будет производиться поиск и название файла который ищем.
# search_path = os.path.abspath(os.path.join('..', '..', '..')) # Путь где будем искать искомый файл.
# search_file = '9.3 Базовые операции с файлами.py'   # Название искомого файла.
# all_paths = find_file(search_path, search_file) # Запускаем функцию.
# check_file_inside(random.choice(all_paths))


import os
speakers_file = open(os.path.join('speakers.txt'), 'r', encoding='utf-8')
sym_count = []
for i_line in speakers_file:
    print(i_line, end='')
    sym_count.append(str(len(i_line)))
sym_count_str = '\n'.join(sym_count)
speakers_file.close()
print(sym_count_str)

counts_file = open('sym_count.txt', 'w')
counts_file.write(sym_count_str)
counts_file.close()

# Практическая работа по данному уроку.
# Задача 1. Сумма чисел
# Во входном файле numbers.txt записано N целых чисел, каждое в отдельной строке.
# Напишите программу, которая выводит их сумму в выходной файл answer.txt.

# Пример:
# Содержимое файла numbers.txt:
# 1
# 2
# 3
# 4
# 10

# Содержимое файла answer.txt
# 20

# Решение задачи 1.
# import os
# sum_number = 0
# numbers = open(os.path.join('numbers.txt'), 'r', encoding='utf-8')
# for i_number in numbers:
#     sum_number += int(i_number)
# numbers.close()
#
# write_number = open('answer.txt', 'w', encoding='utf8')
# write_number.write(str(sum_number))
# write_number.close()

# Задача 2. Всё в одном
# Ваш дружбан, который тоже проходит курс Python Basic, поехал с ноутбуком в другой город, и там у него случилась беда:
# его диск пришлось отформатировать, а доступ в интернет отсутствует. Остался только телефон с мобильным интернетом.
# Так как со связью (и с памятью) проблемы, друг попросил вас скинуть одним файлом все решения и скрипты, которые у вас
# сейчас есть.

# Напишите программу, которая копирует код каждого скрипта в папке проекта python_basic в файл scripts.txt, разделяя
# код строкой из 40 символов *.

# Пример содержимого файла scripts.txt:

# import platform
# import sys
# # info = 'OS info is \n{}\n\nPython version is {} {}'.format(
# #     platform.uname(),
# #     sys.version,
# #     platform.architecture(),
# # )
# #
# # print(info)
# #
# # with open('os_info.txt', 'w', encoding='utf8') as file:
# #     file.write(info)
# # # ****************************************
# # print("Введите первую точку")
# #
# # x1 = float(input('X: '))
# # y1 = float(input('Y: '))
# # print("\nВведите вторую точку")
# #
# # x2 = float(input('X: '))
# # y2 = float(input('Y: '))
# # print("Уравнение прямой, проходящей через эти точки:")
# #
# # x_diff = x1 - x2
# # y_diff = y1 - y2
# # if x_diff == 0:
# #     print("x = ", x1)
# # elif y_diff == 0:
# #     print("y = ", y1)
# # else:
# #     k = y_diff / x_diff
# #     b = y2 - k * x2
# #     print("y = ", k, " * x + ", b)
# # # ****************************************
# import os
# def find_file(cur_path, ending):
#     all_paths = []
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         if i_elem.endswith(ending):
#             all_paths.append(os.path.abspath(path))
#         elif os.path.isdir(path):
#             result = find_file(path, ending)
#             if result: all_paths.extend(result)
#
#     return all_paths
#
#
# def get_text_from_file(path_to_file):
#     file = open(path_to_file, "r", encoding="utf8")
#     result = ""
#     for line in file:
#         result += line
#     return result
#
#
# all_py_files = find_file('..', '.py')  # вместо ".." можно вставить путь до папки python_basic
#
# file_result = open("scripts.txt", "w", encoding="utf8")
#
# for file_path in all_py_files:
#     file_result.write(get_text_from_file(file_path))
#     file_result.write("\n" * 2 + "*" * 80 + "\n" * 2)
#



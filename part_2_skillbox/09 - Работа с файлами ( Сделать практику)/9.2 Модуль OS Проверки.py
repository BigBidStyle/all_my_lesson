
# Код для проверки существования директории в пути. И вывод содержимой папки, если есть такая.
import os
def print_dir(project):
    print('\nСодержимое директории', project)
    if os.path.exists(project):

        for i_elem in os.listdir(project):
            path = os.path.join(project, i_elem)
            print('    ', path)
    else:
        print(f'{project} <-- Такого каталога не существует')

project_list = ['10 - курс', '01 - курс', '02 - курс']   # Список

for i_project in project_list:
    path_to_project = os.path.abspath((os.path.join('..','..', i_project)))
    print_dir(path_to_project)  # Запускаем функцию.

# Задача поиск файла.
# Функция поиска файла в указанной директории.
print('Задача поиска файла на выбранном диске')
def find_file(cur_path, file_name):
    # print(f'Переходим {cur_path}')
    for i_elem in os.listdir(cur_path): # Перебираем папки искомого пути.
        path = os.path.join(cur_path, i_elem)
        # print(f'Просматриваем папку: {path}')
        if file_name == i_elem:
            return path
        if os.path.isdir(path):
            # print(f'Это директория.')
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None

    return result

# Указываем путь к директории, где будет производиться поиск и название файла который ищем.
search_path = os.path.abspath(os.path.join('..', '..', '..', '..')) # Путь где будем искать искомый файл.
search_file = '9.2 Модуль OS Проверки.py'   # Название искомого файла.
file_path = find_file(search_path, search_file) # Запускаем функцию.
if file_path: print(f'Абсолютный путь к искомому файлу: {file_path}')   # Если нашли искомый файл, то вывести путь к нему.
else: print(f'Файл: {search_file} - не найден!')   # Если не нашли файл, то вывести, что файл не найден.

# Практическая работа по данному уроку.
print('\nПрактическая работа по данному уроку.')
# Задача 1. Иконки
# Андрей для себя хочет сделать экспериментальный сайт, где будет красиво отображаться вся структура его диска: папки
# одними иконками, файлы — другими. Поэтому ему нужен код, который поможет определить, какой тип иконки вставить.

# Напишите программу, которая по заданному абсолютному пути определяет, на что указывает этот путь (на директорию, файл,
# или же путь является ссылкой), и выведите соответствующее сообщение. Если путь указывает на файл, то также выведите
# его размер (сколько он весит в байтах). Обеспечьте контроль ввода: проверка пути на существование.

# Подсказка: для вывода размера файла поищите соответствующий метод.

# Пример 1:
# Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py
# Это файл
# Размер файла: 605 байт

# Пример 2:
# Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py
# Указанного пути не существует
print('Задача № 1 - Иконки')
import os
path_to = input('Введите путь: ')
if os.path.isdir(path_to): print('Это папка!')
elif os.path.isfile(path_to): print(f'Это файл! Размером: {os.path.getsize(path_to)} байт.')
else: print('Указанного пути не существует')

# Задача 2. Поиск файла
# В уроке мы написали функцию, которая ищет нужный нам файл во всех подкаталогах указанной директории. Однако, как мы
# понимаем, файлов с таким названием может быть несколько.

# Напишите функцию, которая принимает на вход абсолютный путь до директории и имя файла, проходит по всем вложенным
# файлам и папкам и выводит на экран все абсолютные пути с этим именем.

# Пример:
# Ищем в: C:/Users/Roman/PycharmProjects/Skillbox
# Имя файла: lesson2
# Найдены следующие пути:

# C:/Users/Roman/PycharmProjects/Skillbox\Module15\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module16\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module17\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module18\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module19\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module20\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module21\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module22\lesson2.py


print('Задача № 2 - Поиск файла во всех директориях.')
def find_file(cur_path, file_name):
    # print(f'Переходим {cur_path}')
    for i_elem in os.listdir(cur_path): # Перебираем папки искомого пути.
        path = os.path.join(cur_path, i_elem)
        # print(f'Просматриваем папку: {path}')
        if file_name == i_elem:
            print(f'{file_path}')  # Если нашли искомый файл, то вывести путь к нему.
        elif os.path.isdir(path):
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None

    return result

# Указываем путь к директории, где будет производиться поиск и название файла который ищем.
search_path = os.path.abspath(os.path.join('..', '..', '..')) # Путь где будем искать искомый файл.
search_file = '9.2 Модуль Проверки.py'   # Название искомого файла.
print(f'Искомый файл: {search_file}')
file_path = find_file(search_path, search_file) # Запускаем функцию.


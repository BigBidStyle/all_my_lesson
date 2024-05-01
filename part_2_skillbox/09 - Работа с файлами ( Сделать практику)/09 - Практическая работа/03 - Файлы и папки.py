# Что нужно сделать.
# Напишите программу, которая получает на вход путь до каталога (в том числе это может быть просто корень диска) и
# выводит общее количество файлов и подкаталогов в нём. Также выведите на экран размер каталога в килобайтах (
# 1 килобайт = 1024 байт).

# Важный момент: чтобы посчитать, сколько весит каталог, нужно найти сумму размеров всех вложенных в него файлов.
# Результат работы программы на примере python_basic\Module14:
# E:\PycharmProjects\python_basic\Module14
# Размер каталога (в Кбайтах): 8.373046875
# Количество подкаталогов: 7
# Количество файлов: 15

import os
def info_directory(file_path):
    count_folder = 0
    count_file = 0
    size_folder = 0

    for root, folder, file in os.walk(r'{}'.format(file_path)):

        for _ in folder:
            count_folder += 1

        for name_file in file:
            count_file += 1
            size_folder += os.path.getsize(os.path.join(root, str(name_file)))

    print(f'Размер каталога (в Кбайтах): {size_folder / 1024}')
    print(f'Количество подкаталогов: {count_folder}')
    print(f'Количество файлов: {count_file}')

info_directory(input('Введите директорию:\n'))

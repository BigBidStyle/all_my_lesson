# Задача 2. Дзен Python.
# Что нужно сделать
# В файле zen.txt хранится так называемый Дзен Python — текст философии программирования на языке Python.
# Выглядит он так:

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

# Напишите программу, которая выводит на экран все строки этого файла в обратном порядке.
# Кстати, попробуйте открыть консоль Python и ввести команду.
# Результат работы программы:

# Namespaces are one honking great idea -- let's do more of those!
# If the implementation is easy to explain, it may be a good idea.
# If the implementation is hard to explain, it's a bad idea.
# Although never is often better than *right* now.

# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Основной функционал описан в отдельных функциях.
# Переменные и функции имеют значащие имена, а не только a, b, c, d (подробнее об этом в видео 2.3).
# Входной файл назван так, как указано в задании.

import os
print('Решение задачи № 2')
lines = []
with open(r'zen.txt', 'r', encoding='utf-8') as zen:
    [lines.append(line) for line in zen]
    [print(str_text, end='') for str_text in lines[::-1]]








# 7.8 Практическая работа
# region Цели практической работы
# Применить кортежи на практике, а также закрепить работу со словарями и отработать использование новых методов
# словарей.

# Научиться:
# инициализировать кортежи и работать с ними при решении задач;
# использовать функцию enumerate для оптимизации работы кода;
# одновременно работать и с ключами, и со значениями словаря, получать их отображение с помощью метода;
# использовать функцию zip для решения задач.

# Что входит в работу
# Задача 1. Ревью кода.
# Задача 2. Универсальная программа.
# Задача 3. Игроки.
# Задача 4. По парам.
# Задача 5. Функция сортировки.
# Задача 6. Контакты — 3.
# Задача 7. Своя функция zip.

# Если работаете одновременно со значениями и индексами строки/списка/кортежа, используйте enumerate. Если работаете
# одновременно с ключами и значениями словаря, используйте items.
# endregion Цели практической работы

# region Задача 1. Ревью кода
# region Требование задачи.

# Что нужно сделать
# Ваня работает middle-разработчиком на Python в IT-компании. Один кандидат на позицию junior-разработчика прислал ему
# код тестового задания.

# В задании был словарь из трёх студентов. Необходимо:

# Вывести на экран список пар «ID студента — возраст».
# Написать функцию, которая принимает в качестве аргумента словарь и возвращает два значения: полный список интересов
# всех студентов и общую длину всех фамилий студентов.
# Далее в основном коде вызывается функция, значения присваиваются отдельным переменным и выводятся на экран.

# Ваня — очень придирчивый программист, и после просмотра кода он понял, что этого кандидата на работу не возьмёт, хотя
# код выдаёт верный результат. Вот код кандидата:

# students = {
# 1: {
# 'name': 'Bob',
# 'surname': 'Vazovski',
# 'age': 23,
# 'interests': ['biology, swimming']
# },
# 2: {
# 'name': 'Rob',
# 'surname': 'Stepanov',
# 'age': 24,
# 'interests': ['math', 'computer games', 'running']
# },
# 3: {
# 'name': 'Alexander',
# 'surname': 'Krug',
# 'age': 22,
# 'interests': ['languages', 'health food']
# }
# }
#
# def f(dict):
# lst = []
# string = ''
# for i in dict:
# lst += (dict[i]['interests'])
# string += dict[i]['surname']
# cnt = 0
# for s in string:
# cnt += 1
# return lst, cnt
#
# pairs = []
# for i in students:
# pairs += (i, students[i]['age'])
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)

# Перепишите этот код так, чтобы он был максимально pythonic и Ваня мало к чему мог придраться (только если очень
# захочется). Убедитесь, что программа верно работает. Проверки на существование записей в словаре не обязательны,
# но приветствуются.

# Результат работы программы:
# Список пар «ID студента — возраст»: [(1, 23), (2, 24), (3, 22)]
# Полный список интересов всех студентов: {'running', 'computer games', 'math', 'languages', 'biology, swimming',
# 'health food'}
# Общая длина всех фамилий студентов: 20

# Советы и рекомендации
# Обратите внимание на имена переменных и функций должны быть полезными и понятными (не стоит использовать
# одиночные буквы, непонятные сокращения). Названия не должны пересекаться с уже существующими в Python объектами
# (например, лучше не называть свою переменную print или list).
# Попробуйте найти лишние действия в коде. Если вы сможете получить нужный результат меньшим количеством действий, то
# не нужно заставлять Python выполнять лишние действия. Также нет необходимости заставлять Python выполнять одни и те же
# действия над одним и тем же объектом (например, вызывать функцию с одними и теми же входными данными несколько раз).
# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значимые имена, не только a, b, c, d
# Новый код более оптимизирован и чист по стилю программирования (pythonic), чем старый.
# endregion Требование задачи.
# Вывести на экран список пар «ID студента — возраст».
# Написать функцию, которая принимает в качестве аргумента словарь и возвращает два значения: полный список интересов
# всех студентов и общую длину всех фамилий студентов.
# Далее в основном коде вызывается функция, значения присваиваются отдельным переменным и выводятся на экран.

# Результат работы программы:
# Список пар «ID студента — возраст»: [(1, 23), (2, 24), (3, 22)]
# Полный список интересов всех студентов: {'running', 'computer games', 'math', 'languages', 'biology, swimming',
# 'health food'}
# Общая длина всех фамилий студентов: 20

# # -----------------------------------
# Решение задачи.
# students = {1: {'name': 'Bob','surname': 'Vazovski','age': 23, 'interests': ['biology, swimming']},
#             2: {'name': 'Rob','surname': 'Stepanov','age': 24,'interests': ['math', 'computer games', 'running']},
#             3: {'name': 'Alexander','surname': 'Krug','age': 22,'interests': ['languages', 'health food']}}
#
# pairs_list = []
# interes_dict = []
#
# def function (dict):
#     lenght = 0
#     for id, values_1 in students.items():
#         for title, values_2 in values_1.items():
#             if title == "age":
#                 pairs_list.append((id, values_2))
#             if title == "interests":
#                 enum_interes_dict = {interes_dict.append(title) for index, title in enumerate(values_2)}
#             if title == "surname":
#                 lenght += len(values_2)
#     return pairs_list, interes_dict, lenght
#
# id_pairs, interest, lenght_surname = function(students)
#
# print(f"Список пар «ID студента — возраст»: {id_pairs}")
# print(f"Полный список интересов всех студентов: {interest} ")
# print(f"Общая длина всех фамилий студентов: {lenght_surname}")
# # -----------------------------------
# endregion Задача 1. Ревью кода
# region Задача 2. Универсальная программа
# Что нужно сделать.
# Напишите функцию, возвращающую список элементов итерируемого объекта (кортежа, строки, списка, словаря), у которых
# индекс — это простое число.

# Для проверки на простое число напишите отдельную функцию is_prime.

# Необязательное усложнение: сделайте так, чтобы основная функция состояла только из оператора return и так же
# возвращала список.

# Пример вызова функции:
# print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# Ответ в консоли: [2, 3, 5, 7]

# Пример вызова функции:
# print(crypto('О Дивный Новый мир!'))
# Ответ в консоли: ['Д', 'и', 'н', 'й', 'в', 'й', 'р']

# # -----------------------------------
# def is_prime(num):
#     for i in range(2, (num//2)+1):
#         if num % i == 0:
#             return False
#     return True
# def crypto(in_data):
#     return  [values for num, values in enumerate(in_data,) if is_prime(num)]
#
# print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(crypto('О Дивный Новый мир!'))
# # -----------------------------------
# Советы и рекомендации
# Для нумерации элементов используйте функцию enumerate. Это позволит работать одинаково со всеми структурами данных.

# Что оценивается
# Результат вычислений корректен.
# Весь функционал программы описан в функциях.
# Переменные и функции имеют значимые имена, не только a, b, c, d.
#
# endregion Задача 2. Универсальная программа
# region Задача 3. Игроки
# Что нужно сделать
# У вас есть словарь игроков, которые участвовали в трёх видах спорта. В словаре хранятся пары «ФИ — очки»:

# players = {
# ("Ivan", "Volkin"): (10, 5, 13),
# ("Bob", "Robbin"): (7, 5, 14),
# ("Rob", "Bobbin"): (12, 8, 2)
# }
# Один программист попросил нас прислать другой вариант хранения этой информации для его базы.

# Напишите программу, которая объединяет ключ словаря со значением в один кортеж, и выведите результат на экран.
# Постарайтесь использовать как можно более эффективное решение.

# Результат работы программы:
# [('Ivan', 'Volkin', 10, 5, 13), ('Bob', 'Robbin', 7, 5, 14), ('Rob', 'Bobbin', 12, 8, 2)]

# # -----------------------------------
# Решение задачи.
# players = {("Ivan", "Volkin"): (10, 5, 13),
#            ("Bob", "Robbin"): (7, 5, 14),
#            ("Rob", "Bobbin"): (12, 8, 2)}
#
# def unification(text, number):
#     split_unification = text + number
#     return split_unification
#
# list = [unification(name_surname, number) for name_surname, number in players.items()]
# print(list)
# # -----------------------------------
# Советы и рекомендации
# Не забывайте, что кортежи можно складывать (а + б). Это приведёт к объединению всех элементов двух кортежей.
# Для упрощения кода хорошо подходят генераторы списка.
# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует указанному в задаче.
# Переменные и функции имеют значимые имена, не только a, b, c, d.
#
# endregion Задача 3. Игроки
# region Задача 4. По парам
# Что нужно сделать.
# Напишите программу, которая инициализирует список из 10 случайных целых чисел, а затем делит эти числа на пары
# кортежей внутри списка. Выведите результат на экран.

# Дополнительно: решите задачу несколькими способами.

# Пример:
# Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]

# # -----------------------------------
# Решение задачи.
import random
original_list = list(random.randint(0, 10) for _ in range(10))
# print(original_list)

new_list_1 = [i_1 for i_1 in original_list[::2]]
new_list_2 = [i_2 for i_2 in original_list[1::2]]
print(zip(new_list_1, new_list_2))


# print(f"Оригинальный список: {original_list}")
# print(f"Новый список: {new_list}")

# # -----------------------------------

# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значимые имена, не только a, b, c, d.
# Для решения используются list comprehensions.
# endregion Задача 4. По парам
# region Задача 5. Функция сортировки (Не решена)
# Что нужно сделать.
# Напишите функцию, которая сортирует по возрастанию кортеж, состоящий из целых чисел, и возвращает его отсортированным.
# Если хотя бы один элемент не является целым числом, то функция возвращает исходный кортеж.

# Основной код оставьте пустым или закомментированным (используйте его только для тестирования).

# Пример вызова функции:
# tpl = (6, 3, -1, 8, 4, 10, -5)
# print(tpl_sort(tpl))
# Ответ в консоли: (-5, -1, 3, 4, 6, 8, 10)

# Что оценивается
# Результат вычислений корректен.
# Весь функционал программы описан в виде функции.
# Переменные и функции имеют значимые имена, не только a, b, c, d.

# endregion Задача 5. Функция сортировки
# region Задача 6. Контакты — 3 (Не решена)
# Что нужно сделать.
# Мы уже помогали Степану с реализацией телефонной книги на устройстве, однако внезапно оказалось, что ей не хватает
# ещё одной полезной функции — поиска.

# Напишите программу, которая бесконечно запрашивает у пользователя действие, которое он хочет совершить: добавить
# контакт или найти человека в списке контактов по фамилии.

# Действие «добавить контакт»: программа запрашивает имя и фамилию контакта, затем номер телефона, добавляет их в
# словарь и выводит на экран текущий словарь контактов. Если этот человек уже есть в словаре, то выводится
# соответствующее сообщение.
# Действие «поиск человека по фамилии»: программа запрашивает фамилию и выводит все контакты с такой фамилией и их
# номера телефонов. Поиск не должен зависеть от регистра символов.
#
# Пример работы программы:
#
# Введите номер действия:
#
# Добавить контакт.
# Найти человека.
# При выборе действия 1:
#
# Введите имя и фамилию нового контакта (через пробел): Иван Сидоров
#
# Введите номер телефона: 888
#
# Текущий словарь контактов: {('Иван', 'Сидоров'): 888}
#
# Введите номер действия:
#
# Добавить контакт
# Найти человека
# При выборе действия 1:
#
# Введите имя и фамилию нового контакта (через пробел): Иван Сидоров
#
# Такой человек уже есть в контактах.
#
# Текущий словарь контактов: {('Иван', 'Сидоров'): 888}
#
# Введите номер действия:
#
# Добавить контакт
# Найти человека
# При выборе действия 1:
#
# Введите имя и фамилию нового контакта (через пробел): Алиса Петрова
#
# Введите номер телефона: 999
#
# Текущий словарь контактов: {('Иван', 'Сидоров'): 888, ('Алиса', 'Петрова'): 999}
#
# Введите номер действия:
#
# Добавить контакт
# Найти человека
# При выборе действия 2:
#
# Введите фамилию для поиска: Сидоров
#
# Иван Сидоров 888
#
# Введите номер действия:
#
# Добавить контакт
# Найти человека
# …….
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Основной функционал (действия) описан в отдельных функциях.
# Переменные и функции имеют значимые имена, не только a, b, c, d.
#
# endregion Задача 6. Контакты — 3
# region Задача 7. Своя функция zip (Не решена)
# Что нужно сделать
# В самом конце собеседования вам неожиданно сказали: «Расскажите, что делает функция zip». Чтобы произвести
# впечатление, вы решили не только рассказать о ней, но и написать её аналог.

# Даны строка и кортеж из чисел. Напишите программу, которая создаёт генератор из пар кортежей «символ — число». Затем
# выведите на экран сам генератор и кортежи.

# Пример:
# Строка: abcd
# Кортеж чисел: (10, 20, 30, 40)
# Результат:
# <generator object <genexpr> at 0x00000204A4234048>

# ('a', 10)
# ('b', 20)
# ('c', 30)
# ('d', 40)

# region Решение SkillBox
def shortes_seq_range(string, tpl):
    return min(len(string), len(tpl))

syms_str = 'abc'
nums_tpl = (10, 20, 30, 40)

pairs = ((syms_str[i_elem], nums_tpl[i_elem]) for i_elem in range(shortes_seq_range(syms_str, nums_tpl)))
print(pairs)
for i_elem in pairs:
    print(i_elem)
print(zip(syms_str, nums_tpl))
# endregion Решение Skillbox

# Дополнительно: создайте полный аналог функции zip — сделайте так, чтобы программа работала с любыми итерируемыми
# типами данных.
# endregion Задача 7. Своя функция zip

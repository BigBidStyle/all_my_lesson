# -------------------------------------------------------------------------------------------------------------------- #
# region Практическая работа Курс № 2 (Тема № 2 Базовые коллекции 1 - list (списки))
# region Задание 1. Генерация списка.
# Дано целое число N. Напишите программу, которая формирует список из нечётных чисел от одного до N.

# N = int(input("Введите целое число: "))
# numbers = []
#
# for i in range(N):
#     if i % 2 != 0:
#         numbers.append(i)
# print(f"Список из нечетных чисел от одного до N: {numbers}")
# endregion
# -------------------------------------------------------------------------------------------------------------------- #
# region Задание 2. Турнир.
# Для соревнований по волейболу необходимо сформировать турнирную сетку из восьми человек на два дня.
# На первый день из списка участников решили выбрать каждого второго.
#
# Дан список из восьми имён: Артемий, Борис, Влад, Гоша, Дима, Евгений, Женя, Захар.
# Напишите программу, которая выводит элементы списка только с чётными индексами.
#
# Пример:
# Первый день: ['Артемий', 'Влад', 'Дима', 'Женя']
# day_1 = []
# name_list = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
# for i in range(len(name_list)):
#     if i % 2 == 0:
#         day_1.append(name_list[i])
# print(f"Первый день:{day_1}")
# endregion
# -------------------------------------------------------------------------------------------------------------------- #
# region Задание 3. Клетки.
# В научной лаборатории выводят и тестируют новые виды клеток.
# Есть список из N этих клеток, элементом которого является показатель эффективности,а индексом — ранг клетки.
# Учёные отбирают клетки по следующему принципу:
# если эффективность клетки меньше её ранга, то она не подходит.

# Напишите программу, которая выводит на экран элементы списка, значения которых меньше их индекса.

# Пример:
# Количество клеток: 5
# Эффективность 1 клетки: 3
# Эффективность 2 клетки: 0
# Эффективность 3 клетки: 6
# Эффективность 4 клетки: 2
# Эффективность 5 клетки: 10

# Неподходящие значения: 0 2

# # решение № 1
# error_cell = []
# count_cell = int(input("Введите кол-во клеток: "))
# for number_cell in range(1, count_cell + 1):
#     effect = int(input(f"Эффективность {number_cell} клетки: "))
#     if effect < number_cell:
#         error_cell.append(number_cell)
# print(f"Неподходящие значения : {error_cell}")

# решение № 2
# list_N = []
# for i in range(int(input("Количество клеток: "))):
#     print(f"Эффективность {i + 1} клетки: ", end="")
#     effect = int(input())
#     if i + 1 > effect:
#         list_N.append(effect)
# print(f"\nНеподходящие значение: {list_N}")

# решение № 3 -Еще больше упрощенный вариант.
# list_N = []
# for i in range(int(input("Количество клеток: "))):
#     effect = int(input(f"Эффективность {i + 1} клетки: "))
#     if i + 1 > effect:
#         list_N.append(effect)
# print(f"\nНеподходящие значение: {list_N}")
# endregion Задание 3. Клетки.
# -------------------------------------------------------------------------------------------------------------------- #
# region Задание 4. Видеокарты.
# В базе магазина электроники есть список видеокарт компании NVIDIA разных поколений.
# Вместо полных названий хранятся только числа, которые обозначают модель и поколение
# видеокарты. Недавно компания выпустила новую линейку видеокарт. Самые старшие
# поколения разобрали за пару дней.

# Напишите программу, которая удаляет из списка видеокарт наибольшие элементы.

# Пример:
# Количество видеокарт: 5
# 1 Видеокарта: 3070
# 2 Видеокарта: 2060
# 3 Видеокарта: 3090
# 4 Видеокарта: 3070
# 5 Видеокарта: 3090

# Старый список видеокарт: [3070 2060 3090 3070 3090]
# Новый список видеокарт: [3070 2060 3070]

# Решение 1 (Старое)
# list_number = []
# max_number = 0
#
# for i in range(int(input("Количество видеокарт: "))):
#     print(f"{i + 1} Видеокарта: ", end="")
#     number = int(input())
#     list_number.append(number)
#     if max_number < number:
#         max_number = number
# print(f"\nCтарый список видеокарт: {list_number}")
#
# new_list = []
# for i in list_number:
#     if i != max_number:
#         new_list.append(i)
# print(f"Новый список видеокарт: {new_list}")

# # Решение 2 (Новое - повторение (Использование еще не пройденных материалов)
# list_card = []
# max_number = 0
# for i in range(1, int(input("Количество видеокарт: ")) + 1):
#     list_card.append(int(input(f"{i} Видеокарта: ")))
#     if max_number < list_card[i - 1]:
#         max_number = list_card[i - 1]
# print(f"Старый список видеокарт: {list_card}")
# new_list = []
# list_1 = [new_list.append(i) for i in list_card if i != max_number]
# print(f"Новый список видеокарт: {new_list}")
# endregion Задание 4. Видеокарты.
# -------------------------------------------------------------------------------------------------------------------- #
# region Задание 5. Кино.
# Что нужно сделать
# Илья зашёл на любительский кино сайт, на котором пользователи оставляют рецензии на фильмы.
# Их список:

# films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия",
# "Город грехов", "Мементо", "Отступники", "Деревня"]
#
# Илья на сайте в первый раз. Он хочет зарегистрироваться и сразу добавить часть фильмов
# в список любимых, чтобы позже прочитать рецензии на них.
#
# Напишите программу, в которой пользователь вводит фильм. Если он есть в перечне,
# то добавляется в список любимых. Если его нет, то выводится ошибка. В конце выведите
# весь список любимых фильмов.

# Пример:
# Сколько фильмов хотите добавить? 3
# Введите название фильма: Леон
# Введите название фильма: Безумный Макс
# Ошибка: фильма Безумный Макс у нас нет :(
# Введите название фильма: Мементо
# Ваш список любимых фильмов: Леон, Мементо

# Решение № 1 Старое решение :))) - хуйня какая то причем полная....
# films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия",
#          "Город грехов", "Мементо", "Отступники", "Деревня"]
#
# like_films = []
# count_films = len(films)
#
# for _ in range(int(input("Сколько фильмов хотите добавить: "))):
#     print(f"Введите название фильма: ", end="")
#     introduced_films = (input())
#     count = 0
#     for search in films:
#         count += 1
#         if search == introduced_films:
#             like_films.append(search)
#             count = 0
#             break
#         elif count == count_films and search != introduced_films:
#             print(f"Ошибка: Фильма {introduced_films} у нас нет.")
# print(f"Ваш список любимых фильмов: {like_films}")

# Решение № 2. Правильное решение.
# films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия",
#          "Город грехов", "Мементо", "Отступники", "Деревня"]
#
# my_list = []
# for _ in range(int(input(f"Сколько фильмов хотите добавить? "))):
#     title_film = input("Введите название фильма: ")
#     if title_film in films:
#         my_list.append(title_film)
#     else:
#         print(f"Ошибка: фильма {title_film} у нас нет :(")
#
# print_title = ", ".join(my_list)
# print(f"Ваш список любимых фильмов: {print_title}")

# endregion Задание 5. Кино.
# -------------------------------------------------------------------------------------------------------------------- #
# region Задание 6. Анализ Слова.
# Что нужно сделать
# Напишите программу — анализатор слов, чтобы использовать её для тренировки нейросети и генерировать нужный текст.

# Пользователь вводит слово. Напишите программу, которая считает количество
# уникальных букв в слове. Уникальные буквы — это те, которые встречаются всего один раз.

# Пример 1:
# Введите слово: привет
# Количество уникальных букв: 6

# Пример 2:
# Введите слово: лава
# Количество уникальных букв: 2

# Решение 1 (старое)
# word = input("Введите слово: ")
# new_word = list(word)
# count_word = len(new_word)
# count_number = 0
# for i in new_word:
#     count = 0
#     for n in new_word:
#         if i == n:
#             count += 1
#     if count == 1:
#         count_number +=1
# print(f"Количество уникальных букв: {count_number}")

# Решение № 2 (Повторение)
# word = list(input("Введите слово: "))
# new_list = []
# for i in range(len(word)):
#     if word[i] not in new_list:
#         new_list.append(word[i])
#     else:
#         new_list.remove(word[i])
# print(f"Количество уникальных букв: {len(new_list)}")
# endregion Задание 6. Анализ Слова.
# -------------------------------------------------------------------------------------------------------------------- #
# region Задание 7. Контейнеры.
# Контейнеры на складе лежат в ряд в порядке убывания или равно массы в килограммах.
# На склад привезли ещё один контейнер, который тоже нужно положить на определённое место.

# Напишите программу, которая получает на вход невозрастающую последовательность
# натуральных чисел. Они означают массу каждого контейнера в ряду. После этого
# вводится число X — масса нового контейнера. Программа выводит номер, под которым
# будет лежать новый контейнер. Если в ряде есть контейнеры с массой, как у нового,
# то его нужно положить после них.

# Обеспечьте контроль ввода: все числа не превышают 200.

# Пример:
# Количество контейнеров: 8
# Введите вес контейнера: 165
# Введите вес контейнера: 163
# Введите вес контейнера: 160
# Введите вес контейнера: 160
# Введите вес контейнера: 157
# Введите вес контейнера: 157
# Введите вес контейнера: 155
# Введите вес контейнера: 154

# Введите вес нового контейнера: 162

# Номер, который получит новый контейнер: 3

# Решение № 1 (Старое)
# max_weight = 200
# list_container = []
# def input_container(i, n):
#     while i != n:
#         print(f"Введите вес контейнера: ", end="")
#         weight_container = int(input())
#         if weight_container > max_weight:
#             print("Вес контейнера должен быть меньше 200 кг.")
#             input_container(i, n)
#             break
#         elif weight_container < max_weight and len(list_container) == 0:
#             list_container.append(weight_container)
#             i += 1
#         elif weight_container < max_weight and list_container[-1] >= weight_container:
#              list_container.append(weight_container)
#              i += 1
#         else:
#             print("Вес контейнера должен быть меньше либо равно предыдущему контейнеру.")
#     return
#
# index_number = 0
# number_container = int(input("Количество контейнеров: "))
# input_container(index_number,number_container)
#
# weight_new_container = int(input("\nВведите вес нового контейнера: "))
# for i in range(number_container):
#     if weight_new_container >= list_container[i]:
#         list_container.insert(i, weight_new_container)
#         print(list_container)
#         print(f"Номер, который получит новый контейнер: {i + 1}")
#         break
#     elif weight_new_container <= list_container[number_container-1]:
#         list_container.insert(number_container + 1, weight_new_container)
#         print((list_container))
#         print(f"Номер, который получит новый контейнер: {number_container + 1}")
#         break

# Решение № 2 ( Новое)
# max_weight = 200
# list_container = []
# for i in range(int(input("Введите количество контейнеров: "))):
#     weight = int(input(f"Введите вес контейнера: "))
#     while max_weight < weight:
#         print(f"Вес контейнера должен быть не больше {max_weight}!")
#         weight = int(input(f"Введите вес контейнера: "))
#     else:
#         list_container.append(weight)
#
# new_weight = int(input(f"Введите вес нового контейнера: "))
# while max_weight < new_weight:
#     print(f"Вес контейнера должен быть не больше {max_weight}!")
#     new_weight = int(input(f"Введите вес нового контейнера: "))
# else:
#     list_container.sort(reverse=True)
#     for i in range(len(list_container)):
#         if list_container[i] < new_weight:
#             print(f"Номер, который получит новый контейнер: {i + 1}")
#             break

# Тут конечно можно было убрать переменную max_weight, и прописать числом, так как по условию уже известна эта цифра.
# endregion Задание 7. Контейнеры.
# -------------------------------------------------------------------------------------------------------------------- #
# region Задание 8. Бегущие цифры. (НЕРЕШЕНЕА!!!!!!)
# Вы пишете программу для маленького табло, в котором циклически повторяется один и тот же текст или числа.
# Например, как в метро, автобусах или трамваях.

# Даны список из N элементов и целое число K. Напишите программу, которая циклически сдвигает элементы списка вправо
# на K позиций. Используйте минимально возможное количество операций присваивания.

# Пример 1:
# Сдвиг: 1
# Изначальный список: [1, 2, 3, 4, 5]
# Сдвинутый список: [5, 1, 2, 3, 4]

# Пример 2:
# Сдвиг: 3
# Изначальный список: [1, 4, -3, 0, 10]
# Сдвинутый список: [-3, 0, 10, 1, 4]

#
# list_number = []
# new_list = []
# shift = int(input("Сдвиг: "))
# for i in range(int(input("Введите количество чисел в списке: "))):
#     list_number.append(int(input(f"Введите число: ")))
# print(f"Изначальный список: {list_number}")
# for i in range(shift):
# endregion Задание 8. Бегущие цифры.
# -------------------------------------------------------------------------------------------------------------------- #
# region Задание 9. Полиндром.
# # Продолжите писать анализаторы для текста. Теперь необходимо реализовать код, с помощью которого можно определять
# палиндромы. То есть нужно находить слова, которые одинаково читается слева направо и справа налево.
#
# # Напишите такую программу.
#
# # Пример 1:
# # Введите слово: мадам
# # Слово является палиндромом
#
# # Пример 2:
# # Введите слово: abccba
# # Слово является палиндромом
#
# # Пример 3:
# # Введите слово: abbd
# # Слово не является палиндромом

# word = list(input("Введите слово: "))
# new_list = []
# for i in range(len(word)):

# Решение № 1 (старое)
# word = input("Введите слово: ")
# list_word = list(word)
# count_word = len(list_word)
# index_1 = 0
# index_2 = -1
# word = True
# while index_1 <= count_word:
#     if list_word[index_1] == list_word[index_2]:
#         index_1 += 1
#         index_2 -= 1
#         break
#     elif list_word[index_1] != list_word[index_2]:
#         print("Слово не является палиндроном.")
#         word = False
#         break
# if word:
#     print("Слово является палиндромом!")

# Решение № 2 (Повторное)
# count = 0
# text_list = list(input("Введите слово: "))
# for i in range(len(text_list)):
#     if text_list[i - 1] != text_list[-i]:
#         print("Слово не является палиндромом")
#         count += 1
#         break
# if count == 0:
#     print("Слово является палиндромом")
# endregion Задание 9. Полиндром.
# endregion Практическая работа Курс № 2 (Тема № 2 Базовые коллекции 1 - list (списки))
# -------------------------------------------------------------------------------------------------------------------- #
# region Практическая работа Курс № 2 ( Тема № 3 Методы для работы со списками)
# -------------------------------------------------------------------------------------------------------------------- #
# region Задание № 1 Страшныый код.
# Вашему другу, который тоже начал изучать Python, преподаватель дал такую задачу:
# есть три списка — основной и два побочных. В основном лежат элементы [1, 5, 3],
# а в побочных — [1, 5, 1, 5] и [1, 3, 1, 5, 3, 3] соответственно.

# Первый побочный закидывается в основной, там считается количество цифр 5,
# количество выводится на экран, и затем они удаляются из основного списка.
# После этого в основной закидывается второй побочный список, там считается
# количество цифр 3 и выводится на экран. В конце также выводится и сам список.

# Из интереса вы попросили вашего друга показать код его программы и поняли, что
# сделали это не зря — то, что вы увидели, повергло вас в шок и ужас. Вот сам код:
# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for i in b:
# a.append(i)
# t = 0
# for i in a:
# if i == 5:
# t += 1
# print(t)
# d = []
# for i in a:
# if i != 5:
# d.append(i)
# for i in c:
# d.append(i)
# t = 0
# for i in d:
# if i == 3:
# t += 1
# print(t)
# print(d)

# Используя знания о методах списков, а также о стиле программирования,
# помогите другу переписать программу. Не используйте дополнительные списки.

# Результат работы программы:
# Кол-во цифр 5 при первом объединении: 3
# Кол-во цифр 3 при втором объединении: 4

# Итоговый список: [1, 3, 1, 1, 1, 3, 1, 5, 3, 3]

# ---------------------
# Решение № 1 (Старое) - Лучшие сделал это, чем повторное.
# list_a = [1, 5, 3]
# list_b = [1, 5, 1, 5]
# list_c = [1, 3, 1, 5, 3, 3]
#
# list_a.extend(list_b)
#
# total = 0
# for i in list_a:
#     if i == 5:
#         total += 1
#
# print(f"Кол-во цифр 5 при первом объединении: {total}")
#
# index = 0
# for i in list_a:
#     if i == 5:
#         list_a.pop(index)
#     index += 1
#
# list_a.extend(list_c)
#
# total = 0
# for i in list_a:
#     if i == 3:
#         total += 1
#
# print(f"Кол-во цифр 3 при втором объединении: {total}")
# print(f"\nИтоговый список: {list_a}").

# ---------------------
# Решение № 2 (Повтор) Тут стремно написал... Можно было использовать больше методов.
# list_a = [1, 5, 3]
# list_b = [1, 5, 1, 5]
# list_c = [1, 3, 1, 5, 3, 3]
#
# for i in list_b:
#     list_a.append(i)
#
# total_5 = 0
# for i in list_a:
#     if i == 5:
#         total_5 += 1
# print(f"Кол-во цифр 5 при первом объединении: {total_5}")
#
# for num_5 in list_a:
#     if num_5 == 5:
#         list_a.remove(5)
#
# for i in list_c:
#     list_a.append(i)
#
# total_3 = 0
# for i in list_a:
#     if i == 3:
#         total_3 += 1
# print(f"Кол-во цифр 3 при первом объединении: {total_3}\n")
# print(f"Итоговый список: {list_a}")

# ---------------------
# Решение № 3 апгрейд (Идеальный вариант).
# list_a = [1, 5, 3]
# list_b = [1, 5, 1, 5]
# list_c = [1, 3, 1, 5, 3, 3]
#
# list_a.extend(list_b)
#
# total_5 = 0
# for i in list_a:
#     if i == 5:
#         total_5 += 1
# print(f"Кол-во цифр 5 при первом объединении: {total_5}")
#
# for num in list_a:
#     if num == 5:
#         list_a.remove(5)
#
# list_a.extend(list_c)
#
# total_3 = 0
# for i in list_a:
#     if i == 3:
#         total_3 += 1
#
# print(f"Кол-во цифр 3 при втором объединении: {total_3}")
# print(f"\nИтоговый список: {list_a}")
# endregion Задание № 1 Страшныый код.
# -------------------------------------------------------------------------------------------------------------------- #
# region Задание № 2 Шеренга.
# Что нужно сделать
# Два класса стоят в две отдельные шеренги. В каждом классе ученики выстроены по росту
# (по возрастанию): в одном классе от 160 см до 176 см с шагом 2, во втором классе —
# от 162 см до 180 см с шагом 3. Спустя какое-то время два класса объединяют в одну
# шеренгу и тоже выстраивают их по возрастанию.

# Напишите программу, которая генерирует списки роста для каждого в классе, затем
# объединяет их в один список и сортирует его в порядке возрастания. Выведите
# отсортированный список на экран.

# Формат вывода ответа:
# Отсортированный список учеников: [160, 162, …]

# --------------------
# Решение № 1 (Старое)
# # Создаем список первого класса.
# class_1 = []
# for height in range(160, 176, 2):
#     class_1.append(height)
#
# # Создаем список второго класса.
# class_2 = []
# for height in range(162, 180, 3):
#     class_2.append(height)
#
# # Добавляем к первому списку второй список.
# class_1.extend(class_2)
#
# # Сортируем список по возрастанию.
# class_1.sort()
#
# # Удаляем из списка одинаковые значения.
# from itertools import groupby
# new_class = [el for el, _ in groupby(class_1)] # Но такой способ еще не пройден в материале.
# print(f"Отсортированный список учеников: {new_class}")

# --------------------
# Решение № 2 (повторное)
# build_1 = []
# c_1 = [build_1.append(i) for i in range(160, 176, 2)]
# print(f"Первая шеренга: {build_1}")
#
# build_2 = []
# c_2 = [build_2.append(i) for i in range(162, 180, 3)]
# print(f"Вторая шеренга: {build_2}")
#
# # Тут конечно не мешало бы проверить два списка и решить в каком больше значений!
# # Это для того чтобы уменьшить кол-во операций (не знаю надо или нет)
#
# for i in build_1:  # Берем один элемент из первого списка...
#     if i in build_2:    # Проверяем, есть ли он во втором списке...
#         build_2.remove(i)   # Если есть такое значение, то удаляем его!
#
# build_1.extend(build_2)
# print(f"Отсортированный список учеников: {build_1}")
# endregion Задание № 2 Шеренга.
# -------------------------------------------------------------------------------------------------------------------- #
# region Задание № 3 Детали.
# # В базе данных магазина всякой всячины хранится список названий деталей и их стоимостей:

# # shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000],
# ['обод', 2000], ['шатун', 200], ['седло', 2700]]
# # Продавец решил, что считать количество и стоимость деталей вручную не очень удобно,
# # поэтому решил попросить помощи у программиста, чтобы оптимизировать этот процесс.

# # Напишите программу, которая запрашивает у пользователя деталь, считает их количество, а также общую стоимость.

# # Пример:
# # Название детали: седло
# # Кол-во деталей — 3
# # Общая стоимость — 4500

# Решение 2 (Повторное)
# shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000],
#         ['обод', 2000], ['шатун', 200], ['седло', 2700]]
#
# detail = input("Название детали: ")
# price = 0
# quantity_detail = 0
#
# # Ищем в списке название детали.
# for i_detail in shop:
#     if i_detail[0] == detail:
#         quantity_detail += 1
#         price += i_detail[1]
#
# # Выводим результат на экран.
# if quantity_detail > 0:
#     print(f"Кол-во деталей - {quantity_detail}")
#     print(f"Общая стоимость - {price}")
# else:
#     print("Такой детали нет!")
# endregion Задание № 3 Детали.
# -------------------------------------------------------------------------------------------------------------------- #
# region Задание № 4 Вечеринка.
# В честь своего дня рождения Артём решил закатить вечеринку у себя на даче.
# Он не стал рассылать приглашения, а просто сообщил всем: «Если№ хотите — приходите и своих друзей тоже зовите».
# В ходе вечеринки люди приходили и уходили, ночевать остались не все. К тому же и сама дача не резиновая — на ней
# помещается всего шесть человек.

# Дан изначальный список гостей — имена тех, кто пришёл к началу:

# guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]
# Напишите программу, которая спрашивает у пользователя, ушёл человек или пришёл новый гость, и,
# исходя из ответа, добавляет в список или удаляет из него нужное имя.
# При этом гостей может быть не больше шести. Имена запрашиваются до тех пор, пока пользователь не введёт сообщение
# «Пора спать».

# Пример:

# Сейчас на вечеринке 5 человек: ["Петя", "Ваня", "Саша", "Лиза", "Катя"]
# Гость пришёл или ушёл? пришёл
# Имя гостя: Алекс
# Привет, Алекс!

# Сейчас на вечеринке 6 человек: ["Петя", "Ваня", "Саша", "Лиза", "Катя", "Алекс"]
# Гость пришёл или ушёл? пришёл
# Имя гостя: Гоша
# Прости, Гоша, но мест нет.

# Сейчас на вечеринке 6 человек: ["Петя", "Ваня", "Саша", "Лиза", "Катя", "Алекс"]
# Гость пришёл или ушёл? ушёл
# Имя гостя: Ваня
# Пока, Ваня!

# Сейчас на вечеринке 5 человек: ["Петя", "Саша", "Лиза", "Катя", "Алекс"]
# Гость пришёл или ушёл? Пора спать

# Вечеринка закончилась, все легли спать.
# -------
# Решение № 1 (Старое)
# guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]
# while True:
#     humans = len(guests)
#     print(f"Сейчас на вечеринке {humans} человек: {guests}")
#
#     print(f"Гость пришел или ушел?: ", end="")
#     comand = input()
#
#     if comand == "пришел":
#         print("Имя гостя: ", end="")
#         name = input()
#         if humans <= 5:
#             guests.append(name)
#             print(f"Привет {name}!\n")
#         else:
#             print(f"Прости, {name}, но мест нет.\n")
#
#     elif comand == "ушел":
#         print("Имя гостя: ", end="")
#         name = input()
#         guests.remove(name)
#         print(f"Пока {name}!\n")
#
#     elif comand == "пора спать":
#         print("Вечеринка закончилась.")
#         break

# -------
# Решение № 2 повторное.
# guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]
# while True:
#     humans = len(guests)
#     print(f"Сейчас на вечеринке {humans} человек: {guests}")
#
#     comand = input(f"Гость пришел или ушел?: ")
#
#     if comand == "пришел":
#         name = input("Имя гостя: ")
#
#         if humans <= 5:
#             guests.append(name)
#             print(f"Привет {name}!\n")
#         else:
#             print(f"Прости, {name}, но мест нет.\n")
#
#     elif comand == "ушел":
#         name = input("Имя гостя: ")
#         guests.remove(name)
#         print(f"Пока {name}!\n")
#
#     elif comand == "пора спать":
#         print("Вечеринка закончилась.")
#         break

# endregion Задание № 4 Вечеринка.
# -------------------------------------------------------------------------------------------------------------------- #
# region Задание № 5 Плейлист.
# Что нужно сделать
# Мы пишем приложение для удобного прослушивания музыки. У Вани есть список из девяти песен группы Depeche Mode.
# Каждая песня состоит из названия и продолжительности с точностью до долей минут:

# violator_songs = [
#     ['World in My Eyes', 4,86],
#     ['Sweetest Perfection', 4,43],
#     ['Personal Jesus', 4,56],
#     ['Halo', 4,9],
#     ['Waiting for the Night', 6,07],
#     ['Enjoy the Silence', 4,20],
#     ['Policy of Truth', 4,76],
#     ['Blue Dress', 4,29],
#     ['Clean', 5,83]
# ]

# Из этого списка Ваня хочет выбрать N песен и закинуть их в особый плейлист с другими треками. И
# при этом ему важно, сколько времени в сумме эти N песен будут звучать.
# Напишите программу, которая запрашивает у пользователя количество песен из списка
# и затем названия этих песен, а на экран выводит общее время их звучания.

# Пример:
# Сколько песен выбрать? 3
# Название 1-й песни: Halo
# Название 2-й песни: Enjoy the Silence
# Название 3-й песни: Clean

# Общее время звучания песен: 14,93 минуты

# violator_songs = [['World in My Eyes', 4.86],
#                   ['Sweetest Perfection', 4.43],
#                   ['Personal Jesus', 4.56],
#                   ['Halo', 4.9],
#                   ['Waiting for the Night', 6.07],
#                   ['Enjoy the Silence', 4.20],
#                   ['Policy of Truth', 4.76],
#                   ['Blue Dress', 4.29],
#                   ['Clean', 5.83]]
# ---------
# Решение 1 (Старое)
# print("Сколько песен брать: ", end="")
# number = int(input())
# time = 0
# for n in range(number):
#     print(f"Название {n + 1}-й песни: ",end="")
#     search_song = input()
#     for i_song in violator_songs:
#         if i_song[0] == search_song:
#             time += i_song[1]
# print(f"\nОбщее время звучания песен: {round(time, 2)} минуты.")

# ---------
# # Решение 2 (Повторное)
# time = 0
# for i in range(1, int(input("Сколько песен выбрать? ")) + 1):
#     search_song = input(f"Название {i}-й песни: ")
#     for i_song in violator_songs:
#         if i_song[0] == search_song:
#             time += i_song[1]
# print(f"Общее время звучания песен: {round(time, 2)}")

# ---------
# # Решение 3 (Самому хочется попробовать получиться или нет)
# time = 0
# for i in range(1, int(input("Сколько песен выбрать? ")) + 1):
#     name = input(f"Название {i}-й песни: ")
#     for index in range(len(violator_songs)):
#         if name in violator_songs[index]:
#             time += violator_songs[index][1]
# print(f"Общее время звучания песен: {round(time, 2)}")

# endregion Задание № 5 Плейлист.
# -------------------------------------------------------------------------------------------------------------------- #
# region Задание № 6 Уникальные элементы.
# Даны два списка целых чисел, оба списка заполняются с клавиатуры.
# В первый список вводится три числа, во второй — семь чисел. Напишите программу,
# которая запрашивает у пользователя эти числа, затем расширяет первый список
# элементами второго и после этого оставляет в первом списке только уникальные элементы,
# то есть удаляет лишние повторы чисел. Условный оператор использовать нельзя.

# Пример:
# Введите 1-е число для первого списка: 1
# Введите 2-е число для первого списка: 2
# Введите 3-е число для первого списка: 3
# Введите 1-е число для второго списка: 2
# Введите 2-е число для второго списка: 4
# Введите 3-е число для второго списка: 6
# Введите 4-е число для второго списка: 3
# Введите 5-е число для второго списка: 3
# Введите 6-е число для второго списка: 2
# Введите 7-е число для второго списка: 1

# Первый список: [1, 2, 3]
# Второй список: [2, 4, 6, 3, 3, 2, 1]

# Новый первый список с уникальными элементами: [4, 6, 3, 2, 1]

#----------------
# Решение 1 (Старае)
# list_1 = []
# for number in range(3):
#     print(f"Введите {number + 1}-е число для первого списка: ", end="")
#     digit = int(input())
#     list_1.append(digit)
#
# list_2 = []
# for number in range(7):
#     print(f"Введите {number + 1}-е число для первого списка: ", end="")
#     digit = int(input())
#     list_2.append(digit)
#
# print(f"Первый список: {list_1}")
# print(f"Второй список: {list_2}")
#
# list_1.extend(list_2)
# list_1.sort()
# print(list_1,"\n")
#
# new_list = []
# for i in list_1:
#     if i not in new_list:
#         new_list.append(i)
#
# print(f"Новый первый список с уникальными элементами: {new_list}")
# endregion Практическая работа Курс № 2 (Тема № 3 Методы для работы со списками) Уни
# -------------------------------------------------------------------------------------------------------------------- #
# region Задание № 7 Ролики.
# Частная контора даёт в прокат ролики самых разных размеров.
# Человек может надеть ролики любого размера, которые не меньше размера его ноги.

# Пользователь вводит два списка размеров: N размеров коньков и K размеров ног людей.
# Реализуйте код, который определяет, какое наибольшее число человек сможет одновременно взять ролики и пойти покататься.

# Пример:
# Кол-во коньков: 4
# Размер 1-й пары: 41
# Размер 2-й пары: 40
# Размер 3-й пары: 39
# Размер 4-й пары: 42

# Кол-во людей: 3
# Размер ноги 1-го человека: 42
# Размер ноги 2-го человека: 41
# Размер ноги 3-го человека: 42

# Наибольшее кол-во людей, которые могут взять ролики: 2
# -------------------
# Решение № 1 (Старое)
# size_list = []
# number = int(input("Кол-во коньков: "))
#
# for i in range(number):
#     print(f"Размер {i + 1}-й пары: ", end="")
#     size = int(input())
#     size_list.append(size)
# size_list.sort()
#
# print("\n")
# human_list = []
# human = int(input("Кол-во людей: "))
#
# for man in range(human):
#     print(f"Размер ноги {man + 1}-го человека: ", end="")
#     size_human = int(input())
#     human_list.append(size_human)
# human_list.sort()
#
# count = 0
# for count_1 in range(len(human_list)):
#     for count_2 in range(len(size_list)):
#         if human_list[count_1] >= size_list[count_2]:
#             size_list[count_2] = 0
#             count += 1
#             break
# print(f"Наибольшее кол-во людей, которые могут взять ролики: {count}")
# -------------------
# Решение № 2 (Повторное) - Идеальное решение.
# list_office = []
# for pair in range(1, int(input("Кол-во коньков: ")) + 1):
#     list_office.append(int(input(f"Размер {pair} пары: ")))
#
# count_people = 0
# for people in range(1, int(input("\nКол-во людей: ")) + 1):
#     size = int(input(f"Размер ноги {people}-го человека: "))
#
#     if size < min(list_office):
#         while size < min(list_office):
#             size += 1
#
#     if size in list_office:
#         list_office.remove(size)
#         count_people += 1
#
# print(f"\nНаибольшее кол-во людей, которые могут взять ролики: {count_people}")
# endregion Задание № 7 Ролики.
# -------------------------------------------------------------------------------------------------------------------- #
# region Задание № 8 Считалка. (НЕРЕШЕНА)
# N человек, пронумерованных числами от 1 до N, стоят в кругу.
# Они начинают играть в считалку на выбывание, где каждый K-й по счёту человек выбывает из круга, после чего счёт
# продолжается со следующего за ним человека.

# На вход подаётся количество человек N и номер K. Напишите программу, которая выводит число от 1 до N — это номер
# человека, который останется в кругу последним.

# Пример:
# Кол-во человек: 5
# Какое число в считалке? 7
# Значит, выбывает каждый 7-й человек

# Текущий круг людей: [1, 2, 3, 4, 5]
# Начало счёта с номера 1
# Выбывает человек под номером 2

# Текущий круг людей: [1, 3, 4, 5]
# Начало счёта с номера 3
# Выбывает человек под номером 5

# Текущий круг людей: [1, 3, 4]
# Начало счёта с номера 1
# Выбывает человек под номером 1

# Текущий круг людей: [3, 4]
# Начало счёта с номера 3
# Выбывает человек под номером 3

# Остался человек под номером 4


# Решение 1 (Тогда не решил эту задачу)

# list_people = []
# for number in range(1, int(input("Кол-во человек: ")) + 1):
#     list_people.append(number)
#
# number = int(input("Какое число в считалке?: "))
# print(f"Значит, выбывает каждый {number}-й человек \n")
# index = 0
# while min(list_people) != max(list_people):
#     print(f"Текущий круг людей: {list_people}")
#     print(f"Начало счёта с номера {list_people[index]}")
#     count_list = len(list_people)   # Кол-во людей в считалке.

# endregion Задание № 8 Считалка.
# -------------------------------------------------------------------------------------------------------------------- #
# region Задание № 9 Друзья
# N друзей постоянно берут в долг друг у друга деньги. В какой-то момент им надоело забывать, кто, кому и сколько
# должен, и они придумали систему долговых расписок. И, чтобы начать новый год «с чистого листа», друзья решили оплатить
# все долговые расписки, которые накопились у них друг к другу. Однако выяснилось, что иногда один и тот же
# человек в разные дни выступал как в роли должника, так и в роли кредитора.
#
# Напишите программу, которая по заданным распискам вычислит, сколько всего должен каждый друг выплатить другим
# (или получить с других).
#
# Сначала вводится число N — количество друзей, затем вводится число K — количество долговых расписок, после этого
# следует K троек чисел: номер друга, взявшего в долг, номер друга, давшего деньги, и сумма. Гарантируется, что ни один
# друг не брал в долг сам у себя.
#
# Программа должна вывести «баланс друзей», то есть суммы, которые должны получить или отдать друзья. Положительное
# число означает, что друг должен получить деньги от других, отрицательное — должен отдать деньги.

# Пример 1:
# Кол-во друзей: 2
# Долговых расписок: 3

# 1-я расписка
# Кому: 1
# От кого: 2
# Сколько: 10

# 2-я расписка
# Кому: 1
# От кого: 2
# Сколько: 20

# 3-я расписка
# Кому: 1
# От кого: 2
# Сколько: 20

# Баланс друзей:
# 1: -50
# 2: 50

# Пример 2:
# Кол-во друзей: 3
# Долговых расписок: 1

# 1-я расписка
# Кому: 3
# От кого: 1
# Сколько: 100

# Баланс друзей:
# 1 : 100
# 2 : 0
# 3 : -100

# -----------------
# # Решение 1 (Старое)
# N = int(input("Количество друзей: "))
# K = int(input("Кол-во долговых расписок: "))
# IOU = []
#
# for i in range(N):
#     IOU.append(0)
#
# for c_receipt in range(K):
#     print(f"\n{c_receipt + 1}-я расписка")
#
#     while True:
#         print("Кому: ", end="")
#         credit = int(input()) - 1
#
#         print("От кого: ", end="")
#         debit = int(input()) - 1
#
#         if credit != debit:
#             break
#         else:
#             print("Самому себе нельзя давать в долг! \n")
#
#     print("Сколько: ", end="")
#     money = int(input())
#
#     IOU[credit] += money
#     IOU[debit] -= money
#
# print("\nБаланс друзей:")
# for i in range(N):
#     print(f"{i + 1} : {IOU[i]}")
#
# # -----------------
# # Решение 2 (Повторное)
# check_list = []
# N = list(check_list.append(0) for i in range(int(input("Кол-во друзей: "))))
#
# for i in range(int(input("Долговых расписок: "))):
#     print(f"\n{i + 1}-я расписка")
#     while True:
#         credit = int(input("Кому: ")) - 1
#         debit = int(input("От кого: ")) - 1
#         if (credit or debit) >= len(check_list):
#             print("Таких друзей у тебя нет! :)")
#         elif credit == debit:
#             print("Сам у себя в долг? :) Ха-Ха :D")
#         elif credit != debit:
#             break
#
#     money = int(input("Сколько: "))
#     check_list[credit] -= money
#     check_list[debit] += money
#
# print(f"\nБаланс друзей:", end="\n")
# for i in range(len(check_list)):
#     print(f"{i + 1} : {check_list[i]}")

# endregion Задание 9 Друзья
# -------------------------------------------------------------------------------------------------------------------- #
# region Задание № 10 Симметричная последовательность. (Нерешена)
# Последовательность чисел называется симметричной, если она одинаково читается как слева направо, так и справа налево.
# Например, следующие последовательности являются симметричными:

# 1 2 3 4 5 4 3 2 1
# 1 2 1 2 2 1 2 1

# Пользователь вводит последовательность из N чисел. Напишите программу, которая определяет,
# какое минимальное количество и каких чисел надо приписать в конец этой последовательности,
# чтобы она стала симметричной.

# Пример 1:
# Кол-во чисел: 5
# Число: 1
# Число: 2
# Число: 1
# Число: 2
# Число: 2

# Последовательность: [1, 2, 1, 2, 2]

# Нужно приписать чисел: 3
# Сами числа: [1, 2, 1]

# Пример 2:
# Кол-во чисел: 5
# Число: 1
# Число: 2
# Число: 3
# Число: 4
# Число: 5

# Последовательность: [1, 2, 3, 4, 5]

# Нужно приписать чисел: 4
# Сами числа: [4, 3, 2, 1]

# number_list = []
# enum = list(number_list.append(int(input(f"Число: "))) for i in range(int(input("Кол-во чисел: "))))
# print(f"\nПоследовательность: {number_list}")
#
# count = 0
# new_list = []
# for i in range(0, len(number_list)):
#     if number_list[i] != number_list[-i]:
#         count += 1
#         new_list.append(number_list[-i])
# print(f"\nНужно приписать чисел: {count}")
# print(f"Сами числа: {new_list}")



# endregion Задание № 10 Симметричная последовательность.
# -------------------------------------------------------------------------------------------------------------------- #

# endregion Практическая работа Курс № 2 (Тема № 3 Методы для работы со списками)
# -------------------------------------------------------------------------------------------------------------------- #



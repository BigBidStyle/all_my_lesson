# region Что такое список.(Вывести значение с индексом, присвоить значение индексу)
# Список - это нумерованный набор объектов. Каждый элемент набора содержит только ссылки на объект.
# Именно поэтому список может содержать объекты произвольного типа данных и иметь неограниченную степень вложенности.

# 01 - Списки поддерживают обращение к элементу по индексу (нумерация элементов списка начинается с О), получение среда,
# конкатенацию, повторение, а также проверку на вхождение.

# Ранее было отмечено, что списки относятся к изменяемым типам данных (в отличие от кортежей). Это означает,
# что вы можете не только получить элемент по индексу, но и изменить его. Например:

# Вывести значение с индексом 1.
# List = [1, 2, 3, 4]
# print(List[1])  # 2

# Присвоить значение индексу 1.
# List[1] = 7
# print(List)     # [1, 7, 3, 4]
# endregion
# ---------------------------------------------------------------------------------------------------------------------#
# region Создание Списка тремя способами.
# Создать список можно разными способами. Например, можно использовать функцию list(), которой нужно передать
# последовательность, по которой и будет создан список. Если вы ничего не передаете, будет создан пустой список: 

# List = list('Hello')
# print(List)    # ['H', 'e', 'l', 'l', 'o']

# Можно указать все элементы списка в квадратных скобках, как уже было показано. Обратите внимание,
# что элементы могут быть разных типов:

# List = ["а", "Ь", 1]
# print(List)     # ['а', 'Ь', 1)

# Третий способ заключается в поэлементном формировании списка с помощью метода append:
# List = []
# List.append(1)
# List.append(2)
# List.append(3)
# print(List)     # [1, 2, 3]

# В РНР можно использовать такую конструкцию для добавления элементов
# в список:
# List[ ] = новый_ элемент

# В Python ее использовать нельзя, вы получите сообщение об ошибке. Также
# нужно быть осторожнее со следующей конструкцией:
# a = b = ["а", "b"]
# print(a[0])
# print(b[0])

# Как видите, при создании списка сохраняется ссылка на объект, а не сам объект. Поэтому нам кажется, что мы якобы
# создали два списка, а на самом деле обоим переменным была присвоена ссылка, указывающая на объект.
# Напомню, проверить, ссылаются ли переменные на один и тот же объект, можно с помощью оператора is, например
# (если оператор возвращает True, то переменные ссылаются на один и тот же объект):

# print(a is b)
# Если вам нужно создать вложенные списки, то это лучше делать с помощью 
# метода append(), например:

# List = []
# for i in range(3):
#     List.append([])
#     List[0].append(1)
# print(List)     # [[1, 1, 1], [], []]
# endregion
# ---------------------------------------------------------------------------------------------------------------------#
# region Операции над списками.
# Над списками можно выполнить множество операций. Начнем с доступа к элементу. Для этого используются квадратные
# скобки([]), в которых указывается индекс элемента. Нумерация элементов списка начинается с О.
# Примеры использования [] уже были показаны. 

# Примечание. Поскольку нумерация элементов списка начинается с О, то индекс последнего элемента будет меньше на единицу
# количества элементов. 

# Оператор присваивания можно использовать как для присваивания значения всему списку, так и отдельному элементу:
# list = [1, 2, 3]
# list[1] = 6 # [1, 6, 3]

# В Python 3 при позиционном присваивании перед одной из переменных слева от оператора = можно указать звездочку.
# В этой переменной будет сохраняться список, состоящий из "лишних" элементов. Если таких элементов нет, то список
# будет пустым:
# a, b, *c = [1, 2, 3, 4]
# print(a)    # 1
# print(b)    # 2
# print(c)    # [3, 4]
# Если вы попытаетесь получить доступ к несуществующему элементу, вы получите сообщение об ошибке IndexError.

# >>> list[4]
# IndexError: list index out of range

# В качестве индекса можно использовать отрицательные значения, в этом случае смещение будет отсчитываться с конца...:
# >>> list = [1, 2, 3, 4, 5, 6, 7]
# »> list[-2] # 6
#
# Кроме обращения к элементу по индексу списки поддерживают операцию извлечения среза, которая возвращает указанный
# фрагмент списка:
# [<Начало>:<Конец>:<Шаг>] 
# Все три параметра являются необязательными. Если не указан первый параметр, то используется значение О.
# Если не задан второй параметр, то считается, что нужно возвратить фрагмент до конца списка. Если не задан
# последний параметр, то используется значение 1. 
# Операция среза очень интересная и мощная. Вот, например, как можно вывести элементы списка в обратном порядке: 
# >>> list[: :-1] # [7, 6, 5, 4, 3, 2, 1]

# Вот еще несколько примеров:
# >>> list[:-1] # Без последнего элемента
# [ 1, 2, 3, 4, 5, 6]

# >>> list[1:] # Без первого элемента
# [2, 3, 4, 5, 6, 7]

# >>> list[0:3] # Первые три элемента 
# [ 1, 2, 3]

# >>> list[-1:] # Последний элемент 
# [7]

# Срез позволяет даже изменять элементы списка, например: 
# »> list[1:3] = [8, 9]
# >>> list # [1, 8, 9, 4, 5, 6, 7]

# Только будьте осторожны с этой операцией! 

# Срез - это не единственная полезная операция над списком. Вы можете выполнить конкатенацию списков, 
# используя оператор +: 

# >>> list = [1, 8, 9, 4, 5, 6, 7] 
# >>> list2 = [10, 11, 12] 
# >>> listЗ = list + list2
# print(listЗ) # [1, 8, 9, 4, 5, 6, 7, 10, 11, 12] 

# Если нужно добавить элементы в текущий список, можно использовать 
# оператор +=: 
# >>> list = [1, 8, 9, 4, 5, 6, 7] 
# >>> list += [10, 11, 13]
# print(list) # [ 1, 8, 9, 4' 5, 6, 7, 10, 11, 13] 
# endregion Операции над списками.
# ---------------------------------------------------------------------------------------------------------------------#
# region Многомерные списки.
# Любой элемент списка может содержать любой объект, в том числе и другой список, кортеж, словарь и т.д. Вот как можно
# создать список, состоящий из трех списков:
# >>> list = [[1, 2, 3], ['а','Ь','с'], [9, 8, 7]]
# >>> list # [[1, 2, 3], ['а', 'Ь', 'с'], [9, 8, 7]]

# Чтобы добраться к элементам вложенного списка, нужно указывать два индекса, например:
# >» list[1][2]
# 'с'

# В свою очередь элементы вложенного списка также могут быть списками и т.д. Количество вложений не ограничено,
# поэтому у вас могут быть вот такие странные индексы:

# list[1] [2] [3] [4] ...
# Если того не требует решаемая задача, я бы не советовал увлекаться вложенными списками - так вы сделаете программу
# сложнее, чем она могла бы быть.
# endregion Многомерные списки.
# ---------------------------------------------------------------------------------------------------------------------#
# region Проход по элементам списка.
# Вот как можно перебрать все элементы списка: 
# list = [[1, 2, 3], ['а', 'Ь', 'с'], [9, 8, 7]]
# for i in list:
#     print(i, end=" ")   # [1, 2, 3] ['а', 'Ь', 'с'] [9, 8, 7]
 
# Также для перебора списка можно использовать функцию range(): 
# range([<Haчaлo>,] <Конец> [, <Шаг>]) 
# Пример: 

# list =[1, 2, 3, 4]
# for i in range(len(list)):
#     print(list[i], end=" ")

# list = [1, 2, 3, 4]
# for i in range(len(list[1:3])):
#     print(list[i], end=" ")     # 1 2 3 4

# Данный способ можно использовать не только для итерации по одномерным спискам, как вы бы могли подумать, например:
# list = [[1, 2, 3], ['а', 'Ь', 'с'], [9, 8, 7]]
# for i in range(len(list)):
#     print(list[i], end=" ")     # [1, 2, 3] ['а', 'Ь', 'с'] [9, 8, 7]
# В принципе, для перебора элементов списка можно использовать и цикл  while, но обычно используется цикл for,
# что и было продемонстрировано.
# endregion Проход по элементам списка.
# ---------------------------------------------------------------------------------------------------------------------#
# region Поиск элементов в списке.
# Определить, есть ли элемент в списке, можно с помощью оператора in, например: 
# list = [[1, 2, 3], ['а', 'Ь', 'с'], [9, 8, 7]]
# print(2 in list)    # False
#
# list = [1, 2, 3, 4]
# print(2 in list) # True

# Как видите, данный способ не работает с многомерными списками, поэтому для поиска элемента в таких списках
# правильнее использовать перебор элементов. Хоть медленно, но зато работает.
# Однако оператор in сообщает только, если ли элемент в списке, но он не сообщает его позицию.
# Для этого можно использовать метод index:

# list = [1, 2, 3, 4]
# print(list.index(3))    # 2

# Здесь видно, что элементу 3 соответствует индекс 2. Если указанного элемента нет в списке, вы получите ошибку
# ValueError.
# >>> list.index(7) 
# Traceback (most•recent call last): 
# File "<pyshell#72>", line 1, in <module> 
# list.index(7) 
# ValueError: 7 is not in list 

# Посчитать количество элементов с определенным значением позволяет метод count(): 
# >>> list = [1, 2, 2, 3, 4]
# >>> list.count(2) # 2
# >>> list.count(3) # 1
# >>> list.count (7) # о

# Данный метод можно также использовать в качестве основного метода поиска элемента - если количество равно О,
# то и элемента в списке нет. Вам не нужно обрабатывать никакие исключения, просто анализируйте количество элементов
# и все.

# Функции min() и mах() позволяют найти минимальный и максимальный
# элемент списка соответственно: 
# >>> list = [1, 2, 2, 3, 4] 
# >>> min(list) # 1
# >>> max(list) # 4
# endregion Поиск элементов в списке.
# ---------------------------------------------------------------------------------------------------------------------#
# region Добавление и удаление элементов из списка.
# Для добавления и удаления элементов создано множество методов. Начнем
# с метода append( <объект>), позволяющего добавить элемент в конец списка: 
# >>> list = [1, 2, 3, 4] 
# >>> list.append(5) 
# >>> list # [1, 2, 3, 4, 5]

# Также добавить элементы в конец списка можно и с помощью оператора+=,
# например: 
# >>> list += [6, 7] 
# >>> list # [1, 2, 3, 4, 5, 6, 7]

# Метод insert() вставляет объект в указанную позицию. Синтаксис следующий: 
# insert(<индeкc>, <объект>) 
# Примеры: 
# >>> list = # [1, 2, 3, 4, 5, 6, 7]
# >>> list.insert(O, О) # Вставили ноль в начало списка 
# >>> list # [0, 1, 2, 3, 4, 5, 6, 7]

# >>> list.insert(8, 8) # Вставили 8 в позицию 8
# >>> list # [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Для удаления элементов можно использовать методы рор(), remove() и оператор del. Первый удаляет элемент с указанным
# индексом и возвращает его. Если индекс не указан, удаляется и возвращается последний элемент списка:
# list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# print(list.pop(0))  # о

# list = [ 1, 2, 3, 4, 5, 6, 7, 8]
# print(list.pop())   # 8
# #
# list = [1, 2, 3, 4, 5, 6, 7]
#
# Оператор del ничего не возвращает, а просто удаляет элемент. Например:
# del list[6]
# print(list)     # [1, 2, 3, 4, 5, 6]

# Удалить элемент, содержащий определенное значение, можно с помощью метода remove(): 
# >>> list.remove(5) 
# >>> list # [1, 2, 3, 4, 6]
# endregion Добавление и удаление элементов из списка.
# ---------------------------------------------------------------------------------------------------------------------#
# region Перемещивание элементов и выбор случайного элемента.
# Функция shujfle() из модуля random используется для перемешивания списка случайным образом. Функция перемешивает
# сам список и ничего не # возвращает.
# Пример:
# >>> import random 
# >>> list 
# [1, 2, 2, 3, 4] 
# >>> random.shuffie(list) 
# >>> list # [4, 2, 2, 1, З]

# Выбрать случайный элемент со списка можно с помощью функции choice() 
# из того же модуля:
# >>> random.choice(list) # 4
# >>> random.choice(list) # 2

# Изменить порядок следования элементов можно с помощью метода 
# reverse(). В отличие от среза, данный метод работает с самим списком, а не с 
# его копией: 
# >>> list = [4, 2, 2, 1, З]
# >>> list.reverse() 
# >>> list # [З, 1, 2, 2, 4]
# endregion Перемещивание элементов и выбор случайного элемента.
# ---------------------------------------------------------------------------------------------------------------------#
# region Сортировка cписка.
# Для сортировки списка используется метод sort(), синтаксис которого следующий: 
# sort ( [ key=None] [, reverse=False]) 
# Оба параметра являются не обязательными. Метод изменяет текущий список и ничего не возвращает.
# Попробуем отсортировать список, используя параметры по умолчанию:
# >>> list = [2, 3, 7, 5, 6, 1, 4] 
# >>> list.sort() 
# >>> list # [1, 2, 3, 4, 5, 6, 7]

# Для сортировки в обратном порядке укажите параметр reverse=True: 
# >>> list.sort(reverse=True) 
# >>> list 
# [7, 6, 5, 4, 3, 2, 1]

# Иногда нужно не учитывать регистр символов, для этого нужно вызвать 
# sort() так: 
# list.sort(key=str.lower)

# Помните, что метод sort() изменяет список, а в некоторых случаях этого не 
# нужно делать. Для таких случаев предназначена функция sorted(): 
# sоrtеd(<Последовательность>[, key=None] [, reverse=False]) 
# Первый параметр - это последовательность, которую нужно отсортировать, 
# остальные параметры - такие же, как у метода sort(). Данная функция 
# возвращает отсортированный список и не изменяет исходный.
# endregion Сортировка списка.
# ---------------------------------------------------------------------------------------------------------------------#
# region Преобразование списка в строку.
# Для преобразования списка в строку используется метод jоiп(). Вызывать
# его нужно так:
# <Строка> = <разделитель>.jоin(<последовательность>)
# Пример:
# list = ['h', 'е', 'l', 'l', 'о']
# s = "/".join(list)
# print(s) # h/е/l/l/о

# Здесь в качестве разделителя мы используем пустую строку поэтому по сути, разделителя нет.
# endregion Преобразование списка в строку.
# ---------------------------------------------------------------------------------------------------------------------#
# region Вычисления с большими числовыми массивами.
# NumPy1 - основа для огромного числа научных и технических библиотек 
# Python. Но в то же время NumPy - один из самых больших и самых сложных в использовании модулей. Однако вы можете
# выполнить полезные вещи с NumPy, начиная с простых примеров и экспериментируя с ними.

# Нужно сделать только одно примечание относительно использования NumPy. Относительно распространено использовать
# оператор import numpy as np, что и показано в далее. Это просто сокращает название модуля - так удобнее, если часто
# приходится обращаться к нему. Представим, что вам нужно произвести вычисления с огромными числовыми наборами данных,
# например, с массивами или сетками (таблицами).

# Для любых "тяжелых" вычислений с использованием массивов нужно использовать библиотеку NumPy. Основ_ное назначение
# NumPy - то, что она предоставляет Python объект массива, который более эффективен и лучше подходит для математических
# вычислений, чем стандартный список Python. Вот небольшой пример, иллюстрирующий важные поведенческие
# различия между массивами NumPy и списками: 
# # 01 - Списки Python
# a = [2, 2, 2, 2]
# b = [3, 3, 3, 3]
# print(a * 2) # [2, 2, 2, 2, 2, 2, 2, 2]

# print(a + 10)
# Traceback (most recent call last): 
# File "<pyshell#ll5>", line 1, in <module> 
# а + 10
# TypeError: can only concatenate list (not "int") to list 
# print(a + b) # [2, 2, 2, 2, 3, 3, 3, 3]

# Массивы Numpy
# import numpy as np
# an = np.array([2, 2, 3, 3])
# bn = np.array([5, 5, 7, 7])
# print(an * 2)   # [4 4 6 6]
# print(an + 10)  # [12, 12, 13, 13]
# print(an + bn)  # [ 7, 7, 10, 12]
# print(an * bn)  # [ 10, 10, 21, 31]

# Как видите, основные математические операции с массивами ведут себя иначе. В частности, скалярные операции
# (например, an * 2 или bn + 10) применяются к массиву поэлементно (в случае с обычным списком нужно было писать цикл
# и добавлять в цикле 10 к каждому значению списка). Кроме того, математически операции, когда оба операнда, являются
# массивами, применяются к каждому элементу и в результате создается новый массив.

# Библиотека NumPy предоставляет набор "универсальных функций", которые также доступны для работы с массивами.
# Данные функции представляют собой замену обычных функций, которые 
# вы можете найти в модуле math. Например:

# print(np.sqrt(an))  # [1.41421356 1.41421356 1.73205081 1.73205081]
# print(np.cos(an))   # [-0.41614684 -0.41614684 -0.9899925  -0.9899925 ]

# Использование универсальных функций может быть в сотни раз быстрее, чем перебор массива в цикле поэлементно и
# выполнение необходимых операций над каждым элементом отдельно. Поэтому если вам нужно выполнить операции с
# использованием функций из модуля math над элементами массива, взгляните на аналогичные функции модуля np. Вы должны
# предпочесть их; если это возможно.

# "За кулисами" массивы NumPy выделяются таким же способом, как и в С или Fortran. А именно они являются большими,
# непрерывными областями памяти, состоящие из однородного типа данных. Именно поэтому вы можете сделать массивы просто
# огромными, гораздо больше, чем вы себе можете представить. Например, если вы желаете сделать двумерную таблицу
# 10 ООО х 10 ООО, состоящую из чисел с плавающей запятой, это не проблема.

# import numpy as np
# qrid = np.zeros(shape=(10000, 10000), dtype=float)
# print(qrid)
# результат
# array ( [ [ о.' о.' о.' ... ' о.' о.' о.]'
# [ о.' о.' о.' ... , о.' о.' о� ] ·,
# [ о.' о.' о.' ... , о.' о.' о.]'
# ... ,
# о.' о.' о.' ... , о.' о.' о.]'
# о.' о.' о.' ... , о.' о.' о.]'
# о.' о.' о.' ... , о.' о.' о.]])

# Все обычные операции все еще применяются ко всем элементам одновременно: 
# import numpy as np
# qrid = np.zeros(shape=(10000, 10000), dtype=float)
# qrid += 100
# print(qrid)
# array ( [ [ 100., 100., 100., ... , 100., 100., 100.],
# [ 100., 100., 100., ... , 100., 100., 100.],
# [ 100., 100., 100., ... , 100., 100., 100.],
# ... , 
# 100., 100., 100., ... , 100., 100., 100.],
# 100., 100., 100., ... , 100., 100., 100.],
# 100., 100., 100., ... , 100., 100., 100.]])

# Один чрезвычайно известный аспект NumPy _:_ способ, которым она расширяет список Python,
# индексирующий функциональность - особенно при работе с многомерными массивами. Чтобы проиллюстрировать это,
# сделайте простую двумерную матрицу и попробуйте выполнить некоторые эксперименты:
# import numpy as np
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a)    # ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Показать Ряд О
# print(a[0]) # [1, 2, 3, 4]

# Показать Колонка 1
# print(a[:, 1]) # [ 2, 6, 10]

# Выбираем фрагмент массива и изменяем его
# print(a[1:3, 1:3]) # [[ 6, 7],[ 10, 11]])

# a[1:3, 1:3] += 10
# print(a) #[[ 1, 2, 3, 4], [ 5, 16, 17, 8], [ 9, 20, 21, 12]]
# endregion Вычисления с большими числовыми массивами.
# ---------------------------------------------------------------------------------------------------------------------#
# Шпаргалка

# list.append(obj)	Добавляет элемент obj в конец списка
# list.count(obj)	Возвращает количество элементов со значением obj в списке
# list.clear()	Очищает список
# list.copy()	Возвращает поверхностную копию списка
# list.extend(col)	Добавляет в конец списка элементы коллекции col
# list.index(obj, start=0, stop=-1])	Возвращает индекс первого элемента со значением obj в диапазоне от start до stop
# list.insert(index, obj)	Вставляет объект obj в позицию index, смещая оставшиеся элементы правее
# list.pop(index=-1)	Удаляет и возвращает значение элемента из позиции index
# list.remove(val)	Удаляет первый элемент со значением val в списке
# list.reverse()	Разворачивает список
# list.sort(key=None, reverse=False)	Сортирует список по значению, которое возвращает функция key.
# Для обратной сортировки установите reverse=True

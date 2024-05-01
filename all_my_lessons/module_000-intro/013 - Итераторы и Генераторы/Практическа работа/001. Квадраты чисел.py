# Задача 1. Квадраты чисел
# Что нужно сделать
# Пользователь вводит число N. Напишите программу, которая генерирует последовательность из квадратов чисел от 1 до
# N (1 ** 2, 2 ** 2, 3 ** 2 и так далее). Реализацию напишите тремя способами: класс-итератор, функция-генератор и
# генераторное выражение.
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
# При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
# Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
# Для создания нового класса на основе уже существующего используется наследование.
# Сообщения о процессе получения результата осмыслены и понятны для пользователя.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы/функции имеют прописанную документацию.
# Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs). Если функция/метод ничего не
# возвращает, то используется None.


# Решение № 1 - Класс итератор.

class SquaresIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration

n = int(input("Введите число N: "))
squares_iter = SquaresIterator(n)
for square in squares_iter:
    print(square, end=" ")


#-------------------------------#
# Решение № 2 Функция генератор
def square(numbers):
    for sq_num in range(numbers):
        yield sq_num ** 2

num = int(input(10))
sq = square(num)
for sqn in sq: print(sqn, end=' ')
print(f'<-- Квадраты чисел от 0 до {num}. Решение задачи функцией генератором.')
#-------------------------------#
# Решение № 3. Генераторное выражение.
square = (num ** 2 for num in range(int(input(10))))
[print(sq_num, end=' ') for sq_num in square]
print('<-- Решение задачи генераторным выражением.')
#-------------------------------#

import time
from typing import Callable, Any # <-- Аннотация.

def timer(func: Callable, *args, **kwargs) -> Any:
    """Функция-таймер. Выводит время работы функции и возвращает ее результат."""
    started_at = time.time()
    result = func(*args, **kwargs)
    ended_at = time.time()
    run_time = round(ended_at - started_at, 2)
    print(f"Функция работала {run_time} секунд(ы)")

    return result

def squares_sum() -> int:
    """
    Функция нахождения квадратов для каждого N от 0 до 10000,
    где 0 <= N <= 100

    :return: Сумма квадратов.
    """
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])

    return result

def cubes_sum(number: int) -> int:
    """
    Функция нахождения кубов для каждого N от 0 до 10000,
    где 0 <= N <= 100

    :return: Сумма кубов.
    """
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 3 for i_num in range(10000)])

    return result


my_result = timer(squares_sum)
my_cubes_sum = timer(cubes_sum, 200)
# print(my_cubes_sum)


# Практическая работа.
# Задача 1
# Дана функция func_1, которая принимает число и возвращает результат его сложения с числом 10:

# def func_1(x):
#     return x + 10

# Реализуйте функцию высшего порядка func_2, которая будет возвращать перемножение двух результатов переданной функции.
# Пример основного кода:
# print(func_2(func_1, 9))
# Результат: 361.

# def func_1(x):
#     return x + 10
#
# def func_2(func, number):
#     return func(number) * func(number)
#
# print(f'Результат: {func_2(func_1, 9)}')
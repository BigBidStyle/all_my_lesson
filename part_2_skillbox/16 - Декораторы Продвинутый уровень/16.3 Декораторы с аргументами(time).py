import time
import functools
from typing import Callable, Any

def timer_with_precision(precision) -> Callable:
    def timer_decorator(func: Callable) -> Callable:
        """Декоратор, выводящий время работы."""

        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Any:
            started_at = time.time()
            result = func(*args, **kwargs)
            ended_at = time.time()
            run_time = round(ended_at - started_at, precision)
            print(f"Функция работала {run_time} секунд(ы)")

            return result
        return wrapped_func
    return timer_decorator

@timer_with_precision(precision=2)
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

@timer_with_precision(precision=4)
def cubes_sum(number: int) -> int:
    """
    Функция нахождения куба, для каждого N от 0 до 10000,
    где 0 <= N <= 100
    :return: сумма квадратов.
    """
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 3 for i_num in range(10000)])

my_sum = squares_sum()
my_cubes_sum = cubes_sum(200)
print(squares_sum.__doc__)
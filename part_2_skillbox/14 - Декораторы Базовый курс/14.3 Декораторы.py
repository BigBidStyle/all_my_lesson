import time
from typing import Callable, Any

def timer(func: Callable) -> Callable:
    """Декоратор, выводящий время работы."""

    def wrapped_func(*args, **kwargs) -> Any:

        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_at, 2)
        print(f"Функция работала {run_time} секунд(ы)")

        return result
    return wrapped_func

@timer
def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])

@timer
def cubes_sum(number: int) -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 3 for i_num in range(10000)])

my_sum = squares_sum()
my_cubes_sum = cubes_sum(200)


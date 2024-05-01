import time
from contextlib import contextmanager
from collections.abc import Iterator

@contextmanager
def next_num(num: int) -> Iterator[int]:
    print('Входим в функцию')
    try:
        yield num + 1
    except ZeroDivisionError as exc:
        print(f"Нельзя делить на ноль: ->{exc}")
    finally:
        print("Выполняю дальше...")
    print("Выход из функции.")

with next_num(0) as next:
    print(f'Следующие число = {next}')
    print(10 / next)

# ------------------------------------- #
print("---------------------------------")
# Практическая задача # 1 - Таймер.
@contextmanager
def timer() -> Iterator:
    start = time.time()
    try:
        yield
    except Exception as exc:
        print(exc)
    finally:
        print(time.time() - start)

with timer() as st1:
    print("Первое вычисление:", end='')
    val_1 = 100 * 100 ** 1000000

with timer() as st2:
    print("Первое вычисление:", end='')
    val_2 = 200 * 200 ** 1000000

with timer() as st3:
    print("Первое вычисление:", end='')
    val_3 = 300 * 300 ** 1000000


# ------------------------------------- #
print("---------------------------------")
# Практическая задача # 2 - Директории.
import os
@contextmanager
def in_dir(path):
    cur_path = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(cur_path)


with in_dir('C:\\'):
    print(os.listdir())
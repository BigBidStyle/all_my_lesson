import time


class Timer:
    def __init__(self):
        print("Время работы кода", end =" ")
        self.start = None

    def __enter__(self) -> 'Timer':
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is TypeError:
            print(" <- Есть ошибка")
            return True
        print(time.time() -self.start)

with Timer() as t1:
    print("первой части ->", end=" ")
    val_1 = 100 * 100 ** "fdx" # <- Вставили специально ошибку.
    # Еще како-то вид

with Timer() as t2:
    print("второй части ->", end=" ")
    val_2 = 200 * 200 ** 1000000
    # Еще како-то вид

with Timer() as t3:
    print("третьей части ->", end=" ")
    val_3 = 300 * 300 ** 1000000
    # Еще како-то вид
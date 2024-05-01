# Декораторы функций.
def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("Что-то делаем перед вызовом функции...")
        res = func(*args, **kwargs)
        print("Что-то делаем после вызова функции.")
        return res
    return wrapper  # <- Возвращаем ссылку на внутреннею функцию.

def some_func(title,tag):
    print(f"<{tag}>{title}</{tag}>")

some_func = func_decorator(some_func)
some_func("Python навсегда со мной!!!", "H1")

# -------------------------------------------------------------------------------------------------------------------- #
# Декораторы функций.
import time
def test_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        dt = round(end_time - start_time, 5)
        print(f"Время работы программы {dt} сек.")
        return  res
    return wrapper

@test_time # <-- прописываем декоратор, который хотим применить к этой функции.
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

@test_time  # <-- прописываем декоратор, который хотим применить к этой функции.
def get_fast_node(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b

    return a

# print("---------------")
# get_node = test_time(get_nod)
# res = get_node(2, 100000)
# print(res)
# # print("---------------")
# get_fast_node = test_time(get_fast_node)
# res = get_fast_node(2, 100000)
# print(res)
# print("---------------")
get_nod(2, 100000)
get_fast_node(2, 100000)


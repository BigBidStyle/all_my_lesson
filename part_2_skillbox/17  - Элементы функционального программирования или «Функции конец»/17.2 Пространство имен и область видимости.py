
def f1():
    print("Внутри ф1 num =", number)

def f2():
    number = 50 # локальная переменная
    print("Внутри ф2 num = ", number)

def f3():
    def f4():
        # global number
        nonlocal number # Область видимости из верхней области.
        number = 10
        print("Внутри f3/f4 num =", number)

    number = 30
    print("Внутри f3 num =", number)
    f4()
    print("Внутри f3 num =", number)

number = 100 # глобальная переменная
print("global num = ", number)
f1()
f2()
f3()
print(number)
# ------------------------------------------------------------------------------------------------------------------- #
global_count = {}
print("---------")
def decorator_counter(func):
    local_count = {}

    def wrapped_func(*args, **kwargs):
        global global_count
        nonlocal local_count
        global_count[func.__name__] = global_count.get(func.__name__, 0) + 1
        local_count[func.__name__] = local_count.get(func.__name__, 0) + 1
        print(global_count, local_count)
        return func(*args, **kwargs)

    wrapped_func.check_count = local_count  # добавим на всякий случай ссылку на этот локальный словарь
    return wrapped_func


@decorator_counter
def hello():
    print('hello')


@decorator_counter
def hello_2():
    print('hello')


hello()
hello()
hello_2()
hello_2()
print(hello_2.check_count)

print('*' * 100)
# print(dir(__builtins__))
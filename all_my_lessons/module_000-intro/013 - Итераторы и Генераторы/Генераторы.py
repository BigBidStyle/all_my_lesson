# Генераторы - это итератора, реализованные в виде функции и по которым можно итерироваться только один раз.
# Генераторы - это функции, которые используют выражение yield.
# Генератор чисел фибоначи.
def fibonacci(number):
    cur_val = 0
    next_val = 1
    for _ in range(number):
        yield cur_val # <-- Выдать значение (Он замораживает функцию, со всеми значениями)
        cur_val, next_val = next_val, cur_val + next_val
        if cur_val > 10 ** 6:
            return

def square(nums):
    for num in nums:
        yield num ** 2

# Числа фибоначи.
fib_seq = fibonacci(number=1000000000000)
for i_value in fib_seq:
    print(i_value, end=' ')
print()

# Генератор от генератора
print(sum(square(fibonacci(number=5000))))

# Генератор выражений
cubes_gen = (num ** 3 for num in range(10))
for i_num in cubes_gen:
    print(i_num, end=' ')
print('\n')
# ------------------------------------- #
# Простой пример
def square(numbers):
    for num in range(numbers):
        yield num ** 2

sq = square(10)
for sqn in sq: print(sqn, end=" ")
print('\n')
# ------------------------------------- #
def get_list():
    for i in range(1, 10):
        a = range(i, 11)
        yield sum(a) / len(a)

a = get_list()
print(*list(a))





class Fibonacci:
    """Итератор последовательности Фибоначчи из н-элементов"""
    def __init__(self, number):
        self.counter = 0    # Счетчик.
        self.cur_val = 0    # Первое число.
        self.next_val = 1   # Второе число.
        self.number = number    # Кол-во чисел.

    def __iter__(self):
        self.counter = 0    # Счетчик.
        self.cur_val = 0    # Первое число.
        self.next_val = 1   # Второе число.
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > 1:
            if self.counter > self.number:
                raise StopIteration()
            self.cur_val, self.next_val = self.next_val, self.cur_val + self.next_val

        return  self.cur_val

fib_iterator = Fibonacci(10)
for i_value in fib_iterator:
    print(i_value)





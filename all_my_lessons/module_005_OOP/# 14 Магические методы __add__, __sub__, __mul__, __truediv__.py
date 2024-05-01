# Магические методы для арифметических операций.
# Оператор x + y <-- метод --> __add__() <-- для операции сложения
# Оператор x - y <-- метод -->__sub__() <-- для операции вычитания
# Оператор x * y <-- метод -->__mul__() <-- для операции умножения
# Оператор x / y <-- метод -->__truediv__() <-- для операции деления
# Оператор x // y <-- метод -->__floordiv__() <-- для операции деления
# Оператор x % y <-- метод -->__mod__() <-- для операции деления

# Оператор x += y <-- метод --> __iadd__() <-- для операции сложения
# Оператор x -= y <-- метод -->__isub__() <-- для операции вычитания
# Оператор x *= y <-- метод -->__imul__() <-- для операции умножения
# Оператор x /= y <-- метод -->__itruediv__() <-- для операции деления
# Оператор x //= y <-- метод -->__ifloordiv__() <-- для операции деления
# Оператор x %= y <-- метод -->__imod__() <-- для операции деления

class Clock:
    __DAY = 86400 # число секунд в сутках.

    def __init__(self, seconds: int): # :int <-- нотация для программиста, что бы он передавал целое число.
        if not isinstance(seconds, int):
            raise TypeError('Секунды должны быть целыми числами')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}'

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")

        sc = other
        if isinstance( other, Clock):
            sc = other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds += sc
        return self

c1 = Clock(83588)
c1 = c1 + 1000 # равносильно тому, что прописать с1 = c1.__add__(1000)
print(c1.get_time())

c2 = Clock(2000)
c3 = c1 + c2
print(c3.get_time())

c1 = 100 + c1   # <-- __radd__
print(c1.get_time()) # <-- __radd__

c1 += 100   # <--__iadd__
print(c1.get_time())   # <--__iadd__
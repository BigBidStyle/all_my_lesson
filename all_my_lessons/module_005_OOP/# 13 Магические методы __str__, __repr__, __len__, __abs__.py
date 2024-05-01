# dunder методы (от английского сокращения double underscore)
# __str__() <-- Для отображения информации об объекте класса для пользователей (например, для функции print, str)
# __repr__() <-- Для отображения информации об объекте класса в режим отладки (для разработчиков)
# __len__() <-- Позволяет применить функцию len() к экземплярам класса.
# __abs__() <-- Позволяет применять функцию abs() к экземплярам класса.


class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self): # Магический метод для отладки
        return f'{self.__class__} : {self.name}' # cat дял консоли

    def __str__(self):  # Магический метод для вывода информации пользователю.
        return f'{self.name}' # print(cat) or str(cat)

cat = Cat("Васька")
print(cat, '<- Сработал метод __str__')


class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))

p = Point(-1, 2)
print(len(p))
print(abs(p))



class Point:
    min_coord = 0   # Определяем атрибут.
    max_coord = 100 # Определяем атрибут.

    def __init__(self, x , y):   # Инициализатор объекта класса.
        print("Сработал метод: __init__(self, x , y)")
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        if self.min_coord <= x <= self.max_coord:
            self.x = x
            self.y = y

    # Пример изменения атрибута класса.
    @classmethod
    def set_bound(cls, left):
        cls.min_coord = left

    # --------------------------------------------------- #
    # item <-- атрибут к которому идет обращение.
    # Пример работы __setattr__(self, key, value)
    """__setattr__(self, key, value) - автоматически  вызывается при изменении свойства KEY класса."""
    def __setattr__(self, key, value):
        print("Сработал метод: __setattr__(self, key, value)")
        if key == 'z':
            raise AttributeError('Недопустимое имя атрибута.')
        else:
            object.__setattr__(self, key, value) # Переопределяем объект

    # --------------------------------------------------- #
    # Пример работы __getattribute__(self, item)
    """__getattribute__(self, item) - автоматически вызывается при получении свойства класса с именем item."""
    def __getattribute__(self, item):
        print("Сработал метод: __getattribute__(self, item)")
        if item == 'x':
            raise ValueError('Доступ к X <-- ЗАПРЕЩЕН!!!')
        else:
            return object.__getattribute__(self, item) # Переопределяем объект

    # --------------------------------------------------- #
    # Пример работы __getattr__(self, item)
    """__getattr__(self, item) - автоматически вызывается при получении несуществующего свойства item класса."""
    def __getattr__(self, item):
        print("Сработал метод: __getattr__(self, item):")
        print(f"Несуществующий ключ --> {item}:")
        return False # <-- Это нужно, чтобы не выскакивало сообщение об ошибке, а возвращалось значение.

    # --------------------------------------------------- #
    # Пример работы __delattr__(self, item)
    """__delattr__(self, item) - автоматически вызывается при удалении свойства item (не важно существует оно или нет)"""
    def __delattr__(self, item):
        print("Сработал метод: __delattr__(self, item):")
        object.__delattr__(self, item)  # Переопределяем объект
    # --------------------------------------------------- #

pt1 = Point(1, 2)
pt2 = Point(10, 20)

# Пример изменения атрибута класса.
# pt1.set_bound(-100)
# print(pt1.__dict__)
# print(Point.__dict__)

# Пример работы __getattr__(self, item)
# обращаемся к несуществующему атрибуту
# print(pt1.yy)   # res --> None
# print(pt1.max_coord)

# Пример работы __setattr__(self, key, value)
# pt1.z = 5 # AttributeError: Недопустимое имя(z) атрибута.

# Пример работы __getattribute__(self, item)
# a = pt1.x # res = ValueError: Доступ к X <-- ЗАПРЕЩЕН!!!
# a = pt1.y

# Пример работы __delattr__(self, item)
del pt1.x
print(pt1.__dict__)
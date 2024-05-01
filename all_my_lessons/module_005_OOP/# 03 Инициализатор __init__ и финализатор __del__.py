class Point:
    color = 'red'
    circle = 1

    def __init__(self, x: int = 0, y: int = 0) -> None:   # Инициализатор __init__ объекта класса Point.
        print('Инициализатор __init__ класса Point.' + str(self))
        self.x = x  # Через инициализатор __init__ определяем новый атрибут x классу Point.
        self.y = y  # Через инициализатор __init__ определяем новый атрибут y классу Point.

    def __del__(self):  # Финализатор класса.
        print('Удаление экземпляра: ' + str(self))

pt = Point(1, 2)    # Для инициализатора __init__ дополнительно указываем два параметра.
print(pt.__dict__)  # Выводим локальные свойства экземпляра класса Point.

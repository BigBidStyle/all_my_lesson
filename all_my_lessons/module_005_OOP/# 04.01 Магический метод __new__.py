class Point:
    def __new__(cls, *args):  # Магический метод __new__
        print(f'Вызов __new__ для {str(cls)}')
        return super().__new__(cls) # Ссылка на базовый класс в котором вызывается магический метод __new__.

    def __init__(self, x = 0, y = 0): # Инициализатор объекта класса.
        print(f'Вызов __init__ для {str(self)}')
        self.x = x
        self.y = y

    def __del__(self):  # Финализатор класса.
        print('Удаление экземпляра: ' + str(self))

pt = Point(1, 2)


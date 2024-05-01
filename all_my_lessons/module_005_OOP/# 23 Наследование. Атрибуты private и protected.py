class Geom: # Базовый класс.
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f'Инициализатор Geom для {self.__class__}.')
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

class Rect(Geom):   # Дочерний класс.
    def __init__(self, x1, y1, x2, y2, fill = 'red'):
        super().__init__(x1, y1, x2, y2) # <-- Называется делегированием.
        self._fill = fill

    def get_coords(self):
        return (self._x1, self._y1)

r = Rect(0, 0, 10, 20)
print(r._x1)
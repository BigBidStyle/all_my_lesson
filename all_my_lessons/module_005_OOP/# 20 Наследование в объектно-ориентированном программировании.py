class Geom: # Базовый класс или родительский класс.
    name = 'Geom'
    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

# Если один класс определяется на основе другого - называется наследованием.
class Line(Geom):   # Подкласс или дочерний класс.
    name = 'Линия.' # Переопределение.
    def draw(self):
        print('Рисование линии.')

class Rect(Geom):   # Подкласс или дочерний класс.
    name = 'Прямоугольник.' # Переопределение.
    def draw(self):
        print('Рисование прямоугольника.')

l = Line()
r = Rect()

l.set_coords(1, 1, 2, 2)
r.set_coords(2, 2, 5, 6)
print(l.name)
print(r.name)


# Задача 1. Транспорт
# У нас есть парк транспорта. У каждого транспорта есть цвет и скорость, и каждый умеет двигаться и подавать сигнал.
# В парке транспорта стоят:

# Автомобили. Они могут ездить только по земле.
# Лодки. Ездят только по воде.
# Амфибии. Могут перемещаться и по земле, и по воде.

# Напишите код, который реализует соответствующие классы и методы. Класс «Транспорт» должен быть абстрактным и
# содержать абстрактные методы.

# Также добавьте класс-примесь, в котором реализован функционал проигрывания музыки. «Замешайте» этот класс в «Амфибию»

from abc import ABC, abstractmethod

class MusicMixin:
    def play_music(self):
        print("""SIR-MIX-A-LOT""")

class Transport(ABC):
    @abstractmethod
    def ride_on_earth(self):
        pass

    @abstractmethod
    def ride_on_water(self):
        pass

class Car(Transport):
    def ride_on_earth(self):
        print("Едем по земле")

class Boat(Transport):
    def ride_on_water(self):
        print("Ходим по воде")

class Amphibian(Car, Boat, MusicMixin):
    pass


amph_transport = Amphibian()
amph_transport.ride_on_earth()
amph_transport.ride_on_water()
amph_transport.play_music()




# Задача 2. Фигуры
#
# При моделировании компьютерных объектов используются два типа фигур: прямоугольники и квадраты. Каждая из них имеет координаты XY,
# длину и ширину. Также каждая фигура может менять координаты (двигаться) и менять размер.
#
# Реализуйте такие классы. Учтите, что с точки зрения интерфейса прямоугольник и квадрат — это разные фигуры и работают они по-разному.
# В частности, по разному работает метод изменения размера фигуры, так как у квадрата все стороны равны.

# Вариант с примесью - когда один метод работает одинаково для двух классов
class Figure:

    def __init__(self, pos_x, pos_y, length, width):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length
        self.width = width

    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


class ResizeAbleMixin:
    def resize(self, length, width):
        self.length = length
        self.width = width


class Rectangle(Figure, ResizeAbleMixin):
    pass


class Square(Figure, ResizeAbleMixin):

    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size, size)


# Второй вариант с абстрактным классом и переопределением метода изменения размеров

class Figure(ABC):

    def __init__(self, pos_x, pos_y, length, width):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length
        self.width = width

    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def resize(self, width, length):
        pass


class Rectangle(Figure):

    def resize(self, width, length):
        self.width = width
        self.length = length


class Square(Figure):

    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size, size)

    def resize(self, width, length):
        if width == length:
            self.width = width
            self.length = length
        else:
            print("У квадрата стороны равны!")

rect_1 = Rectangle(pos_x=10, pos_y=20, length=5, width=6)
rect_2 = Rectangle(pos_x=30, pos_y=40, length=10, width=11)
square_1 = Square(pos_x=50, pos_y=70, size=7)
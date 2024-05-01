# Практическая работа.
# Задача 1. Машина 2.
# Модернизируйте класс Toyota из прошлого урока. Атрибуты остаются такими же:

# Цвет машины (например, красный),
# Цена (один миллион),
# Максимальная скорость (200),
# Текущая скорость (ноль).

# Добавьте два метода класса:

# Отображение информации об объекте класса.
# Метод, который позволяет устанавливать текущую скорость машины.
# Проверьте работу этих методов.

import random

class Toyota:
    color = 'red'
    price = int(1e6)
    max_speed = 200
    now_speed = 0

    def info_car(self):
        print('\nColor car: {}\nCar cost: {}\nMaximum speed: {}\nNow speed: {}'
              .format(self.color, self.price, self.max_speed, self.now_speed))

    def new_speed(self, new_speed):
        self.now_speed = new_speed

car = Toyota()
car.new_speed(input('Input new speed for car: '))
car.info_car()

print(Toyota.now_speed)

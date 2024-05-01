"""Для одной игры необходимо реализовать механику магии, где при соединении двух элементов получается новый.
У нас есть четыре базовых элемента: «Вода», «Воздух», «Огонь», «Земля». Из них получаются новые:
«Шторм», «Пар», «Грязь», «Молния», «Пыль», «Лава».

Таблица преобразований:

Вода + Воздух = Шторм;
Вода + Огонь = Пар;
Вода + Земля = Грязь;
Воздух + Огонь = Молния;
Воздух + Земля = Пыль;
Огонь + Земля = Лава.

Напишите программу, которая реализует все эти элементы. Каждый элемент необходимо организовать как отдельный класс.
Если результат не определён, то возвращается None.

Примечание: сложение объектов можно реализовывать через магический метод __add__, вот пример использования:"""
# print('Пример магического метода __add__')
# class ExampleOne:
#     def __add__(self, other):
#         return ExampleTwo()
#
# class ExampleTwo:
#     answer = 'сложили два класса и вывели'
#
# first_example = ExampleOne()
# second_example = ExampleTwo()
# result = first_example + second_example
# print(result.answer)

"""Дополнительно: придумайте свой элемент (или элементы) и реализуйте его взаимодействие с остальными."""

class Element:
    def __init__(self, name):
        self.name = name

class Water(Element):
    def __init__(self):
        super().__init__("Вода")

class Air(Element):
    def __init__(self):
        super().__init__("Воздух")

class Fire(Element):
    def __init__(self):
        super().__init__("Огонь")

class Earth(Element):
    def __init__(self):
        super().__init__("Земля")

class Storm(Element):
    def __init__(self):
        super().__init__("Шторм")

class Steam(Element):
    def __init__(self):
        super().__init__("Пар")

class Mud(Element):
    def __init__(self):
        super().__init__("Грязь")

class Lightning(Element):
    def __init__(self):
        super().__init__("Молния")

class Dust(Element):
    def __init__(self):
        super().__init__("Пыль")

class Lava(Element):
    def __init__(self):
        super().__init__("Лава")

def combine_elements(element1, element2):
    if isinstance(element1, Water) and isinstance(element2, Air) or isinstance(element1, Air) and isinstance(element2, Water):
        return Storm()
    elif isinstance(element1, Water) and isinstance(element2, Fire) or isinstance(element1, Fire) and isinstance(element2, Water):
        return Steam()
    elif isinstance(element1, Water) and isinstance(element2, Earth) or isinstance(element1, Earth) and isinstance(element2, Water):
        return Mud()
    elif isinstance(element1, Air) and isinstance(element2, Fire) or isinstance(element1, Fire) and isinstance(element2, Air):
        return Lightning()
    elif isinstance(element1, Air) and isinstance(element2, Earth) or isinstance(element1, Earth) and isinstance(element2, Air):
        return Dust()
    elif isinstance(element1, Fire) and isinstance(element2, Earth) or isinstance(element1, Earth) and isinstance(element2, Fire):
        return Lava()
    else:
        return None

# Пример использования
water = Water()
air = Air()

result = combine_elements(water, air)
if result:
    print(f"При соединении {water.name} и {air.name} получается {result.name}")
else:
    print("Невозможно соединить эти элементы")

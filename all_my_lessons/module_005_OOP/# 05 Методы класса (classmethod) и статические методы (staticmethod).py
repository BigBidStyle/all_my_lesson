class Vector:
    min_coord = 0   # Определяем атрибут классу Vector.
    max_coord = 100 # Определяем атрибут классу Vector.

    @classmethod    # Метод класса работает не посредственно с атрибутами этого класса.
    def validate(cls, arg: int) -> True:  # Объявляем метод класса.
        return cls.min_coord <= arg <= cls.max_coord # Возвращает True если попадает в диапазон.

    def __init__(self, x: int , y: int) -> None:   # Инициализатор объекта класса.
        self.x = self.y = 0 # Присваиваем по умолчанию значение 0 переменной x и y.
        # Если проходим проверку, то присваиваем заданные значение x и y, иначе они будут равняться 0.
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coords(self):
        return self.x, self.y

    @staticmethod   # Не имеет доступа ни к атрибутам класса, ни к атрибутам его экземпляра.
    # Сервисная функция.
    # Делают для того что функция связана с самой тематикой класса.
    def norm2(x, y):
        return x * x + y * y

print(Vector.validate(5)) # Вызываем метод класса validate, со значением 5. и если по условию 5 попадает в диапазон
# атрибутов класса, то он возвращает TRUE, иначе вернет False.
print(Vector.validate(1001)) # <-- А вот здесь не вошли в диапазон аргументов.

print(f'{Vector.norm2(5, 6)} <-- Отработал статический метод.')
# ---------------------------------------- #
v = Vector(1, 2000) # Создание экземпляра класса.
res = Vector.get_coords(v)
print(res)

v = Vector(1, 2)   # Создание экземпляра класса.
res = Vector.get_coords(v)
print(res)





# Механизм инкапсуляции
# attribute (без одного или двух подчеркиваний вначале) - Публичное свойство (Public)
# _attribute (c одним подчеркиванием) - режим доступа (protected)(служит для обращения внутри класса и во
#     всех его дочерних классах) Нижнее подчеркивание не ограничивает в использование, оно только сигнализируют
#     программисту об использование этого свойства в не класса...
# __attribute (с двумя подчеркиваниями) - режим доступа (private)(служит для обращения только внутри класса)


# Пример работы в режиме доступа Private.
class Point:
    def __init__(self, x = 0, y =0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y): # Запускаем проверку
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x): # Приватный метод.
        return type(x) in (int, float) # Выполняем проверку.

    # Сеттеры и гетеры или интерфейсные методы.
    def set_coords(self, x, y): # <-- Сеттер.
        if self.__check_value(x) and self.__check_value(y): # Запускаем проверку
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами.')

    def get_coords(self): # <- Геттер.
        return self.__x, self.__y # Возвращаем координаты в виде кортежа

pt = Point(1, 2) # Создаем экземпляр класса.
# print(pt.__y, pt.__y) # <-- Таким способом обращаться нельзя.
pt.set_coords(10, 20) # <-- Внутри класса к таким атрибутам можно обращаться.
print(pt.get_coords()) # <-- Возвращаем значения

print(dir(pt)) # ['_Point__check_value', '_Point__x', '_Point__y', '__class__' ...}]
# _Point__x and _Point__y <-- Кодовые имена которые находятся в экземпляре класса
print(pt._Point__x) # <-- Так делать не рекомендуется...

# Чтобы сильней защитить доступ надо установить модуль accessif
# from accessif import private, protected

from string import ascii_letters # Модуль содержит набор все латинские буквы.

class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper() # Делаем буквы заглавными.

    def __init__(self, fio, old, ps, weight):

        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_ps(ps)
        self.verify_weight(weight)

        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight

    # проверка имени, фамилии, отчества.
    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО - должно быть строкой!')

        f = fio.split() # Разделяем ФИО на три слова (пробел получается разделитель)
        if len(f) != 3: # Если не три слова
            raise  TypeError('Неверный формат записи.')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('В ФИО должен быть хотя бы один символ.')
            # Проверка, чтобы ФИО содержало только допустимые символы.
            if len(s.strip(letters)) != 0: # если ФИО содержит только разрешенные символы, то
                # strip их удалит, а если есть не разрешенные символы, то он их подсчитает.
                raise TypeError('В ФИО можно использовать только буквенные символы и дефис.')

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old <14 or old > 120:
            raise TypeError('Возраст должен быть в диапазоне [14; 100]')

    @ classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError('Вес должен быть вещественным числом и от 20 и выше.')

    @ classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError('Паспорт должен быть строкой.')

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('Неверный формат паспорта.')

        for p in s:
            if not p.isdigit():
                raise TypeError('Серия и номер паспорта должны быть числами')


    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps

p = Person('Сухомлинова Мария Павловна', 18, '1234 567890', 55.0)
# p.old = 33
p.passport = '4321 098765'
# print(p.__dict__)
#

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self): # <-- Геттер (Возвращает закрытое приватное свойство)
        return self.__old

    @old.setter
    def old(self, old): # <-- Сеттер (Присваивать приватному свойству новое значение)
        self.__old = old

    @old.deleter
    def old(self): # <-- Делитер
        del self.__old


    # old = property(get_old, set_old) # <- Свойства property (если обращаемся через него, то изначально вызывается
    # Свойство get_old, а если записываем в него данные или изменяем то вызывается свойство set_old).
    # Если в классе есть свойство property, то в первую очередь вызывается он.
# ---------------------------------------- #
# Пример работы свойства property.
p = Person('Sergey', 20)
# del p.old # <-- пример работы делитера.
p.old = 5
print(p.__dict__)

from typing import List

class Person:
    """Базовый класс Человек"""

    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    def shout(self):
        print("Я - Человек")

class Employee(Person):
    """Работник. Дочерний класс от Person"""

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.__salary = 20000

    def get_salary(self) -> int:
        return self.__salary

    def shout(self):
        print("Я - работник")

class Parent(Person):
    """Родитель. Дочерний класс от Person"""

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.__kids = ['Tom', 'Jerry']

    def get_kids(self) -> list[str]:
        return self.__kids

    # def shout(self):
    #     print("Я - родитель")

class Citizen(Parent, Employee):
    """Житель - является и родителем и работником"""
    # def shout(self):
    #     print("Я - работник")


my_citizen = Citizen(name='Anton', age=30)
print(my_citizen.get_salary())
print(my_citizen.get_kids())
my_citizen.shout()
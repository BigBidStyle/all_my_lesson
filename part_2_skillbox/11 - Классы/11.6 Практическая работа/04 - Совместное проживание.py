"""Задача 5. Совместное проживание.
Что нужно сделать.
Чтобы понять, стоит ли ему жить с кем-то или лучше остаться в гордом одиночестве, Артём решил провести необычное
исследование. Для этого он реализовал модель человека и модель дома.

Человек может (должны быть такие методы):

Есть (+ сытость, − еда);
работать (− сытость, + деньги);
играть (− сытость);
ходить в магазин за едой (+ еда, − деньги);

прожить один день (выбирает одно действие согласно описанному ниже приоритету и выполняет его).
У человека есть (должны быть такие атрибуты):

Имя,
степень сытости (изначально 50),

дом.
В доме есть:

Холодильник с едой (изначально 50 еды),
тумбочка с деньгами (изначально 0 денег).
Если сытость человека становится меньше нуля, человек умирает.

Логика действий человека определяется следующим образом:

Генерируется число кубика от 1 до 6.

Если сытость < 20, то нужно поесть.
Иначе, если еды в доме < 10, то сходить в магазин.
Иначе, если денег в доме < 50, то работать.

Иначе, если кубик равен 1, то работать.
Иначе, если кубик равен 2, то поесть.

Иначе играть.

По такой логике эксперимента человеку надо прожить 365 дней.

Реализуйте такую программу и создайте двух людей, живущих в одном доме. Проверьте работу программы несколько раз. """

print('Решение задачи № 4 (Совместное проживание)')
import random

class Action:
    day_live = 0  # Переменная сколько дней прожито в доме.
    end = False

    def number(self, index):
        drawn_number = random.randint(1, 6)
        print(f'Для {people[index].name} сгенерировано число: {drawn_number}, значит ', end="")
        if drawn_number == 1:
            self.work(index)
        elif drawn_number == 2:
            self.eat(index)
        else:
            self.play(index)

    def info_house(self, index):
        if house.food <= 10:
            print('Мало еды в доме', end=' ')
            self.shop(index)
        elif house.money <= 50:
            print('Мало денег в доме', end=' ')
            self.work(index)
        else:
            self.number(index)

    def info_lodger(self, index):
        if people[index].satiety == 0:
            print(f'{people[index].name} покинул игру! :(')
            Action.end = True
        elif people[index].satiety <= 20:
            self.eat(index)

        else:
            print(f'{people[index].name} имеет {people[index].satiety} сытости.')
            self.info_house(index)

    def eat(self, index):
        print('надо покушать.') # + сытость, − еда
        people[index].satiety += 1
        house.food -= 1
        print(f'{house.food} <-- еды в доме')

    def work(self,index): # работать (− сытость, + деньги);
        print('надо поработать.')
        people[index].satiety -= 1
        house.money += 1
        print(f'{house.money} <-- Денег в доме' )

    def shop(self, index):  # + еда, − деньги
        print('пошел в магазин.')
        house.food += 1
        house.money -= 1
        print(f'{house.money} <-- Денег в доме' )
        print(f'{house.food} <-- еды в доме')


    def play(self, index): # играть (− сытость);
        print('надо поиграть.')
        people[index].satiety -= 1



    def enum_action(self):
        while not self.end or self.day_live != 365:
            for index in range(0, 2):
                self.info_lodger(index)
            self.day_live += 1
            print(f'Закончился День {self.day_live}')
            if self.day_live == 365:
               self.end = True
        else:
            print('Жильцы прожили вместе год!!!')

# endregion class Action.

class People:
    def __init__(self, index):
            self.name = input(f'Введите имя для {index}-го игрока: ')
            self.satiety = 50 # Сытость игрока.

class House:
    food = 50   # Еды в доме.
    money = 0   # Денег в доме.

people = [] # Создаем список людей.
house = House() # Создаем атрибут класса House.
[people.append(People(num)) for num in range(1, 3)] # Создаем атрибуты людей.
test_live = Action()
test_live.enum_action()



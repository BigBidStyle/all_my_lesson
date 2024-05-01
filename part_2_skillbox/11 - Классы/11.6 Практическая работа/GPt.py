print('Решение задачи № 4 (Совместное проживание)')
import random

class Action:
    def __init__(self, people, house):
        self.people = people
        self.house = house

    def eat(self, index):  # ходить в магазин за едой (+ еда, − деньги);
        if self.house.food >= 10:
            self.house.food -= 10
            self.people[index].satiety += 20
            print(f'{self.people[index].name} поел(а).')
        else:
            print('В доме не хватает еды!')

    def work(self, index): # работать (− сытость, + деньги);
        if self.people[index].satiety >= 10:
            self.people[index].satiety -= 10
            self.house.money += 50
            print(f'{self.people[index].name} поработал(а).')
        else:
            print(f'{self.people[index].name} слишком голоден(а) для работы!')

    def shop(self, index):  # + еда, − деньги
        if self.house.money >= 50:
            self.house.money -= 50
            self.house.food += 50
            print(f'{self.people[index].name} сходил(а) в магазин.')
        else:
            print('В доме не хватает денег!')

    def play(self, index): # играть (− сытость);
        if self.people[index].satiety >= 10:
            self.people[index].satiety -= 10
            print(f'{self.people[index].name} поиграл(а).')
        else:
            print(f'{self.people[index].name} слишком голоден(а) для игры!')

    def enum_action(self):
        for index in range(len(self.people)):
            drawn_number = random.randint(1, 6)
            print(f'Для {self.people[index].name} сгенерировано число: {drawn_number}, значит ', end="")
            if self.people[index].satiety < 20:
                self.eat(index)
            elif self.house.food < 10:
                self.shop(index)
            elif self.house.money < 50:
                self.work(index)
            elif drawn_number == 1:
                self.work(index)
            elif drawn_number == 2:
                self.eat(index)
            else:
                self.play(index)

class People:
    def __init__(self, index):
        self.name = input(f'Введите имя {index}-го жильца: ')
        self.satiety = 50

class House:
    def __init__(self):
        self.food = 50
        self.money = 0

people = []
house = House()
for index in range(1, 3):
    people.append(People(index))

actions = Action(people, house)
for _ in range(365):
    actions.enum_action()
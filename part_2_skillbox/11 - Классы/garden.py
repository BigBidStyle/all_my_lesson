class Potato:   # Класс под названием картошка.
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'} # Статический атрибут (Стадия зрелости картошки)

    def __init__(self, index): # Инициализатор класса.
        self.index = index # Номер грядки.
        self.state = 0  # Стадия роста картошки по умолчанию равно нулю.

    def grow(self): # Метод роста картошки.
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self): # Проверяем каждую картошку.
        if self.state == 3:
            return True
        return  False

    def print_state(self): # Метод вывода сообщения о стадии роста картошки.
        print('Картошка {} сейчас {}'.format(self.index, Potato.states[self.state]))


class PotatoGarden: # Класс под названием грядка.
    def __init__(self, count): # Инициализатор класса.
        self.potatoes = [Potato(index) for index in range (1, count + 1)] # Инициализируем грядки.

    def grow_all(self): # Метод, который взращивает всю картошку на грядке.
        print('Картошка прорастает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self): # Проверка созрела ли вся поляна.
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка еще не созрела!\n')
        else:
            print('\nВся картошка созрела.')

res = PotatoGarden(5)

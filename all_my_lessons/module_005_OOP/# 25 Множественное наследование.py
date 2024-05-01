class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print('Init Goods')
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name},{self.weight},{self.price}')

class MixinLog:
    ID = 0
    def __init__(self):
        print('Init MixinLog')
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00")

class Notebook(Goods, MixinLog):
    pass

n = Notebook('Acer', 1.5, 30000)
n.print_info()
n.save_sell_log()
print(Notebook.__mro__) # Список классов, который обходится при поиске того или иного продукта
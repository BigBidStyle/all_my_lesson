class DataBass:
    # Паттерн Singleton (Делает так, что бы в программе существовал, ровно один экземпляр класса)
    __instance = None   # Атрибут класса. Он будет ссылкой на экземпляр класса.

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None: # Проверяем атрибут __instance, и если он принимает значение None
            cls.__instance = super().__new__(cls) # Тогда этому атрибуту присвоим адрес нового созданного объекта.
        return cls.__instance

    def __del__(self):  # Финализатор
        DataBass.__instance = None  # Вновь присваиваем атрибуту __instance значение None.

    def __init__(self, user, psw, port): # Магический метод __init__ для инициализации экземпляра класса.
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Соединение с БД: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Закрытие соединение с БД.')

    def read(self):
        return 'Данные из БД.'

    def write(self, data):
        print(f'Запись в БД {data}')

db = DataBass('root', '1234', '80')
db2 = DataBass('root2', '5678', '40')

print(id(db) == id(db2))  # Проверка


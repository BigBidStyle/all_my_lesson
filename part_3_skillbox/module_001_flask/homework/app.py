import datetime
import random

from flask import Flask     # Импортируем модуль.
app = Flask(__name__)   # <-- Создаем экземпляр класса.(Указываем его имя)

@app.route('/hello_world')
def hello_world():
    return f'Привет, мир!'

cars = ("Chevrolet", "Renault", "Ford", "Lada=")
@app.route('/car')
def car():
    global cars
    return f'{random.choice(cars)}'

cats = ('корниш-рекс', 'русская голубая', 'шотландская', 'вислоухая', 'мейн-кун', 'манчкин')
@app.route('/cats')
def cat():
    global cats
    return f'{random.choice(cats)}'


@app.route('/get_time/now')
def time_now():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f'Точное время: {current_time}'


@app.route('/get_time/future')
def time_future():
    current_time_after_hour = (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime('%H:%M:%S')
    return f'Точное время через час будет: {current_time_after_hour}'


@app.route('/get_random_word')
def random_word():
    return f'Не было времени на решение...'


count = 0   # Объявляем переменную.
@app.route('/counter')   # <-- url_routing (маршрутизация запроса)
def counter():  # <-- end_point точка подключения к браузеру.
    global count    # Глобальной переменной...
    count += 1  # ..прибавляем единицу.
    return f'Число открытий страницы: {count}'  # <-- Вывод содержимого в браузере.

if __name__ == "__main__":  # <-- Условии запускается не посредственно на локальном компьютере.
    app.run(debug=True) # <-- Запуск локального веб-сервера.
    # В качестве параметра передаем значение...
    # Debug = true --> Для того что в браузере показывались все ошибки при разработке сайта. По окончании написания
    # сайта следует перевести флаг на False, это для того случайные ошибки пользователь не видел.

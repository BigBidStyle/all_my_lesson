import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/hello')  # <-- url_routing (маршрутизация запроса)
def test_function():  # <-- end_point точка подключения к браузеру.
    now = datetime.datetime.now().utcnow()
    return f'Это новая тестовая страничка, ответ сгенерирован в {now}'  # <-- Вывод содержимого в браузере.

@app.route('/hello_world')  # <-- url_routing (маршрутизация запроса)
def hello_word():  # <-- end_point точка подключения к браузеру.
    return f'Привет BigBid'  # <-- Вывод содержимого в браузере.

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
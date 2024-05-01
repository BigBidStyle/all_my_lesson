import os.path
from flask import Flask

app = Flask(__name__)


# ----------------------------------------------------- #
@app.route('/hello/<username>')
def hello_world(username):
    return f'Привет, {username}'


# ----------------------------------------------------- #
@app.route('/even/<int:number>')
def even(number: int):
    if number % 2:
        res = '<b>нечетное</b> и выделяется жирным шрифтом'  # b<-- bold (жирный)
    else:
        res = 'Четное'
    return f'Число {number} - {res}.'


# ----------------------------------------------------- #
@app.route('/compare/<int:number_1>/<int:number_2>')
def compare(number_1, number_2):
    if number_1 < number_2:
        res = 'меньше'
    elif number_1 > number_2:
        res = 'больше'
    else:
        res = 'равны'
    return f'<h3>Число {number_1} {res} {number_2}</h3>'


@app.route('/check_exists/<path:file_name>')
def check_exists(file_name):
    """
     Проверка, существование файла с относительным путем в файловой системе.
     :param file_name: Относительный путь
     :return: http ответ.
     """
    file_exists = os.path.exists(file_name)
    result = 'существует' if file_exists else 'не существует'
    status_code = 200 if file_exists else 404
    return f'<i>File {file_name} - {result}. Status code: {status_code}</i>'


# # ----------------------------------------------------- #
if __name__ == '__main__':
    app.run(debug=True, port=5555)

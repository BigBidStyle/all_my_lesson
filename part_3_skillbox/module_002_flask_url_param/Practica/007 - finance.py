import datetime

from flask import Flask

app = Flask(__name__)
storage = {}

@app.route('/add/<date>/<int:number>') # <-- сохранение информации о совершённой в рублях трате за какой-то день.
def add(date: str, number: int):
    year = int(date[:4])
    print(year)
    month = int(date[4:6])
    day = int(date[6:8])
    if check_date(year, month, day):
        storage.setdefault(year, {}).setdefault(month, 0)
        storage[year][month] += number
        return f'Данные записаны! {storage}'
    else:
        return f'Введенная не корректная дата'


@app.route('/calculate/<int:year>') # <-- получение суммарных трат за указанный год.
def calculate_year(year: int):
    sum_expense = 0
    try:
        for expense in storage[year].values():

            sum_expense += expense
        return f'Расходы за {year} год, составили {sum_expense} руб.'
    except KeyError:
        return f'Нет расходов по {year} году.'


@app.route('/calculate/<int:year>/<int:month>') # <-- получение суммарных трат за указанные год и месяц.
def calculate_month(year: int, month:int ):
    try:
        return f'Расходы за {year} год и {month} месяц составили {storage[year][month]}'
    except KeyError:
        return f'Нет расходов по {year} году и {month} месяцу.'


def check_date(year:int, month:int, day:int) -> bool:
    """Проверка даты"""
    try:
        datetime.datetime(year, month, day)
        res_date = True
    except ValueError:
        res_date = False
    return res_date

if __name__ == "__main__":
    app.run(debug=True)
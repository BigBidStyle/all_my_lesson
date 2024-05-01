# Первый вариант.
from flask import Flask
from datetime import datetime

weekday = int(datetime.today().weekday())
weekdays_list = ('воскресенья', 'понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы')

app = Flask("__name__")

@app.route('/good_days/<username>')
def good_days(username: str) -> str:
    return f'<i>{username} Привет, {username}. Хорошей(го) {weekdays_list[weekday]}<i>'

if __name__ == "__main__":
    app.run(debug=True, port=5545)

# Второй вариант с методом Jinja.



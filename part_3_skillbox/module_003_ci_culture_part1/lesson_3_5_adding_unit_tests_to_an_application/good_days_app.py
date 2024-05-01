from flask import Flask
from datetime import datetime

weekdays_list = ('Хорошего воскресенья',
                 'Хорошего понедельника',
                 'Хорошего вторника',
                 'Хорошей среды',
                 'Хорошего четверга',
                 'Хорошей пятницы',
                 'Хорошей субботы')

app = Flask("__name_")

@app.route('/good_days/<username>')
def good_days(username: str) -> str:
    weekday = int(datetime.today().weekday())
    return f'{username} Привет, {username}. {weekdays_list[weekday]}'

if __name__ == "__main__":
    app.run(debug=True)

# Второй вариант с методом Jinja.

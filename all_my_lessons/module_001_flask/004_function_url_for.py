from flask import Flask, render_template, url_for

app = Flask("__name_")
menu = ["Установка", "Первое приложение", "Обратная связь"]

@app.route("/")
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)

@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about.html', title="О сайте", menu=menu)

@app.route('/profile/<username>')
def profile(username):
    return f'<i> Пользователь: {username}</i>'

with app.test_request_context(): # тест контекстного запроса.
    print(url_for('index'))
    print(url_for('about'))
    print(url_for('profile', username = "WaterWave"))

# if __name__ == "__main__":
#     app.run(debug=True)


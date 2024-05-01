from flask import Flask

app = Flask(__name__)

@app.route("/max_number/<path:numbers>")
def max_number(numbers):
    numbers = numbers.split('/')
    try:
        num_int = [int(x) for x in numbers]
    except ValueError:
        return 'Ошибка, должны быть только числа!'
    return f'Максимальное число: {max(num_int)}'

if __name__ == "__main__":
    app.run(debug=True)


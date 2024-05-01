from flask import Flask
import os
app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

@app.route('/preview/<int:size>/<path:relative_path>')
def preview(size: int, relative_path: str):
    abs_path = os.path.join(BASE_DIR, relative_path)
    with open(abs_path, 'r') as file:
        result_text = file.read(size)
        result_size = len(result_text)
    return f'<b>{abs_path} </b>{result_size}<br>{result_text}'

if __name__ == "__main__":
    app.run(debug=True)
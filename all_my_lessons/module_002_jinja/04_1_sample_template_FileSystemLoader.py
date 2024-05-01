from jinja2 import Environment, FileSystemLoader # FileSystemLoader <-- Стандартный системный загрузчик.

persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иванушка", "old": 33, "weight": 94.0}
]

file_loader = FileSystemLoader('templates') # Указываем в какой папке хранятся наши шаблоны.
env = Environment(loader=file_loader) # Указываем ссылку на наш загрузчик.
tm = env.get_template('main.html') # Указываем какой шаблон получить.
msg = tm.render(users = persons)
print(msg)
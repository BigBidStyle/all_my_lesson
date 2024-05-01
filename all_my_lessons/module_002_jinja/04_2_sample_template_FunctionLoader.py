from jinja2 import Environment, FunctionLoader # FileSystemLoader <-- Стандартный системный загрузчик.

persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иванушка", "old": 33, "weight": 94.0}
]

def load_tpl(path):
    if path == "index":
        return '''Имя {{u.name}}, возраст {{u.old}}.'''
    else:
        return '''Данные: {{u}}'''

file_loader = FunctionLoader(load_tpl) # Указываем где хранятся наши шаблоны.
env = Environment(loader=file_loader) # Указываем ссылку на наш загрузчик.
tm = env.get_template('index') # Указываем какой шаблон получить.
msg = tm.render(u = persons[0])
print(msg)
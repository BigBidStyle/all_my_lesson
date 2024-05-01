from jinja2 import Template
# region Применение фильтров.

cars = [
    {'model': 'Ауди', 'price': 23000},
    {'model': 'Шкода', 'price': 17300},
    {'model': 'Вольво', 'price': 44300},
    {'model': 'Фольксваген', 'price': 21300}]

tpl = "Суммарная цена автомобилей: {{ cs|sum(attribute='price', start = 0) }}" # <-- Шаблон
tm = Template(tpl)
msg = tm.render(cs = cars)
print(msg)

# ----------------------------------------------- #
tpl = "Максимальная цена у автомобиля: {{ (cs|max(attribute='price')).model }}"
tm = Template(tpl)
msg = tm.render(cs = cars)
print(msg)

# ----------------------------------------------- #
tpl = "Рандомный автомобиль: {{ (cs|random).model }}"
tm = Template(tpl)
msg = tm.render(cs = cars)
print(msg)

# ----------------------------------------------- #
tpl = "Меняем буквы на заглавные: {{ cs|replace('o', 'O') }}"
tm = Template(tpl)
msg = tm.render(cs = cars)
print(msg)
# endregion Применение фильтров.
#------------------------------------------------------------------------------- #
print('# ----------------- #')
print("Применение фильтров")
persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иванушка", "old": 33, "weight": 94.0}
]

# tpl = '''
# {%- for u in users -% }
# {% filter upper %} {{u.name}} {% endfilter %}
# {% endfor -%}
# '''



tm = Template(tpl)
msg = tm.render(users=persons)
print(msg)
# ----------------------------------------------- #
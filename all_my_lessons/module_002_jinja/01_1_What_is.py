from jinja2 import Template  # Jinja <-- Модуль для обработки шаблонов в Python.
# ---------------------------------------- #
name = "BigBid"
age = [24, 1]

# Пример 1
tm = Template("Привет! Мне {{age[0]}} года и зовут меня {{name}}.")  # <-- Шаблон
msg = tm.render(name=name, age=age)
print(msg)
# ---------------------------------------- #
# Пример 2
tm = Template("Привет! Мне {{age*2}} года и зовут меня {{name.upper()}}.")
msg2 = tm.render(name=name, age=age)
print(msg2)
# ---------------------------------------- #
# Пример 3
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

per = Person("BigBidStyle", 15)
tm = Template("Привет! Мне {{p.age}} года и зовут меня {{p.name}}.")
msg3 = tm.render(p=per)
print(msg3)
# ---------------------------------------- #
# Пример 4
per = {"name": "Алеша", "age": 34}
tm = Template("Привет! Мне {{p.age}} года и зовут меня {{p.name}}.")
msg4 = tm.render(p=per)
print(msg4)
# ---------------------------------------- #
# Пример 5
per = {"name": "Алеша", "age": 34}
tm = Template("Привет! Мне {{p['age']}} года и зовут меня {{p['name']}}.")
msg5 = tm.render(p=per)
print(msg5)
# ---------------------------------------- #

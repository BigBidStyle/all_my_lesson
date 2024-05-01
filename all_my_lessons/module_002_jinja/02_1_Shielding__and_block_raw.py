from html import escape
from jinja2 import Template

# Экранирование. Пример 1
data = '''{% raw %}Модуль Jinja вместо
определения {{ name }}
подставляет соответствующие значение{% endraw %}.'''

tp = Template(data)
msg = tp.render(name="Федор")

print(msg)
# -------------------------------------------------- #
# Экранирование. Пример 2
link = '''В HTML-документе ссылки определяются так
<a href="#">Ссылка</a>'''

tm = Template("{{ link | e }}")  # Установлен флаг на экранирование.
msg2 = tm.render(link=link)
print(msg2)  # &lt;a href=&#34;#&#34;&gt;Ссылка&lt;/a&gt;

# -------------------------------------------------- #
# Экранирование. Пример 3 Самый быстрый и в одну строчку.
link = '''В HTML-документе ссылки определяются так
<a href="#">Ссылка</a>'''

msg3 = escape(link)
print(msg3)  # &lt;a href=&#34;#&#34;&gt;Ссылка&lt;/a&gt;

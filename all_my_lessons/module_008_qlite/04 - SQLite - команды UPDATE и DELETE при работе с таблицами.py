# UPDATE - Изменение записей в таблице.
# UPDATE имя-таблицы SET имя_столбца = новое_значение WHERE условие.

# DELETE - Удаление записей из таблицы.

import sqlite3 as sq
# con = sq.connect('saper.db')    # Соединение с базой данных.
# cur = con.cursor()  # Запрос в базу данных.
# con.close() # Закрытие базы данных.

with sq.connect('saper.db') as con:
    cur = con.cursor()  # Запрос в базу данных.
    cur.execute('DROP TABLE IF EXISTS users')   # Если существует таблица users, то удалить ее.

    # Вызвать метод execute, в который передается SQL запрос для работы с базой данных.
    cur.execute(""" CREATE TABLE IF NOT EXISTS users 
    (user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL, sex INTEGER NOT NULL DEFAULT 1, old INTEGER, score INTEGER)""")

    cur.execute("INSERT INTO users (name, old, score) VALUES('Михаил', 19, 1000)")
    cur.execute("INSERT INTO users (name, old, score) VALUES('Федор', 32, 200)")
    cur.execute("INSERT INTO users (name, old, score) VALUES('Николай', 22, 500)")

    cur.execute("UPDATE users SET score = score + 500  WHERE sex = 2")
    cur.execute("UPDATE users SET score = score + 555  WHERE name LIKE 'Федор'")
    cur.execute("UPDATE users SET score = score + 100  WHERE name LIKE 'М%'") # М% Начинается на м.
    cur.execute("UPDATE users SET score = score + 100  WHERE name LIKE 'В_р%'")

    # cur.execute("DELETE FROM users WHERE user_id IN(2,6)")

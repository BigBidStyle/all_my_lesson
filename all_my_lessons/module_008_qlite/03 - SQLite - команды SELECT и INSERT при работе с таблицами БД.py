# INSERT Добавление записи в таблицу.
# INSERT INTO <table name> (<column_name_1>, ,column_name_2>, ...) VALUES(<value1>,<value2>,...).
# INSERT INTO <table_name> VALUES(<value1>, <value2>, ...).

import sqlite3 as sq
with sq.connect('saper.db') as con: # Соединение с базой данных.
    cur = con.cursor()  # Запрос в базу данных.

    cur.execute('DROP TABLE IF EXISTS users')   # Если существует таблица users, то удалить ее.

    # Вызвать метод execute, в который передается SQL запрос для работы с базой данных.
    cur.execute(""" CREATE TABLE IF NOT EXISTS users 
    (user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL, sex INTEGER NOT NULL DEFAULT 1, old INTEGER, score INTEGER)""")

    cur.execute("INSERT INTO users (name, old, score) VALUES('Михаил', 19, 1000)")
    cur.execute("INSERT INTO users (name, old, score) VALUES('Федор', 32, 200)")
    cur.execute("INSERT INTO users (name, old, score) VALUES('Николай', 22, 500)")

    cur.execute('SELECT * FROM users')
    cur.execute('SELECT rowid, * FROM users')   # Показать колонку ID и выбрать все поля из таблицы users
    print(cur.fetchall())   # Получение результата из SQL запроса.

    cur.execute('SELECT * FROM users WHERE score < 1000')
    print(cur.fetchall())   # Получение результата из SQL запроса.
    # cur.execute('SELECT* FROM users WHERE score BETWEEN 500 AND 1000')

    # Приоритеты not, and, or.
    # ORDER BY ... сортировки списка по возрастанию.
    # ORDER BY ASC ... Явная сортировка по возрастанию.
    # ORDER BY ... DESC сортировки списка по убыванию.
    # LIMIT Сколько записей будем выбирать из выборки. LIMIT 5 Взято пять записей.
    # LIMIT 2, 5 Пропустить две записи и взять 5

    # cur.fetchall() Получение результата из SQL запроса.

    cur.execute('SELECT name, old, score FROM users')
    result_1 = cur.fetchmany(2)     # Возвращает число записей не более size.
    result_2 = cur.fetchone()   # Возвращает первую запись.
    print('\n', result_1)
    print(result_2)
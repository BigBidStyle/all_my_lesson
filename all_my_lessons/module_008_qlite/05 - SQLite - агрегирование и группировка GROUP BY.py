# Python SQLite 3 # 5: агрегирование и группировка GROUP BY
import sqlite3 as sq

with sq.connect('saper.db') as con:     # Соединение с базой данных.
    cur = con.cursor()  # Запрос в базу данных.
    cur.execute('DROP TABLE IF EXISTS games')   # Если существует таблица games, то удалить ее.

    # Вызвать метод execute, в который передается SQL запрос для работы с базой данных.
    cur.execute(""" CREATE TABLE IF NOT EXISTS games 
    (user_id INTEGER, score INTEGER, time INTEGER)""")

    cur.execute("INSERT INTO games (user_id, score, time) VALUES(1, 200, 100000)")
    cur.execute("INSERT INTO games (user_id, score, time) VALUES(1, 300, 110010)")
    cur.execute("INSERT INTO games (user_id, score, time) VALUES(2, 500, 100010)")
    cur.execute("INSERT INTO games (user_id, score, time) VALUES(1, 400, 201034)")
    cur.execute("INSERT INTO games (user_id, score, time) VALUES(3, 100, 200010)")
    cur.execute("INSERT INTO games (user_id, score, time) VALUES(2, 600, 210000)")
    cur.execute("INSERT INTO games (user_id, score, time) VALUES(2, 300, 210010)")
    # ---------------------------------------- #
    cur.execute("SELECT count(user_id) as count FROM games WHERE user_id = 1")
    # Получение уникального значения. (DISTINCT)
    cur.execute("SELECT count(DISTINCT user_id) as count FROM games")
    # Получение уникальных ID.
    cur.execute("SELECT DISTINCT user_id as count FROM games")
    cur.execute("SELECT SUM(score) as sum_score FROM games WHERE user_id = 1")
    cur.execute("SELECT MAX(score) as sum_score FROM games WHERE user_id = 1")
    # ---------------------------------------- #
    # Группировка записей в выборке.
    cur.execute("SELECT user_id, sum(score) as sum FROM games WHERE score > 100 GROUP BY user_id ORDER BY sum DESC")
    # ---------------------------------------- #
    print(cur.fetchall())   # Получение результата из SQL запроса.

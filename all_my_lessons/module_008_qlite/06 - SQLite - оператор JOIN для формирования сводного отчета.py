# Python SQLite 3 #6: оператор JOIN для формирования сводного отчета
import sqlite3 as sq    # Подключение модуля SQLite 3.
with sq.connect('saper.db') as con:     # Соединение с базой данных.
    cur = con.cursor()  # Запрос в базу данных.
    # Сводный отчет (Пользовательская выборка)
    cur.execute("SELECT name, sex, games.score FROM games JOIN users ON games.user_id = users.rowid")
    print(cur.fetchall())

    # Простое объединение двух таблиц.
    cur.execute("SELECT name, sex, games.score FROM users, games")
    print(cur.fetchall())

    cur.execute("SELECT name, sex, sum(games.score) as score "
                "FROM games "
                "JOIN users ON games.user_id = users.rowid "
                "GROUP BY user_id ORDER BY score DESC")
    print(cur.fetchall())
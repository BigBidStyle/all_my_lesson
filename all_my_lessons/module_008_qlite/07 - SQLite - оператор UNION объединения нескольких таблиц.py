# Python SQLite 3 # 5: Union - объединение таблиц.
import sqlite3 as sq

with sq.connect('table.db') as con:     # Соединение с базой данных.
    cur = con.cursor()  # Запрос в базу данных.

    cur.execute('DROP TABLE IF EXISTS tab1')   # Если существует таблица games, то удалить ее.
    cur.execute(""" CREATE TABLE IF NOT EXISTS tab1 (score INTEGER, 'from' TEXT)""")
    cur.execute("INSERT INTO tab1 VALUES(100, 'tab1')")
    cur.execute("INSERT INTO tab1 VALUES(200, 'tab1')")
    cur.execute("INSERT INTO tab1 VALUES(300, 'tab1')")

    cur.execute('DROP TABLE IF EXISTS tab2')
    cur.execute(""" CREATE TABLE IF NOT EXISTS tab2 (val INTEGER, type TEXT)""")
    cur.execute("INSERT INTO tab2 VALUES(200, 'tab2')")
    cur.execute("INSERT INTO tab2 VALUES(300, 'tab2')")
    cur.execute("INSERT INTO tab2 VALUES(400, 'tab2')")

    cur.execute("SELECT score, 'from' FROM tab1 UNION SELECT val, type FROM tab2 ORDER BY 'from'")
    print(cur.fetchall())
    # [(100, 'from'), (200, 'from'), (200, 'tab2'), (300, 'from'), (300, 'tab2'), (400, 'tab2')]

    cur.execute("SELECT score FROM tab1 UNION SELECT val FROM tab2")
    print(cur.fetchall())
    # [(100,), (200,), (300,), (400,)]
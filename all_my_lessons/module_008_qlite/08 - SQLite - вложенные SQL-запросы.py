# Python SQLite 3 # 08 вложенные SQL-запросы.mp4

# Python SQLite 3 # 5: Union - объединение таблиц.
import sqlite3 as sq # Импортируем модуль.

with sq.connect('lessons.db') as con:     # Соединение с базой данных.
    cur = con.cursor()  # Запрос в базу данных.

    cur.execute('DROP TABLE IF EXISTS students')   # Если существует таблица games, то удалить ее.
    cur.execute(""" CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT, sex INTEGER, old INTEGER )""")
    cur.execute("INSERT INTO students VALUES(1, 'Коля', 1, 17)")
    cur.execute("INSERT INTO students VALUES(2, 'Маша', 2, 18)")
    cur.execute("INSERT INTO students VALUES(1, 'Вася', 1, 19)")
    cur.execute("INSERT INTO students VALUES(2, 'Даша', 2, 17)")

    cur.execute('DROP TABLE IF EXISTS marks')
    cur.execute(""" CREATE TABLE IF NOT EXISTS marks (id INTEGER, subject TEXT, mark INTEGER)""")
    cur.execute("INSERT INTO marks VALUES(1, 'Си', 4)")
    cur.execute("INSERT INTO marks VALUES(2, 'Си', 3)")
    cur.execute("INSERT INTO marks VALUES(3, 'Си', 4)")
    cur.execute("INSERT INTO marks VALUES(1, 'Физика', 3)")
    cur.execute("INSERT INTO marks VALUES(3, 'Физика', 5)")
    cur.execute("INSERT INTO marks VALUES(1, 'Вышка', 5)")
    cur.execute("INSERT INTO marks VALUES(2, 'Вышка', 4)")
    cur.execute("INSERT INTO marks VALUES(1, 'Физ-ра', 5)")
    cur.execute("INSERT INTO marks VALUES(2, 'Химия', 3)")
    cur.execute("INSERT INTO marks VALUES(3, 'Черчение', 5)")

    cur.execute("SELECT mark FROM marks WHERE id = 2 AND subject = 'Си'")
    cur.fetchall() #'<-- Оценка полученная Марией по языку Си')

    cur.execute("""SELECT name, subject, mark FROM marks 
                join students ON students.rowid = marks.id
                WHERE mark > () AND subject LIKE 'Си'""")
    print(cur.fetchall())

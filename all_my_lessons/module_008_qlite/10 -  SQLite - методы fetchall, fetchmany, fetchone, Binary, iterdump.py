# Python SQLite # 10 методы fetchall, fetchmany, fetchone, Binary, iterdump

import sqlite3 as sq
cars = [("Audio", 52642),
        ("Mercedes", 57127),
        ("BMV", 90154),
        ("Volvo", 29000),
        ("Bentley", 350000)]


with sq.connect('cars.db') as con:
    con.row_factory = sq.Row # Переделываем в список
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS cars')
    cur.execute("""
        CREATE TABLE IF NOT EXISTS cars 
        (car_id INTEGER PRIMARY KEY AUTOINCREMENT, model TEXT, price INTEGER)""")

    cur.executemany('INSERT INTO cars VALUES(NULL, ?, ?)', cars)
    cur.execute('SELECT * FROM cars')
    for result in cur:
        print(result['model'], result['price'])
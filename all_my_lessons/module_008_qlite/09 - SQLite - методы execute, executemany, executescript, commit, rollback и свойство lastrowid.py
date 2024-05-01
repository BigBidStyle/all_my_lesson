import sqlite3 as sq
cars = [("Audio", 52642),
        ("Mercedes", 57127),
        ("BMV", 90154),
        ("Volvo", 29000),
        ("Bentley", 350000)]
con = None
try:
    with sq.connect('cars.db') as con:
        cur = con.cursor()
        cur.execute('DROP TABLE IF EXISTS cars')
        cur.executescript("""
            CREATE TABLE IF NOT EXISTS cars 
            (car_id INTEGER PRIMARY KEY AUTOINCREMENT, model TEXT, price INTEGER);
            CREATE TABLE IF NOT EXISTS cust  
            (name TEXT, tr_in INTEGER, buy INTEGER)""")

        cur.execute('BEGIN')
        cur.executemany('INSERT INTO cars VALUES(NULL, ?, ?)', cars)
        cur.execute('UPDATE cars SET price = :Price WHERE model LIKE "A%"', {'Price' : 0})
        cur.executescript('DELETE FROM cars WHERE model LIKE "M%"; UPDATE cars SET price = price + 1000')

        con.execute('INSERT INTO cars VALUES(NULL, "Запорожец", 1000)')
        last_row_id = cur.lastrowid
        buy_car_id = 2
        cur.execute('INSERT INTO cust VALUES("Федор", ?, ?)', (last_row_id, buy_car_id))
        con.commit() # Сохранение в базу данных всех внесенных изменений.
except sq.Error as error:
    if con: con.rollback() # откатываем все внесенные изменения до изначального состояния.
    print("Ошибка выполнения программы: \n", error)
finally:
    if con: con.close()
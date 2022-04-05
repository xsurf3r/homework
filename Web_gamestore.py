import sqlite3

db = sqlite3.connect('web gamestore.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS store (
    login TEXT,
    password TEXT,
    cash BIGINT
)""")

db.commit()

user_login = input('Login: ')
user_password = input('Password: ')

sql.execute("SELECT login FROM store")
if sql.fetchone() is None:
    sql.execute("INSERT INTO store VALUES ()")
else:
    print('Такая запись уже имеется!')  
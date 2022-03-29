import sqlite3

db=sqlite3.connect("titanicDB.db")

tabulu_nosaukumi = db.execute("""SELECT name * FROM sqlite_schema WHERE type = 'table';""")

rezultats = tabulu_nosaukumi.fetchall()
print (rezultats)
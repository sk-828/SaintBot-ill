import sqlite3
con=sqlite3.connect("charaDB.db")
try:
    con.execute("DROP TABLE if exists chara;")
    con.execute("CREATE TABLE chara (id INTEGER PRIMARY KEY,name TEXT UNIQUE,pass TEXT UNIQUE,guildID INTEGER,autorID INTEGER);")
except sqlite3.IntegrityError:
    con.rollback()
finally:
    con.commit()
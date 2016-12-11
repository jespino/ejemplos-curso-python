import sqlite3

con = sqlite3.connect("ejemplo.db")
cur = con.cursor()
cur.execute("create table if not exists points (x, y)")
cur.execute("DELETE FROM points")

cur.executemany("insert into points values (?, ?)", ((1,2), (3,4), (5,6)))
con.commit()

cur.execute("select * from points where x > :min", {"min": 2})
print cur.fetchall()

from mysql import connector

con = connector.connect(db="pythonavanzado", user="root")
cur = con.cursor()
cur.execute("create table IF NOT EXISTS points (x INT, y INT)")
cur.execute("TRUNCATE points")

cur.executemany("insert into points values (%s, %s)", ((1,2), (3,4), (5,6)))
con.commit()

cur.execute("select * from points where x > %(min)s", {"min": 2})
print cur.fetchall()


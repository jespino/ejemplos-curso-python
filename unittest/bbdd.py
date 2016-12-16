import unittest
import sqlite3


class DBTestCase(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect("ejemplo.db")
        self.cur = self.con.cursor()
        self.cur.execute("create table if not exists points (x, y)")

    def test_insert_select(self):
        self.cur.executemany("insert into points values (?, ?)", ((1,2), (3,4), (5,6)))
        self.con.commit()
        self.cur.execute("select * from points where x > :min", {"min": 2})
        data = self.cur.fetchall()
        self.assertEqual(data[0], (3, 4))
        self.assertEqual(data[1], (5, 6))

    def tearDown(self):
        self.cur.execute("DELETE FROM points")
        self.con.close()


if __name__ == "__main__":
    unittest.main()

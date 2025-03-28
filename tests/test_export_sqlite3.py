import unittest
import sqlite3
import os
import csv

class TestSqliteExport(unittest.TestCase):

    def setUp(self):
        self.db_name = 'test_export.db'
        self.table_name = 'mytable'
        self.csv_file = 'export_sqlite3.csv'

        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute(f'CREATE TABLE IF NOT EXISTS {self.table_name} (id INTEGER, name TEXT)')
        cur.execute(f'INSERT INTO {self.table_name} VALUES (1, "Alice")')
        conn.commit()
        conn.close()

    def test_export_creates_csv(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM {self.table_name}')
        rows = cur.fetchall()

        with open(self.csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([desc[0] for desc in cur.description])
            writer.writerows(rows)

        conn.close()

        self.assertTrue(os.path.exists(self.csv_file))
        with open(self.csv_file, 'r') as f:
            lines = f.readlines()
            self.assertGreater(len(lines), 1)  # header + at least 1 row

    def tearDown(self):
        os.remove(self.db_name)
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)

if __name__ == '__main__':
    unittest.main()

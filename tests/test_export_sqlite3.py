# -----------------------------------------------------------------------------
# csv-db-bridge — Universal Import/Export Toolkit for CSV and Databases
# -----------------------------------------------------------------------------
# Author: Siergej Sobolewski <s.sobolewski@hotmail.com>
# License: GNU General Public License v3.0 (GPL-3.0)
#
# This file is part of csv-db-bridge.
# 
# csv-db-bridge is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# csv-db-bridge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------

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

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

import cx_Oracle
import csv

conn = cx_Oracle.connect('username/password@host:port/sid')
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO table_name (column1, column2, column3) VALUES (:1, :2, :3)",
            (row[0], row[1], row[2])
        )
        cursor.close()

conn.commit()
conn.close()

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

import ibm_db
import csv

dsn = (
    "DRIVER={IBM DB2 ODBC Driver};"
    "DATABASE=my_database;"
    "HOSTNAME=my_hostname;"
    "PORT=50000;"
    "PROTOCOL=TCPIP;"
    "UID=my_username;"
    "PWD=my_password;"
    "SECURITY=SSL;"
)
conn = ibm_db.connect(dsn, "", "")
stmt = ibm_db.exec_immediate(conn, "SELECT * FROM employees")
rows = ibm_db.fetch_assoc(stmt)

with open('employees.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(rows[0].keys())
    for row in rows:
        writer.writerow(row.values())

ibm_db.close(conn)

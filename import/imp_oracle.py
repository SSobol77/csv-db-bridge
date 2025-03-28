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

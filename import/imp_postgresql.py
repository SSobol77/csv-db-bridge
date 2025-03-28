import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myuser",
    password="mypassword"
)
cur = conn.cursor()
cur.execute("SELECT * FROM mytable")
rows = cur.fetchall()
cur.close()
conn.close()

with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([i[0] for i in cur.description])
    for row in rows:
        writer.writerow(row)

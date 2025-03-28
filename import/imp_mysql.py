import mysql.connector
import csv

db = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="mydatabase"
)
cursor = db.cursor()
cursor.execute("SELECT * FROM mytable")
data = cursor.fetchall()

with open('data.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow([i[0] for i in cursor.description])
    for row in data:
        writer.writerow(row)

db.close()

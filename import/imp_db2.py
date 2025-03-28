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

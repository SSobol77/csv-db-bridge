import boto3
import csv

client = boto3.client('rds-data')

response = client.execute_statement(
    secretArn='<secret_arn>',
    database='<database_name>',
    resourceArn='<resource_arn>',
    sql="SELECT * FROM <table_name>"
)
data = response['records']

fieldnames = ['column1', 'column2', 'column3']
with open('data.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow({
            'column1': row[0]['stringValue'],
            'column2': row[1]['stringValue'],
            'column3': row[2]['longValue'],
        })

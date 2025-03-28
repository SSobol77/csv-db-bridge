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

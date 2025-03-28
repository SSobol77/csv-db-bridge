import csv
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']
cursor = collection.find()

with open('data.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age', 'gender'])
    for document in cursor:
        writer.writerow([document['name'], document['age'], document['gender']])

from pymongo import MongoClient
from employee import Employee

client = MongoClient('localhost', 27017)
db = client['mydatabase']
mycol = db['employees']


def add_to_db(item: dict) -> None:
    # {'_id': username, username: EmployeeObj}
    mycol.insert_one(item)


def find_from_db(param: dict) -> dict:
    # query = {'_id': <username>} to search by username ID
    mydoc = mycol.find(param)
    return mydoc


'''
x = mycol.insert_one(mydict)
print(x.inserted_id)

print(client.list_database_names())
print(db.list_collection_names())

mycol = mydb["employees"]

mydb = {
    'John1': {'fname': 'John',
              'lname': 'smith',
              'employID': 1111,
              'minwage': 12,
              'overtime': 14
              }
}

x = mycol.insert_one(mydb)
print(x.inserted_id)

print('collection names:')
print(mydb.list_collection_names())

print('database names:')
print(client.list_database_names())
'''

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ajaysj141:Kuchtohlogkahenge@ineuronprojects.53vs8nv.mongodb.net/?appName=Ineuronprojects"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# 3. Create / select database
db = client["test_database"]

# 4. Create / select collection
collection = db["user_details"]

# 5. Insert dummy document
data = {
    "surname": "Patel",
    "email": "patel.dummy@email.com"
}
data = {
    "surname": "Pal",
    "email": "pal.dummy@email.com"
}

data = {
    "surname": "Pal1",
    "email": "pal1.dummy@email.com"
}

data = {
    "surname": "Pal2",
    "email": "pal2.dummy@email.com"
}
result = collection.insert_one(data)

print("Inserted document ID:", result.inserted_id)

# 6. Read and print data
for doc in collection.find():
    print(doc)

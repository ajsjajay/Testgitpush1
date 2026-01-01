# ------------------- MongoDB + Python (PyMongo) - Single File Learning Code -------------------
# GOAL:
# 1) Connect to MongoDB using your connection URL
# 2) Choose a database name
# 3) Choose a collection name inside that database
# 4) Insert MULTIPLE customer records
# 5) Read and print the stored data to confirm

from pymongo import MongoClient
# WHY this line is written:
# - Without this import, Python does not know how to connect to MongoDB.
# - MongoClient is the bridge between Python and MongoDB.


connection_url = "Your URL MONGO DB to be pasetd"
# WHY this line is written:
# - MongoDB needs an address so Python knows WHERE to connect.
# - This URL points to your remote MongoDB (Atlas / Cloud).


client = MongoClient(connection_url)
# WHY this line is written:
# - This creates the MAIN connection object.
# - Think: "I now have access to MongoDB."
# - IMPORTANT: No database or collection is created here.


db = client["customer_management_db"]
# WHY this line is written:
# - MongoDB can have many databases.
# - This line tells Python which database NAME to use.
# - IMPORTANT: Database is NOT created yet.


collection = db["customers"]
# WHY this line is written:
# - Inside a database, data lives in collections.
# - This line tells Python which collection NAME to use.
# - IMPORTANT: Collection is NOT created yet.


customers_data = [
    {
        "surname": "Reddy",
        "email": "reddy.customer@email.com"
    },
    {
        "surname": "Patel",
        "email": "patel.customer@email.com"
    },
    {
        "surname": "Sharma",
        "email": "sharma.customer@email.com"
    }
]
# WHY this is written:
# - This is MULTIPLE customer data prepared in Python.
# - IMPORTANT: Data is still NOT in MongoDB yet.


insert_result = collection.insert_many(customers_data)
# WHY this line is written (MOST IMPORTANT):
# - This is the FIRST real action sent to MongoDB.
# - THIS LINE causes MongoDB to:
#   ✅ Create database "customer_management_db" (if it does not exist)
#   ✅ Create collection "customers" (if it does not exist)
#   ✅ Insert ALL customer records
# - If DB/collection already exist, MongoDB only inserts the data.


print("Inserted document IDs:")
for inserted_id in insert_result.inserted_ids:
    print(inserted_id)
# WHY this is written:
# - MongoDB automatically creates a unique ID for each record.
# - Printing them confirms all records were inserted.


print("\nNow reading data from MongoDB to confirm it is really stored:")
# WHY this is written:
# - Clear message to explain why records are printed below.


for record in collection.find():
    print(record)
# WHY this is written:
# - find() fetches all stored records.
# - Seeing output proves data is really inside MongoDB.
# ---------------------------------------------------------------------------------------------

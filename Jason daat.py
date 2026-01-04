# ---------------- MongoDB + Python : Insert COMPLEX JSON (Beginner, One File) ----------------
# Connection chain (read once):
# client → db → collection → data
# Meaning: connect → choose database → choose collection → send data

from pymongo import MongoClient
# WHAT: import statement (tool name)
# WHY: Python must know how to talk to MongoDB
# IF NOT: Python cannot connect to MongoDB

try:
    connection_url = "Your URL"
    # WHAT: connection string (text value)
    # WHY: tells Python WHERE MongoDB is (cloud / remote)
    # IF NOT: no address → no connection

    client = MongoClient(connection_url)
    # WHAT: connection object
    # WHY: opens door to MongoDB server
    # IF NOT: nothing can talk to MongoDB

    db = client["customer_management_db"]
    # WHAT: database name reference
    # WHY: tells MongoDB which database name we want to use
    # IF NOT: MongoDB does not know where to store data

    collection = db["orders"]
    # WHAT: collection name reference
    # WHY: tells MongoDB which collection inside the database
    # IF NOT: MongoDB does not know which table-like place to use

    # This is COMPLEX JSON data (nested + list)
    # It is still ONLY in Python memory at this point




    complex_order_data = {
        "order_id": "ORD1001",
        "customer": {
            "first_name": "AjZ",
            "last_name": "Marj",
            "email": "ajay.kumar@email.com"
        },
        "items": [
            {
                "product_name": "Laptop",
                "price": 900,
                "quantity": 1
            },
            {
                "product_name": "Mouse",
                "price": 20,
                "quantity": 2
            }
        ],
        "shipping_address": {
            "city": "Dublin",
            "country": "Ireland",
            "pin": "D01XYZ"
        },
        "order_status": "confirmed",
        "payment": {
            "method": "card",
            "paid": True
        }
    }
    # WHAT: complex JSON (dictionary + list inside)
    # WHY: MongoDB stores data exactly like this (nested allowed)
    # IF NOT: nothing meaningful to store


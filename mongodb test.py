try:
    import pymongo
    print("✅ pymongo is installed")
    print("Version:", pymongo.__version__)
except ImportError:
    print("❌ pymongo is NOT installed")
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
print(client.list_database_names())

from pymongo import MongoClient

connection_url = "YOUR URL"
client = MongoClient(connection_url)

try:
    # 🔴 MOST IMPORTANT LINE (STEP 1) 🔴
    database_names = client.list_database_names()
    # WHAT: list of database names
    # WHY: MongoDB can have many databases
    # IF NOT: we cannot know which databases exist

    print("\nALL DATABASES AND THEIR DATA:\n")

    for db_name in database_names:
        # WHAT: one database name at a time
        # WHY: to enter each database separately
        # IF NOT: only one database would be processed

        print("DATABASE:", db_name)

        db = client[db_name]
        # WHAT: database reference
        # WHY: tells MongoDB which database to open
        # IF NOT: collections inside cannot be accessed

        collection_names = db.list_collection_names()
        # WHAT: list of collection names
        # WHY: data is stored inside collections
        # IF NOT: no data locations known

        if not collection_names:
            print("  (No collections found)")

        for col_name in collection_names:
            print("  COLLECTION:", col_name)

            collection = db[col_name]
            # WHAT: collection reference
            # WHY: tells MongoDB which collection to read
            # IF NOT: documents cannot be fetched

            # 🔴 MOST IMPORTANT LINE (STEP 2) 🔴
            records = collection.find()
            # WHAT: cursor with all documents
            # WHY: pulls all data from this collection
            # IF NOT: no data is read

            empty = True
            for doc in records:
                empty = False
                print("    DATA:", doc)

            if empty:
                print("    (No data found)")

        print("-" * 60)

except Exception as e:
    print("Error while reading databases or data.")
    print(e)
    # WHAT: error message
    # WHY: shows permission / connection / URL issues
    # IF NOT: program stops without reason

# ---------------- END OF FILE ----------------


# MEMORY (3 lines only):
# Purpose: show each database separately and print its data
# Key line: database_names = client.list_database_names()
# Confirm: database name prints, then collections and data under it
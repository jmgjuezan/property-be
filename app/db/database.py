from dotenv import find_dotenv, load_dotenv
import os
import pymongo

load_dotenv(find_dotenv())

CONNECTION_STRING: str = os.getenv("DATABASE_URL", "")

DATABASE_NAME = "prop-mgmt"

try:
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = client[DATABASE_NAME]
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
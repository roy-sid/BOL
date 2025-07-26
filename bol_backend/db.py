# db.py

import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]

# Example: db.stories, db.users
print("MONGO_DB_NAME =", MONGO_DB_NAME)
print("MONGO_URI =", MONGO_URI)

import os
from pymongo import MongoClient
from dotenv import load_dotenv


def getConnection():
    load_dotenv()

    mongo_url = os.getenv('MONGO_DB_URL')
    mongo_db_name = os.getenv('MONGO_DB_NAME')
    client = MongoClient(mongo_url)
    db = client[mongo_db_name]
    return db

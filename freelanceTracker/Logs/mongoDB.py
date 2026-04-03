from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
uri=os.getenv("MONGO_URI")
mongo_client = MongoClient(uri)
db=os.getenv("MONGO_DB")
mongo_db = mongo_client[db]
collection = mongo_db['logs']


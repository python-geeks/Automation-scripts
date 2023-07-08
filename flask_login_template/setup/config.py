import os

import pymongo
from dotenv import load_dotenv

load_dotenv()
template = os.environ["TEMPLATE"]
secret_key = os.environ["SECRET_KEY"]
client = pymongo.MongoClient(os.environ["MONGO_CONNECTION_STRING"])
db = client.registration

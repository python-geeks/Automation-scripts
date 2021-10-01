from dotenv import load_dotenv
import pymongo
import os

load_dotenv()
template = os.environ['TEMPLATE']
secret_key = os.environ['SECRET_KEY']
client = pymongo.MongoClient(os.environ['MONGO_CONNECTION_STRING'])
db = client.registration

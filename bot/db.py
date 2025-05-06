from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from .config import MONGODB_URI

client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))

db = client['auth_bot']
users_collection = db['users']
subscriptions_collection = db['subscriptions']

main_app_db = client['main_app']
price_collection = main_app_db['price'] 
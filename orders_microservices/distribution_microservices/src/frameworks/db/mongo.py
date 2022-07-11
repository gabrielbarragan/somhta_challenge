import os
from pymongo import MongoClient

from dotenv import load_dotenv

load_dotenv()

# Conexión a una base de datos NoSQL por medio del ORM PYMONGO (MongoDB).

class PymongoClient():

    def __init__(self):

        # Obtener el string de conexión los datos de la Base de datos y la colección desde variables de entorno.

        __db_url: str =os.environ["MONGODB_URL"]
        db_name: str = os.environ["MONGODB_NAME"]
        collection_name: str= os.environ["MONGODB_COLLECTION_NAME"]

        self.client = MongoClient(__db_url)
        
        self.database = self.client[db_name]

        self.collection = self.database[collection_name]



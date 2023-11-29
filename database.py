from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://root:root@cluster0.q2qibny.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
        db = client["dbb_products_app"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db

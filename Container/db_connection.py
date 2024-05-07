import pymongo 

def get_mongo_client():
    url = 'mongodb+srv://jeguerreror:yKqFqH09LxGZVKgq@cluster0.hmv7pqa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
    client = pymongo.MongoClient(url)
    return client

def get_database(client, db_name='geo_cat_db'):
    return client[db_name]
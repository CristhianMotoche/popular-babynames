from pymongo import MongoClient

def get_collection(config):
    client = get_connection(config['host'], config['port'])
    db = client[config['db']]
    return db[config['collection']]

def get_connection(host, port):
    return MongoClient(host, port)

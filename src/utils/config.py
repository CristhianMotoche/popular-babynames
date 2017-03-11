import os

def read_config():
    config = { 'host' : os.environ['HOST']
            , 'port' : int(os.environ['PORT'])
            , 'db' : so.environ['DB']
            , 'collection' : so.environ['COLLECTION']
            }
    return config

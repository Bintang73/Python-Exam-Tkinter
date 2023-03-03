from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class connection:
    def __init__ (self):
        self.username = ""

    def check_database(self):
        info = False
        mongodb = open("./file.txt", "r")
        mongo_read = mongodb.read()
        mongo_url = mongo_read.split("mongo_url=")[1] 
        try:
            client = MongoClient(mongo_url)
            client.admin.command('ismaster')
            info = True
        except ConnectionFailure:
            print("Server not available")
            info = False
        except:
            info = False

        return info

    
        
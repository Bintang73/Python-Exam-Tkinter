from pymongo import MongoClient

class Deluser:
    def __init__ (self, username):
        self.username = username

    def delete(self):
        mongodb = open("./file.txt", "r")
        mongo_read = mongodb.read()
        mongo_url = mongo_read.split("mongo_url=")[1] 
        
        myclient = MongoClient(mongo_url)
        mydb = myclient["db_ujian"]
        mycol = mydb["user_login"]

        mydict = { "username": self.username}

        res = mycol.delete_one(mydict)
                
        return res
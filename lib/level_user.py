from pymongo import MongoClient

class Leveluser:
    def __init__ (self, username):
        self.username = username

    def fullname(self):
        mongodb = open("./file.txt", "r")
        mongo_read = mongodb.read()
        mongo_url = mongo_read.split("mongo_url=")[1] 
        
        myclient = MongoClient(mongo_url)
        mydb = myclient["db_ujian"]
        mycol = mydb["user_login"]

        find_user = mycol.find_one({"username": self.username})

        res = False

        if find_user == None:
            res = False
        else:
            res = find_user["hak_akses"]
                
        return res
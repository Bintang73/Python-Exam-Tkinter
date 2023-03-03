from pymongo import MongoClient

class Changepass:
    def __init__ (self, username, password):
        self.username = username
        self.password = password

    def change(self):
        mongodb = open("./file.txt", "r")
        mongo_read = mongodb.read()
        mongo_url = mongo_read.split("mongo_url=")[1] 
        
        myclient = MongoClient(mongo_url)
        mydb = myclient["db_ujian"]
        mycol = mydb["user_login"]

        find_user = {"username": self.username}
        newvalues = { "$set": { "password": self.password } }

        mycol.update_one(find_user, newvalues)
                
        return "ok"
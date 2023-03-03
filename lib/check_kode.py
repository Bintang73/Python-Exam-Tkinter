from pymongo import MongoClient

class Checkkode:
    def __init__ (self, username, kode):
        self.username = username
        self.kodeku = kode

    def kode(self):
        mongodb = open("./file.txt", "r")
        mongo_read = mongodb.read()
        mongo_url = mongo_read.split("mongo_url=")[1] 
        
        myclient = MongoClient(mongo_url)
        mydb = myclient["db_ujian"]
        mycol = mydb["user_login"]

        find_userku = mycol.find_one({"username": self.username})

        find_user = find_userku["kode_digunakan"]

        a = []

        for x in find_user:
            a.append(x["kode_ujian"])
        

        res = False

        if self.kodeku in a:
            res = False
        else:
            res = True
                
        return res
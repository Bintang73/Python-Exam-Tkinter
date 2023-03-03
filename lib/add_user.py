from pymongo import MongoClient

class Adduser:
    def __init__ (self, username, password, fullname, hakakses):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.hakakses = hakakses

    def add(self):
        mongodb = open("./file.txt", "r")
        mongo_read = mongodb.read()
        mongo_url = mongo_read.split("mongo_url=")[1] 
        
        myclient = MongoClient(mongo_url)
        mydb = myclient["db_ujian"]
        mycol = mydb["user_login"]

        mydict = { "username": self.username, "password": self.password, "full_name": self.fullname, "hak_akses": self.hakakses, "kode_digunakan": [] }

        res = mycol.insert_one(mydict)
                
        return res
from pymongo import MongoClient

class Delsoal:
    def __init__ (self, kode):
        self.kode = kode

    def delete(self):
        mongodb = open("./file.txt", "r")
        mongo_read = mongodb.read()
        mongo_url = mongo_read.split("mongo_url=")[1] 
        
        myclient = MongoClient(mongo_url)
        mydb = myclient["db_ujian"]
        mycol = mydb["bank_soal"]

        mydict = { "kode": self.kode}

        res = mycol.delete_one(mydict)
                
        return res
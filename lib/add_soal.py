from pymongo import MongoClient

class Addsoal:
    def __init__ (self, kode, durasi, matkul, json):
        self.kode = kode
        self.durasi = durasi
        self.matkul = matkul
        self.json = json

    def add(self):
        mongodb = open("./file.txt", "r")
        mongo_read = mongodb.read()
        mongo_url = mongo_read.split("mongo_url=")[1] 
        
        myclient = MongoClient(mongo_url)
        mydb = myclient["db_ujian"]
        mycol = mydb["bank_soal"]

        mydict = { "kode": self.kode, "durasi": self.durasi, "matkul": self.matkul, "soal": self.json }

        res = mycol.insert_one(mydict)
                
        return res
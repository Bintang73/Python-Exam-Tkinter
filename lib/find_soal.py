from pymongo import MongoClient

class Findsoal:
    def __init__ (self, kodeujian):
        self.kodeujian = kodeujian

    def kode(self):
        mongodb = open("./file.txt", "r")
        mongo_read = mongodb.read()
        mongo_url = mongo_read.split("mongo_url=")[1] 
        
        myclient = MongoClient(mongo_url)
        mydb = myclient["db_ujian"]
        mycol = mydb["bank_soal"]

        find_user = mycol.find_one({"kode": self.kodeujian})
        
        if find_user == None:
            jumlah = {
                "status": 404,
                "msg": "Kode Soal Tidak Ditemukan!"
            }
        else:
            find_jumlah = find_user["soal"]
            jumlah = {
                "status": 200,
                "jumlah": len(find_jumlah),
                "durasi": find_user["durasi"],
                "matkul": find_user["matkul"],
                "msg": find_jumlah
            }
                
        return jumlah
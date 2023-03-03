from pymongo import MongoClient

class Addresult:
    def __init__ (self, kode, arraylist, username):
        self.kode = kode
        self.arraylist = arraylist
        self.username = username

    def add(self):
        mongodb = open("./file.txt", "r")
        mongo_read = mongodb.read()
        mongo_url = mongo_read.split("mongo_url=")[1] 
        
        myclient = MongoClient(mongo_url)
        mydb = myclient["db_ujian"]
        mycol = mydb["user_login"]


        myclient2 = MongoClient(mongo_url)
        mydb2 = myclient2["db_ujian"]
        mycol2 = mydb2["bank_soal"]
        
        find_soal = mycol2.find_one({"kode": self.kode})

        find_jawaban = find_soal["soal"]

        jawaban_asli = []
        for  z in find_jawaban:
            jawaban_asli.append(z["jawaban"])

        jawaban_benar = []
        jawaban_salah = []
        nomor_benar = []
        nomor_salah = []

        for v in range(len(jawaban_asli)):
            if jawaban_asli[v] == self.arraylist[v]:
                jawaban_benar.append(jawaban_asli[v])
                nomorb = v + 1
                nomor_benar.append(nomorb)
            elif jawaban_asli[v] != self.arraylist[v]:
                jawaban_salah.append(self.arraylist[v])
                nomors = v + 1
                nomor_salah.append(nomors)
        
        totalsoal = int(len(jawaban_asli))
        totalbenar = int(len(jawaban_benar))
        toalsalah = int(len(jawaban_salah))

        n = (totalsoal-toalsalah)/totalsoal * 100


        mydict = { "kode_ujian": self.kode, "jawaban": self.arraylist, "benar": len(jawaban_benar), "salah": len(jawaban_salah), "nilai": n, "nomor_benar": nomor_benar, "nomor_salah": nomor_salah }

        find_user = {"username": self.username}
        newvalues = { "$push": { "kode_digunakan": mydict } }

        res = mycol.update_one(find_user, newvalues)
                
        return res
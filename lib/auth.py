from pymongo import MongoClient

class auth:
    def __init__ (self, username, password):
        self.username = username
        self.password = password

    def acc_login(self):
        info = None
        mongodb = open("./file.txt", "r")
        mongo_read = mongodb.read()
        mongo_url = mongo_read.split("mongo_url=")[1] 
        
        myclient = MongoClient(mongo_url)
        mydb = myclient["db_ujian"]
        mycol = mydb["user_login"]

        find_user = mycol.find_one({"username": self.username})

        if find_user == None:
            info = {
                "status": 400,
                "msg": "Username Tidak Ditemukan"
            }
        else:
            if find_user["password"] == self.password:
                info = {
                    "status": 200,
                    "msg": "Login Berhasil!"
                }
            else:
                info = {
                    "status": 403,
                    "msg": "Kata Sandi salah!"
                }
                
        return info
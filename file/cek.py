
from pymongo import MongoClient

'''x = Findsoal("xoxo").kode()

q = ["A", "B", "D", "E", "E", "E", "A", "B", "C", "D"]
p = ["A", "B", "X", "E", "E", "E", "B", "B", "C", "D"]

a = x["msg"]

c = []
for  z in a:
    c.append(z["jawaban"])

benar = []
salah = []

for v in range(len(q)):
    if q[v] == p[v]:
        benar.append(q[v])
    elif q[v] != p[v]:
        salah.append(p[v])

n = (40-0)/40 * 100'''

mongodb = open("./file.txt", "r")
mongo_read = mongodb.read()
mongo_url = mongo_read.split("mongo_url=")[1]

myclient = MongoClient(mongo_url)
mydb = myclient["db_ujian"]
mycol = mydb["user_login"]

#ind_user = {"username": "bintang"}
#newvalues = { "$push": { "kode_digunakan": { "status": "ok"} } }

#res = mycol.update_one(find_user, newvalues)

find_user = mycol.find_one({"username": "bintang"})


kode = find_user["kode_digunakan"]

a = []

for x in kode:
    a.append(x["kode_ujian"])

print(a)

if "xoxox" in a:
    print("ADA")

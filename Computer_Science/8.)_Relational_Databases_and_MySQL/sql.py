import mysql.connector as ms

db = ms.connect(host = "localhost",user = "root",passwd = "Tejas@035611",database = "electricity")
print()
data = db.cursor()
data.execute("select * from ebill;")
for i in data:
    print(i)
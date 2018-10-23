import MySQLdb
db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="banking")        
cur = db.cursor()
cur.execute("SELECT * FROM memberTBL")
for row in cur.fetchall():
    print row[0]

db.close()

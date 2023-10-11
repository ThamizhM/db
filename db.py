import pymysql 
con = pymysql.connect(host="ENMA",user="root",password="",database="student")
cur = con.cursor
cur.execute("select * from stud_per")
data = cur.fetchall()
print(data)
db.close
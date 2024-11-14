import mysql.connector as conn


# mydb




mydb=conn.connect(host='localhost',user='root',passwd="madh2004")
mydb
cursor = mydb.cursor()
cursor.execute("show databases")
cursor.fetchall()
cursor.execute('use Vendor')
cursor.execute("insert into cleaned_dataset values(1001,'Library','General',34.98,1)")


# cursor.fetchall()

cursor.fetchall()
cursor.execute("SELECT * FROM cleaned_dataset")
rows = cursor.fetchall()
for row in rows:
    print(row)
mydb.commit()
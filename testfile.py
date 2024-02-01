import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="it_elective"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM veryfastfood"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
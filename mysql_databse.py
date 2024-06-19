import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Admin",
  database="hospital"
)

mycursor = mydb.cursor()

def insert(sql, data):
    try:
        for params in data:
            try:
                mycursor.execute(sql, params)
                mydb.commit()
            except mysql.connector.Error as err:
                mydb.rollback()
    finally:
        if mycursor:
            mycursor.close()

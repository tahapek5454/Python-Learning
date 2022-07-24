
# you shoul install mysql-connector with pip
import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    # database = "schooldb"
)



mycursor = connection.cursor()
mycursor.execute('Show Databases')

for i in mycursor:
    print(i)
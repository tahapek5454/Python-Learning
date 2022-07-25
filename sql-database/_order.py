import mysql.connector

conn = mysql.connector.connect(host='localhost', user = 'root', password = '', database = 'node_app')

cursor = conn.cursor()

cursor.execute('SELECT name , price FROM products ORDER BY price , name DESC') # price a gore siralar

result = cursor.fetchall()   # tek bir veri gelmesi icin fetchone

for i in result:
    print(f'Name = {i[0]} Price = {i[1]}')

import mysql.connector

conn = mysql.connector.connect(host='localhost', user = 'root', password = '', database = 'node_app')

cursor = conn.cursor()

cursor.execute('SELECT name , price FROM products WHERE price > 1000') # where kosul belirtirsin gerisi ayni

result = cursor.fetchall()   # tek bir veri gelmesi icin fetchone

for i in result:
    print(f'Name = {i[0]} Price = {i[1]}')

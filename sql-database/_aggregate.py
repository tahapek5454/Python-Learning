import mysql.connector

conn = mysql.connector.connect(host='localhost', user = 'root', password = '', database = 'node_app')

cursor = conn.cursor()

# sql = 'SELECT COUNT(*) FROM products ' # satir sayisini verir
# sql = 'SELECT SUM(price) FROM products ' # secilen kolonun toplamini verir
# sql = 'SELECT AVG(price) FROM products ' # secilen kolonun ortalamasini verir
# sql = 'SELECT MAX(price) FROM products ' # secilen kolonun max verir
sql = 'SELECT MIN(price) FROM products ' # secilen kolonun min verir


cursor.execute(sql) # where kosul belirtirsin gerisi ayni

result = cursor.fetchall()   # tek bir veri gelmesi icin fetchone

for i in result:
    # print(f'Satir sayisi {i[0]}')
    # print(f'Toplam fiyat {i[0]}')
    # print(f'Ortalma fiyat {i[0]}')
    # print(f'Max fiyat {i[0]}')
    print(f'Min fiyat {i[0]}')
    # print(f'Name = {i[0]} Price = {i[1]}')

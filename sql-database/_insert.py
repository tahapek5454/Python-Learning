import mysql.connector

def insertProduct(name,price,img,description):

    connection = mysql.connector.connect(host = 'localhost' ,user = 'root',password = '',database = 'node_app')
    cursor = connection.cursor()

    sql = 'INSERT INTO products(name,price,image_url,description) VALUES(%s, %s , %s,%s)'
    values = (name,price,img,description)        

    cursor.execute(sql,values) #verilen sorguyu uygalatiyotuz

    try:
        connection.commit() # commit ederek sorguyu database e aktariyoruz
        print(f'{cursor.rowcount} tane kayit eklendi')
        print(f'Son eklenen kaydin id si  {cursor.lastrowid}')
    except Exception as ex:
        print("hata")
        print(ex)
    finally:
        connection.close()  
        print('Baglanti sonlandi')



def insertMultiProduct(liste):

    connection = mysql.connector.connect(host = 'localhost' ,user = 'root',password = '',database = 'node_app')
    cursor = connection.cursor()

    sql = 'INSERT INTO products(name,price,image_url,description) VALUES(%s, %s , %s,%s)'
    values = liste
    cursor.executemany(sql,values) #verilen sorguyu toplu sekilde uygulatiyoruz

    try:
        connection.commit() # commit ederek sorguyu database e aktariyoruz
        print(f'{cursor.rowcount} tane kayit eklendi')
        print(f'Son eklenen kaydin id si  {cursor.lastrowid}')
    except Exception as ex:
        print("hata")
        print(ex)
    finally:
        connection.close()  
        print('Baglanti sonlandi')



liste = []

while True:
    name = input('Urun adini giriniz : ')
    price = int(input('Urunun fiyatini tam sayi biciminde giririniz : '))
    img = input('Ressim adini giriniz : ')
    description = input("Urunun tanimiini giriniz : ")

    liste.append((name,price,img,description))

    result = input('Devam etmek istiyor musunuz ? e/h')

    if result == 'h':
        print('Islem sonlandirlidi')
        print(liste)
        insertMultiProduct(liste)
        break



        
        


import mysql.connector

def updateProduct(id,name,price):

    connection = mysql.connector.connect(host = 'localhost' ,user = 'root',password = '',database = 'node_app')
    cursor = connection.cursor()

    sql = 'UPDATE products SET  name = %s , price = %s WHERE id = %s'
    values = (name,price,id)        

    cursor.execute(sql,values) #verilen sorguyu uygalatiyotuz

    try:
        connection.commit() # commit ederek sorguyu database e aktariyoruz
        print(f'{cursor.rowcount} tane kayit Guncelledi')
        
    except Exception as ex:
        print("hata")
        print(ex)
    finally:
        connection.close()  
        print('Baglanti sonlandi')


updateProduct(3,'pinpon',1234)
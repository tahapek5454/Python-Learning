import mysql.connector

def deleteProduct(id):

    connection = mysql.connector.connect(host = 'localhost' ,user = 'root',password = '',database = 'node_app')
    cursor = connection.cursor()

    sql = 'DELETE FROM products WHERE id = %s'
    values = (id,)   # tek degiskende de , koymak zorundasın      

    cursor.execute(sql,values) #verilen sorguyu uygalatiyotuz

    try:
        connection.commit() # commit ederek sorguyu database e aktariyoruz
        print(f'{cursor.rowcount} tane kayit silindi')
        
    except Exception as ex:
        print("hata")
        print(ex)
    finally:
        connection.close()  
        print('Baglanti sonlandi')


deleteProduct(3)
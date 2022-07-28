import mysql.connector

def joinProduct():

    connection = mysql.connector.connect(host = 'localhost' ,user = 'root',password = '',database = 'node_app')
    cursor = connection.cursor()

    sql = 'SELECT p.id , p.name , c.name FROM products p INNER JOIN categories c ON p.c_id = c.id'
            

    cursor.execute(sql) #verilen sorguyu uygalatiyotuz

    try:
        result = cursor.fetchall()
        print(f'{cursor.rowcount} tane kayit geldi')

        for i in result:
            print(f'id : {i[0]} name : {i[1]}  category name : {i[2]}')
        
    except Exception as ex:
        print("hata")
        print(ex)
    finally:
        connection.close()  
        print('Baglanti sonlandi')


joinProduct()
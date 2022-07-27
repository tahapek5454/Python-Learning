# 1- Workbench IDE ile schooldb isminde bir database oluşturup Student tablosunu ekleyiniz.
    # Id,StudentNumber,Name,Surname,Birthdate,Gender

# 2- Database bağlantısını oluşturunuz. (connection.py)

# 3- Aşağıdaki bilgiler için insert sorguları oluşturup kayıtları ekleyiniz.


    # ("301","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    # ("302","Ali","Can",datetime(2005, 6, 17),"E"),
    # ("303","Canan","Tan",datetime(2005, 7, 7),"K"),
    # ("304","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    # ("305","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    # ("306","Ali","Cenk",datetime(2003, 8, 25),"E")

# 4- Aşağıdaki sorguları yazınız.
#   a- Tüm öğrenci kayıtlarını alınız.
#   b- Tüm öğrencilerin sadece öğrenci no, ad ve soyad bilgilerini alınız.
#   c- Sadece kız öğrencilerin ad ve soyadlarını alınız.
#   d- 2003 doğumlu öğrenci bilgilerini alınız. 
#   e- İsmi Ali ve doğum tarihi 2005 olan öğrenci bilgilerini alınız.
#   f- ad veya soyadı içinde 'an' ifadesi geçen kayıtları alınız. 
#   g- Kaç erkek öğrenci vardır ?
#   h- Kız öğrencileri harf sırasına göre getiriniz.


import mysql.connector
from datetime import datetime


class Student:


    connection = mysql.connector.connect(host='localhost',user='root',password='',database='schooldb')
    cursor = connection.cursor()


    def __init__(self,id,studentNumber,name,surname,birthdate,gender) -> None:

        self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
    
    def addStudent(self):

        sql = 'INSERT INTO student(s_number,name,surname,birthdate,gender) VALUES(%s,%s,%s,%s,%s)'
        value = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender)

        self.cursor.execute(sql,value)

        try:
            self.connection.commit() # class in bir ozelligini cagriiyoruz self de kullanabilir class ismi de
            print(f'{self.cursor.rowcount} tane kayit eklendi')
        except Exception as ex:
            print(ex)
        finally:
            self.connection.close()
            print('Baglanti kesildi databasesinizi kontrol ediniz')
    
    @staticmethod
    def addStudents(liste):
        sql = 'INSERT INTO student(s_number,name,surname,birthdate,gender) VALUES(%s,%s,%s,%s,%s)'
        values = liste

        Student.cursor.executemany(sql,values)

        try:
            Student.connection.commit() # callassin ozelli static method da oldugundan direkt class ismiyle
            print(f'{Student.cursor.rowcount} tane kayit eklendi')
        except Exception as ex:
            print(ex)
        finally:
            Student.connection.close()
            print('Baglanti kesildi databasesinizi kontrol ediniz')
    
    @staticmethod
    def getStudents():
        sql = 'SELECT * FROM student'

        Student.cursor.execute(sql)

        result = Student.cursor.fetchall()

        for i in result:
            print(f'id = {i[0]} - Number = {i[1]} - Name = {i[2]} - Surname = {i[3]} - Birthdate = {i[4]} - Gender = {i[5]}')

    
    @staticmethod
    def getStudentsBasic():
        sql = 'SELECT s_number , name , surname FROM student'

        Student.cursor.execute(sql)

        result = Student.cursor.fetchall()

        for i in result:
            print(f'Number = {i[0]} - Name = {i[1]} - Surname = {i[2]}')

    @staticmethod
    def getGirls():

        sql = 'SELECT  name , surname FROM student WHERE  gender = "K" '

        Student.cursor.execute(sql)

        result = Student.cursor.fetchall()

        for i in result:
            print(f'Name = {i[0]} - Surname = {i[1]}')
    
    @staticmethod
    def getStudentsWithDate(date):
        sql = 'SELECT * FROM student WHERE birthdate BETWEEN "'+date+'-01-01" AND "'+date+'-12-30"'

        Student.cursor.execute(sql)

        result = Student.cursor.fetchall()

        for i in result:
            print(f'id = {i[0]} - Number = {i[1]} - Name = {i[2]} - Surname = {i[3]} - Birthdate = {i[4]} - Gender = {i[5]}')

    @staticmethod
    def getStudentsWithYearWithName(name , date):
        sql = 'SELECT * FROM student WHERE name = "'+name+'" AND YEAR(birthdate) = '+date

        Student.cursor.execute(sql)

        result = Student.cursor.fetchall()

        for i in result:
            print(f'id = {i[0]} - Number = {i[1]} - Name = {i[2]} - Surname = {i[3]} - Birthdate = {i[4]} - Gender = {i[5]}')

    @staticmethod
    def getStudentsWithHasStr(string):
        sql = 'SELECT * FROM student WHERE name LIKE "%'+string+'%" '

        Student.cursor.execute(sql)

        result = Student.cursor.fetchall()

        for i in result:
            print(f'id = {i[0]} - Number = {i[1]} - Name = {i[2]} - Surname = {i[3]} - Birthdate = {i[4]} - Gender = {i[5]}')

    @staticmethod
    def getBoyCount():
        sql = 'SELECT gender , COUNT(*) as count FROM student WHERE gender = "E" GROUP BY gender'

        Student.cursor.execute(sql)

        result = Student.cursor.fetchall()

        for i in result:
            print(f'Erkek Sayisi = {i[1]}')
    

    @staticmethod
    def getGirlWithOrder():
        sql = 'SELECT * FROM student WHERE gender = "K" ORDER BY name'

        Student.cursor.execute(sql)

        result = Student.cursor.fetchall()

        for i in result:
            print(f'id = {i[0]} - Number = {i[1]} - Name = {i[2]} - Surname = {i[3]} - Birthdate = {i[4]} - Gender = {i[5]}')
#-------------------------------------------------------------------------------------------

def insertValues(liste):

    connection = mysql.connector.connect(host='localhost',user='root',password='',database='schooldb')
    cursor = connection.cursor()

    sql = 'INSERT INTO student(s_number,name,surname,birthdate,gender) VALUES(%s,%s,%s,%s,%s)'
    values = liste

    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayit eklendi')
    except Exception as ex:
        print(ex)
    finally:
        connection.close()
        print('Baglanti kesildi databasesinizi kontrol ediniz')

#------------------------------------------------------------------------------------------------

liste = [
    ("309","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    ("310","Ali","Can",datetime(2005, 6, 17),"E"),
    ("311","Canan","Tan",datetime(2005, 7, 7),"K"),
    ("312","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    ("313","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    ("314","Ali","Cenk",datetime(2003, 8, 25),"E")
]

 
# insertValues(liste) bu bizim topluca kayıt etmemizi saglayacak

# ayse = Student(8,'308','Ayse','Sezer',datetime(2000,9,23),'K')
# ayse.addStudent()

# Student.addStudents(liste)

# Student.getStudents()

# Student.getStudentsBasic()

# Student.getGirls()

# Student.getStudentsWithDate(str(2003))

# Student.getStudentsWithYearWithName('Ahmet','2005')

# Student.getStudentsWithHasStr('an')

# Student.getBoyCount()

Student.getGirlWithOrder()

# taha pek

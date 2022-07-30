from hashlib import new
from _connection import connection
from datetime import datetime
from _Class import Class
from ClassLesson import ClassLesson
from Lesson import Lesson
from Student import Student
from Teacher import Teacher

class DbManage:

    def __init__(self) -> None:

        self.connection = connection
        self.cursor = self.connection.cursor()
    
    def __del__(self) -> None:
        self.connection.close()
        print('Db baglantisi kesildi')
 

    def getStudentById(self, id):

        sql = 'SELECT * FROM student WHERE id = %s'
        values = (id,)

        self.cursor.execute(sql,values)

        try:
            
            obj = self.cursor.fetchone()

            return Student.crateStudents(obj)

        except Exception as ex:
            print('eror',ex)

    

    def getStudentsByClassId(self, id):
        
        sql = 'SELECT * FROM student WHERE class_id = %s'
        values = (id,)

        self.cursor.execute(sql,values)

        try :
            obj = self.cursor.fetchall()
            return Student.crateStudents(obj)
        except Exception as ex:
            print('Eoror',ex)
    


    def deleteStudent(self,studentid):
        sql = "delete from student where id=%s"
        value = (studentid,)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
        except Exception as ex:
            print('hata:', ex)

    def getClasses(self):
        
        sql = 'SELECT * FROM class'
        

        self.cursor.execute(sql)

        try :
            obj = self.cursor.fetchall()
            return Class.createClass(obj)
        except Exception as ex:
            print('Eoror',ex)


    def addStudent(self, student : Student):
        sql = 'INSERT INTO student(s_number,name,surname,birthdate,gender,class_id) VALUES(%s,%s,%s,%s,%s,%s)'
        value = (student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.class_id)

        self.cursor.execute(sql,value)

        try:
            self.connection.commit() 
            print(f'{self.cursor.rowcount} tane kayit eklendi')
        except Exception as ex:
            print('eror',ex)
        
    
    def editStudent(self, student : Student):
        sql = 'UPDATE student SET  s_number = %s , name = %s , surname = %s , birthdate = %s , gender = %s , class_id = %s WHERE id = %s'
        values = (student.number,student.name,student.surname,student.birthdate,student.gender,student.class_id,student.id)        

        Student.cursor.execute(sql,values) #verilen sorguyu uygalatiyotuz

        try:
            Student.connection.commit() # commit ederek sorguyu database e aktariyoruz
            print(f'{Student.cursor.rowcount} tane kayit Guncelledi')
        
        except Exception as ex:
            print("eror",ex)


    def addTeacher(self, teacher : Teacher):
        pass

    def editTeacher(self, teacher : Teacher):
        pass




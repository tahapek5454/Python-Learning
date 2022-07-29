class Student:

    def __init__(self,id,studentNumber,name,surname,birthdate,gender,class_id) -> None:

        self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.class_id = class_id
    
    @staticmethod
    def crateStudents(obj):

        liste = []

        if isinstance(obj,tuple):

            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6])
        else :

            for objj in obj:

                liste.append(Student(objj[0],objj[1],objj[2],objj[3],objj[4],objj[5],objj[6]))
            
            return liste



class Class:

    def __init__(self,id,name,teacher_id) -> None:

        self.id = id
        self.teacher_id = teacher_id
        self.name = name
    

    @staticmethod
    def createClass(obj):

        liste = []

        if isinstance(obj,tuple):

            return Class(obj[0],obj[1],obj[2])
        else :

            for objj in obj:

                liste.append(Class(objj[0],objj[1],objj[2]))
            
            return liste
        
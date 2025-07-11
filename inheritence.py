class Wizard:
    def __init__(self , age , name) :
        if not name:
            raise ValueError("invalid name!")
        self.name = name  
        self.age = age

class Student(Wizard):
    def __init__(self ,age ,name , house) :
        super().__init__(age , name)
        self.house = house 


class Professor(Wizard):
    def __init__(self ,age ,  name , subject):
        super().__init__(age , name)
        self.subject = subject

student = Student(18 , "Harry" , "Gryffindor")
professor = Professor(200 , "Dumbledor" , "Defend against dark magic")

print(student.name , student.house , sep=":")
print(professor.name , professor.subject , sep=":")
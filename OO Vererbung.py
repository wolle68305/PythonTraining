class Student():
    def __init__(self, firstName, surName):
        self.firstName = firstName
        self.surName = surName

    def name(self):
        return self.firstName + " " + self.surName    
    
class WorkingStudent(Student):
    #durch das Student in der Klasse wird gesagt, dass alles von der Klasse Student geerbt werden soll
    def __init__(self, firstName, surName, company):
        self.firstName = firstName
        self.surName = surName
        self.company = company
     
    
student = Student("Max", "Müller")
student2 = WorkingStudent("Daniel", "Wolf", "Wolf GmbH")
print(student.name())    
print(student2.name())
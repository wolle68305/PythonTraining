class Student():
    #Allgemeine Student Klasse, die von der WorkingStudent Klasse vererbt wird
    def __init__(self, firstName, surName):
        self.firstName = firstName
        self.surName = surName

    def name(self):
        return self.firstName + " " + self.surName    
    
class WorkingStudent(Student):
    #durch das Student in der Klasse wird gesagt, dass alles von der Klasse Student geerbt werden soll
    #bei der Print Ausgabe hat man daher Zugriff auf die Methode name für den Student2 (WorkingStudent)
    def __init__(self, firstName, surName, company):
        #self.firstName = firstName
        #self.surName = surName
        #um firstName und surName nicht zweimal schreiben zu müssen, kann man auch die init der Student Klasse aufrufen,
        #von der die Klasse WorkingStudent erbt (von der Elternklasse)
        super().__init__(firstName, surName)
        self.company = company

    def name(self):
        #Überschreibt die Methode name der Klasse Student
        return "WorkingStudent:" + self.firstName + " " + self.surName 
    
    def name2(self):
        #Alternative, greift auf die Methode name der Student Klasse zu und gibt Vorname und Nachname zurück
        return super().name() + " (" + self.company + ")"
     
#Standard Student Objekt wird erstellt    
student = Student("Max", "Müller")

#Working Student Objekt wird erstellt
student2 = WorkingStudent("Daniel", "Wolf", "Wolf GmbH")


#Unterschied von Type und IsInstance

#bei Type wird keine Vererbung beachtet
print(type(student))

if type(student) == Student:
    print("Diese Zeile wird nur für einen Student ausgegeben")

#student2 ist sowohl ein Working Student, als auch ein Student wegen der Vererbung
print(isinstance(student2,WorkingStudent))
print(isinstance(student2,Student))

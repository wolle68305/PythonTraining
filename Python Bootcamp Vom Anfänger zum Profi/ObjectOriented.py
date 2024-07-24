def startMain():
    functionChoice = input("Welche Funktion soll ausgeführt werden: ")

    if int(functionChoice) == 1:
        function1()

    if int(functionChoice) == 2:
        function2()

    if int(functionChoice) == 3:
        function3() 

    if int(functionChoice) == 4:
        function4()

    if int(functionChoice) == 5:
        function5()             

def function1():
    erik = Student()
    erik.firstname = "Erik"
    erik.lastname = "Mustermann"
    get_name(erik)

def function2():
    erik = Student()
    erik.firstname = "Erik"
    erik.lastname = "Mustermann"
    #ruft Methode name der Klasse Student auf
    erik.name()

def function3():
    erik = Student()
    erik.firstname = "Erik"
    erik.lastname = "Mustermann"

    c = Company()
    c.legalName = "Mustermann"
    c.legalType = "GmbH"

    #Die Funktion bekommt das Objekt übergeben und ruft bei diesem Objekt dann die Methode name auf 
    name_5x(erik)
    name_5x(c)

def function4():
    #Konstruktor Aufruf
    erik = Student2("Erik", "Mustermann")
    erik.increaseTerm(5)
    erik.name() 

def function5():
    #Konstruktor Aufruf
    erik = Student2("Erik", "Mustermann")
    erik.increaseTerm(5)
    print("Der Rückgabewert der Methode get_term lautet: " + erik.get_term()) 


class Student():
    def name(self):
        print(self.firstname + " " + self.lastname)

class Student2():
    #Konstruktor Aufruf mit der Zuweisung der Atrribute firstName und lastName
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        #Doppelter Unterstrich bedeutet dass die Eigenschaft privat ist und man kann nur noch innerhalb der Klasse auf "term" zugreifen
        self.__term = 1

    def name(self):
        print(self.firstName + " " + self.lastName + " (Semester : " + str(self.__term) + ")")

    def increaseTerm(self, increaseNumber):
        #Methode zur Erhöhung des Semesters
        #Doppelter Unterstrich bedeutet dass die Eigenschaft privat ist und man nicht mehr von außen zugreifen kann
        self.__term = self.__term + increaseNumber    

    def get_term(self):
        #Getter Methode zum Erhalt der Term Eigenschaft
        return str(self.__term)
    
    def __do_something(self):
        #private Methode, die nur innerhalb der Klasse aufrufbar ist
        pass

class Company():
    def name(self):
        print(self.legalName + " " + self.legalType)        

def get_name(student):
    print(student.firstname + " " + student.lastname)

def name_5x(v):
    #Die Funktion bekommt das Objekt übergeben und ruft bei diesem Objekt dann die Methode name auf 
    v.name()
    v.name()
    v.name()
    v.name()
    v.name()

startMain()    
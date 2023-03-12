#Tupel ist eine unveränderliche Datenstruktur

def main():
    vTupel = ()
    vTupel = create_Tupel(vTupel)

    print(vTupel)
    print(vTupel,0)

    #gibt mehrere Werte zurück und schreibt diese in die entsprechenden Variablen
    name, age, job = returnMultipleValuesFromTupel()

    function4()

def create_Tupel(affectedTupel):
    affectedTupel = ("Daniel Wolf",34,"Informatiker")
    return affectedTupel

def return_SingleValueFormTupel(affectedTupel, positionOfReturnValue):
    return affectedTupel[positionOfReturnValue]

def easyWayValuesFromTupelToVariables(affectedTupel):
    name, age, job = affectedTupel
    #schreibt innerhalb einer Zeile die Werte des Tuppels in die 3 Variablen
    #Anzahl der Variablen muss genauso viel sein wie die Anzahl der Elemente in einem Tupel

def returnMultipleValuesFromTupel():
    return ("Max Mustermann", 40, "Informatiker")

def function4():
    students = [
        ("Max Müller", 22),
        ("Monika Mustermann", 23)
    ]

    #Variante 1
    #for student in students:
        #name, age = student
        #print(name)
        #print(age)

    #variante 2
    for name, age in students:
        print(name)
        print(age)    
main()
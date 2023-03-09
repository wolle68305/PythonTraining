#Tupel ist eine unveränderliche Datenstruktur

def main():
    vTupel = ()
    vTupel = create_Tupel(vTupel)

    print(vTupel)
    print(vTupel,0)

    name, age, job = returnMultipleValuesFromTupel()
    #gibt mehrere Werte zurück und schreibt diese in die entsprechenden Variablen

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

main()
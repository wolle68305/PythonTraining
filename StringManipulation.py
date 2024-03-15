def main():
    #vS_Text  = "Hallo Welt"
    #print(substring_Function(vS_Text))
    #print(substring_Function2(vS_Text))
    #print(substring_Function3(vS_Text))
    #print(partOfTheString(vS_Text))
    #lineBreak()
    fStringMethode()

def substring_Function(vS_Text):
    #Ausgabe "Hallo"
    #gleiches Prinzip wie bei List Slicing
    return vS_Text[0:5]

def substring_Function2(vS_Text):
    #Ausgabe "Welt"
    #beginnt mit dem viert letzten Zeichen und läuft bis zum Ende
    return vS_Text[-4:]

def substring_Function3(vS_Text):
    #Ausgabe "Hallo Welt"
    return vS_Text[:]

def partOfTheString(vS_Text):
    #Ausgabe a
    return vS_Text[1]

def lineBreak():
    print("Hallo \nWelt")

def fStringMethode():
    name = "Daniel Wolf"
    alter = 36
    #f String wandelt alle Variablen in ein String um
    #mit dem Backslash kann man bei der Codezeile einen Zeilenumbruch verwenden
    print(f"Hier kommt die Einladung für {name} "+ \
          f"zu seinem {alter}. Geburtstag")

main()



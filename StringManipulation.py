def main():
    vS_Text  = "Hallo Welt"
    print(substring_Function(vS_Text))
    print(substring_Function2(vS_Text))
    print(substring_Function3(vS_Text))

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

main()



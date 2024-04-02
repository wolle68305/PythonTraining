def set_EmpfaengerName():
    global vS_EmpfaengerName
    global vS_EmpfaengerGeschlecht
    vS_EmpfaengerName = input("Bitte gebe den Empfängernamen ein: ")
    vS_EmpfaengerGeschlecht = input("Bitte gebe das Empfängergeschlecht ein [male/female]: ")

def set_EigeneDaten():
    global vS_EigenerName
    global vS_EigenesAlter
    global vS_EigeneStadt

    vS_EigenerName = input("Bitte gebe den eigenen Namen ein: ")
    vS_EigenesAlter = input("Bitte gebe dein Alter ein: ")
    vS_EigeneStadt = input("Bitte gebe deine Stadt ein: ")

def printout_Text():
    if vS_EmpfaengerGeschlecht == "male":
        print("Sehr geehrter Herr " + vS_EmpfaengerName + ",")
    else:
        print("Sehr geehrte Frau " + vS_EmpfaengerName + ",")    
    print("")
    print("Mein Name ist " + vS_EigenerName)
    print("Ich bin " + vS_EigenesAlter)
    print("Ich komme aus " + vS_EigeneStadt)

set_EmpfaengerName()
set_EigeneDaten()
printout_Text()
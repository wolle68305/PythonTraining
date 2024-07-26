def main():
    #startProgramm1()
    #startProgramm2()
    startProgramm3()


#erweitert die Exception Klasse von Python und somit kann man eine eigene Fehlermeldung kreieren
class InvalidEmailError(Exception):
    pass

def send_mail(email, subject, content):
    if not "@" in email:
        raise InvalidEmailError("email does not contain an @")

def startProgramm1():
    try:
        send_mail("hallo", "Betreff", "Inhalt")
    except:
        print("Bitte gebe eine gültige Email ein")


#---------------------------------------------------------

def startProgramm2():
    try:
        file = open("existiert.txt", "r")
    except FileNotFoundError:
        print("Datei nicht gefunden")
    finally:
        file.close()
        print("Programmende")

def startProgramm3():
    try:
        with open("existiert.txt", "r") as file:
            print(file)
    except FileNotFoundError:
        print("Datei wurde nicht gefunden")



main()
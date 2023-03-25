#Liste ist eine veränderliche Datenstruktur

def start_main():
    liste1 = []
    liste2 = [] 
    #liste1 = fill_List(liste1)
    liste1  = fill_List2(liste1)
    #Ausgaben der Ergebnisse der Funktionen
    print_List(liste1)
    #print(return_LastListElement(liste1))
    #print(return_FirstListElement(liste1))
    #print(list_slicing1(liste1))
    #print(list_slicing2(liste1))
    #print(list_slicing3(liste1))
    print(list_comprehensions(liste1,liste2))
    print(list_comprehensions2(liste1,liste2))
    list_multidimensional()


def fill_List(liste1):
    liste1 = ["gut", "hilfreich", "besser", "optimal"]
    return liste1

def fill_List2(liste1):
    liste1 = [1, 2, 3, 4, 5, 6, 7, 8]
    return liste1

def set_List2(liste1):
    liste2 = set(liste1)
    return liste2

def print_List(liste):
    print(liste)    

def return_LastListElement(liste):
    #Ausgabe "optimal"
    return liste[-1]

def return_FirstListElement(liste):
    #Ausgabe "gut"
    return liste[0]    

def list_slicing1(liste):
    #Ausgabe "hilfreich, besser"
    #Doppelpunkt bedeutet List Slicing
    return liste[1:3]

def list_slicing2(liste):
    #Ausgabe "gut, hilfreich, besser"
    #Es wird alles ausgegeben bis auf den letzten Eintrag
    #0 kann in diesem Fall auch weggelassen werdden
    return liste[0:-1]
    
def list_slicing3(liste):
    #Ausgabe "hilfreich, besser, optimal"
    #bis auf den ersten Wert wird alles ausgegeben
    return liste[1:]    

def list_comprehensions(liste1 , liste2):
    for x in liste1:
        liste2.append(x*x)
    return liste2    

def list_comprehensions2(liste1, liste2):
    return [x * x for x in liste1]

def list_multidimensional():
    #mehrdimensionale Liste
    liste3 = [
        ["Berlin", "München", "Köln"],
        ["Budapest", "Pecs", "Sopron"]
    ]

    #Ausgabe von Teil1
    part1 = liste3[0]

    #Ausgabe Berlin von Teil1
    city1 = liste3[0][0]

def listsInDictionaries():
    #Listen in Dictionaries
    students = {
        "Informatik": ["Max", "Monika"],
        "BWL": ["Erik", "Franziska"]
    }

    #Ausgabe von Liste Informatik -> Ausgabe lautet Max und Monika
    print(students["Informatik"])


start_main()
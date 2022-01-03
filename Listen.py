def start_main():
    liste1 = []
    liste1 = fill_List(liste1)
    print_List(liste1)
    print(return_LastListElement(liste1))
    print(return_FirstListElement(liste1))
    print(list_slicing1(liste1))
    print(list_slicing2(liste1))
    print(list_slicing3(liste1))

def fill_List(liste1):
    liste1 = ["gut", "hilfreich", "besser", "optimal"]
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
    return liste[1:3]

def list_slicing2(liste):
    #Ausgabe "gut, hilfreich, besser"
    #Es wird alles ausgegeben bis auf den letzten Eintrag
    #0 kann in diesem Fall auch weggelassen werdden
    return liste[0:-1]
    
def list_slicing3(liste):
    #Ausgabe "hilfreich, besser, optimal"
    
    return liste[1:]    
start_main()
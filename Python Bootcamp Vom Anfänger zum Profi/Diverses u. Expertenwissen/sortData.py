def main():
    #methode1()
    #methode2()
    methode3()

# %%
def methode1():
    l = ["Max", "Monika", "Erik", "Franziska"]

    #reverse Parameter beeinflusst die Reihenfolge, hier jetzt Absteigend
    l.sort(reverse=True)
    print(l)
    print(get_length(l))



def get_length(item):
    return len(item)


def methode2():
    #Sortiert nach Anzahl der Zeichen pro Name
    l = ["Max", "Monika", "Erik", "Franziska"]
    #get_lenth ohne Klammern
    l.sort(key=get_length)

    #kürzere Schreibweise, hier übergebe ich Python die Len Funktion als Schlüsselbegriff
    #l.sort(key=len)
    print(l)

def methode3():
    #Hier werden die Keys von dem Dictionary sortiert
    d = {"Köln":"CGN", "Budapest": "BUD", "Saigon": "SGN"}
    #die Sorted Funktion erstellt eine neue Liste / Dictionary
    print(sorted(d))
    print(d)

main()
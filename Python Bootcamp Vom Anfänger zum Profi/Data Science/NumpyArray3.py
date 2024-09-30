import numpy as np

a = np.array([1, 2, 3])

print(a * 2)
#Ausgabe: [2 4 6]


class MyArray():
    def __init__(self, liste):
        self.liste = liste

    #spezielle Methode die bei dem * Zeichen aufgerufen wird
    def __mul__(self, other):
        nListe = []
        for element in self.liste:
            nListe.append(element * other)
        return MyArray(nListe)

a = MyArray([1,2,3])
b = a * 2
#__mul__ Methode wird aufgerufen und es wird die 2 als Parameter übergeben

print(b.liste)
class Cube():
    #Konstruktor, bei dem mit "side" die Kantenlänge definiert wird
    def __init__(self, side):
        self.side = side

    def surface(self) -> int:
            return self.side ** 2 * 6
    
    def volume(self) -> int:
            return self.side **3
    
#eine Instanz der Cube Klasse wird erstellt mit der Kantenlänge 3
a = Cube(3)

#testen der Methoden
print(a.surface())

print(a.volume())
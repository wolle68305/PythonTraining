#Statische Variablen

class Car():
    #die Variable bzw. der Wert hängt dann nur an jeder einzelnen Instanz die durch Car erstellt wird
    def __init__(self) -> None:
        self.price = "expensive"

c = Car()
print(c.price)
c.price = "cheap"
print(c.price)
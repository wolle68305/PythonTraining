def main():
    book = PhoneBook()
    book.add("Mustermann", "+4912345")
    book.add("Müller", "+49678910")

    print(book.get("Mustermann"))
    print(book)
    print(len(book))

class PhoneBook():
    def __init__(self):
        #im Konstruktor wird ein privates Dictionary erstellt, auf das nur innerhalb der Klasse zugegriffen werden kann
        self.__entries = {}

    def add(self, name, phone_numnber):
        self.__entries[name] = phone_numnber    

    def get(self, name):
        if name in self.__entries:#
            return self.__entries[name]
        else:
            return None    

    def __str__(self):
         #Diese Funktion wird mit dem Befehl "print(book)" in der main() Methode aufgerufen
         #Alternative zum Debuggen
         return "PhoneBook(" + str(self.__entries) + ")"  

    def __repr__(self):
         #Diese Funktion sollte zusätzlich zu __str__ geschrieben werden, man kann diese ggf. über "nur" book aufrufen         
         #Die Funktion ruft entsprechend die Funktion __str__ auf um redundanten Code zu vermeiden
         return self.__str__()  
    
    def __len__(self):
        #Gibt die Anzahl der Einträge zurück die sich in dem Dictionary befinden
        #ohne diese Funktion funktioniert die "len"-Funktion im Main() Bereich nicht
        return len(self.__entries)
main()        
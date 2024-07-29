def main():
    methode1()
    methode2()
    methode3()
    methode4()


def methode1():
    #gibt das Wort "Hallo" fünf mal aus
    multi_print(5)

    #alternative Möglichkeit einen Parameter zu übergeben, hier gibt man an, welchem Parameter man welchen Wert übergibt
    #hier wird dreimal Welt ausgegeben
    multi_print(word="Welt")

#number und word bekommen einen Default Wert zugewiesen, falls kein Übergabeparameter geliefert wird
def multi_print(number = 3, word = "Hallo"):
    for i in range(0,number):
        print(word)

def methode2():
    l = [1,2,3]

    #der Methode "methode21" werden die jeweiligen Listeneinträge als Parameter übergeben
    methode21(l[0], l[1], l[2])
    
    #Alternative Variante wäre die folgende, hier wird gesagt, teile die Liste in die verschiedenen Elemente auf und übergebe diese als Parameter
    methode21(*l)
    

def methode21(a, b, c):
    print(a)
    print(b)
    print(c)

def methode3():
    #Hier wird am Ende 7 ausgegeben
    print(methode31(1,2,3,4,5,6,7))

def methode31(*params):
    #mit "*params" muss ich dann nicht alle Parameter einzeln auflisten sondern bekomme hier dann ein Tupel mit den übergegebenen Werten
    print(params)
    #hier habe ich beim ersten Durchlauf die 1 in der Variable "current_max" stehen
    current_max = params[0]
    for item in params:
        if item > current_max:
            current_max = item
    return current_max

def methode4():
    methode41(key="value", key2="Value 2")

    d={"key": "Ich bin der Schlüssel", "param2": "Ich bin der Parameter"}
    #ACHTUNG: bei beiden Varianten müssen die Key Werte mit den Parameter Begriffen übereinstimmen
    #Variante 1 zum Ausgeben der Werte aus dem Dictionary
    method42(d["key"], d["param2"])

    #Variante 2
    method42(key = d["key"], param2=d["param2"])

    #Variante 3
    method42(**d)


def methode41(**args):
    #die Methode bekommt als Parameter ein Dictionary übergeben
    #Ausgabe "{'key': 'value', 'key2':'Value 2'}"
    print(args)

def method42(key, param2):
    print(key)
    print(param2)


main()
import queue

def main():
    #Queue verhält sich wie eine Warteschlange
    q = queue.Queue()

    #PriorityQueue sortiert die Werte in der Queue nach Dringlichkeit (je niedriger der erste Werte ist, desto dringlicher ist der Wert)
    pq = queue.PriorityQueue()

    q.put("Hallo")
    q.put("Welt")
    q.put("Hallo")
    q.put("Mars")

    #erster Wert bestimmt die Dringlichkeit
    pq.put((10, "Hallo Welt"))
    pq.put((15, "Mars"))
    pq.put((5, "Wichtig"))

    methode1(q)
    methode2(q)
    methode3(pq)
    methode4()

def methode1(q):
    #gibt das Objekt q aus
    print(q)

    #gibt "Hallo" aus und entfernt es daran aus der Queue
    print(q.get())

    #gibt Welt aus, da "Hallo" davor aus der Queue entfernt wurde
    print(q.get())

def methode2(q):
    #gibt alle Werte der Queue aus bis die Queue leer ist
    #in diesem Fall existieren nur noch zwei Werte in der Queue, nämlich "Hallo" und "Mars"
    print(q.qsize())
    while not q.empty():
        element = q.get()
        print(element)

def methode3(pq):
    #es wird als erstes "Wichtig" ausgegeben, da es die niedrigste Dringlichkeitszahl hat
    print(pq.get())

def methode4():
    #zählt die gleichen Buchstaben zusammen in einem Dictionary und danach werden die Buchstaben inkl. Anzahl der gleichen Buchstaben in eine Priority Queue geschrieben
    #Wenn man eine absteigende Sortierung haben möchte, dann muss ein "-" vor den number Parameter in der "put" Methode
    text = "A A A A B B B C C C C C C C D D D D D E E E E E E E"
    d= {}

    for word in text.split(" "):
        if word in d:
           d[word] = d[word] + 1     
        else:
            d[word] = 1
    pq = queue.PriorityQueue()
    for word, number in d.items():
        pq.put((number, word))

    print(pq.get())

main()
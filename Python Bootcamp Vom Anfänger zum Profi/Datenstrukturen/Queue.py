import queue

#Queue verhält sich wie eine Warteschlange
q = queue.Queue()

q.put("Hallo")
q.put("Welt")
q.put("Hallo")
q.put("Mars")

#gibt das Objekt q aus
print(q)

#gibt "Hallo" aus und entfernt es daran aus der Queue
print(q.get())

#gibt Welt aus, da "Hallo" davor aus der Queue entfernt wurde
print(q.get())
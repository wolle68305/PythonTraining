#bei einem Set kann die Sortierung verloren gehen, bei einer Liste ist eine Sortierung gegeben

def main():
    #method1()
    method2()

def method1():
    s = {"Hallo", "Welt"}
    print(s)
    s.add("Mars")
    print(s)

    #das Wort Hallo existiert schon in dem Set und wird daher nicht nochmal hinzugefügt
    s.add("Hallo")
    print(s)

    if "Mars" in s:
        print("das Wort existiert in s")

def method2():
    text = "Hallo Welt Hallo Mars Hallo Welt"
    
    #mit set() erstelle ich ein neues leeres Set -> nur {} ist belegt für ein Dictionary
    s = set()
    for word in text.split(" "):
        if word not in s:
            print(word)
        s.add(word)
    print(s)  
    print(len(s                                             ))  
        

main()
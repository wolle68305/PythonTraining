import os
def main():
    #pathToFile = "/home/daniel/TransferSynology/Python Training/gaeste.txt"
    pathToFile = pathJoiner()
    print(pathToFile)
    
    #method1(pathToFile)
    #method2(pathToFile)
    #method3(pathToFile)
    #method4(pathToFile)
    #method5(pathToFile)
    #getCurrentFolderLocation()
    #pathJoiner()
    


def method1(pathToFile):
    f = open(pathToFile , "r")
    print(f.read())

def method2(pathToFile):
    #Ausgeben der ganzen Datei
    #UTF-8 untersützt alle Codierungen also auch Umlaute etc.
    with open(pathToFile, 'r', encoding='utf-8') as file:
        print(file.read())

def method3(pathToFile):
    #Datei wird Zeile für Zeile durchlaufen
    #file ist nur innerhalb von with verfügbar
    with open(pathToFile, 'r', encoding='utf-8') as file:
        for line in file:
            print("---")
            print(line)

def method4(pathToFile):
    #Datei wird Zeilenweise durchlaufen und in einem String ausgegeben
    #.strip() entfernt den Zeilenumbruch als auch Leerzeichen und Tabulator hinter und vor dem Werte der in der Variable name steht
    with open(pathToFile, 'r', encoding='utf-8') as file:
        for name in file:
            print("---")
            text = f"Hallo {name.strip()}, \n\n" + \
                    "Ich möchte dich gerne zu meinem Geburtstag einladen. \n\n" + \
                    "Viele Grüße"
            print(text)

def method5(pathToFile):
    with open(pathToFile, 'r') as file:
        print(file.read())            

def getCurrentFolderLocation():
    print(os.getcwd())

def pathJoiner() -> str:
    #verbindet einen Path als Zeichenkette (z.B. wenn ein Unterordner existiert)
    #diese Methode setzt dann abhängig vom OS automatisch ein / oder ein \ ein
    #print(os.path.join('/home' ,'daniel', 'TransferSynology', 'Python Training' , 'gaeste.txt'))
    return os.path.join('/home' ,'daniel', 'TransferSynology', 'Python Training' , 'gaeste.txt')

main()
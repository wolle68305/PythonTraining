import os
#from os import listdir

def main():
    #pathToFile = "/home/daniel/TransferSynology/Python Training/gaeste.txt"
    pathToFolder = pathFolderJoiner()
    method1('.')
    method1(pathToFolder)
    method2(pathToFolder)
    #method3(pathToFolder)
    
    #gibt den Pfad der aktuellen Datei zurück
    print(__file__)
    
    
def method1(pathToFolder):    
    #listet alle Dateien auf in einem Ordner als Sammlung
    print(os.listdir(pathToFolder))

def method2(pathToFolder):
    #listet einzeln alle Dateien auf, die sich in dem Ordner befinden
    for file in os.listdir(pathToFolder):
        print(file)
        print(os.)

def method3(pathToFolder):
    print(os.path.join(pathToFolder,"TestOrdner"))
    
    #prüfen, ob der Ordner existiert
    #Alternativ wäre "os.path.isDir()"
    if os.path.exists(os.path.join(pathToFolder,"TestOrdner")):
        print("Ordner existiert schon")
    else:    
        os.mkdir(os.path.join(pathToFolder,"TestOrdner"))
        print("Ordner erstellt")

def pathFolderJoiner() -> str:
    #liefert den Pfad des Ordners zurück
    #verbindet einen Path als Zeichenkette (z.B. wenn ein Unterordner existiert)
    #diese Methode setzt dann abhängig vom OS automatisch ein / oder ein \ ein
    #print(os.path.join('/home' ,'daniel', 'TransferSynology', 'Python Training' , 'gaeste.txt'))
    return os.path.join('/home' ,'daniel', 'TransferSynology', 'Python Training', 'Aufraeumen')


main()
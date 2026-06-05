import os
import time
import csv

#fileName = "C:\"
def main():
    testPath = pathFolderJoiner()

    with open(pathFileJoiner(), "w", newline='') as csvFile:
        readOutFolder(testPath, csvFile)
    
    
def readOutFolder(vS_Path, csvFile):
    for file in os.listdir(vS_Path): 
        if os.path.isfile(vS_Path + '/' + file):
            try:
                modifiedDate = time.ctime(os.path.getmtime(vS_Path + '/' + file))
                wr = csv.writer(csvFile, delimiter=';',quoting=csv.QUOTE_ALL)
                wr.writerow([vS_Path + '/' + file + ';' + modifiedDate])
            except Exception as errorMessage:
                print(errorMessage)
                info = file
                print(info)
            #print(vS_Path + '/' + file + ';' + modifiedDate)
        else:
            readOutFolder(vS_Path + '/' + file, csvFile)

def pathFolderJoiner() -> str:
    #liefert den Pfad des Ordners zurück
    #verbindet einen Path als Zeichenkette (z.B. wenn ein Unterordner existiert)
    #diese Methode setzt dann abhängig vom OS automatisch ein / oder ein \ ein
    #print(os.path.join('/home' ,'daniel', 'TransferSynology', 'Python Training' , 'gaeste.txt'))
    #return os.path.join("PFAD")
    return "Test"

def pathFileJoiner() -> str:
    #liefert den Pfad des Ordners zurück
    #verbindet einen Path als Zeichenkette (z.B. wenn ein Unterordner existiert)
    #diese Methode setzt dann abhängig vom OS automatisch ein / oder ein \ ein
    #print(os.path.join('/home' ,'daniel', 'TransferSynology', 'Python Training' , 'gaeste.txt'))
    #return os.path.join("PFAD")
    return "Test"

main()
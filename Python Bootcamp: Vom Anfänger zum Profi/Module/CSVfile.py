import csv
import os

def main():
    #pathToFile = "/home/daniel/TransferSynology/Python Training/gaeste.txt"
    pathToFolder = pathFolderJoiner()
    method1(pathToFolder)

    

def method1(pathToFolder):
        with open(pathToFolder, newline='') as csvfile:
             spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
             for row in spamreader:
                  print(' '.join(row))



def pathFolderJoiner() -> str:
    #liefert den Pfad des Ordners zurück
    #verbindet einen Path als Zeichenkette (z.B. wenn ein Unterordner existiert)
    #diese Methode setzt dann abhängig vom OS automatisch ein / oder ein \ ein
    #print(os.path.join('/home' ,'daniel', 'TransferSynology', 'Python Training' , 'gaeste.txt'))
    return os.path.join('/home' ,'daniel', 'TransferSynology', 'Python Training','Mappe1.csv')


main()
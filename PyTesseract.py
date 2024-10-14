import os
import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image
#from os import listdir

def main():
    #pathToFile = "/home/daniel/TransferSynology/Python Training/gaeste.txt"
    pathToFolder = pathFolderJoiner()
    
    image = cv2.imread(pathToFolder)

    string = pytesseract.image_to_string(image)

    print(string)
    
    


def pathFolderJoiner() -> str:
    #liefert den Pfad des Ordners zurück
    #verbindet einen Path als Zeichenkette (z.B. wenn ein Unterordner existiert)
    #diese Methode setzt dann abhängig vom OS automatisch ein / oder ein \ ein
    #print(os.path.join('/home' ,'daniel', 'TransferSynology', 'Python Training' , 'gaeste.txt'))
    return os.path.join('/home' ,'daniel', 'TransferSynology', 'Python Training', 'IMG_0618.PNG')


main()
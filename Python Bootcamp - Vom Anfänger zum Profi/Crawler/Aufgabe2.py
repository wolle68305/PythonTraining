import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import csv
import os

#Objektorientierte Methode

def main():
    url = "https://python.beispiel.programmierenlernen.io/index.php"
    pathToFolder = pathFolderJoiner()
    writeCSV(pathToFolder, url)
    

class ArticleFetcher():
    def fetch(self, url):
        
        time.sleep(1)
        print(url)
        r = requests.get(url)
        #Webseite läuft durch den BeautifulSoup
        doc = BeautifulSoup(r.text, "html.parser")
        
        #hier wird das crawled Object in eine Liste geschrieben und diese wird am Ende das ausgegeben
        
        nexturl = ""
        for navigation in doc.select(".navigation"):
            nexturl = urljoin(url,navigation.select_one(".btn-primary").attrs["href"])
        
        return nexturl     

def pathFolderJoiner() -> str:
    #liefert den Pfad des Ordners zurück
    #verbindet einen Path als Zeichenkette (z.B. wenn ein Unterordner existiert)
    #diese Methode setzt dann abhängig vom OS automatisch ein / oder ein \ ein
    #print(os.path.join('/home' ,'daniel', 'TransferSynology', 'Python Training' , 'gaeste.txt'))
    return os.path.join('/home' ,'daniel', 'TransferSynology', 'Python Training','Mappe1.csv') 


def writeCSV(pathToFolder, url):
    fetcher = ArticleFetcher()
    with open(pathToFolder, 'w', newline='', encoding='utf-8') as csvfile:
        urlWriter = csv.writer(csvfile,delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        for urlObject in fetcher.fetch(url):
            while urlObject != "":                                                             
                urlWriter.writerow([urlObject])   
main()    
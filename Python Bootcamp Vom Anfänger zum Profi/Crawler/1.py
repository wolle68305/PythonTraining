import requests
from bs4 import BeautifulSoup

def main():
    r = requests.get("https://python.beispiel.programmierenlernen.io/index.php")
    #Webseite läuft durch den BeautifulSoup
    doc = BeautifulSoup(r.text, "html.parser")
    #method1(r)
    #method2(r)
    #method3(doc)
    #method4(doc)
    #method5(doc)
    #method6(doc)
    #method7(doc)
    #method8(doc)
    method9(doc)

def method1(r):
    #zeigt mir alle Eigenschaften von dem r Object an
    print(r.__dict__)

def method2(r):
    #Ausgabe HTML Code der Seite
    print(r.text)

def method3(doc):
    print(doc)

def method4(doc):
    #gibt mir alle P-Elemente (<p>) zurück, die sich auf der Webseite befinden
    print(doc.find_all("p"))

def method5(doc):
    #durchläuft alle p Elemente
    for p in doc.find_all("p"):
        #print(p)
        #Ausgabe nur Text der P Elemente
        print(p.text)
        #Ausgabe des Attributes (class) von dem jeweiligen P Element 
        print(p.attrs)

def method6(doc):
    #gib mir alle Elemente mit der Class  "card" zurück
    print(doc.select(".card"))
    
def method7(doc):
    for card in doc.select(".card"):
        print(card.select_one(".emoji").text)

def method8(doc):
    #gibt mir alle <span> Elemente innerhalb eines Bereiches mit der Class "card-title"
    for span in doc.select(".card-title span"):
        print(span)

def method9(doc):
    for card in doc.select(".card"):
        emoji = card.select_one(".emoji").text
        content = card.select_one(".card-text").text
        title = card.select(".card-title span")[1].text
        picture  = card.select_one("img")
        print(emoji)
        print(title)
        print(content)
        #greift bei dem Picture Element auf das Attribute src zu
        print(picture.attrs["src"])


main()    
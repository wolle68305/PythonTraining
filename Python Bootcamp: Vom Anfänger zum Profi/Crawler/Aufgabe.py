import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

#Objektorientierte Methode

def main():
    url = "https://python.beispiel.programmierenlernen.io/index.php"
    #r = requests.get("https://python.beispiel.programmierenlernen.io/index.php")
    #Webseite läuft durch den BeautifulSoup
    #doc = BeautifulSoup(r.text, "html.parser")
    #method1(doc)
    #method2(doc)
    fetcher = ArticleFetcher()
    #fetcher.fetch()

    i = 1
    while url != "":
        url = fetcher.fetch(url)
        #i += 1

    #for article in fetcher.fetch(url):
    #    print(article.picture)











def method1(doc):    
    for card in doc.select(".card"):
        emoji = card.select_one(".emoji").text
        content = card.select_one(".card-text").text
        title = card.select(".card-title span")[1].text
        picture  = card.select_one("img")
        
        #hier wird ein Object "crawled" erstellt und diesem Objekt werden die entsprechenden Initialwerte übergeben
        crawled = CrawledArticle(emoji, content, title, picture)

        print(crawled.emoji)
        
def method2(doc):    
    #hier wird das crawled Object in eine Liste geschrieben und diese wird am Ende das ausgegeben
    articles = []
    for card in doc.select(".card"):
        emoji = card.select_one(".emoji").text
        content = card.select_one(".card-text").text
        title = card.select(".card-title span")[1].text
        picture  = card.select_one("img")
        
        #hier wird ein Object "crawled" erstellt und diesem Objekt werden die entsprechenden Initialwerte übergeben
        crawled = CrawledArticle(emoji, content, title, picture)

        articles.append(crawled)

    for article in articles:
         print(article.emoji)        

class CrawledArticle:
    def __init__(self,emoji, content, title, picture):
        self.emoji = emoji
        self.content = content
        self.title = title
        self.picture = picture

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
            #content = card.select_one(".card-text").text
            #title = card.select(".card-title span")[1].text
            #picture  = card.select_one("img")
            
            #urljoin berechnet mithilfe der Website URL und dem relativen Link zu dem Bild den richtigen Pfad zu dem Bild
            #äpicture  = urljoin(url, card.select_one("img").attrs["src"])
            
            #hier wird ein Object "crawled" erstellt und diesem Objekt werden die entsprechenden Initialwerte übergeben
            #crawled = CrawledArticle(emoji, content, title, picture)

            #articles.append(crawled)
        return nexturl       

main()    
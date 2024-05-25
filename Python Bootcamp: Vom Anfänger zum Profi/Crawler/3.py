import requests
from urllib.parse import urljoin

#urljoin berechnet mithilfe der Website URL und dem relativen Link zu dem Bild den richtigen Pfad zu dem Bild
url = urljoin("http://python.beispiel.programmierenlernen.io/index.php","./img/1.jpg")
print(url)
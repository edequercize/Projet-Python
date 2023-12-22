import requests
from bs4 import BeautifulSoup

url = "http://www.memoire-du-cyclisme.eu/eta_tdf/tdf1982.php"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Recherche des éléments contenant les informations des étapes
stages = soup.find_all('b')  # Les noms des gagnants semblent être en gras

for stage in stages:
    if "km" in stage.text:  # Identifier les lignes contenant les informations des étapes
        winner_info = stage.find_next('b').text.strip()  # Le gagnant est le prochain élément en gras
        print(winner_info)
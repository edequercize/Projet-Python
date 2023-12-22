import requests
from bs4 import BeautifulSoup
import csv

# URL de la page web
url = "https://ledicodutour.com/coureurs/coureurs/coureurs_e/echave.html"

# Récupération du contenu de la page
response = requests.get(url)
html_content = response.content

# Parsing du contenu HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Extraction du nom du coureur
nom_du_coureur = soup.find('h1').get_text(strip=True)
# Remplacer les virgules et les espaces superflus
nom_formate = nom_du_coureur.replace(',', '').replace('  ', ' ').strip()
nom_formate = nom_formate.replace(' dans le Tour de France', '')
# Préparation des données à enregistrer
data_to_save = []
data_to_save.append([nom_formate])

# Extraction des informations et ajout du nom formaté à chaque ligne
infos_td511 = soup.find_all("td", class_="td511")
for info in infos_td511:
    text = info.get_text(strip=True)
    if "Participations au Tour" in text or "Victoire d'étape" in text or "Jour en maillot jaune" in text or "Passages en tête à un col" in text:
        data_to_save.append([text])

# Nom du fichier CSV
filename = "data_coureur_tdf.csv"

# Écriture des données dans un fichier CSV
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in data_to_save:
        csvwriter.writerow(row)
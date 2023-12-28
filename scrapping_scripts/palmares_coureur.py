import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

# Lire le fichier CSV contenant les noms des coureurs
coureur_tdf = pd.read_csv("TDF_Riders_History.csv")

# Liste des noms des coureurs

coureur_tdf['Rider'] = coureur_tdf['Rider'].str.title()
noms_coureurs = list(set(coureur_tdf.iloc[:, 2].tolist()))


def format_nom_url(nom):
    mots = nom.split()
    nom_famille = mots[-1].lower()
    if len(mots) > 1 and mots[-2][0].isupper():
        nom_famille = f"{mots[-2].lower()}_{nom_famille}"
    return nom_famille

# Préparation des données à enregistrer
data_to_save = []

# Boucle sur les noms des coureurs
for nom_coureur in noms_coureurs:
    # Construction de l'URL
    url = f"https://ledicodutour.com/coureurs/coureurs/coureurs_{nom_coureur[0].lower()}/{format_nom_url(nom_coureur)}.html"

    try:
        # Récupération du contenu de la page
        response = requests.get(url, verify=False)
        html_content = response.content

        # Parsing du contenu HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extraction et formatage du nom du coureur
        h1_element = soup.find('h1')
        if h1_element:
            nom_du_coureur = h1_element.get_text(strip=True).replace(' dans le Tour de France', '')
            print(f"Traitement de : {nom_du_coureur}")  # Log pour débogage

            # Extraction des informations
            infos_td511 = soup.find_all("td", class_="td511")
            for info in infos_td511:
                text = info.get_text(strip=True)
                if "Participations au Tour" in text or "Victoire d'étape" in text or "Jour en maillot jaune" in text or "Passages en tête à un col" in text:
                    data_to_save.append([text])
        else:
            print(f"Aucun élément 'h1' trouvé pour l'URL : {url}")

    except requests.exceptions.SSLError as e:
        print(f"Erreur SSL lors de l'accès à l'URL {url}: {e}")

# Nom du fichier CSV
filename = "palmares_tdf.csv"

# Écriture des données dans un fichier CSV
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in data_to_save:
        csvwriter.writerow(row)

print(f"Terminé. Les données ont été écrites dans {filename}")
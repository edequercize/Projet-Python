import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

# Création de la base de données et de la table
conn = sqlite3.connect('prix.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS laureats (
        id INTEGER PRIMARY KEY,
        nom TEXT,
        prix TEXT,
        annee TEXT
    )
''')
def scraper_wikipedia(nom):
    url = f"https://fr.wikipedia.org/wiki/{nom.replace(' ', '_')}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    resultats = []

    # Assuming the trophies are in a table with a specific class or id
    table = soup.find('table', {'class': 'your_table_class_here'})
    if table:
        rows = table.find_all('tr')
        for row in rows[1:]:  # Skip header row
            cols = row.find_all('td')
            if len(cols) > 2:  # Assuming at least 3 columns: Name, Prize, Year
                nom_scrape = cols[0].get_text().strip()
                prix = cols[1].get_text().strip()
                annee = cols[2].get_text().strip()

                cursor.execute('INSERT INTO laureats (nom, prix, annee) VALUES (?, ?, ?)', (nom_scrape, prix, annee))
                conn.commit()

                resultats.append([nom_scrape, prix, annee])

    return resultats

# Charger les données de coureurs du Tour de France
coureur_tdf = pd.read_csv("TDFF_Riders_History.csv")
colonne_noms_coureur = coureur_tdf.iloc[:, 2]

# Liste pour stocker les données de tous les coureurs
liste_coureur_tdf = [['nom','prix','annee']]

# Scraper les données pour chaque coureur et les ajouter à la liste
for nom in colonne_noms_coureur:
    nom_formatte = nom.title()  # Formater le nom si nécessaire
    resultats_nom = scraper_wikipedia(nom_formatte)
    liste_coureur_tdf.extend(resultats_nom)

# Fermeture de la connexion à la base de données
conn.close()

# Afficher les résultats (facultatif)
for ligne in liste_coureur_tdf:
    print(ligne)
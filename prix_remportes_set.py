import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd


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
    # Construire l'URL de Wikipedia (à adapter selon le format des URLs)
    url = f"https://fr.wikipedia.org/wiki/{nom.replace(' ', '_')}"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for item in soup.find_all('div', class_='prix_class'):
        nom = item.find('span', class_='nom_class').get_text()
        prix = item.find('span', class_='prix_class').get_text()
        annee = item.find('span', class_='annee_class').get_text()

        cursor.execute('INSERT INTO laureats (nom, prix, annee) VALUES (?, ?, ?)', (nom, prix, annee))

coureur_tdf = pd.read_csv("TDF_Riders_History.csv")

liste_coureur_tdf = [['nom','prix','annee']]

colonne_noms_coureur = coureur_tdf.iloc[:, 2]

for nom in colonne_noms_coureur:
    liste_coureur_tdf.append(scraper_wikipedia(nom))





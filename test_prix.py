import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

def scraper_wikipedia(nom):
    # Construire l'URL de Wikipedia
    url = f"https://fr.wikipedia.org/wiki/{nom.replace(' ', '_')}"
    print(f"URL: {url}")

    response = requests.get(url)
    print(f"Réponse HTTP: {response.status_code}")

    soup = BeautifulSoup(response.content, 'html.parser')
    for item in soup.find_all('div', class_='prix_class'):
        nom = item.find('span', class_='nom_class').get_text()
        prix = item.find('span', class_='prix_class').get_text()
        annee = item.find('span', class_='annee_class').get_text()

        print(f"Nom: {nom}, Prix: {prix}, Année: {annee}")

        cursor.execute('INSERT INTO laureats (nom, prix, annee) VALUES (?, ?, ?)', (nom, prix, annee))

# Connexion à la base de données SQLite
conn = sqlite3.connect('prix.db')
cursor = conn.cursor()

coureur_tdf = pd.read_csv("TDF_Riders_History.csv")
colonne_noms_coureur = coureur_tdf.iloc[:, 2]

for nom in colonne_noms_coureur:
    nom_formatte = nom.title() 
    scraper_wikipedia(nom_formatte)

# Exécuter une requête SQL pour sélectionner toutes les données de la table
query = "SELECT * FROM laureats"
df = pd.read_sql_query(query, conn)

# Afficher les premières lignes du DataFrame
print(df.head())
df.to_csv('prix_remportés.csv', index=False)
# Fermeture de la connexion à la base de données
conn.close()
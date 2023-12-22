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
    # Construire l'URL de Wikipedia
    url = f"https://fr.wikipedia.org/wiki/{nom.replace(' ', '_')}"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Liste pour stocker les données scrapées pour ce nom
    resultats = []

    # Trouver la table de palmarès - cela peut nécessiter des ajustements
    tables = soup.find_all('table', class_='wikitable')
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) > 1:  # Assurez-vous qu'il y a suffisamment de colonnes
                # Extraire les données de chaque colonne
                # Cela peut nécessiter des ajustements en fonction de la structure de la table
                prix = cols[0].get_text(strip=True)
                annee = cols[1].get_text(strip=True)

                # Ajouter les données dans la base de données SQLite
                cursor.execute('INSERT INTO laureats (nom, prix, annee) VALUES (?, ?, ?)', (nom, prix, annee))
                conn.commit()

                # Ajouter les données à la liste des résultats
                resultats.append([nom, prix, annee])

    # Retourner les résultats pour ce nom
    return resultats

# Charger les données de coureurs du Tour de France
coureur_tdf = pd.read_csv("TDF_Riders_History.csv")
colonne_noms_coureur = coureur_tdf.iloc[:, 2]

# Liste pour stocker les données de tous les coureurs
liste_coureur_tdf = [['nom','annee','prix']]

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

from test_prix3 import liste_coureur_tdf
print(liste_coureur_tdf)
# Convertir la liste en DataFrame
liste_coureur_tdf = pd.DataFrame(liste_coureur_tdf[1:], columns=liste_coureur_tdf[0])

# Sauvegarder le DataFrame dans un fichier CSV
liste_coureur_tdf.to_csv('prix_coureur_tdf', index=False)





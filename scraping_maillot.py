##########################################
#  Scrapping Wikipedia pour le Palmarès  #
##########################################

import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la page Wikipedia
url = "https://fr.wikipedia.org/wiki/Palmar%C3%A8s_du_Tour_de_France"

# Récupérer le contenu de la page
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Trouver le tableau "Palmarès complet"
table = soup.find('table', {'class': 'wikitable'})

# Extraire les données du tableau
rows = table.find_all('tr')
data = []
for row in rows:
    cols = row.find_all(['th', 'td'])
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

# Créer un DataFrame avec les données
df = pd.DataFrame(data)
df.columns = df.iloc[0]  # Définir la première ligne comme en-tête
df = df.drop(df.index[0])  # Supprimer la première ligne (en-tête)

# Sélectionner uniquement les colonnes souhaitées
selected_columns = ['Grand Prix de la montagne', 'Par points', 'Meilleur jeune', 'Prix de la combativité']
df_selected = df[selected_columns]

# Afficher le DataFrame
print(df_selected)

# Enregistrer le DataFrame dans un fichier CSV
df_selected.to_csv('palmares_tour_de_france_selected_columns.csv', index=False)


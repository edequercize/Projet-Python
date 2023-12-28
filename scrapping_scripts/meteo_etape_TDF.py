import pandas as pd
import requests
from bs4 import BeautifulSoup

# Fonction pour scraper la météo
def scrape_weather(year, stage):
    decade = f"{year[:3]}0_{year[:3]}9"
    url = f"http://www.memoire-du-cyclisme.eu/eta_tdf_{decade}/tdf{year}_{stage}.php"
    response = requests.get(url)
    if response.status_code != 200:
        return "Non disponible"
    soup = BeautifulSoup(response.content, 'html.parser')
    weather_search = soup.find_all(string=lambda text: "Météo :" in text)
    return weather_search[0].split(":")[1].strip() if weather_search else "Non disponible"

# Lecture du fichier CSV
df = pd.read_excel('C:/Users/Utilisateur/Documents/cours ENSAE/2A/1_semestre/projet_datascience_python/tour_de_france/dates_etapes.xlsx')



# Scraping de la météo pour chaque étape
df['Weather'] = df.apply(lambda row: scrape_weather(str(row['annee']), str(row['numero_etape'])), axis=1)

# Enregistrement du DataFrame mis à jour
df.to_excel('dates_etapes.xlsx', index=False)

print("Mise à jour du fichier Excel terminée.")
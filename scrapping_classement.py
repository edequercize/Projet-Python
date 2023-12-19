import requests
from bs4 import BeautifulSoup
import pandas as pd



def decennie(year):
    decen = []
    borne_inf = 0
    borne_supp = 0
    unite = year % 10
    milliers = year // 1000
    centaines = (year // 100) % 10
    dizaines = (year // 10) % 10
    if unite >= 7:
        borne_inf = milliers*1000 + centaines*100 + dizaines*10 + 7
        borne_supp = milliers*1000 + centaines*100 + (dizaines+1)*10 + 6
    else:
        borne_inf = milliers*1000 + centaines*100 + (dizaines-1)*10 + 7
        borne_supp = milliers*1000 + centaines*100 + dizaines*10 + 6
    return((borne_inf,borne_supp))




# Fonction pour extraire les vainqueurs d'une année donnée
def scrape_winners(year):
    url = f"https://ledicodutour.com/etapes/etapes_par_annees/etapes_{decennie(year)[0]}_{decennie(year)[1]}/etapes_{year}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    winners = []
    for tr in soup.find_all('tr'):
        cells = tr.find_all('td')
        if len(cells) > 1:
            stage_info = cells[1].get_text().strip()
            if 'Etape :' in stage_info:
                winner = stage_info.split(':')[1].strip()
                winners.append(winner)
    
    return winners

data = []

# Boucler sur chaque année
for year in range(1947, 2023):  # Modifier selon les années souhaitées
    winners = scrape_winners(year)
    for stage, winner in enumerate(winners, start=1):
        data.append({'Year': year, 'Stage': stage, 'Winner': winner})

# Créer le DataFrame
df = pd.DataFrame(data)

# Enregistrer dans un fichier CSV
df.to_csv('winners.csv', index=False)  # Nom de fichier modifié pour refléter le format CSV
print("Mise à jour du fichier CSV terminée.")
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


def scrape_winners(year):
    try:
        url = f"https://ledicodutour.com/etapes/classement_etapes/classement_etapes_{decennie(year)[0]}_{decennie(year)[1]}/classement_etapes_{year}.html"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Échec de la requête HTTP pour l'année {year}")
            return []

        soup = BeautifulSoup(response.content, 'html.parser')

        # Liste pour stocker les classements des étapes
        classements_etapes = []

        # Identifier les sections qui contiennent les classements d'étapes
        sections_etapes = soup.find_all('p', style=lambda value: value and 'color: rgb(0, 51, 255)' in value)

        for section in sections_etapes:
            # Extraire le texte de la section
            text = section.get_text(strip=True)
            # Diviser le texte pour séparer le nom de l'étape et le gagnant
            parts = text.split('-')
            if len(parts) >= 2:
                nom_etape = parts[0].strip()
                gagnant = parts[1].split('.')[0].strip()
                classements_etapes.append((nom_etape, gagnant))
            else:
                continue  # Passer à la section suivante si le format n'est pas correct

    except Exception as e:
        print(f"Erreur lors du scraping de l'année {year}: {e}")
        return []

    return classements_etapes

data = []

# Boucler sur chaque année
for year in range(1947, 2023):  # Modifier selon les années souhaitées
    winners = scrape_winners(year)
    for stage, winner in enumerate(winners, start=1):
        data.append({'Year': year, 'Stage': stage, 'Winner': winner})

# Créer le DataFrame
df = pd.DataFrame(data)

# Enregistrer dans un fichier CSV
df.to_csv('winners2.csv', index=False)  # Nom de fichier modifié pour refléter le format CSV
print("Mise à jour du fichier CSV terminée.")
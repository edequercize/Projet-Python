import pandas as pd

df = pd.read_excel("dates_etapes.xlsx")


# on considère qu'au mois de juin/juillet, le temps par défaut est le beau temps
df['Weather'] = df['Weather'].replace(["Non disponible", "", "\\", None], "beau temps")

# Enregistrer le DataFrame mis à jour
df.to_excel('C:/Users/Utilisateur/Documents/cours ENSAE/2A/1_semestre/projet_datascience_python/tour_de_france/dates_etapes.xlsx', index=False)

print("Mise à jour du fichier Excel terminée.")


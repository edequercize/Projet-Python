import pandas as pd

# Charger le fichier CSV existant
df = pd.read_csv('palmares_maillot.csv')

# Créer une liste d'années en excluant les périodes 1915-1918 et 1940-1946
annees = list(range(1903, 1915)) + list(range(1919, 1940)) + list(range(1947, 2024))

# Vérifier si la longueur des années correspond au nombre de lignes dans le DataFrame
if len(df) == len(annees):
    df['Année'] = annees
else:
    print("Erreur : Le nombre d'années ne correspond pas au nombre de lignes dans le DataFrame.")

# Enregistrer le DataFrame modifié dans un nouveau fichier CSV
df.to_csv('palmares_maillot.csv', index=False)
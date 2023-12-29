# Python pour la Data Science - Projet Tour de France (TDF)
> 1 semestre 2A ENSAE, IPP
Rascoussier Matthieu, Salomé C, Eloi de Quercize 

## Description du projet
Fichier principal : `Main_TDF.ipynb`

Tous les fichiers python dans le dossier scrapping_scripts ont permis de récolter des informations soit sur Wikipédia soit sur LeDicoduTour qui nous avait donné son accord pour utiliser les données de son site. Run ces codes peut prendre plus d'une heure, je recommande de ne pas les faire tourner.

**Étape 1 : Problématique - Prédiction du Tour de France (individuel et par équipes)**

Dans l'univers du cyclisme professionnel, remporter le Tour de France est le rêve de nombreux coureurs. Cette compétition demande une combinaison de compétences physiques, techniques et tactiques. Chaque édition du Tour de France offre un parcours de course différent, mais la structure générale reste inchangée, avec des étapes variées comprenant des sections de plat, des contre-la-montre et des ascensions en montagne.

La problématique centrale de cette étude se concentre sur la prédiction, en fonction de certaines caractéristiques, du profil du coureur susceptible de remporter le Tour de France, et quels sont les cyclistes pouvant y prétendre.

En se basant sur les données disponibles, cette recherche vise à répondre aux questions suivantes : Quels sont les facteurs cruciaux qui contribuent au succès individuel d'un coureur au Tour de France ? Comment ces caractéristiques varient-elles pour les équipes dans le cadre du classement par équipes ? Pour répondre à ces interrogations, une approche multidimensionnelle sera adoptée, prenant en compte des variables telles que les performances individuelles, grâce à certaines compétitions passées, les performances spécifiques à certaines étapes, la catégorie météo, et d'autres paramètres clés.

**Étape 2 : Recherche de données**

Pour mener à bien notre projet de prédiction du Tour de France (TDF), nous avons entrepris une recherche de données provenant de sources variées, fiables et autorisées.

*Base de données initiale (GitHub) :*

Nous avons débuté notre analyse en exploitant une base de données préexistante disponible sur GitHub, créée par thomascamminady et intitulée "TDF_Riders_History.csv". Cet ensemble de données initiales comprenait des informations sur les coureurs participant au Tour de France ainsi que leurs temps respectifs.

*Scraping des données sur Wikipedia :*

Afin d'enrichir notre base de données initiale, nous avons effectué un scrapping de la page Wikipedia dédiée au palmarès des coureurs du Tour de France. Cela inclut les victoires, les grands prix de la montagne, les classements par points, les distinctions du meilleur jeune et les prix de la combativité. Ces informations sont essentielles pour évaluer la performance et la polyvalence des coureurs.

*Scraping sur LeDicoDuTour :*

Nous avons également consulté le site LeDicoDuTour pour obtenir des détails précis sur les différentes étapes du Tour de France, classées par typologie (plat, montagne, etc.) et par année. Ces données nous permettent d'analyser les performances des coureurs et d'entraîner le modèle de prédiction.

*Scraping de la météo :*

La météo joue un rôle significatif dans les performances des cyclistes. Par conséquent, nous avons extrait des données météorologiques pertinentes du site http://www.memoire-du-cyclisme.eu/. Ces informations incluent les conditions météorologiques par étape du Tour de France, permettant une analyse approfondie des facteurs environnementaux influençant les résultats.

*Autorisations et remerciements :*

Nous avons pris soin d'obtenir toutes les autorisations nécessaires pour accéder et utiliser les données. En particulier, nous tenons à exprimer notre gratitude envers les contributeurs de www.memoire-du-cyclisme.eu et de LeDicoDuTour.com qui ont généreusement autorisé l'utilisation de leurs informations, ainsi qu'aux sites Web tels que Wikipedia.

**Étape 3 : Transformation des données**

La transformation des données est une étape cruciale dans le processus d'analyse et de modélisation. Elle vise à préparer les données brutes pour qu'elles soient exploitables par le modèle prédictif. Voici les principales étapes de transformation des données pour la prédiction du TDF:

*Chargement des bases de données et traitement des erreurs et des valeurs manquantes:*

On a débuté par télécharger les bases de données brutes depuis un drive public. Une fois que l'importation des différentes bases de données a été faite, il a fallu identifier et traiter les erreurs éventuelles dans les données. Cela peut inclure la correction de valeurs aberrantes ou la suppression de lignes contenant des erreurs ou des valeurs manquantes. 

Le fichier principal, "test_merge", a été dédié à la construction, au nettoyage, et à la génération de statistiques descriptives pour assurer la qualité des données utilisées dans le modèle prédictif.

*Fusion des bases de données et suppression des colonnes redondantes ou inutiles :*

L'identification les clés de jointure entre les différentes bases de données a ensuite permis de les fusionner en conséquence. Chaque colonne de chaque base de données a été analyée pour identifier les redondances ou qui n'apportaient pas de valeur significative à l'analyse. 

La première base de données, "coureur_tdf", a été soigneusement nettoyée en conservant des informations cruciales telles que le nom du coureur, le classement par année, l'équipe, le temps, l'année, la distance, etc. Une deuxième base de données, "prix_coureur_tdf", a été téléchargée et nettoyée, avec une attention particulière portée à la correction des erreurs de scraping concernant les gagnants des étapes et les porteurs du maillot jaune. 

*Création de nouvelles variables :*

La création d'un dictionnaire répertoriant les victoires des coureurs a permis d'améliorer la qualité des données, tandis qu'une fusion avec la première base de données a été réalisée pour intégrer ces informations. Cette fusion a conduit à la création d'une base de données consolidée, "merged_df", qui a ensuite fait l'objet d'un nettoyage approfondi.
Une colonne supplémentaire, "classement_equipe", a été créée pour évaluer les performances des équipes en agrégeant les trois temps les plus faibles des coureurs. Cela a contribué à définir le classement final des équipes.

Une fonction a été développée pour normaliser les classements d'équipes, fournissant ainsi une échelle entre 0 et 1, où 1 représente le classement le moins favorable. Cette normalisation facilitera la tâche du modèle lors de la prédiction.

Enfin, la base de données finale, "df_trie", a été sauvegardée au format CSV, comprenant des colonnes essentielles telles que le nom du coureur, le nombre de Tours de France, le nombre de victoires d'étapes, le nombre de jours en maillot jaune, l'équipe, l'année, la distance, le nombre d'étapes, les temps totaux, et d'autres caractéristiques pertinentes. Une fois ces étapes de transformation des données effectuées, l'ensemble de données est prêt à être utilisé dans le processus de modélisation pour la prédiction du Tour de France.

**Étape 4 : Statistiques Descriptives**

Dans cette étape, nous effectuons des analyses statistiques descriptives pour mieux comprendre nos données et évaluer la pertinence de l'application d'un modèle prédictif. Nous examinons plusieurs aspects clés liés au TDF et aux performances des coureurs et des équipes.

*Distribution des Caractéristiques Principales :*

1. Nombre de Victoires d'Étape (nbre_victoire_etape) : Analyse de la distribution du nombre de victoires d'étape parmi les coureurs.

2. Classement de l'Équipe (classement_equipe) : Distribution des classements des équipes tout au long des années du Tour.

3. Distance (distance_km) : Distribution des distances parcourues en kilomètres tout au long des années du Tour.

4. Nombre de Tours de France (nbre_tdf) : Distribution du nombre de Tours de France auxquels les coureurs ont participé.

*Relations entre les caractéristiques :*

1. Nombre de Victoires d'Étape vs Classement Général : Relation entre le nombre de victoires d'étape et le classement général pour identifier d'éventuelles corrélations.

*Évolution Temporelle des Équipes :*

1. Heatmap des Performances des Équipes depuis 2015 : Création d'une heatmap basée sur la base de données groupée par équipe, en se concentrant sur les années postérieures à 2015. Cette visualisation permet d'observer l'évolution des performances des équipes au fil du temps.

*Performances Individuelles des Coureurs :*

1. Base de Données par Coureur depuis 2010 : Graphiques illustrant les statistiques élémentaires depuis 2010, notamment la moyenne du classement individuel, le nombre de participations par coureur, la variance du classement individuel, et le meilleur classement individuel.

2. Base de Données Individuelle depuis 1980 : Base de données plus étendue depuis 1980 pour comprendre les tendances et les évolutions à plus long terme.

*Effet du Nombre de Participations sur le Meilleur Classement :*

1. Nuage de Points - Nombre de Participations vs Meilleur Classement Individuel depuis 1980 : Graphiques de l'effet du nombre de participations sur le meilleur classement individuel. Cette analyse permet de déterminer si une relation existe entre la fréquence de participation et les performances individuelles.

**Étape 5 : Modèles prédictifs**
 
Cette partie est l'aboutissement de notre projet. L'objectif est de tester différents modèles pour prédire au mieux les résultats individuels et par équipe du tour de France. 

1. On test différents modèles prédictifs (Linear Regression, Support Vector Regression, Decision Tree Regressor, Random Forest Regressor, Gradient Boosting Regressor) pour le rang des différents coureurs cyclistes. On obtient globalement des modèles satisfaisant, le meilleur étant le Random Forest Regressor.

2. On veut maintenant savoir quelles caractéristiques sont les plus importantes. Pour cela nous devons un modèle linéaire (Linear Regression). On obtient ensuite des résultats intéressants ! Etre le meilleur jeune ou gagner le grand prix de la montagne a un grand effet sur la victoire. En effet être un très bon grimpeur est connu pour être très important pour gagner le tour de France comme on peut le lire sur l'article suivant : https://www.pickx.be/fr/2071727/quel-est-le-profil-ideal-pour-gagner-le-tour-de-france.

3. Enfin nous ré-appliquons la méthode 1 pour essayer de prédire le résultat par équipe. Cette fois ci le meilleur modèle est le Gradient Boosting Regressor. Les indicateurs sont, comme pour le classement individuel, satisfaisants.

Tous les fichiers python  commençant par scrapping ont permis de récolter des informations soit sur Wikipédia soit sur LeDicoduTour qui nous avait donné son accord pour utiliser les données de son site. Run ces codes peut prendre plus d'une heure, je recommande de ne pas les faire tourner

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
Une fois que l'importation les différentes bases de données collectées lors de l'étape de recherche de données a été faite, il a fallu identifier et traiter les erreurs éventuelles dans les données. Cela peut inclure la correction de valeurs aberrantes ou la suppression de lignes contenant des erreurs, des valeurs manquantes. 

*Fusion des bases de données et suppression des colonnes redondantes ou inutiles :*
L'identification les clés de jointure entre les différentes bases de données a ensuite permis de les fusionner en conséquence. Chaque colonne de chaque base de données a été analyée pour identifier les redondances ou qui n'apportaient pas de valeur significative à l'analyse. La suppression des colonnes inutiles simplifie les données et améliore les performances du modèle.

Une fois ces étapes de transformation des données effectuées, l'ensemble de données est prêt à être utilisé pour la création du modèle prédictif.

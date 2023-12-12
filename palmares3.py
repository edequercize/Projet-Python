import requests
import urllib3
from bs4 import BeautifulSoup
import csv
import re 



# Liste des noms des coureurs (assurez-vous que cette liste est correctement définie)
noms_coureurs = [
    "Henri Abadie", "Djamolidine Abdoujaparov", "Jean Adriaenssens", "Mario Aerts",
    "Christophe Agnolutto", "Joaquim Agostinho", "Lucien Aimar", "Gonzalo Aja",
    "Julian Alaphilippe", "Robert Alban", "Raul Alcala", "Rudi Altig",
    "Kim Andersen", "Phil Anderson", "Henri Anglade", "Jacques Anquetil",
    "Jesus Aranzabal", "Moreno Argentin", "Luciano Armani", "Lance Armstrong",
    "Dominique Arnaud", "Dominique Arnould", "José Luis Arrieta", "Angel Arroyo",
    "Fabio Aru", "Kurt-Asle Arvesen", "Kasper Asgreen", "Mikel Astarloza",
    "Giancarlo Astrua", "John Lee Augustyn", "Magnus Backstedt", "Armand Baeyens",
    "Emile Baffert", "Pierino Baffi", "Jean-Claude Bagot", "Serge Baguet",
    "Federico Bahamontes", "Antonio Bailetti", "Jan Bakelants", "Luis Balague",
    "Fabio Baldato", "Ercole Baldini", "Alessandro Ballan", "Franco Balmamion",
    "Romain Bardet", "Warren Barguil", "Nicolas Barone", "Carlos Barredo",
    "Gino Bartali", "Vincent Barteau", "Ivan Basso", "Marino Basso",
    "Giovanni Battaglin", "Graziano Battistini", "Steve Bauer", "Gilbert Bauvin",
    "Pierre Bazzo", "Benoni Beheyt", "Vicente Belda", "Giancarlo Bellini",
    "Gilbert Bellone", "Joseba Beloki", "Nino Benedetti", "Daniele Bennati",
    "Sam Bennett", "Tiesj Benoot", "Louis Bergaud", "Natnael Berhane",
    "Egan Bernal", "Jean-François Bernard", "Jean-René Bernaudeau", "Lorenzo Bernucci",
    "Yvon Bertin", "Rubens Bertogliati", "Evgueni Berzin", "Paolo Bettini",
    "Pierre Beuffeuil", "Serafino Biagioni", "Pello Bilbao", "René Binggeli",
    "Laurent Biondi", "Franco Bitossi", "René Bittinger", "Jeroen Blijlevens",
    "Maurice Blomme", "Chris Boardman", "Edvald Boasson Hagen", "Stanislas Bober",
    "Louison Bobet", "Maciej Bodnar", "Udo Bolts", "Guido Bontempi",
    "Michael Boogerd", "Lars Boom", "Tom Boonen", "Gianluca Bortolami",
    "Jacques Bossis", "Santiago Botero", "Jean Bourles", "Albert Bourlon",
    "Miguel Bover", "Eric Boyer", "Ferdinand Bracke", "Pierre Brambilla",
    "Frans Brands", "Jean Brankart", "Beat Breu", "Erik Breukink",
    "Laurent Brochard", "Dino Bruni", "Joseph Bruyère", "Johan Bruyneel",
    "Hernan Buenahora", "Gianni Bugno", "Marcus Burghardt", "Emmanuel Busto",
    "Francisco Cabello", "Samuel Cabrera", "Norbert Callens", "Lilian Calmejane",
    "Sylvain Calzati", "Angel Camargo", "Fermo Camellini", "Francis Campaner",
    "Juan Campillo", "David Canada", "Fabian Cancellara", "Louis Caput",
    "Richard Carapaz", "Félix Cardenas", "Guido Carlesi", "Andrea Carrea",
    "Damiano Caruso", "Francisco Casagrande", "Sandy Casar", "Jimmy Casper",
    "Davide Cassani", "Francis Castaing", "Juan-Carlos Castillo", "Nino Catalano",
    "José Catieau", "Mattia Cattaneo", "Mark Cavendish", "Robert Cazala",
    "Bruno Cengh","Bruno Cenghialta", "Pino Cerami", "André Chalmel", "Georges Chappe", "Anthony Charteau", "Sylvain Chavanel",
    "Philippe Chevallier", "Claudio Chiappucci", "Franco Chioccioli", "Eduardo Chozas", "Adolf Christian",
    "Giulio Ciccone", "Mario Cipollini", "Simon Clarke", "Thierry Claveyrolat", "Régis Clère", "Juan José Cobo Acebo",
    "Stefano Colage", "Jean-Claude Colotti", "Salvatore Commesso", "Luciano Conati", "Alberto Contador",
    "Roberto Conti", "Silvano Contini", "Baden Cooke", "Fausto Coppi", "Thierry Cornillet", "Giovanni Corrieri",
    "Magnus Cort Nielsen", "Benoît Cosnefroy", "Rui Alberto Costa", "Laudelino Cubino", "Steve Cummings",
    "Carlos Da Cruz", "Acacio Da Silva", "José Da Silva", "Emile Daems", "Michele Dancelli",
    "Jean-Pierre Danguillaume", "Tom Danielson", "André Darrigade", "Wilfried David", "Roger De Breuker",
    "Alfred De Bruyne", "Peter De Clercq", "Roger De Cnijf", "Thomas De Gendt", "Daan De Groot",
    "Alessandro De Marchi", "Johan De Muynck", "Tommaso De Pra", "Johan De Roo", "Théo De Rooy",
    "Jos De Schoenmaecker", "Eric De Vlaeminck", "Roger De Vlaeminck", "Etienne De Wilde", "Ronald De Witte",
    "Fons De Wolf", "Steve De Wolf", "Georges Decaux", "Nino Defilippis", "John Degenkolb", "Michel Dejouhannet",
    "Erik Dekker", "Hans Dekkers", "David De La Fuente", "Mickaël Delage", "José Del Ramo", "Ludo Delcroix",
    "Adolphe Deledda", "Régis Delépine", "Pedro Delgado", "Gilles Delion", "Raymond Delisle", "Arnaud Démare",
    "Marc Demeyer", "Serge Demierre", "Fedor Den Hertog", "Rohan Dennis", "Willy Derboven", "Germain Derijcke",
    "Laurent Desbiens", "Armand Desmet", "Gilbert Desmet", "Cyril Dessel", "André Desvasges", "Hendrik Devos",
    "Rudy Dhaenens", "Mariano Diaz", "Jan Diederich", "Ludo Diercksens", "Walter Diggelmann", "Rémy Di Gregorio",
    "Danilo Di Luca", "Maurice Diot", "Jean-Philippe Dojwa", "Manuel Jorge Dominguez", "Custodio Dos Reis",
    "Jean Dotto", "Jean-Pierre Ducasse", "Gilbert Duclos-Lassalle", "Maarten Ducrot", "Laurent Dufaux",
    "Jean Dumont", "Samuel Dumoulin", "Tom Dumoulin", "Jacky Durand", "Adriano Durante", "Kristijan Durasek",
    "Marcel Dussault", "Léo Duyndam", "Martin Earley", "Federico Echave", "Vladimir Efimkin", "Viatcheslav Ekimov",
    "Alberto Elli", "Seamus Elliott", "Jan Engels", "José Maria Errandonea", "Fernando Escartin", "Jacques Esclassan",
    "David Etxebarria", "Cadel Evans", "Caleb Ewan", "Henk Faanhof", "Edouard Fachleitner", "Alessandro Fantini",
    "Tyler Farrar", "Vito Favero", "Pierrick Fédrigo", "Brice Feillu", "Romain Feillu", "Gianni Ferlenghi",
    "Juan Fernandez", "Paulo Ferreira", "Giuseppe Fezzardi", "Giovanni Fidanza", "Laurent Fignon",
    "Juan Antonio Flecha","Robert Forest", "Jean Forestier", "Dominique Forlini", "Omar Fraile Mattaranz",
    "Oscar Freire", "Urs Freuler", "Mogens Frey", "Dario Frigo", "Herman Frison", "Christopher Froome",
    "José Manuel Fuente", "Anselmo Fuerte", "Dominique Gaigne", "Jean Gainche", "Francisco Galdos",
    "Joaquim Galera", "Félix Gall", "Tony Gallopin", "Andres Gandarias", "Juan Manuel Garate",
    "José Vicente Garcia Acosta", "Dominique Garde", "Aitor Garmendia", "Stefano Garzelli", "Charly Gaul",
    "Bernard Gauthier", "Jean-Louis Gauthier", "Fernando Gaviria", "Martial Gayant", "Antonio Gelabert",
    "Albertus Geldermans", "Raphaël Géminiani", "Jean-Pierre Genet", "Alexandre Geniez", "Linus Gerdemann",
    "Simon Gerrans", "Simon Geschke", "Massimo Ghirotto", "Philippe Gilbert", "Kurt Gimmi", "Felice Gimondi",
    "Michele Gismondi", "Gilbert Glaus", "Walter Godefroot", "Jean Goldschmidt", "Rolf Golz", "Aitor Gonzalez",
    "Aurelio Gonzalez", "Igor Gonzalez de Galdeano", "José Jaime Gonzalez Pico", "José Antonio Gonzalez Linares",
    "Julian Gorospe", "Ivan Gotti", "Jean Graczyk", "Rolf Graf", "André Greipel", "Dylan Groenewegen",
    "Charly Grosskost", "Georges Groussard", "Joseph Groussard", "Ercole Gualazzini", "Mirko Gualdi",
    "Giuseppe Guerini", "Pietro Guerra", "Cyrille Guimard", "Cees Haast", "Patrice Halgand", "Bo Hamburger",
    "Tyler Hamilton", "Andrew Hampsten", "Jacques Hanegraaf", "Rob Harmeling", "Roger Hassenforder",
    "Heinrich Haussler", "Jens Heppner", "Mathieu Hermans", "Omar Hernandez", "Jesus Herrada", "Luis Herrera",
    "Pascal Hervé", "Ryder Hesjedal", "Stéphane Heulot", "Yves Hezard", "Bernard Hinault", "George Hincapie",
    "Jai Hindley", "Jos Hinsen", "Marc Hirschi", "Barry Hoban", "Joseph Hoevenaers", "Serhiy Honchar",
    "Johnny Hoogerland", "Frank Hoste", "Hugo Houle", "Robert Hunter", "Valentin Huot", "Thor Hushovd",
    "Joseph Huysmans", "Emile Idée", "Maxim Iglinskiy", "Guy Ignolin", "Raymond Impanis", "Daryl Impey",
    "Miguel Indurain", "Livio Isotti", "Serguei Ivanov", "Gorka Izaguirre Insausti", "Ion Izaguirre Insausti",
    "Maurice Izier", "Joseph Jacobs", "Rolf Jaermann", "Fabio Jakobsen", "Jörg Jaksche", "Laurent Jalabert",
    "Jan Janssen", "Marcel Janssens", "Zenon Jaskula", "Arnold Jeannesson", "Julio Jimenez", "Patrocinio Jimenez",
    "Tobias Halland Johannessen", "Christian Jourdan", "Pascal Jules", "Bob Julich", "Bob Jungels", "Blel Kadri",
    "Lennard Kämna", "Tanel Kangert", "Gerben Karstens", "Sean Kelly", "Willy Kemp", "Fredrik Kessiakoff",
    "Matthias Kessler", "Désiré Keteleer", "Kim Kirchen", "Jann Kirsipuu", "Vasil Kiryienka", "Robert Kiserlovski",
    "Marcel Kittel", "Andreas Klöden", "Servais Knaven", "Gerrie Knet","Hugo Koblet", "Bernard Kohl", "Dimitri Konishev", "Patrick Konrad", "Sören Kragh Andersen",
    "Jann Krekels", "Alexander Kristoff", "Karsten Kroon", "Steven Kruijswijk", "Ferdi Kübler", "Hennie Kuiper",
    "Karl-Heinz Kunde", "Stefan Küng", "Sepp Kuss", "Michal Kwiatkowski", "Bernard Labourdette", "Matthieu Ladagnous",
    "Victor Lafay", "Roberto Laiseka", "Roger Lambrecht", "Johan Lammerts", "Yves Lampaert", "Floyd Landis",
    "Sebastian Lang", "Guy Lapébie", "Christophe Laporte", "Miguel Maria Lasa", "Pablo Lastras", "Pierre Latour",
    "Nello Lauredi", "Michel Laurent", "Dag-Otto Lauritzen", "Christophe Lavainne", "Apo Lazaridès", "Lucien Lazaridès",
    "Pierre Le Bigaut", "André Le Dissez", "Maurice Le Guilloux", "Jean Le Guilly", "Jean-Claude Lebaube",
    "Luc Leblanc", "Laurent Lefèvre", "Levi Leipheimer", "Ismael Lejarreta", "Marino Lejarreta", "Philippe Leleu",
    "Massimiliano Lelli", "Eric Leman", "Paul Lemeteyer", "Christophe Le Mével", "Greg LeMond", "Adolfo Leoni",
    "Désiré Letort", "Roger Lévêque", "Marco Lietti", "Hubert Linard", "Pascal Lino", "Ludo Loos", "Miguel Angel Lopez",
    "Vicente Lopez Carril", "Jesus Lorono", "Henk Lubberding", "Jorg Ludewig", "Olaf Ludwig", "Alexey Lutsenko",
    "Jo Maas", "Frans Maassen", "Marc Madiot", "Valentin Madouas", "Erich Maechler", "Freddy Maertens",
    "Fiorenzo Magni", "Ricardo Magrini", "François Mahé", "Rafal Majka", "Jean Mallejac", "Henri Manders",
    "Laurent Mangel", "Fernando Manzanèque", "Thierry Marie", "René Marigil", "Jacques Marinelli", "René Martens",
    "Daniel Martin", "Raymond Martin", "Tony Martin", "Daniel Martinez", "Egoi Martinez", "Juan Martinez Oliver",
    "Mariano Martinez", "Miguel Angel Martinez Torres", "Gabriel Mascaro", "Henri Massal", "Rodolfo Massi",
    "Imerio Massignan", "Raymond Mastrotto", "Hubert Mathis", "Pierre Matignon", "Nico Mattan", "Michael Matthews",
    "Rudy Matthijs", "Claude Mattio", "Iban Mayo", "Robbie McEwen", "Bradley McGee", "Jordi Meeus", "Roland Meier",
    "Frans Melckenbeeck", "Denis Menchov", "Antonio Menendez", "Christophe Mengin", "Pierre-Henry Mentheour",
    "Juan Miguel Mercado", "Axel Merckx", "Eddy Merckx", "Tim Merlier", "Alain Meslet", "Georges Meunier",
    "Jacques Michaud", "David Millar", "Robert Millar", "Nicolas Minali", "Mario Minieri", "Joseph Mirando",
    "Matej Mohoric", "Amaël Moinard", "Rudy Molard", "Jean-Luc Molineris", "Pierre Molineris", "Marcel Molines",
    "Bauke Mollema", "Frédéric Moncassin", "David Moncoutié", "Gianpaolo Mondini", "Sven Montgomery",
    "Reynel Montoya", "Carmelo Morales", "Christophe Moreau", "Primo Mori", "Michael Morkov", "Joseph Morvan",
    "Francesco Moser", "Moreno Moser", "Gianni Motta", "Charly Mottet", "Marcello Mugnain", "Edouard Müller", "Federico Munoz", "Pedro Munoz", "Javier Murguialday", "Johan Museeuw",
    "Stefan Mutter", "Daniele Nardello", "Ramunas Navardauskas", "José Nazabal", "Jean-Patrick Nazon",
    "Wilfried Nelissen", "Gastone Nencini", "Jan Nevens", "Vincenzo Nibali", "Mikel Nieve", "Henk Nijdam",
    "Jelle Nijdam", "Rinaldo Nocentini", "Jan Nolten", "Anatole Novak", "Luis Ocana", "Javier Ochoa",
    "Stan Ockers", "Ben O'Connor", "Stuart O'Grady", "Abraham Olano", "Andres Oliva", "Bert Oosterbosch",
    "Christophe Oriol", "Luis Otano", "Sergueï Outschakov", "Arigo Padovan", "Vladimiro Panizza", "Marco Pantani",
    "Jarlinson Pantano", "Aldo Parecchini", "Fabio Parra", "Sergio Parsani", "Javier Pascual Rodriguez",
    "Alfredo Pasotti", "Sergio Paulinho", "Eddy Pauwels", "Serge Pauwels", "Jorgen Pedersen", "Mads Pedersen",
    "Ludo Peeters", "Joël Pelier", "Franco Pellizotti", "Victor Hugo Pena", "Ronan Pensec", "Jean-Christophe Péraud",
    "Oscar Pereiro Sio", "Anthony Perez", "José Perez Frances", "Ruben Perez Moreno", "Domingo Perurena",
    "Alessandro Petacchi", "Nans Peters", "Gosta Petterson", "Rudy Pevenage", "Luciano Pezzi", "Fabrice Philippot",
    "Jasper Philipsen", "Davis Phinney", "Lech Piasecki", "Mariano Piccoli", "Thomas Pidcock", "Leonardo Piepoli",
    "Jeff Pierce", "Jakob Piil", "Jérôme Pineau", "Roger Pingeon", "Thibaut Pinot", "Georges Pintens",
    "Kléber Piot", "Fritz Pirard", "Eddy Planckaert", "Joseph Planckaert", "Walter Planckaert", "Willy Planckaert",
    "Ruben Plaza Molina", "Miguel Poblet", "Massimo Podenzana", "Wouter Poels", "Tadej Pogacar", "Pascal Poisson",
    "Eros Poli", "Giancarlo Polidori", "Nils Politt", "Michel Pollentier", "Yaroslav Popovych", "Henk Poppe",
    "Richie Porte", "Raymond Poulidor", "Nelson Powless", "Filippo Pozzato", "Jacques Pras", "Georg Preidler",
    "Cees Priem", "Celestino Prieto", "René Privat", "Louis Proost", "Marcel Queheille", "Bernard Quennehen",
    "Maurice Quentin", "Bernard Quilfen", "Nairo Alexander Quintana Rojas", "Jan Raas", "Michael Rasmussen",
    "Christian Raymond", "Raoul Rémy", "Guido Reybrouck", "Mauro Ribeiro", "Christophe Riblon", "Riccardo Ricco",
    "Pascal Richard", "Bjarne Riis", "Oliveiro Rincon", "Raymond Riotte", "Roger Rivière", "Jean Robic",
    "Brian Robinson", "Nicolas Roche", "Stephen Roche", "Carlos Rodriguez Cano", "Francesco Rodriguez",
    "Nelson Rodriguez", "Joaquin Rodriguez Oliver", "Michael Rogers", "Primoz Roglic", "Antonin Rolland",
    "Pierre Rolland", "André Romero", "Tony Rominger", "Aldo Ronconi", "Steven Rooks", "Fabio Roscioli",
    "André Rosseel", "Vincenzo Rossello", "Giovanni Rossi", "Louis Rostollan", "Karel Rottiers", "Didier Rous","Denis Roux", "Laurent Roux", "Jérémy Roy", "Bernardo Ruiz", "Pello Ruiz Cabestany",
    "Raimondas Rumsas", "Niki Ruttimann", "Tino Sabbadini", "Peter Sagan", "Gérard Saint", "Cristian Salvato",
    "José Samyn", "Grégorio San Miguel", "Luis Leon Sanchez", "Samuel Sanchez", "Luis Pedro Santamarina",
    "Giacinto Santambrogio", "Angel José Sarrapio", "Carlos Sastre", "Cyril Saugrain", "Paolo Savoldelli",
    "Maximilian Schachmann", "Fritz Schaer", "Julien Schepens", "Silvano Schiavon", "Andy Schleck",
    "Frank Schleck", "Jean-Pierre Schmitz", "Briek Schotte", "Willy Schroeders", "Stefan Schumacher",
    "Edy Schutz", "Massimiliano Sciandri", "Gino Sciardis", "Eddy Seigneur", "Edouard Sels", "Patrick Sercu",
    "Marc Sergeant", "José Serpa", "José Serra", "Marcos Serrano", "Christian Seznec", "Leonardo Sierra",
    "François Simon", "Jérôme Simon", "Pascal Simon", "Régis Simon", "Mauro Simonetti", "Gilberto Simoni",
    "Tom Simpson", "Jesper Skibby", "Toms Skujins", "Roland Smet", "Mauricio Soler", "Gerrit Solleveld",
    "Nicki Sorensen", "Rolf Sorensen", "Edgard Sorgeloos", "Joseph Spruyt", "Jean Stablinski", "Gert Steegmans",
    "Tom Steels", "Neil Stephens", "Julien Stevens", "Alex Stieda", "Zdenek Stybar", "Jan Svorada",
    "Roger Swerts", "Sylvester Szmyd", "Giuseppe Tacca", "Pietro Tarchini", "Eloi Tassin", "Valerio Tebaldi",
    "Willy Teirlinck", "Lucien Teisseire", "Mike Teunissen", "Dylan Teuns", "Klaus-Peter Thaler",
    "Jean-Claude Theillière", "Gert-Jan Theunisse", "Bernard Thévenet", "Geraint Thomas", "Joseph Thomin",
    "Dietrich Thurau", "Claude Tollet", "Pavel Tonkov", "Pedro Torres", "Roberto Torres", "Matteo Tosatto",
    "Guerrino Tosello", "Georg Totschnig", "Mario Traversoni", "Matteo Trentin", "André Trochut",
    "Anthony Turgis", "Amets Txurruka", "Piotr Ugrumov", "Jan Ullrich", "Rigoberto Uran", "Bernard Vallet",
    "Alejandro Valverde", "Michel Van Aerde", "Wout Van Aert", "Greg Van Avermaet", "Léo Van Bon",
    "Bernard Van de Kerckhove", "Kurt Van de Wouwer", "Willy Van den Bergen", "Georges Van den Berghe",
    "Martin Van den Bossche", "Jurgen Van den Broeck", "Ferdi Van den Haute", "Adrie Van der Poel",
    "Mathieu Van der Poel", "Johan Van de Velde", "Edward Van Dyck", "Cees Van Espen", "Wim Van Est",
    "Tejay Van Garderen", "Martin Van Geneugden", "Adrie Van Houwelingen", "Lucien Van Impe", "Rik Van Linden",
    "Rik Van Looy", "Willy Van Neste", "Jean-Paul Van Poppel", "Daniel Van Ryckeghem", "Herman Van Springel",
    "Rik Van Steenbergen", "Albert Van Vlierberghe", "Léo Van Vliet", "Teun Van Vliet", "Eric Vanderaerden",
    "Jelle Vanendert", "Willy Vannitsen", "Flavio Vanzella", "Oscar de Jesus Vargas", "Robert Varn","Robert Varnajo", "Alain Vasseur", "Cédric Vasseur", "Peter Velits", "Rik Verbrugghe", "Nico Verhoeven",
    "Michel Vermeulin", "Pol Verschuere", "Eddy Verstraeten", "Gérard Vianen", "Frédéric Vichot",
    "José Luis Viejo", "René Vietto", "Pierre-Raymond Villemiane", "Jonas Vingegaard", "Alexandre Vinokourov",
    "Richard Virenque", "Elia Viviani", "Jacques Vivier", "Thomas Voeckler", "Jens Voigt", "Gerrit Voorting",
    "Bart Voskamp", "Alexis Vuillermoz", "Marinus Wagtmans", "Wout Wagtmans", "Roger Walkowiak", "Marc Wauters",
    "Pieter Weening", "Fabian Wegmann", "Paul Wellens", "Tim Wellens", "Johnny Weltz", "Bradley Wiggins",
    "Adrie Wijnands", "Ludwig Wijnants", "Daniel Willems", "Peter Winnen", "Guido Winterberg", "Rolf Wolfshohl",
    "Michael Woods", "Michaël Wright", "Marcel Wüst", "Adam Yates", "Sean Yates", "Simon Yates", "Erik Zabel",
    "David Zabriskie", "Ilnur Zakarin", "Stefano Zanini", "Italo Zilioli", "Hubert Zilverberg", "Urs Zimmermann",
    "Joop Zoetemelk", "Haimar Zubeldia", "Alex Zülle"
    ]





# Désactiver les avertissements sur les requêtes HTTPS non vérifiées
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def format_nom_url(nom):
    mots = nom.split()
    nom_famille = mots[-1].lower()
    if len(mots) > 2 and mots[-2][0].isupper():
        particule = mots[-2].lower()
        nom_famille = f"{particule}_{nom_famille}"
    return nom_famille


data_to_save = []
data_dict = {}

for nom_coureur in noms_coureurs:  
    data_dict[nom_coureur] = {'Participations': 0, 'Victoires': 0, 'Maillot Jaune': 0}
    url = f"https://ledicodutour.com/coureurs/coureurs/coureurs_{format_nom_url(nom_coureur)[0].lower()}/{format_nom_url(nom_coureur)}.html"

    try:
        response = requests.get(url, verify=False)
        if response.status_code != 200:
            print(f"Page non trouvée pour {nom_coureur} à l'URL: {url}")
            continue
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')

        infos_td511 = soup.find_all("td", class_="td511")
        for info in infos_td511:
            text = info.get_text(strip=True)
            if "Participations au Tour" in text:
                data_dict[nom_coureur]['Participations'] = int(re.findall(r'\d+', text)[0])  # Utilisation d'une expression régulière
            elif "Victoire d'étape" in text:
                data_dict[nom_coureur]['Victoires'] = int(re.findall(r'\d+', text)[0])  # Utilisation d'une expression régulière
            elif "Jour en maillot jaune" in text:
                data_dict[nom_coureur]['Maillot Jaune'] = int(re.findall(r'\d+', text)[0])  # Utilisation d'une expression régulière
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'accès à l'URL {url}: {e}")

for coureur, infos in data_dict.items():
    data_to_save.append([
        coureur,
        infos['Participations'],
        infos['Victoires'],
        infos['Maillot Jaune']
    ])

filename = "palmares_tdf2.csv"

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in data_to_save:
        csvwriter.writerow(row)

print(f"Terminé. Les données ont été écrites dans {filename}")
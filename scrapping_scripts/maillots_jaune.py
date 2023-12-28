import requests
from bs4 import BeautifulSoup
import csv

# URL of the page
url = 'https://fr.wikipedia.org/wiki/Statistiques_du_classement_g%C3%A9n%C3%A9ral_du_Tour_de_France'

# Make a request to fetch the page content
response = requests.get(url)
html = response.content

# Parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Find the table you're interested in. You might need to check the class or id of the table by inspecting the webpage.
# This is a generic way to get the first table, you might need to adjust it to target the right one.
table = soup.find('table', {'class': 'wikitable sortable'})

# Lists to hold the extracted data
names = []
yellow_jerseys = []

# Assuming the first row is the header and the specific columns are known
for row in table.find_all('tr')[1:]:  # Skip the header row
    cells = row.find_all('td')
    if len(cells) > 1:  # To ensure it's a row with data
        name = cells[1].text.strip()  # Adjust the index according to the actual column
        yellow_jersey = cells[3].text.strip()  # Adjust the index according to the actual column
        names.append(name)
        yellow_jerseys.append(yellow_jersey)

# Print or process the extracted data
for name, jersey in zip(names, yellow_jerseys):
    print(f"{name}: {jersey}")

# Save the data to a CSV file
with open('maillot_jaune.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Yellow Jerseys'])  # Writing header
    for name, jersey in zip(names, yellow_jerseys):
        writer.writerow([name, jersey])

print("Data has been written to maillot_jaune.csv")
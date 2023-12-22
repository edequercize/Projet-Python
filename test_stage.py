from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests

# URL de la page
url = 'https://www.les-sports.info/cyclisme-sur-route-liste-epreuves-s2-c0-b0-p2.html'

# Initialiser le navigateur
browser = webdriver.Chrome()
browser.get(url)

# Attendre que la page charge
time.sleep(5)

# Trouver tous les liens du Tour de France
links = browser.find_elements(By.XPATH, "//a[contains(@href, 'cyclisme-sur-route-tour-de-france')]")

def scrape_etapes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    etapes = soup.find_all('a', href=True, text='Détail')
    classements = []

    for etape in etapes:
        etape_url = 'https://www.les-sports.info' + etape['href']
        etape_response = requests.get(etape_url)
        etape_soup = BeautifulSoup(etape_response.content, 'html.parser')

        tableau = etape_soup.find('table', class_='tab')
        if tableau:
            lignes = tableau.find_all('tr')
            for ligne in lignes[1:]:
                colonnes = ligne.find_all('td')
                if colonnes:
                    classement = {
                        'Position': colonnes[0].text.strip(),
                        'Coureur': colonnes[1].text.strip(),
                        'Equipe': colonnes[2].text.strip(),
                        'Temps': colonnes[3].text.strip()
                    }
                    classements.append(classement)
    return classements

for link in links:
    href = link.get_attribute('href')
    if href:
        browser.get(href)
        time.sleep(3)  # Attendre que la page charge

        # Scrape les classements pour chaque étape
        classements = scrape_etapes(browser.current_url)
        for classement in classements:
            print(classement)

        browser.get(url)
        time.sleep(5)

browser.quit()
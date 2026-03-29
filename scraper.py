import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://books.toscrape.com/"

print("Starte den Scan...")

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('article', class_='product_pod')
liste = []

for book in books:
    titel = book.h3.a['title']
    preis = book.find('p', class_='price_color').get_text()
    liste.append({"Titel": titel, "Preis": preis})

df = pd.DataFrame(liste)

df['Preis'] = df['Preis'].str.replace('£', '').str.replace('Â', '')

df.to_csv('meine_erste_liste.csv', index=False, sep=';', encoding='utf-8-sig')

print("Fertig! Die Liste wurde für Excel optimiert.")

import os
os.startfile('meine_erste_liste.csv')
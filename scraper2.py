import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "http://books.toscrape.com/catalogue/page-1.html"
alle_buecher = []

while url:
    print(f"Scanne gerade: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    books = soup.find_all('article', class_='product_pod')
    for book in books:
        titel = book.h3.a['title']
        preis = book.find('p', class_='price_color').get_text()
        alle_buecher.append({"Titel": titel, "Preis": preis})
    
    
    next_btn = soup.find('li', class_='next')
    if next_btn:
        next_url_part = next_btn.a['href']
        url = "http://books.toscrape.com/catalogue/" + next_url_part
    else:
        url = None
    
    time.sleep(1)

df = pd.DataFrame(alle_buecher)
df['Preis'] = df['Preis'].str.replace('£', '').str.replace('Â', '')
df.to_csv('alle_buecher.csv', index=False, sep=';', encoding='utf-8-sig')

print(f"Fertig! Insgesamt {len(alle_buecher)} Bücher gesammelt.")

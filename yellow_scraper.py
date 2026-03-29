from bs4 import BeautifulSoup
import pandas as pd
import os

file_path = "miami.html"

if not os.path.exists(file_path):
    print(f"❌ Fehler: Die Datei '{file_path}' wurde nicht im Ordner gefunden!")
else:
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")

    listings = soup.find_all('div', class_=lambda x: x and ('v-card' in x or 'result' in x))
    
    results = []

    for item in listings:
        try:
            name_tag = item.find('a', class_='business-name')
            name = name_tag.get_text(strip=True) if name_tag else "N/A"
        
            phone_tag = item.find('div', class_='phones')
            phone = phone_tag.get_text(strip=True) if phone_tag else "N/A"
            
            address_tag = item.find('div', class_='adr')
            address = address_tag.get_text(strip=True) if address_tag else "N/A"

            if name != "N/A":
                results.append({
                    "Firma": name,
                    "Telefon": phone,
                    "Adresse": address
                })
        except Exception as e:
            continue

    if results:
        df = pd.DataFrame(results)
        df.to_excel("Miami_Gyms_Final_Leads.xlsx", index=False)
        print(f"✅ ERFOLG! {len(results)} Gyms wurden aus der Datei extrahiert.")
        print("Datei 'Miami_Gyms_Final_Leads.xlsx' ist fertig für den Kunden!")
    else:
        print("❌ Keine Daten gefunden. Sicher, dass es die richtige HTML-Datei ist?")
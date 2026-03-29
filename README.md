# 🚀 Professional Web Scraper / Professioneller Web-Scraper (Python)

---

## 📂 Projekt-Stufen / Project Versions

Ich habe zwei Versionen des Scrapers entwickelt, um verschiedene Anforderungen abzudecken:

### 1️⃣ Basis-Scraper (`scraper.py`)
* **Ziel:** Schnelle Extraktion einer einzelnen Seite.
* **Umfang:** Erfasst die ersten **20 Bücher** (Titel & Preis).
* **Besonderheit:** Perfekt für schnelle Datenchecks und kleine Listen.

### 2️⃣ Profi-Scraper (`scraper2.py`)
* **Ziel:** Vollautomatische Datengewinnung über die gesamte Website.
* **Umfang:** Scannt alle **50 Seiten** und liefert über **1.000 Datensätze**.
* **Besonderheit:** Inklusive "Pagination-Logik" (automatisches Blättern) und erweitertem Data Cleaning für den direkten Excel-Import.

---

[English below]

## 🇩🇪 Deutsch: Projektübersicht
Ein leistungsstarker Web-Scraper, der speziell für das Extrahieren von E-Commerce-Daten entwickelt wurde. Dieses Projekt zeigt, wie man professionell Daten sammelt, bereinigt und für Kunden aufbereitet.

### ✨ Funktionen
* **Vollständige Seiten-Navigation:** Scannt automatisch alle verfügbaren Seiten (z. B. 50+ Seiten).
* **Datenbereinigung:** Entfernt störende Symbole (Â, £) für eine saubere Excel-Liste.
* **Excel-Optimiert:** Speichert im `;` Format mit `utf-8-sig` für perfekte Darstellung in Microsoft Excel.
* **Sicheres Scraping:** Eingebaute Pausen (Timeouts) gegen Server-Sperren.

---

## 🇺🇸 English: Project Overview
A high-performance web scraper designed for e-commerce data extraction. This project demonstrates professional data mining capabilities for international clients.

### ✨ Features
* **Full Pagination Support:** Automatically crawls through all available pages (e.g., 50+ pages).
* **Data Cleaning:** Removes currency symbols and formatting noise for immediate use.
* **Excel-Optimized:** Exports to `;` separated CSV with `utf-8-sig` encoding for perfect display.
* **Respectful Scraping:** Includes delays between requests to avoid server blocks.

---

## 🛠️ Tech Stack
* **Python** (BeautifulSoup4, Pandas, Requests)

## 📈 Ergebnis / Results
Das Skript hat erfolgreich **1.000 Produkte** extrahiert und strukturiert gespeichert. / The script successfully extracted **1,000 products** into a clean table.

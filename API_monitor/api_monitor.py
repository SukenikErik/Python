import requests
import sqlite3
import os
import datetime

# --- 1. Konfiguráció és Útvonalak ---
mappa = os.path.dirname(os.path.abspath(__file__))
db_utvonal = os.path.join(mappa, "adatok.db")

def inicializalas():
    """Létrehozza az adatbázist és a táblát, ha még nincs."""
    conn = sqlite3.connect(db_utvonal)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS api_valaszok (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            idopont TEXT,
            cim TEXT,
            kesz INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def mentes_sql(cim, kesz_statusz):
    """Elmenti az API választ az SQL táblába."""
    conn = sqlite3.connect(db_utvonal)
    cursor = conn.cursor()
    idopont = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute("INSERT INTO api_valaszok (idopont, cim, kesz) VALUES (?, ?, ?)", 
                   (idopont, cim, 1 if kesz_statusz else 0))
    
    conn.commit()
    conn.close()
    print("✓ Adat sikeresen mentve az SQL adatbázisba.")

def futtatas():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    try:
        valasz = requests.get(url, timeout=5)
        if valasz.status_code == 200:
            adat = valasz.json()
            print(f"API válasz érkezett: {adat['title']}")
            
            # Mentés az adatbázisba
            mentes_sql(adat['title'], adat['completed'])
        else:
            print(f"Hiba: {valasz.status_code}")
    except Exception as e:
        print(f"Hiba történt: {e}")

# --- Főprogram ---
if __name__ == "__main__":
    inicializalas()
    futtatas()
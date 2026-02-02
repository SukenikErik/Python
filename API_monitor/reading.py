import sqlite3

def adatok_kilistazasa():
    conn = sqlite3.connect("adatok.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM api_valaszok")
    sorok = cursor.fetchall()

    print("--- AZ ADATBÁZIS TARTALMA ---")
    for sor in sorok:
        print(f"ID: {sor[0]} | Időpont: {sor[1]} | Cím: {sor[2]}")
    
    conn.close()

if __name__ == "__main__":
    adatok_kilistazasa()
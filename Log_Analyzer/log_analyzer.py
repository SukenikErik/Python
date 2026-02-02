import os

mappa = os.path.dirname(os.path.abspath(__file__))
log_utvonal = os.path.join(mappa, "server_logs.txt")

def log_szures_es_mentes():
    if not os.path.exists(log_utvonal):
        print("Hiba: A log fájl nem található!")
        return

    keresett_szo = input("Milyen típusú bejegyzéseket keresel? (INFO, ERROR, CRITICAL): ").upper()
    talalatok = []
    
    with open(log_utvonal, "r", encoding="utf-8") as f:
        for sor in f:
            if keresett_szo in sor.upper():
                tiszta_sor = sor.strip()
                talalatok.append(tiszta_sor)
    
    if not talalatok:
        print("Nincs találat.")
        return

    print(f"\nTalálatok száma: {len(talalatok)}")
    valasz = input("\nSzeretnéd menteni a nem duplikált találatokat? (igen/nem): ").lower()
    
    if valasz == "igen":
        uj_mentesek = 0
        duplikat_szam = 0
        
        for sor in talalatok:
            tipus = "EGYEB"
            if "ERROR" in sor.upper(): tipus = "ERROR"
            elif "INFO" in sor.upper(): tipus = "INFO"
            elif "CRITICAL" in sor.upper(): tipus = "CRITICAL"
            
            riport_fajl = os.path.join(mappa, f"{tipus}_riport.txt")
            
            # --- ELLENŐRZÉS: Benne van-e már a fájlban? ---
            mar_letezik = False
            if os.path.exists(riport_fajl):
                with open(riport_fajl, "r", encoding="utf-8") as rf:
                    if sor in rf.read():
                        mar_letezik = True
            
            # --- MENTÉS: Csak ha még nincs benne ---
            if not mar_letezik:
                with open(riport_fajl, "a", encoding="utf-8") as f:
                    f.write(sor + "\n")
                uj_mentesek += 1
            else:
                duplikat_szam += 1
        
        print(f"\nMentés kész!")
        print(f"Új sorok hozzáadva: {uj_mentesek}")
        print(f"Kiszűrt duplikátumok: {duplikat_szam}")
    else:
        print("A mentés elmaradt.")

if __name__ == "__main__":
    log_szures_es_mentes()
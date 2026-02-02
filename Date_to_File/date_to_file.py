import datetime
import os

def log_esemeny(uzenet):
    mappa_utvonal = os.path.dirname(os.path.abspath(__file__))
    log_fajl_helye = os.path.join(mappa_utvonal, "szerver.log")

    idopont = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_sor = f"[{idopont}] AI Platform Status: {uzenet}\n"

    try:
        with open(log_fajl_helye, "a", encoding="utf-8") as f:
            f.write(log_sor)
        print(f"Log sikeresen mentve ide: {log_fajl_helye}")
    except Exception as e:
        print(f"Hiba történt a naplózás során: {e}")

log_esemeny("Rendszer ellenőrzés: Minden komponens üzemkész.")
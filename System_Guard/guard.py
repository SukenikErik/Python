import psutil
import datetime
import time
import json
import os

MAPPA = os.path.dirname(os.path.abspath(__file__))
RIPORT_UTVONAL = os.path.join(MAPPA, "report.json")

def get_system_metrics():
    try:
        metrics = {
            "cpu_percent": psutil.cpu_percent(interval=1),
            "memory_percent": psutil.virtual_memory().percent,
            "disk_free_gb": round(psutil.disk_usage('/').free / (1024**3), 2),
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return metrics
    except Exception as e:
        print(f"Hiba az adatok lekérésekor: {e}")
        return None

def analyze_health(history):

    cpu_values = [h["cpu_percent"] for h in history]
    avg_cpu = sum(cpu_values) / len(cpu_values)

    utolso_meres = history[-1]
    max_mem = max([h["memory_percent"] for h in history])
    szabad_hely = utolso_meres["disk_free_gb"]
    
    print(f"\n--- DIAGNÓZIS ---")
    print(f"Átlagos CPU terhelés: {avg_cpu:.2f}%")
    print(f"Csúcs memóriahasználat: {max_mem}%")
    print(f"Aktuális szabad hely: {szabad_hely} GB")

    if avg_cpu > 75 or max_mem > 90 or szabad_hely < 10:
        return "KRITIKUS"
    elif avg_cpu > 50:
        return "FIGYELMEZTETÉS (Magas terhelés)"
    else:
        return "STABIL"

def mentes_jsonba(history, status):

    report_data = {
        "status": status,
        "metadata": {
            "platform": "Windows/Linux System Guard",
            "measurements_count": len(history),
            "generated_at": str(datetime.datetime.now())
        },
        "measurements": history
    }
    
    try:
        with open(RIPORT_UTVONAL, "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=4)
        print(f"\n[SIKER] A riport elmentve: {RIPORT_UTVONAL}")
    except IOError as e:
        print(f"Hiba a fájl mentésekor: {e}")

def main():
    history = []
    meresi_szam = 5
    
    print(f"Rendszer-egészségügyi mérés indítása ({meresi_szam} mintavétel)...")
    
    for i in range(meresi_szam):
        data = get_system_metrics()
        if data:
            history.append(data)
            print(f"[{data['timestamp']}] {i+1}. mérés: CPU: {data['cpu_percent']}% | RAM: {data['memory_percent']}%")

        if i < meresi_szam - 1:
            time.sleep(2)

    if history:

        rendszer_allapot = analyze_health(history)
        print(f"Záró státusz: {rendszer_allapot}")

        mentes_jsonba(history, rendszer_allapot)

if __name__ == "__main__":
    main()
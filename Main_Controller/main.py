import os
import subprocess
import sys
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def menu_megjelenites():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 40)
    print("   AI OPS - KÖZPONTI VEZÉRLŐEGYSÉG   ")
    print("=" * 40)
    print("1. API Monitor (Válaszidő mérés)")
    print("2. Log Analizátor (Hibaszűrés)")
    print("3. System Guard (Erőforrás figyelő)")
    print("4. Dátum-fájl műveletek (Date_to_File)")
    print("5. Kilépés")
    print("-" * 40)

def script_futtatasa(mappa_nev, fajl_nev):
   
    target_dir = os.path.join(BASE_DIR, mappa_nev)
    script_path = os.path.join(target_dir, fajl_nev)
    
    if os.path.exists(script_path):
        print(f"\n[INFO] Indítás: {mappa_nev}/{fajl_nev}...")
        try:
            subprocess.run([sys.executable, script_path], check=True, cwd=target_dir)
            input("\nSikeres futtatás. Nyomj Entert a menühöz...")
        except subprocess.CalledProcessError:
            print("\n[!] A script hibával állt le.")
            time.sleep(2)
        except Exception as e:
            print(f"\n[!] Váratlan hiba: {e}")
            time.sleep(2)
    else:
        print(f"\n[HIBA] A fájl nem található: {script_path}")
        time.sleep(3)

def main():
    while True:
        menu_megjelenites()
        valasztas = input("Válassz egy menüpontot (1-5): ")

        match valasztas:
            case "1":
                script_futtatasa("API_monitor", "api_monitor.py")
            case "2":
                script_futtatasa("Log_Analyzer", "log_analyzer.py")
            case "3":
                script_futtatasa("System_Guard", "guard.py")
            case "4":
                script_futtatasa("Date_to_File", "date_to_file.py")
            case "5":
                print("\nKilépés... Szép napot!")
                break
            case _: 
                print("\nÉrvénytelen opció, próbáld újra!")
                time.sleep(1)

if __name__ == "__main__":
    main()
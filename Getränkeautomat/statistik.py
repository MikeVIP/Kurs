__version__ = "0.0.1"
__author__ = "MB"
__description__ = "Statistikmodul für den Getränkeautomaten"

# Variablen zur Datenspeicherung
verkaufszahlen = {}
umsätze = {}

def erhöhe_verkauf(name, preis):
    # https://www.w3schools.com/python/ref_dictionary_get.asp

    # Aktualisieren der Anzahl der verkauften Getränke
    verkaufszahlen[name] = verkaufszahlen.get(name, 0) + 1
    # Aktualisieren der Gesamteinnahmen für ein bestimmtes Getränk
    umsätze[name] = umsätze.get(name, 0) + preis
    
def zeige_statistik():
    # Überschrift
    print("Verkaufsstatistiken".center(50))
    print(f"{'Getränk':<14} {'Verkaufte Stückzahl':>14} {'Gesamterlös':>14}")
    print("-" * 50)

    # Zeilen aus zwei Wörterbüchern ausschreiben
    for name, sztuki in verkaufszahlen.items():
        print(f"{name:<14} {sztuki:>14} {umsätze[name]:>14.2f}")



def gesamtumsatz():
    print(f"Gesamtumsatz: {round(sum(umsätze.values()), 2)}")

# Test
if __name__ == "__main__":
    erhöhe_verkauf("Cola", 1.50)
    erhöhe_verkauf("Cola", 1.10)
    erhöhe_verkauf("Wasser", 0.90)
    erhöhe_verkauf("Saft", 2.00)
    erhöhe_verkauf("Saft", 2.00)
    erhöhe_verkauf("Saft", 1.80)
    erhöhe_verkauf("Wasser", 0.99)
    
    zeige_statistik()

    gesamtumsatz()

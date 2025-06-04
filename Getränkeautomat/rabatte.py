def ermittle_rabatt(cena):
    print("Haben Sie eine Membercard?")
    print("0: Keine Karte")
    print("1: Regular Card (10%)")
    print("2: Premium Card (15%)")

    wybor = input("Bitte wählen Sie: ").strip()

    if wybor == "1":
        rabat = 0.10
        print("Regular Card erkannt – 10% Rabatt.")
    elif wybor == "2":
        rabat = 0.15
        print("Regular Card erkannt – 15% Rabatt.")
    else:
        rabat = 0.0
        print("Kein Rabatt.")

    nowa_cena = round(cena * (1 - rabat), 2)
    print(f"Neuer Preis: {nowa_cena:.2f}€")
    return nowa_cena

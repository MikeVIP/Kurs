def einkaufsliste(**lista):
    if not lista:
        return "Lista zakupów jest pusta."

    wynik = "Lista zakupów:\n"
    for produkt, ilosc in lista.items():
        wynik += f"\t - {produkt.capitalize()}:\t {ilosc}\n"
    
    return wynik

zakupy = {
    "mleko": "2 litry",
    "chleb": "1 sztuka",
    "jabłka": "1 kg",
    "kawa": "500 g",
    "makaron": "2 opakowania",
    "jajka": "10 sztuk",
    "ser": "300 g",
    "pomidory": "1,5 kg",
    "jogurt": "4 kubeczki",
    "masło": "250 g",
    "banany": "1 kg",
    "sok pomarańczowy": "1 litr"
}

print(einkaufsliste(**zakupy))
# or
print(einkaufsliste(banany="1 kg", jabłka="1 kg", kawa="500 g"))

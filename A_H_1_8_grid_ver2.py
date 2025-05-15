litery = "ABCDEFGH"
numery = range(1, 9)

for litera in litery:
    wiersz = []
    for numer in numery:
        wiersz.append(f"{litera}{numer}")
    print(" ".join(wiersz))

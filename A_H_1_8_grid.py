litery = "ABCDEFGH"
numery = range(1, 9)
 
wynik = [f"{litera}{numer}" for litera in litery for numer in numery]
 
for indeks in range(0, len(wynik), 8):
    print(" ".join(wynik[indeks:indeks+8]))

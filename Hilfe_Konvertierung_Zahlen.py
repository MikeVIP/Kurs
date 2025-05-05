def konwertuj(spr_liczbe, jezyk = 'pl'):
    # Jezyki w slowniku.
    komunikaty = {
        'pl': {
            'binarna': 'To jest liczba binarna.',
            'osemkowa': 'To jest liczba ósemkowa.',
            'dziesietna': 'To jest liczba dziesiętna.',
            'szesnastkowa': 'To jest liczba szesnastkowa.',
            'niepoprawna': 'Niepoprawny format liczby.'
        },
        'en': {
            'binarna': 'This is a binary number.',
            'osemkowa': 'This is an octal number.',
            'dziesietna': 'This is a decimal number.',
            'szesnastkowa': 'This is a hexadecimal number.',
            'niepoprawna': 'Invalid number format.'
        },
        'de': {
            'binarna': 'Das ist eine Binärzahl.',
            'osemkowa': 'Das ist eine Oktalzahl.',
            'dziesietna': 'Das ist eine Dezimalzahl.',
            'szesnastkowa': 'Das ist eine Hexadezimalzahl.',
            'niepoprawna': 'Ungültiges Zahlenformat.'
        }
    }

    # Sprawdzenie cz jest jezyk
    if jezyk not in komunikaty:
        jezyk = 'pl'

    # Skrypt
    try:
        liczba = int(spr_liczbe, 0)

        print(f"0b - Liczba binarna, 0o - ósemkowa, 0x - szesnastkowa", "\n"*2)
        
        print(f"{komunikaty[jezyk]['dziesietna']} Liczba: {liczba}")
        print(f"{komunikaty[jezyk]['binarna']} Liczba: {bin(liczba)}") 
        print(f"{komunikaty[jezyk]['osemkowa']} Liczba: {oct(liczba)}") 
        print(f"{komunikaty[jezyk]['szesnastkowa']} Liczba: {hex(liczba)}")
    except ValueError:
        print(komunikaty[jezyk]['niepoprawna'])

konwertuj("0x1A")
konwertuj("0b1010")
konwertuj("11")

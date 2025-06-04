import random
class KodGenerator:
    def generuj_kod(self, dlugosc=4, unikalne=False, tryb='kolory'):
        kolory = ['czerwony', 'zielony', 'niebieski', 'żółty', 'biały', 'czarny']
        liczby = ['1', '2', '3', '4', '5', '6']
        
        if tryb == 'kolory':
            symbole = kolory
        elif tryb == 'liczby':
            symbole = liczby
        else:
            print("Dostępne tryby to: 'kolory' lub 'liczby'")
        
        if unikalne and dlugosc > len(symbole):
            print(f"Nie można wygenerować unikalnego kodu - dostępnych symboli: {len(symbole)}, żądana długość: {dlugosc}")
        
        if unikalne:
            kod = random.sample(symbole, dlugosc) 
        else:
            kod = [random.choice(symbole) for _ in range(dlugosc)] 
        
        return kod

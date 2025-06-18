import os
import time
from generator_kodu import KodGenerator  

def wyczysc_ekran():
    os.system('cls' if os.name == 'nt' else 'clear')

def powitanie():
    wyczysc_ekran()
    print("=" * 50)
    print("🎮  WITAJ W GRZE MASTERMIND  🎮".center(50))
    print("=" * 50)
    print("\nSpróbuj odgadnąć ukryty kod!")
    print("Zasady: komputer tworzy tajny ciąg symboli, a Ty musisz go zgadnąć.\n")
    time.sleep(2)

def wybierz_trudnosc():
    trudnosci = ['latwy', 'sredni', 'trudny']
    print("Dostępne poziomy trudności:")
    print(" - łatwy    (6 symboli, unikalne kolory)")
    print(" - średni    (6 symboli, powtórzenia dozwolone)")
    print(" - trudny   (8 symboli, szersza paleta, powtórzenia dozwolone)\n")

    while True:
        wybor = input("Wybierz poziom trudności (latwy/sredni/trudny): ").strip().lower()
        if wybor in trudnosci:
            return wybor
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.\n")

def main():
    powitanie()
    trudnosc = wybierz_trudnosc()

    generator = KodGenerator()
    kod = generator.generuj_kod(trudnosc=trudnosc)

    print("\n✅ Tajny kod został wygenerowany! ")
    print("Kod (debug):", kod)  #TODOuzupełnić
    print("\nRozpocznij zgadywanie!")

if __name__ == "__main__":
    main()
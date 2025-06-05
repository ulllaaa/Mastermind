import generator_kodu

def mastermind():
    ukryty_kod = generator_kodu.KodGenerator().generuj_kod(4, unikalne=False)


mastermind()
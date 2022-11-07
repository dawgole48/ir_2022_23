class Liczba:
    system = 10
    znaki = "ABCDEFGHIJKLMNOPRSTUVWXYZ";
    def __init__(self, liczba, system):
        self.system = system;
        self.liczba = liczba;

    def przeliczanie(self, liczba, sys_zr, sys_doc):
        l_doc = 0;
        wynik = 0;
        dlugosc = len(liczba)
        for i in range(0, dlugosc):
            znak = liczba[i]
            wynik += (pow(sys_zr, dlugosc - i) - 1) * int(znak)
            print(znak, wynik);


lcz = Liczba(10, 2)
lcz.przeliczanie("01101", 2, 10)
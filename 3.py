def silnia(i):
    wynik = 1;
    wynik_dzialanie = "";
    j = 1;
    while(j <= i):
        wynik *= j
        print(j, wynik)
        j += 1
    return wynik

LICZBA = 20
silnia(LICZBA)
pliki = {
        "D:/pantadeusz_pl.txt",
        "D:/pantadeusz_bez_pl.txt",
        "D:/pantadeusz_bez_pl",
        "D:/pt.txt",
        "D:/pt_OK.txt"
    }
def sprawdzenie(nazwa_pliku):
    plik = open(nazwa_pliku);
    tekst = plik.read()
    samogloski = "BCĆDFGHJKLŁMNŃPRSŚTWZŹŻ"
    count = 0
    count_samo = 0

    for i in range(len(tekst)):
        if tekst[i].isalpha():
            count += 1
        if(tekst[i].upper() in samogloski):
            count_samo += 1

    print("Plik: ", nazwa_pliku)
    print("Liczba znaków:", len(tekst))
    print("Liczba liter:", count)
    print("Liczba samogłosek:", count_samo, "\n")

for plik in pliki:
    sprawdzenie(plik)
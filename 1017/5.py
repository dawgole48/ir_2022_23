from random import randint
from xml.etree.ElementTree import tostring
n = 10;
random = randint(0,n)
graTrwa = True;

while graTrwa:
    try:
        liczba = int(input("Liczba od 1 do "+tostring(n)+": "))
    except: 
        print("Wartosc musi byc liczba")
        exit()

    if(liczba == random):
        print("Wygrana")
        graTrwa = False
    elif(liczba<random):
        print("za mala")
    elif(liczba>random):
        print("za duza")
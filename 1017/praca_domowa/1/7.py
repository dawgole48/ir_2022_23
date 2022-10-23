def an(a1, r, n):
    return (a1 + r*(n-1))
def silnia(n):
    w = 1
    if(n > 0):
        for i in range(0,n):
            w = w * (i+1)
        return w
    else:
        return False
def alt(liczba, i, r = 0):
    if(liczba%2 == r):
        return -(i)
    else:
        return i
    
n = int(input("Podaj n: "))
if(n<=0):
    print("N nie może być ujemne");
else:
    licznik = 0
    mianownik = 1
    wartosc = 0;
    for i in range(1,n+1):
        licznik += an(2, 5, i)
        mianownik *= an(3, 4, i)
        print(licznik, mianownik)
    wartosc = round(licznik/mianownik)
    print("Wartosc: ", wartosc)
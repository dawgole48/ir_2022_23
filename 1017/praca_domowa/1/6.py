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
    
n = int(input("Podaj n: "))
if(n<=0):
    print("N nie może być ujemne");
else:
    licznik = 0
    mianownik = 0
    wartosc = 0;
    for i in range(1,n+1):
        licznik += silnia(i)
        mianownik += an(-0.2, 0.3, i)
        print(licznik, mianownik)
    wartosc = round(licznik/mianownik)
    print("Wartosc: ", wartosc)
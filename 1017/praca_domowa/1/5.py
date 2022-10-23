def an(a1, r, n):
    return (a1 + r*(n-1))
    
n = int(input("Podaj n: "))
if(n<=0):
    print("N nie może być ujemne");
else:
    licznik = 1
    mianownik = -30
    wartosc = 0;
    for i in range(1,n+1):
        licznik *= an(2, 0.5, i)
        mianownik *= 0.1
        print(licznik, mianownik)
    wartosc = round(licznik/mianownik)
    print("Wartosc: ", wartosc)
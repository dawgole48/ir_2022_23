def an(a1, r, n):
    return (a1 + r*(n-1))

n = int(input("Podaj n: "))
if(n<=0):
    print("N nie może być ujemne");
else:
    licznik = 0
    mianownik = 1
    wartosc = 0;
    for i in range(1,n+1):
        licznik += i
        mianownik *= an(2, 4, i)
        print(licznik, "/", mianownik)
    wartosc = round(licznik/mianownik)
    print("wartosc: ", wartosc)
        

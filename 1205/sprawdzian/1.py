a = []
b = []
a.append(int(input("Podaj licznik 1. ułamka: ")))
a.append(int(input("Podaj mianownik 1. ułamka: ")))
b.append(int(input("Podaj licznik 2. ułamka: ")))
b.append(int(input("Podaj mianownik 2. ułamka: ")))
print(a[0], "/", a[1])
print(b[0], "/", b[1])

def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    else:
        return a

def nww(a, b):
    return a*b / nwd(a,b)

mianownik = nww(a[1], b[1])

a[0] = (mianownik/a[1]) * a[0]
b[0] = (mianownik/b[1]) * b[0]

print(a[0], "/", mianownik)
print(b[0], "/", mianownik)

wynik = a[0] + b[0];
w_nwd = nwd(wynik, mianownik);
wynik = wynik/w_nwd
mianownik = mianownik/w_nwd

print("wynik: ", wynik, "/", mianownik)

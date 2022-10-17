n = 20
d = 4
a = -0
wynik = 1
for i in range(0, n):
    
    a = (a + (d if a>0 else -d)) * -1
    wynik = wynik * a;
    print(a)

print("Wynik: ", wynik)
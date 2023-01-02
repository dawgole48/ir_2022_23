n = int(input("Podaj ilosc wyrazow ciagu: "))
a1 = 1
a2 = 1
a3 = 1
for i in range(0, n):
    if(i<3):
        print(a1)
    else:
        a = a1 + a2 + a3
        a2 = a1
        a3 = a2
        a1 = a
        print(a1)

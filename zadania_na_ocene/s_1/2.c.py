n = int(input("Podaj ilosc wyrazow ciagu: "))
a1 = -1
a2 = -1
an = 0;
for i in range(0, n):
    an = a1
    if(a1 == 0):
        a1 = -1 * a2
    elif(a1 != 0 and a2 != 0):
        a1 = 0
    a2 = an
    print(a1)

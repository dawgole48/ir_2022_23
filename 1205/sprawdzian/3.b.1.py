def a(n):
    if(i<0):
        return 0
    elif(i<3):
        return 1
    return a(n-1) + a(n-2) + a(n-3)

n = int(input("Podaj ilosc wyrazow ciagu: "))
for i in range(0, n):
    print(i, a(i))

#DO
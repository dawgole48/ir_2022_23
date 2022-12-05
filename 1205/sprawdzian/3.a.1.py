def a(n):
    if(n<0):
        return 0
    return a(n-1)*2 + 1

n = int(input("Podaj ilosc wyrazow ciagu: "))
for i in range(0, n):
    print(a(i))

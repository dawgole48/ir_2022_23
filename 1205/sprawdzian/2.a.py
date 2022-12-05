from math import pow
n = int(input("Podaj ilosc wyrazow ciagu: "))
for i in range(0, n):
    print(int(pow(2, i+1)))
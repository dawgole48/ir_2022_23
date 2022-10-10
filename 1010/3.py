def silnia(n):
    if(n == 0):
        return 1
    return (n * silnia(n-1))

n = 1000
for i in range(0,n):
    print(i, silnia(i))
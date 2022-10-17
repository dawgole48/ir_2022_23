from re import S


n = 10
def silnia(n):
    w = 1
    if(n > 0):
        for i in range(0,n):
            w = w * (i+1)
        return w
    else:
        return False

w = 0;
for i in range (0,n):
    s = silnia(i+1)
    print(s)
    w = w + s
print("wynik: ", w)
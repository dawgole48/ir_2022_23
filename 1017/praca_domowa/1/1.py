n = 20
a = -2
d = 3
s = 0
for i in range (1,n):
    print(a)
    s = s + a
    a = ((a + (d if a>0 else -d)) * -1)

print("wynik: ", s)
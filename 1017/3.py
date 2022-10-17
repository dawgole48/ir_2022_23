a0 = 1
a1 = 1
n = 2137
for i in range (1, n):
    a2 = a0 + 3*a1
    a0 = a1
    a1 = a2

if(n==0):
    print(1)
elif(n==1):
    print(1)
else:
    print(a2)
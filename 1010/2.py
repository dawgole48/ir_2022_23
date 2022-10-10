def fib(n):
    if(n==0):
        return 1
    elif(n==1):
        return 1

    return fib(n-1) + fib(n-2)

n = 100
for i in range(0,n):
    print(i, fib(i))
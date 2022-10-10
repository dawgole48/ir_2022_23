print("")


def Fibonacci(n):
    a1 = 1
    a2 = 1

    try:
        n = int(input)
    except:
        return 0

    if(n<=0):
        return 0
    elif(n<3):
        return 1
    else:
        for i in range(0, n-2):
            a3 = a1 + a2
            a1 = a2
            a2 = a3
        return a3
def an(n):
    if(n==0):
        return 1
    elif(n==1):
        return 1
    return (an(n-2) + 3 * an(n-1))

def bn(n):
    if(n==0):
        return 1
    elif(n==1):
        return 1
    return (bn(n-1) * bn(n-2) + 3)



for i in range(100):
    print(i, bn(i))

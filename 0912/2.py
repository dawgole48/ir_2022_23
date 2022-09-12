a = float(input('podaj a:'))
b = float(input('podaj b:'))
c = float(input('podaj c:'))

if a > b:
    if a > c:
        print('a')
    elif a == c:
        print('a, c')
    else:
        print('c')
elif b > a:
    if b > c:
        print('b')
    elif b == c:
        print('b, c')
    else:
        print('c')
elif a == b:
        print('a, b')
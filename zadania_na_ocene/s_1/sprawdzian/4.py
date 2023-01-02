import random
random.seed(4)
for i in range(100):
    a = random.randrange(0,6)
    b = random.randrange(0,6)
    c = random.randrange(0,6)

    if(a!=0 and b!=0 and c!=0):
        if(a+b>c and b+c>a and c+a>b):
            if((a*a)+(b*b)==(c*c) or (a*a)+(c*c)==(b*b) or (b*b)+(c*c)==(a*a)):
                print(a, b, c, 'Mozna zbudowac trojkat prostokatny')
            elif((a*a)+(b*b)<(c*c) or (a*a)+(c*c)<(b*b) or (b*b)+(c*c)<(a*a)):
                print(a, b, c, 'Mozna zbudowac trojkat rozwartokatny')
            else:
                print(a, b, c, 'Mozna zbudowac trojkat otrokatny')
        else:
            print(a, b, c, 'trojkatu nie mozna zbudowac')
    else:
        print(a, b, c, 'Bok nie moze miec 0')
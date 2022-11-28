from random import randint
n = 100000
trafienia = 0
strzaly = 0
for i in range( 0, n ):
    strzaly += 1
    x = randint( 0, 26 )
    y = randint( 0, 26 )
    if( x < 26 and x > -26 and y < ( 10 - ( x * x ) ) and y > ( x * x ) ):
        trafienia += 1
print( trafienia / strzaly )
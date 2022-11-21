from random import randint
os_y = 9
x1 = -8
x2 = 1

strzaly = 0
trafienia = 0

n = 1000000
for i in range( 0, n ):
    strzaly += 1
    x = randint( x1, x2 )
    y = randint( 0, os_y )
    if( y < ( - ( x * x ) - ( 7 * x ) + 2 ) ):
        trafienia += 1;

print( trafienia / strzaly )
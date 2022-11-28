import math
a = 1
b = int( input() )
n = b
for i in range( 0, 10 ):
    c = ( a + b ) / 2
    a = c
    b = n / a
    print( a, b )
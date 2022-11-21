import math
n = 2
pole_suma = 0

for i in range( 0, n - 1 ):
    p1 = math.sin( math.pi * i / n )
    p2 = math.sin( math.pi * ( i + 1 ) / n )
    h = math.pi / n
    pole = ( p1 + p2 ) * h / 2
    print( pole )
    pole_suma += pole
print( "Pole funkcji: ", pole_suma )

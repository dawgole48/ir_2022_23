from random import random
import math

punkty = 0;
n = input("Ilosc strzalow: ")

r = 0.5;

for i in range(int(n)):
    x = random()
    y = random()
    l = math.sqrt( (x-0.5)*(x-0.5) + (y-0.5)*(y-0.5) )
    print( x, y, l )
    if( l < r ):
        punkty += 1

print(punkty)

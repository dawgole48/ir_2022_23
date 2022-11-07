from random import random
import math

n = input("Podaj ilosc strzalow: ")
punkty = 0

for i in range (int(n)):
    x = random()*math.pi
    y = random()
    if(y > math.sin(x)):
        punkty += 1
    print(x, y, math.sin(x))

print(punkty)



from operator import truediv
from random import randint

class gra:
    graTrwa = False
    n = 10

    def __init__(self, n):
        self.graTrwa = True
        self.n = n
        self.random = randint(0,self.n);

    def graj(self, liczba):
        while self.graTrwa:
            if(liczba == self.random):
                self.graTrwa = False
                return("Wygrana")
                
            elif(liczba<self.random):
                return("za mala")
            elif(liczba>self.random):
                return("za duza")
    

g = gra(10);
print(g.graj(7))
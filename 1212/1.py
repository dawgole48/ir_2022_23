plik = open('D:/Users/DAWGOLE48/Desktop/filsoon.tv', 'r');
safemodeXD = 0
print('Kim jest filsoon?')
lines = plik.read().splitlines()
for line in lines:
    if(safemodeXD and line[0] != "#"):
        print("- "+line)
    elif(safemodeXD != 1):
        print("- "+line.strip("#"))
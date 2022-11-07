a = '10101010'
po2 = 1
dz = 0
for i in range(8):
    print(i)
    if(a[-i] == 1):
        dz += 2**i

print(dz)
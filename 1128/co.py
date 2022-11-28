a = 'ala ma kota'
a = a.split()
b = []
print( a )
for i in range( len( a ) ):
    print( a[i] )
a[0] = 'A'
for i in range( len( a ) ):
    print( a[i] )
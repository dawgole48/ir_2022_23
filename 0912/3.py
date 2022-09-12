a = float(input('Podaj a:'))
b = float(input('Podaj b:'))
c = float(input('Podaj c:'))

najw = 0;
def sprawdz(a, b, c, call = None):
    global najw
    w = 'Najwieksze: '
    if a>=najw:
        najw = a
        w = w + 'a, '
    if b>=najw:
        najw = b
        w = w + 'b, '
    if c>=najw:
        najw = c
        w = w + 'c, '
    if(call != None): 
        call(w)
sprawdz(a,b,c)
sprawdz(a,b,c,print)


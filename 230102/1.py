offset = int(input("Podaj przesunięcie: "))
text = input("Podaj tekst do zaszyfrowania: ")

out = ""
for let in text:
    out += chr(ord(let) + offset)

print(out)
import sys
total=0
s = input('Numero do cartao (sem sinais) -->')
if (len(s) != 16):
    print("Numero errado. faca de novo")
    exit()
for i in range(0,16,2):
    acum=int(s[i])*2
    if (acum > 9):
        acum=acum-9
        total=total+acum
for i in range(1,17,2):
    total=total+int(s[i])
if ((total%10) != 0 or total > 150):
    print("Cartao invalido")
    exit()
print ("Cartao valido: %s" % s)
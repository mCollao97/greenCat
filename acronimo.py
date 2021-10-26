stringUsuario = input('Ingrese una cadena de texto socio: ')
while True:
    if stringUsuario.isdigit():
        stringUsuario = input("reingrese una cadena mijo, no sea wn")
    else:
        break
miString = stringUsuario.split(' ')
miChar = ''
for i in miString:
    miChar += i[0]
print ("su acronimo es:",miChar)

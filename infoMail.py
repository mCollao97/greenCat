correo = input('Ingrese su dirección de correo: ')
emailDescompuesto = correo.split('@')
nombrePersona = input('Ingrese su nombre porfavor: ')
nombreDescompuesto = nombrePersona.split(' ')
while True:
    if len(nombrePersona.split()) < 4:
        nombrePersona = input('error, reingrese un nombre válido: ')
    else:
        break
print('Hola',nombreDescompuesto[0],' veo que usas una dirección de correo @',emailDescompuesto[1],', increible!')

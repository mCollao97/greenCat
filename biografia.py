from datetime import datetime

nombreCompleto = input('Ingrese su nombre completo: ')
while True:
    if len(nombreCompleto.split()) < 4:
        nombreCompleto = input('error, reingrese un nombre válido: ')
    else:
        break
while True:
    try:
        fechaNac = input("Ingrese fecha nacimiento en formato DD-MM-YYYY: ")
        datetime.strptime(fechaNac, '%d-%m-%Y')
        break
    except ValueError:
        print("Fecha inválida")
print(fechaNac)

direccion = input('Ingrese su direccion por favor: ')
while True:
    if (direccion.isdigit()):
        direccion = input("Ingrese su dirección correcta porfavor: ")
    else:
        break
metasPersonales = input('Podria usted indicarme sus metas personales: ')
while True:
    if (metasPersonales.isdigit()):
        metasPersonales = input("Ingrese texto por favor, no numeros ")
    else:
        break

print("Nombre: ",nombreCompleto)
print("Fecha de Nacimiento: ",fechaNac)
print("Direccion: ",direccion)
print("Metas personales: ",metasPersonales)

cadenaUno = input('Ingrese una palabra: ')
cadenaDos = ""
for letra in cadenaUno:
    cadenaDos = letra + cadenaDos
if cadenaUno == cadenaDos:
    print('es palindromo')
else:
    print('no es palindromo')

from random import randint
numeroAleatorio = randint(0,50)
flag = 0
contador = 0;

while True:
    contador += 1
    if flag == 0:
        x = float(input('Ingrese un numero entre 1 y 50: '))
        flag = 1
    else:
        while x<0 or x>50:
            x = float(input('Error, numero se sale de la escala, reingrese: '))

        if x == numeroAleatorio:
            print("Felicidades, has conseguido ganar el juego.")
            break
        else:
            x = float(input("Lo siento, no has adivinado el número, reingresa otro"))
            continue
print('te ha tomado',contador,'intentos')

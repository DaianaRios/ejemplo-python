## adivina adivinador
import random
numero_aleatorio = random.randrange(0,100)
gane = False
print("Tenes 5 intentos para adivinar un entre 0 y 99")
intento = 1
while intento < 6 and not gane :
          numeroIngresado = int (input ('ingresa tu numero : '))
          if numeroIngresado == numero_aleatorio :
              print('Ganaste ! y necesitaste {} intentos !!!' .format(intento))
              gane = True
          else:
              print('mmmm...No.. ese numero no es...segui intentando.')
              intento +=1
if not gane :
    print('\n Perdiste :(\n El número era: {}'.format(numero_aleatorio))
__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

print('JUEGO DE CARTAS')
print('*' * 80)

#Dos jugadores y 3 rondas.-
sec='Copa','Basto','Espada','Oro'
puntajeJugador1=0
puntajeJugador2=0

#1era Ronda
print('[Primera ronda]')
#Para jugador1
num1=random.randint(1,12)
palo1=random.choice(sec)
print('Primer jugador obtiene', num1, 'de', palo1)

#Para jugador2
num2=random.randint(1,12)
palo2= random.choice(sec)
print('Segundo jugador obtiene', num2, 'de', palo2)

suma = num1 + num2
if num1 > num2:
    puntajeJugador1 += suma
elif num1 < num2:
    puntajeJugador2 += suma
else:
    if palo1=='Oro':
        puntajeJugador1 += suma
    elif palo2=='Oro':
        puntajeJugador2 += suma
    else:
        puntajeJugador1 += num1
        puntajeJugador2 += num2

#2da Ronda
print('[Segunda ronda]')
#Para jugador1
num1=random.randint(1,12)
palo1=random.choice(sec)
print('Primer jugador obtiene', num1, 'de', palo1)

#Para jugador2
num2=random.randint(1,12)
palo2= random.choice(sec)
print('Segundo jugador obtiene', num2, 'de', palo2)

suma = num1 + num2
if num1 > num2:
    puntajeJugador1 += suma
elif num1 < num2:
    puntajeJugador2 += suma
else:
    if palo1=='Oro':
        puntajeJugador1 += suma
    elif palo2=='Oro':
        puntajeJugador2 += suma
    else:
        puntajeJugador1 += num1
        puntajeJugador2 += num2

#3 Ronda
print('[Tercera ronda]')
#Para jugador1
num1=random.randint(1,12)
palo1=random.choice(sec)
print('Primer jugador obtiene', num1, 'de', palo1)

#Para jugador2
num2=random.randint(1,12)
palo2= random.choice(sec)
print('Segundo jugador obtiene', num2, 'de', palo2)

suma = num1 + num2
if num1 > num2:
    puntajeJugador1 += suma
elif num1 < num2:
    puntajeJugador2 += suma
else:
    if palo1=='Oro':
        puntajeJugador1 += suma
    elif palo2=='Oro':
        puntajeJugador2 += suma
    else:
        puntajeJugador1 += num1
        puntajeJugador2 += num2

#Verifico quien fue el ganador
print('*' * 80)
print('El total obtenido para el jugador 1 es: ', puntajeJugador1)
print('El total obtenido para el jugador 2 es: ', puntajeJugador2)
if puntajeJugador1 > puntajeJugador2:
   print('El ganador del juego fue el Participante 1!')
elif puntajeJugador2 > puntajeJugador1:
    print('El ganador del juego fue el Participante 2!')
else:
   print('Los jugadores empataron!')
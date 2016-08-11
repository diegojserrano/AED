__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

print('Pares e Impares')
print('*' * 80)

#Subproblema 1: Primera ronda
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
suma = dado1 + dado2
print("Primera ronda: Los dados suman:",suma,"(",dado1,"y",dado2,")")
if suma%2 != 0:
    jugador1 = suma
    jugador2 = 0
else:
    jugador1 = 0
    jugador2 = suma
print("Jugador 1:",jugador1,"Jugador 2:",jugador2)

#Subproblema 2: Segunda ronda
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
suma = dado1 + dado2
print("Segunda ronda: Los dados suman:",suma,"(",dado1,"y",dado2,")")
if suma%2 != 0:
    jugador1 = jugador1 + max(dado1,dado2)
    jugador2 = jugador2 - min(dado1,dado2)
else:
    jugador2 = jugador2 + max(dado1,dado2)
    jugador1 = jugador1 - min(dado1,dado2)
print("Jugador 1:",jugador1,"Jugador 2:",jugador2)

#Subproblema 3: Determinar resultado
if jugador1 > jugador2:
    resultado = "Ganó el JUGADOR 1"
elif jugador2 > jugador1:
    resultado = "Ganó el JUGADOR 2"
else:
    resultado= "EMPATE"

#Resultado
print('*' * 80)
print('[' * 10,resultado,']' * 10)
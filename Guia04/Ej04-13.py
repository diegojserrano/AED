__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

#Titulos
print('Piedra, Papel o Tijera - Humano vs. Máquina')
print('*' * 80)

#Ingreso de datos
opcion = int(input('Piedra (0), Papel(1) o Tijera (2)? Indique su opción: '))

#Proceso
elementos = ('Piedra','Papel','Tijera')
humano = elementos[opcion]
maquina = random.choice(elementos)
print("Máquina elige",maquina)

if humano == maquina:
    resultado= "Empataron"
elif humano == 'Piedra':
    if maquina== 'Papel':
        resultado = "Ganó la MÁQUINA (Papel envuelve a Piedra)"
    elif maquina == 'Tijera':
        resultado = "Ganó el HUMANO (Piedra rompe a Tijera)"
elif humano == 'Papel':
    if maquina == 'Piedra':
        resultado = "Ganó el HUMANO (Papel envuelve a Piedra)"
    elif maquina == 'Tijera':
        resultado = "Ganó la MÁQUINA (Tijera corta a Papel)"
elif humano == 'Tijera':
    if maquina == 'Piedra':
        resultado = "Ganó la MÁQUINA (Piedra rompe a Tijera)"
    elif maquina == 'Papel':
        resultado = "Ganó el HUMANO (Tijera corta a Papel)"

#Mostrar resultados
print("¡",resultado,"!")
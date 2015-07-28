__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

TIEMPO_TAXI = 45

# Titulo y carga de datos
print('Ejercicio L - Determinacion de tiempo de llegada a aeropuerto')
print('Las horas se ingresaran en formato HH:mm por ejemplo 14:45 o 05:30')
partida = input('Ingrese la hora de partida en formato HH:mm :')
llegada = input('Ingrese la hora de llegada en formato HH:mm :')

# Procesos

# Sacamos la hora de la cadena de caracteres
hora_partida = int(partida[0:2])
# Sacamos los minutos de la cadena de caracteres
minutos_partida = int(partida[3:])

# Sacamos la hora de la cadena de caracteres
hora_llegada = int(llegada[0:2])
# Sacamos los minutos de la cadena de caracteres
minutos_llegada = int(llegada[3:])

#Transformamos HH de la hora de partida a minutos y la acumulamos a los mm de los minutos de partida
minutos_partida += hora_partida * 60
#Transformamos la HH de la hora de llegada a minutos y la acumulamos a los mm de los minutos de llegada
minutos_llegada += hora_llegada * 60

duracion_viaje_minutos = minutos_llegada - minutos_partida

hora_llegada_hotel = (minutos_llegada + TIEMPO_TAXI) // 60
minutos_llegada_hotel = (minutos_llegada + TIEMPO_TAXI) %60

# Presentacion de Resultados
print('La duracion del viaje es de: ',duracion_viaje_minutos,' minutos')

print('El viajero llega la hotel a las ',(str(hora_llegada_hotel)+':'+str(minutos_llegada_hotel)))





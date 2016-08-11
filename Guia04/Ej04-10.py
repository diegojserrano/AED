__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

print('Promedio de temeraturas')
print('=' * 80)

print('\nIngreso de temperaturas')
temp1 = round(random.uniform(15.1, 45.9),2)
temp2 = round(random.uniform(15.1, 45.9),2)
temp3 = round(random.uniform(15.1, 45.9),2)

# Procesos calculo del promedio
promedio = (temp1 + temp2 + temp3) / 3

# Salida de resultados
print ('El promedio de las temperaturas ingresadas fue de ', promedio, ' grados')

if temp1 > promedio or temp2 > promedio or temp3 > promedio:
    print('Existe al menos una temperatura que supera al promedio')
else:
    print('Todas las temperaturas estan por debajo del promedio')
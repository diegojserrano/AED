__author__ = 'Catedra Algoritmos y Estructuras de Datos'

# Constantes
ADICIONAL_KM = 0.30

# Titulo y carga de datos
print('Ejercicio M - Costo boleto de viaje')
costo_base = float(input('Ingrese el costo base del boleto: '))
kilometros = int(input('Ingrese los kilometros a recorrer: '))

# Procesos
adicional = kilometros * 0.30
costo_total = costo_base + adicional

# Presentacion de Resultados
print('El costo del viaje es ', costo_total)
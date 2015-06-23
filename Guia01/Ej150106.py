__author__ = 'Catedra Algoritmos y Estructura de Datos'

# Titulo y carga de datos
print('Ejercicio F - Ver Fecha en diferente formato')
fecha = input('Ingrese la fecha que desea separar en formato dd/mm/yyyy: ')

# Procesos
dias = fecha[0:2]
meses = fecha[3:5]
anios = fecha[6:]

# Presentacion de Resultados
print('Dia: ', dias, ' - Mes: ', meses, ' - Año: ', anios)


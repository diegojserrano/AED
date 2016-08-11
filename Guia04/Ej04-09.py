__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

ANIO_ACTUAL = 2016

print('La Galeria de Arte')
print('Lectura de Datos')
print('=' * 80)

anio_obra1 = int(input('Ingrese el año de creacion de la primer obra: '))
anio_obra2 = int(input('Ingrese el año de creacion de la segunda obra: '))
anio_obra3 = int(input('Ingrese el año de creacion de la tercer obra: '))

# Proceso para determinar si hay que renovar stock
renovar_stock = False
if ANIO_ACTUAL - anio_obra1 < 10:
    renovar_stock = True

if ANIO_ACTUAL - anio_obra2 < 10:
    renovar_stock = True

if ANIO_ACTUAL - anio_obra3 < 10:
    renovar_stock = True

son_antiguas = anio_obra1 < 1901 and anio_obra2 < 1901 and anio_obra3 < 1901

# Mostrar resultados
if son_antiguas:
    print('Todas las obras de arte son anteriores al siglo XX, carisimas!!!!!!')

if renovar_stock:
    stock = 'Renovar Stock'
else:
    stock = 'Tenemos obras disponibles para vender'
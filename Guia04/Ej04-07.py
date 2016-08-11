__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Comercio')
print('Carga de Articulos Vendidos')
print('=' * 40)

print('Datos del primer Articulo')
print('_' * 40)
nombre = input('Ingrese el nombre del articulo: ')
cantidad = int(input('Ingrese la cantidad vendida del articulo: '))
precio = float(input('Ingrese el precio unitario del articulo: '))
articulo1 = nombre, cantidad, precio

print('\n')
print('Datos del segundo Articulo')
print('_' * 40)
nombre = input('Ingrese el nombre del articulo: ')
cantidad = int(input('Ingrese la cantidad vendida del articulo: '))
precio = float(input('Ingrese el precio unitario del articulo: '))
articulo2 = nombre, cantidad, precio

print('\n')
print('Datos del tercer Articulo')
print('_' * 40)
nombre = input('Ingrese el nombre del articulo: ')
cantidad = int(input('Ingrese la cantidad vendida del articulo: '))
precio = float(input('Ingrese el precio unitario del articulo: '))
articulo3 = nombre, cantidad, precio

# Calculo de la ganancua obtenida por cada tipo de articulo
articulo1 = articulo1[0], articulo1[1] * articulo1[2]
articulo2 = articulo1[0], articulo1[1] * articulo1[2]
articulo3 = articulo1[0], articulo1[1] * articulo1[2]

# Busqueda de la mayor ganacia
if articulo1[1] > articulo2[1] and articulo1[1] > articulo3[1]:
    mayor = articulo1
elif articulo2[1] > articulo3[1]:
    mayor = articulo2
else:
    mayor = articulo3

# Salida con calculo de porcentajes
print('El articulo que mayor aporte realizo fue ', mayor[0], ' con una ganancia de $', mayor[1])

total = articulo1[1] + articulo2[1] + articulo3[1]
porcentaje = mayor[1] * 100 / total
print('y representa el ', porcentaje, '% del total de ingresos')
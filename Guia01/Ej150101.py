__author__ = 'Catedra Algoritmos y Estructuras de Datos'

# Desarrolle un programa para calcular el área de un triángulo, cargando por teclado el valor de la base,
#  pero sabiendo que su altura es igual al cuadrado de la base.
# (Observar que la altura no es un dato... sólo se indica la forma de calcularla de acuerdo a la base que sí es un dato)

# Titulos y Lectura de datos
print('Ejercicio A - Calculo del area de un triangulo')
base = float(input('Ingrese la base del triangulo: '))

# Procesos
# Se obtiene la altura del triangulo
h = base ** 2
area = (base * h)/2

# Presentacion de resultados
print('El area de un triangulo es ', area)
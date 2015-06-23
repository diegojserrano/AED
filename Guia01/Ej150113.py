__author__ = 'Catedra Algoritmos y Estructuras de Datos'

# Titulo y Carga de datos
print('Ejercicio Ll - Resumen eleccion centro vecinal')
apellido = input('Ingrese el apellido del candidato: ')
nombre = input('Ingrese el nombre del candidato: ')
votos = int(input('Ingrese la cantidad de votos: '))

# Procesos
iniciales = nombre[0] + apellido[0]
cantidad_x = 'x' * votos

# Presentacion de Resultados
print(iniciales, '(', votos, ')')
print(cantidad_x)
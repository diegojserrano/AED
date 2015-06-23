__author__ = 'Catedra Algoritmos y Estructuras de Datos'

# Titulo y carga de datos
print('Ejercicio E - Calculo de polinomio y discriminante ecuacion 2 grado')
a = float(input('Ingrese el valor de la constante a del polinomio: '))
b = float(input('Ingrese el valor de la constante b del polinomio: '))
c = float(input('Ingrese el valor de la constante c del polinomio: '))
x = float(input('Ingrese el valor de la x del polinomio: '))

# Procesos
y = a * (x ** 2) + b * x + c
discriminante = b ** 2 - 4 * a * c

# Presentacion de Resultados
print('La y del polinomio de segundo grado es ', y)
print('El discriminante del polinomio es ', discriminante)
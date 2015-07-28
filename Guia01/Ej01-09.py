__author__ = 'Catedra Algoritmos y Estructuras de Datos'

# Titulos y Carga de Datos
print('Ejercicio I - Calculo de angulos')
x = float(input('Ingrese el valor de la suma de los angulos a buscar: '))
y = float(input('Ingrese el valor de la resta de los angulos a buscar: '))

# Procesos

# x = alfa + beta
# y = alfa - beta
# Análisis:
# x = alfa + beta  =>  alfa = x - beta
# y = alfa - beta => y = x-beta-beta => y = x - 2 beta => y + 2 beta = x => 2 beta = x - y => beta = (x-y)/2
# Si beta = (x-y)/2 entonces:
# Si y = alfa - beta => y + beta = alfa

beta = (x-y)/2
alfa = y + beta

print('Valor del angulo alfa: ', alfa)
print('Valor del angulo beta: ', beta)



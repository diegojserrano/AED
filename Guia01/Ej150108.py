__author__ = 'Catedra Algoritmos y Estructuras de Datos'

# Titulo y carga de datos
print('Ejercicio H - Calculo de plazo fijo')
capital = float(input('Ingrese el capital del plazo fijo: '))

# Procesos
capital_final = capital * 1.023 - 20
#La función round(x,n) Retorna el número flotante x, pero redondeado a n dígitos a la derecha del punto decimal.(Ficha 2)
capital_final = round(capital_final, 2)

# Presentacion de resultados
print('El capital final que se obtiene del plazo fijo es ', capital_final)


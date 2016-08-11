__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Titulo y carga de datos
print('PALABRA ENMASCARADA')
palabra = input('Ingrese palabra a enmascarar:')

# Procesos

asteriscos = "*" * (len(palabra)-2)
enmascarada = palabra[0] + asteriscos + palabra[-1]

# Resultados
print('\nLa palabra enmascarada es:', enmascarada)
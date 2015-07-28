__author__ = 'Catedra Algoritmos y Estructuras de Datos'

# Titulo y Carga de datos
print('Ejericio K - Porcentajes de votos parlamentarios')
votos_favor_ley = int(input('Ingrese la cantidad de votos a favor de la ley: '))
votos_encontra_ley = int(input('Ingrese la cantidad de votos a favor en contra de la ley: '))

# Procesos
total = votos_favor_ley + votos_encontra_ley
porcentaje_favor = votos_favor_ley / total * 100
porcentaje_contra = votos_encontra_ley / total * 100

# Presentacion de resultados
print('El porcentaje de votos a favor fue de ', porcentaje_favor, '%')
print('El porcentaje de votos en contra fue de ', porcentaje_contra, '%')

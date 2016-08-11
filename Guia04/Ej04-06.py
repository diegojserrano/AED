__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Jornal de Operario')
print('=' * 80 , '\n')

print("Ingreso de datos")
print('-' * 80)
turno = int(input('Ingrese el turnos del operario (1 - Diurno, 2 - Nocturno): '))
horas = int(input('Ingrese la cantidad de horas trabajadas: '))

print('\nProcesos de datos')
if turno == 1:
    total = horas * 35.5
elif turno == 2:
    total = horas * 40.60
else:
    total = 0

print('\nPresentacion de resultados')
if total != 0:
    print('La empresa le debe pagar al operario un jornal de $', total)
else:
    print('No se ha calculado el jornal porque no se ingreso un turno valido.')
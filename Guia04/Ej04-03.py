print('Calculo de regularidad de una alumno')
print('*' * 80)

#ingreso de datos
primer_parcial = float(input('Ingrese la nota del primer parcial: '))
segundo_parcial = float(input('Ingrese la nota del segundo parcial: '))
practicos = float(input('Ingrese el promedio de los trabajos practicos: '))

#procesos

promedio = (primer_parcial + segundo_parcial + practicos) / 3

condicion = ''
if promedio < 4:
    condicion = 'Alumno Libre'
elif promedio >= 4 and promedio <= 8:
    condicion = 'Alumno Regular'
else:
    condicion = 'Alumno Promocionado'

#Salidas
print('El promedio del alumno fue de ', round(promedio,2), ' y su condicion es ', condicion)

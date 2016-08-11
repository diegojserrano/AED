__author__ = 'Catedra de Algoritmos y Estructuras de Datos'
print('Busqueda del mayor par de orden par')
print('=' * 80)
orden = 0
mayor = 0
numero = int(input('Ingrese un numero (El proceso cortara cuando ingrese 0): '))
while numero !=0:
    if orden % 2 == 0 and numero % 2 == 0 and numero > mayor:
        mayor = numero
    orden += 1
    numero = int(input('Ingrese otro numero: '))
print('El mayor numero par ingresado en orden par es ', mayor)

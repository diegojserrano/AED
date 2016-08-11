__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Análisis de Texto')
print('*' * 80)

#Inicialización
letras = 0
palabras = 0
palS = 0
tieneSA= False
palSA = 0

#Carga de datos y proceso
ant = None
act = None
while act != '.':
    act = input('Ingrese caracter (con . termina): ')
    if (act == ' ' or act == '.') and ant != None:
        palabras += 1
        #Termina en s?
        if ant == 's':
            palS += 1
        #Contiene la expresión sa?
        if tieneSA == True:
            palSA += 1
        #Reiniciar las variables de palabra
        tieneSA = False
    else:
        letras += 1
        #Identificar expresión sa
        if act=='a' and ant=='s':
            tieneSA = True
    ant = act

#Resultados
print('*' * 80)
if palabras == 0:
    prom = 0
else:
    prom = letras/palabras
print('El promedio de letras por palabra es',prom)
print('Las palabras terminadas en S son',palS)
print('Las palabaras con la expresión SA son',palSA)
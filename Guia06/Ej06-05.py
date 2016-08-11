__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('CENSO POBLACIONAL')
print('*' * 80)

#Inicializar contadores y acumuladores
varones = 0
mujeres = 0
escolares = 0
mayor_80 = False

#Primera carga de datos de corte antes del ciclo
sexo = input('Ingrese sexo (M/F - Otro valor termina): ')

#Proceso repetitivo
while sexo=='M' or sexo=='F':
    #Carga de datos que no determinan el corte del ciclo
    edad =int(input('Ingrese edad: '))
    #Contar varones y mujeres
    if sexo=='M':
        varones+=1
    else:
        mujeres+=1
    #Contar mujeres en edad escolar
    if sexo=='F' and edad >= 4 and edad <= 18:
        escolares+=1
    #Detectar hombres de más de 80 años
    if sexo=='M' and edad > 80:
        mayor_80 = True
    #Nueva carga de dato de corte dentro del ciclo
    sexo = input('Ingrese sexo (M/F - Otro valor termina): ')

#Resultados
print('*' * 80)
if varones > mujeres:
    print('Hay más varones que mujeres')
elif mujeres > varones:
    print('Hay más mujeres que varones')
else:
    print('La cantidad de mujeres y varones es igual')
print('Las mujeres en edad escolar son:',escolares)
if mayor_80==True:
    print('Hay hombres mayores a 80 años')
else:
    print('NO hay hombres mayores a 80 años')
    
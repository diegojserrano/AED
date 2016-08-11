__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Postulantes a un empleo')
print('=' * 80, '\n')

print('Lectura de Datos del primer postulante')
nombre = input('Ingrese el nombre: ')
preguntas = int('Inngrese la cantidad de preguntas que se le realizaron: ')
respondidas = int(input('Ingrese la cantidad de preguntas que respondio: '))

postulante1 = nombre, preguntas, respondidas

print('\nLectura de Datos del segundo postulante')
nombre = input('Ingrese el nombre: ')
preguntas = int('Inngrese la cantidad de preguntas que se le realizaron: ')
respondidas = int(input('Ingrese la cantidad de preguntas que respondio: '))

postulante2 = nombre, preguntas, respondidas

print('\nLectura de Datos del tercer postulante')
nombre = input('Ingrese el nombre: ')
preguntas = int('Inngrese la cantidad de preguntas que se le realizaron: ')
respondidas = int(input('Ingrese la cantidad de preguntas que respondio: '))

postulante3 = nombre, preguntas, respondidas

# Procesos
porcentaje = postulante1[2] / postulante1[1] * 100
postulante1 = postulante1[0], round(porcentaje, 2)

porcentaje = postulante2[2] / postulante2[1] * 100
postulante2 = postulante2[0], round(porcentaje, 2)

porcentaje = postulante3[2] / postulante3[1] * 100
postulante3 = postulante3[0], round(porcentaje, 2)

# determinar nivel en base al porcentaje de cada postulante
if postulante1[1] > 90:
    nivel = 'Nivel superior'
elif 75 <= postulante1[1] < 90:
    nivel = 'Nivel Medio'
elif 50 <= postulante1[1] < 75:
    nivel = 'Nivel Regular'
else:
    nivel = 'Fuera de Nivel'

postulante1 = postulante1[0], postulante1[1], nivel

if postulante2[1] > 90:
    nivel = 'Nivel superior'
elif 75 <= postulante2[1] < 90:
    nivel = 'Nivel Medio'
elif 50 <= postulante2[1] < 75:
    nivel = 'Nivel Regular'
else:
    nivel = 'Fuera de Nivel'

postulante2 = postulante2[0], postulante2[1], nivel

if postulante3[1] > 90:
    nivel = 'Nivel superior'
elif 75 <= postulante3[1] < 90:
    nivel = 'Nivel Medio'
elif 50 <= postulante3[1] < 75:
    nivel = 'Nivel Regular'
else:
    nivel = 'Fuera de Nivel'

postulante3 = postulante3[0], postulante3[1], nivel

if postulante1[1] > postulante2[1] and postulante1[1] > postulante3[1]:
    mayor = postulante1
elif postulante2[1] > postulante3[1]:
    mayor = postulante2
else:
    mayor = postulante3


    #presentacion de resultados
print('El Postulante ', postulante1[0], ' obtuvo el nivel ', postulante1[2])
print('El Postulante ', postulante2[0], ' obtuvo el nivel ', postulante2[2])
print('El Postulante ', postulante3[0], ' obtuvo el nivel ', postulante3[2])

print('El postulante que obtuvo el puesto es ', mayor[0], ' al responder correctamente el ', mayor[1],
      '% obteniendo un nivel ', mayor[2])

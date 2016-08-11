__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Calculo tiempo ganador de posta 4 x 100 estilos')
print('*' * 80)

# tomo cada estilo y lo paso centesimas para sumar

espalda = 52 * 100 + 15
pecho = 62 * 100 + 75
mariposa = 59 * 100 + 80
crol = 48 * 100 + 15

total = espalda + pecho + mariposa + crol

# Una vez obtenido el total convertimos a minutos, 
# segundos y centesimas para el tiempo total
# Para determinar el total de minutos debemos saber
# cuantas centesimas tiene un minuto
# 1 min -> 60 seg y 1 seg -> 10 cs => 1 min = 60 * 100

minutos = total // 6000
resto = total % 6000

segundos = resto // 100
centesimas = resto % 100

print('El equipo ganador de la posta lo hizo en ', minutos, ' minutos ', segundos, ' segundos y ', centesimas , ' centesimas')
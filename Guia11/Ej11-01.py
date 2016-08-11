__author__ = 'Catedra de Algoritmos y Estructuras de Datos'
print("PROCESADOR DE TEXTO\n")

#Incializamos variables
ss = ssi = scc = False
cvocal = clet = cc = cpal = csi = cvi = c1v = ccc = cif = acu = 0
vocales = "AEIOU"
primera = ultima = None
menor = 0

texto = input("Ingrese el texto a procesar:")
texto = texto.upper()

for car in texto:
    if car != " " and car != ".":
        clet += 1
        #detector SI
        if car == "S" and clet == 1:
          ss = True
        else:
            if car == "I" and ss:
                ssi = True
            ss = False

        #detector vocales
        if car in vocales:
            cvocal += 1

        #inicio - fin
        if clet == 1:
            primera = car

        ultima = car

        #detector cc
        if car == "C":
            cc += 1
            if cc == 2:
                scc = True
        else:
            cc = 0

    #fin de palabra
    else:
        if clet > 0:
            cpal += 1
            if cpal == 1:
                menor = clet
            elif clet < menor:
                menor = clet

        if ssi:
            csi += 1

        if cvocal == 1:
            c1v += 1

        if (ultima in vocales) and (clet % 2 == 1):
            cvi += 1

        if scc:
            ccc += 1

        acu += clet

        if primera == ultima:
            cif += 1

        clet = 0
        ss = False
        ssi = False
        cc = 0
        scc = False
        cvocal = 0


#Calculamos promedios y porcentajes
porc = 0
prom = 0
if cpal > 0:
    porc = cvi * 100 / cpal
    prom = acu / cpal

print("*Cantidad de palabras que comienzan con la expresión \"SI\":", csi)
print("*Cantidad de palabras que terminan con una vocal y tienen una cantidad impar de letras:", cvi)
print("*Cantidad de palabras con una única vocal:", c1v)
print("*Cantidad de palabras que comienzan y terminan con la misma letra:", cif)
print("*Cantidad de palabras que contienen la expresión \"CC\":", ccc)
print("*Porcentaje de palabras que terminan con una vocal y tienen una cantidad impar de letras:", porc, "%")
print("*Longitud de la palabra más corta:", menor)
print("*Promedio de letras por palabra:", prom)
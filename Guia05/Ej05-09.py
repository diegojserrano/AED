__author__ = 'Catedra de Algoritmos y Estructuras de Datos' 

 # Carga de datos
 a=int(input("Ingrese el número a: "))
 b=int(input("Ingrese el número b: "))
 c=int(input("Ingrese el número c: "))

 #Subproblema 1: Identificar el orden para cada número ingresado
 if a>b and a>c:
     may=a
     if b>c:
         med=b
         men=c
     else:
         med=c
         men=b
 elif b>c and b>a:
     may=b
     if c>a:
         med=c
         men=a
     else:
         med=a
         men=c
 else:
     may=c
     if b>a:
         med=b
         men=a
     else:
         med=a
         men=b

 #Subproblema 2: Determinar si el tercero es igual al resto de la división de los dos primeros
 if men==may%med:
     print("El tercero es igual al resto de la división de los dos primeros")
 else:
     print("El tercero NO es igual al resto de la división de los dos primeros")
     
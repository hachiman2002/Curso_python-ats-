#BUCLE FOR
"""
El bucle for se utiliza para recorrer los elementos de un objeto
iterable (lista, tupla, conjunto, diccionario, …) y ejecutar un bloque
de código. En cada paso de la iteración se tiene en cuenta a un
único elemento del objeto iterable, sobre el cuál se pueden aplicar
una serie de operaciones.
"""
"""
for i in [1,2,3,4,5,"graciany"]:#una lista
    print("hola mundo")
    print(f"elemento {i}")
"""

####################################

coleccion = {"Alejandro":22,"Maria":12,"Jose":24}#diccionario

"""
for i in coleccion:
   #print(f"Elemento: {i}")#solo muestra la clave del diccionario
   #print(f"{coleccion[i]}")#imprime los valores del diccionario
   #print(f"{i}->{coleccion[i]}")
"""
"""
for clave,valor in coleccion.items():
    print(f"{clave}->{valor}")
"""
####################################
"""
coleccion1 = "Graciany"

for i in coleccion1:
    #print(f"hola")#lo imprimra segun los caracteres
    #print(i)#imprime elemento por elemento
    print(f"{i}",end="")
"""

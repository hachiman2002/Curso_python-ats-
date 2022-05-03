#Diccionarios
"""
Los diccionarios en Python nos permiten almacenar una serie de mapeos
entre dos conjuntos de elementos, llamados keys and values
(Claves y Valores). Todos los elementos en el diccionario se
encuentran encerrados en un par de corchetes {}
"""

diccionaro = {} #diccionario vacio
diccionarioB = {"azul":"blue","rojo":"red","verde":"green"}

diccionarioB["amarillo"] = "yellow"#agregar valores
diccionarioB["azul"] = "BLUE"#modificando el valor
del(diccionarioB["verde"])#elimina una clave y tambien el valor

#print(diccionarioB)
#print(diccionarioB["azul"])#imprime el valor de la clave

datos = {"Graciany":{"edad":22,"estatura":1.73},"Jose":[21,1.75],"Maria":[22,1.65]}
#ingresamos una lista dentro deldiccionario
print(datos)
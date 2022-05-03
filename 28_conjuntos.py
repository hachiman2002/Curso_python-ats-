#conjuntos
"""
Un conjunto es una colección desordenada de valores no repetidos.
Los conjuntos de Python son análogos a los conjuntos matemáticos.
El tipo de datos que representa a los conjuntos se llama set.
El tipo set es mutable: una vez que se ha creado un conjunto,
puede ser modificado.

"""
conjunto = set()
#cuando es conjunto vacio y se le quieren agreagar elementos

conjunto = {1,2,3,"hola",3.56}
#dentro de un conjunto no se pueden colocar listas
#cuando hay dos o mas elementos iguales se guardara como valor unico

conjunto.add(5)#agrega el elemento
conjunto.add("adios")
conjunto.discard(3)#elimina el elemento
conjunto.clear()#elimina el conjunto

#print(3 not in conjunto)#indica si no esta dentro del conjunto



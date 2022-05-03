#tuplas
"""
Una tupla es una secuencia de valores agrupados. Una tupla sirve para agrupar,
como si fueran un único valor, varios valores que, por su naturaleza, deben
ir juntos. El tipo de datos que representa a las tuplas se llama tuple. El
tipo tuple es inmutable: una tupla no puede ser modificada una vez que ha
sido creada.
"""

tupla = (4,"hola",6,78,[1,2,3],4)

#print(tupla[-2])#imprime un element osegun el indice que se le indique
#print(1:)#imprime de de un indice a otro
#print(4 in tupla)#muestra si ese elemento esta dentro de la tupla
#print(tupla.index("hola"))#muestra en que indice esta el elemento
#print(tupla.count(4))#muestra cuantas veces esta ese elemento
#print(len(tupla))#cuenta los elementos de la tupla


######transformar una tupla a lista
tupla = (4,"hola",6,78,[1,2,3],4)
lista = list(tupla)

######transformar una lista a tupla
lista = [4,"hola",6,78,[1,2,3],4]
tupla= tuple(lista)
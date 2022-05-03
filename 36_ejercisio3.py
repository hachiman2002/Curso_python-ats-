"""
EJERCISIO 3:Escriba un programa donde cree una lista con los siguientes
personajes del señor de los anillos.

nombre:Aragorn
clase:Guerrero
raza:Dunadan del norte

nombre:Gandalf
clase:Mago
raza:Istar

nombre:Legolas
clase:Arquero
raza:Elfo Sindar
"""
personajes = []#Creando una lista vacia

p = {"nombre":"Aragon","Clase":"Guerero","Raza":"Dunadan del Norte"}
personajes.append(p)#Agregamos a la lista el personaje

p = {"nombre":"Gandalf","Clase":"Mago","Raza":"Istar"}
personajes.append(p)#Agregamos a la lista el personaje

p = {"nombre":"Legolas","Clase":"Arquero","Raza":"Elfo Sindar"}
personajes.append(p)#Agregamos a la lista el personaje

print(personajes)
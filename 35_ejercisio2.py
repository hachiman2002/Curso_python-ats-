"""
EJERCISIO 2:Escriba un programa que tenga dos listas y que a continuacion
cree las siguientes listas(en las que no debe haber repeticiones)
*1:lista de palabras que aparecen en las dos listas
*2:lista de palabras que aparecen en la primera lista, pero no en la segunda
*3:lista de palabras que aparecen en la segunda lista, pero no en la
*4:lista de palabras que aparecen en ambas lista
"""

lista1 = {"hola","universidad","años","nombre"}
lista2 = {"hola","colegio","dias","nombre","apellido"}

#c1 --> conjunto 1
c1 = set(lista1)
c2 = set(lista2)

print(f"1:{c1 | c2}")
print(f"2:{c1 - c2}")
print(f"3:{c2 - c1}")
print(f"4:{c1 & c2}")

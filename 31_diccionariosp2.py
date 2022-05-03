#diccionarios

equipo = {10:"Paulo Dybala",11:"Douglas Costa",7:"Cristiano Ronaldo",17:"Mario Mandzuzick"}

print(equipo[10])
print(equipo.get(6,"no existe un jugador con ese numero"))
"""
get () devuelve el valor de la clave especificada,
si el valor no está en el diccionario o un valor predeterminado.
"""
print(11 in equipo)#comprueba si esta dentro del diccionario segun la clave
print(equipo.keys())#solo muestra las claves
print(equipo.values())#solo muestra los nombres
print(equipo)#muestra el diccionario completo
print(equipo.items())#me integra t0do dentro de una lista
print(len(equipo))#cuenta los elementos
equipo.clear()#elimina el diccionario
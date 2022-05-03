# conjuntos

a = {1,2,3}
b = {3,4,5}
c = {3,2,1}
ab = {1,2,3,4,5}
"""
print(a == b)
print(a == c)#son iguales aunque tengan los elementos desordenados
print(len(a))#cuenta los elementos
"""

d = a | b#une los conjuntos
print(d)

#interseccion: son los elementos que estan en ambos conjuntos
e = a & b

#diferencia: elementos del primer conjunto que no estan en el segundo
f = a - b
#diferencia: elementos del segundp conjunto que no estan en el primero
h = b - a

#diferencia simetrica: elementos que estan en a y b pero no estan en ambos conjuntos
i = a^b

#subconjubto
print(a.issubset(c))

#super conjunto
print(c.issuperset(a))

#conjuntos disconexos:comparten algun elemento en comun
print(a.isdisjoint(b))

#conjuntos inmutables: no se puede modificar
j = frozenset({1,2,3})


print(i)
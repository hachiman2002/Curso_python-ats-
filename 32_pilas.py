#pilas con listas
"""
Una pila (stack en inglés) es una lista ordenada o estructura de datos
que permite almacenar y recuperar datos, siendo el modo de acceso a sus
elementos de tipo LIFO (del inglés Last In, First Out, «último en
entrar, primero en salir»).
"""
pila = [1,2,3]

pila.append(4)#agreaga elementos al final
pila.append(5)
#pila inicial
print(pila)


#sacando elementos por el final
n = pila.pop()
print(f"sacando el elemento {n}")

print(pila)
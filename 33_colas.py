#colas con listas
"""
Una cola (también llamada fila) es una estructura de datos, caracterizada
por ser una secuencia de elementos en la que la operación de inserción
push se realiza por un extremo y la operación de extracción pull por
el otro.
"""

cola = ["maria","alejandro","graciany"]

#agregamos elementos al final de la cola
cola.append("karla")
cola.append("flor")

print(cola)

#sacando elementos por el principio de la cola
n = cola.pop(0)

print(f"estan atendiendo a {n}")

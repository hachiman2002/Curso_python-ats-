#listas parte 2

listaA = ["lunes","martes","miercoles","jueves","viernes",40,5.67,[1,2,3],True]

#print(len(listaA))-cuenta los elementos de la lista

listaB = [1,2,3,4,5]
listaB2 = ["1a","2a","3a","4a","5a"]
listaB3 = listaB + listaB2#suma dos listas

listaB.append(6)#agrega un elemnto al final de la lista
listaB.append("Graciany")
listaB.extend([6,7,8])#agrega varios elementos al final de la lista


listaC = [1,2,4,5]
listaC.insert(2,3)#inserta un elemento a la lista
#primero va el indice y luego el elemento

listaD = [1,2,3,4,5,"Graciany",1,2,3,4,5,"Graciany",1]
"""
print(3 in listaD)#muestra si el elemento esta dentro de la lista
print("Graciany" in listaD)
print(listaD.index)#retorna el indice del valor que estes buscando
print(listaD.index("Graciany"))
print(listaD.count)#indica cuantos valores hay en la lista
"""
listaE = [1,2,3,4,5,"Graciany"]
listaE.pop(3)#elimina el elemento segun el indice
listaE.remove(1)#elimina el elemento segun el elemento
listaE.clear()#elimina la lista completa
listaE.reverse()#invierte la lista


listaG = [1,2,3,4,5,"Graciany"]*2
#print(listaG)

listaH = [1,4,6,3,4,2,5]
listaH.sort()#ordena los elementos
listaH.sort(reverse=True)#las ordena desendentemente

print(listaD)
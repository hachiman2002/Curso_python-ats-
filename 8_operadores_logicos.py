"""
OPERADORES LOGICOS:

and(conjuncion)--> and-->multiplicacion logica (true= 1,false=0)
or(disyuncion)--> or -->tiene que haber un verdadero
negacion--> not-->retorna lo contrario

1-Permite construir expresiones logucas, se obtiene como resultado
BOOLEANOS.

prioridad: not, and, or
"""

#ejemplo
"""
a = 10
b = 12
c = 13
d = 10

operacion = ((a>b)or(a<c))and((a==c)or(a>=b))
print(operacion)
"""

#ejercisio

a = 10
b = 15
c = 20

resultado = not((a>b)or(b<c))
print(resultado)
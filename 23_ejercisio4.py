"""
EJERCISIO 4
Construir un progra,a que simule el funcionamiento de una
calculadora que pueda realizar las cuatro operaciones aritmeticas
basicas (suma,resta,mult y div).El usuario debe especificar la operacion
con el primer caracter del nombre de la operacion

"""
operacion = str(input("Elija las siguientes opciones:S-R-M-D: ").upper())
n1 = float(input("Digite el primer valor:"))
n2 = float(input("Digite el segundo valor:"))

if operacion =='S':
    print(n1 + n2)
elif operacion =='R':
    print(n1 - n2)
elif operacion =='M':
    print(n1 * n2)
elif operacion == 'D':
    print(n1 / n2)
else:
    print("Se equivoco de operacion")
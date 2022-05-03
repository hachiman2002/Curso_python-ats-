#BUCLE WHILE
"""
Python utiliza el bucle while de forma similar a otros lenguajes
populares. El bucle while evalúa una condición y luego ejecuta un
bloque de código si la condición es verdadera. El bloque de código
se ejecuta repetidamente hasta que la condición llega ser o es falsa.
"""
"""
import math

numero = int(input("Digite un numero:"))

#while = mientras
while numero<0:
    print("Error...Ingrese numero positivo")
    numero = int(input("Digite un numero:"))

print(f"\nSu raiz cuadrada es:{(math.sqrt(numero)):.2f} ")
"""

i = 0

while i<10:
    print(i)
    i += 1
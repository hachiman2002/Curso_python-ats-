"""
Hacer un programa para ingresar el radio de un circulo y se
reporte su area y la longitud de la circunferencia
"""

import math

r = float(input("Ingrese el radio:"))

area = math.pi * r**2
long = 2 * math.pi * r

print(f"Area={area:.2f}")
print(f"Longitud={long:.2f}")

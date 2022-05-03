"""
Una tienda ofrece un descuento del 15% sobre el total de la compra y un
cliente desea saber cuanto pagar finalmente por su compra
"""

print("'COMERCIAL GRACIANY'")

total = float(input("Indique el total de su compra: "))
p_final = total-(total*0.15)

print(f"El total con descuento es de {p_final} pesos:.2f")
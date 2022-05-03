#Condicionales combinados

edad = int(input("EDAD="))

if 0<edad<100:
    #edad>0 and edad<100:
    print("edad correcta")
    if edad>=18:
        print("Es mayor de edad")
    else:
        print("es menor de edad")

else:
    print("edad incorrecta")
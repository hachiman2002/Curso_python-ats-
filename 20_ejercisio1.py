#saber si un numero es par o impar o si ambos lo son

n1 = int(input("Digite el numero 1:"))
n2 = int(input("Digite el numero 2:"))

if n1%2==0 and n2%2==0:
    print(f"{n1} y {n2} son par")
elif n1%2==0:
    print(f"{n1} es par")
elif n2%2==0:
    print(f"{n2} es par")
else:
    print("ambos numeros son impares")
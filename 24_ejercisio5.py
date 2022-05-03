"""
EJERCISIO 5:
*Hacer un programa que simule un cajero automatico con un sueldo
inicial de $1000 y tendra el siguiente menu de opciones:

1.Ingresar dinero
2.Retirar dinero
3.Mostrar dinero disponible
4.salir
"""
saldo = 1000
print("\t.:MENU:.")
print("1.Ingresar dinero")
print("2.Retirar dinero")
print("3.Mostrar dinero disponible")
print("4.salir")
opcion = int(input("ELIJA UNA OPCIÓN: "))


if opcion==1:
    ingreso = float(input("Monto a ingresar:"))
    m_final = ingreso + saldo
    print(f"Saldo actual = {m_final}")
elif   opcion==2:
    retiro = float(input("Monto a retirar:"))
    if retiro>saldo:
        print("No tiene esa cantidad de dinero")
    else:
        m_final = saldo - retiro
        print(f"Saldo actual = {m_final}")
elif opcion==3:
    print(f"Saldo actual = {saldo}")

elif opcion==4:
    print("Precione ENTER para salir")

else:
    print("ERROR")
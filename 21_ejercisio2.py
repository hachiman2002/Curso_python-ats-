

n1 = int(input("Digite numero 1:"))
n2 = int(input("Digite numero 2:"))
n3 = int(input("Digite numero 3:"))

if n2<n1>n3:
    if n2>n3:
        print(f"{n1}-{n2},{n3}")
    else:
        print(f"{n1}-{n3}-{n2}")

elif n1<n2>n3:
    if n1>n3:
        print(f"{n2}-{n1}-{n3}")
    else:
        print(f"{n2}-{n3}-{n1}")

elif n1<n3>n2:
    if n3>n1:
        print(f"{n3}-{n1},{n2}")
    else:
        print(f"{n3}-{n2}-{n1}")
else:
    print("'error' reevalue el ejercisio")
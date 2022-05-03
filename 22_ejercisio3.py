"""
hacer un progrma que pida un caracter e indique si es una vocal o no
"""
vocal = str(input("Indique una letra: ").lower())

if vocal=='a' or  vocal=='e' or vocal=='i' or vocal=='o' or vocal=='u':
    print(f"{vocal} es una vocal")
else:
    print("no es una vocal")
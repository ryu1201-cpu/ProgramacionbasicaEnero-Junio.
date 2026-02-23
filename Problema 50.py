#Problema 50

n = int(input("Ingresa el número de productos: "))
nombres = []
claves = []
existencias = []
for i in range(n):
    nombres.append(input(f"Nombre del producto {i+1}: "))
    claves.append(input(f"Clave del producto {i+1}: "))
    existencias.append(int(input(f"Existencia del producto {i+1}: ")))
opcion = input("¿Buscar por índice, nombre o clave? (indice/nombre/clave): ").lower()
if opcion == "indice":
    indice = int(input("Ingresa el índice: "))
    if 0 <= indice < n:
        print(f"Nombre: {nombres[indice]}, Clave: {claves[indice]}, Existencia: {existencias[indice]}")
    else:
        print("Índice inválido")
elif opcion == "nombre":
    nom_buscar = input("Ingresa el nombre a buscar: ")
    if nom_buscar in nombres:
        idx = nombres.index(nom_buscar)
        print(f"Nombre: {nombres[idx]}, Clave: {claves[idx]}, Existencia: {existencias[idx]}")
    else:
        print("Producto no encontrado")
elif opcion == "clave":
    cla_buscar = input("Ingresa la clave a buscar: ")
    if cla_buscar in claves:
        idx = claves.index(cla_buscar)
        print(f"Nombre: {nombres[idx]}, Clave: {claves[idx]}, Existencia: {existencias[idx]}")
    else:
        print("Producto no encontrado")
else:
    print("Opción inválida")

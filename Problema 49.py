#Problema 49

n = int(input("Ingresa el número de productos: "))
nombres = []
claves = []
existencias = []
for i in range(n):
    nombres.append(input(f"Nombre del producto {i+1}: "))
    claves.append(input(f"Clave del producto {i+1}: "))
    existencias.append(int(input(f"Existencia del producto {i+1}: ")))
# Opción 1: Buscar por índice
indice = int(input("Ingresa el índice del producto a buscar (0 a {n-1}): "))
if 0 <= indice < n:
    print(f"Nombre: {nombres[indice]}, Clave: {claves[indice]}, Existencia: {existencias[indice]}")
else:
    print("Índice inválido")
# Opción 2: Mostrar todos en diccionario
productos_dict = {}
for i in range(n):
    productos_dict[claves[i]] = {"nombre": nombres[i], "existencia": existencias[i]}
print("Todos los productos en diccionario:")
for clave, info in productos_dict.items():
    print(f"Clave: {clave}, Nombre: {info['nombre']}, Existencia: {info['existencia']}")

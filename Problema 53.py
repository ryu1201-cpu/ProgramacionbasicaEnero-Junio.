#Problema 53

datos = []
while True:
    dato = input("Ingresa un dato (o escribe 'no' para terminar): ")
    if dato.lower() == "no":
        break
    # Intentar convertir a número si es posible
    try:
        dato = float(dato)
    except ValueError:
        pass
    datos.append(dato)
datos_ordenados = sorted(datos)
print("Lista ordenada:", datos_ordenados)

#Problema 46: Crea un programa que reciba 10 datos y los muestre elevados al cuadrado.

datos = []
for i in range(10):
    num = float(input(f"Ingresa el dato {i+1}: "))
    datos.append(num)
for num in datos:
    print(f"{num} elevado al cuadrado es {num**2}")

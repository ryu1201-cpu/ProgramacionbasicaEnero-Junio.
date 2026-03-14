#Problema 58:  Crear una función para llenar una lista de numeros.

def llenar_lista_numeros():
    lista = []
    n = int(input("¿Cuántos números desea agregar? "))
    for i in range(n):
        while True:
            try:
                num = float(input(f"Ingrese el número {i+1}: "))
                lista.append(num)
                break
            except ValueError:
                print("Error: Ingrese un número válido.")
    return lista

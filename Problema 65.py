#Problema 65:  Escribir un programa que pida números al usuario, mostrar el factorial de cada uno y, al finalizar, la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.

def calcular_factorial(num):
    if num < 0:
        return "No existe factorial de números negativos."
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

# Programa principal
contador = 0
while True:
    entrada = input("Ingrese un número para calcular su factorial (o 'fin' para terminar): ")
    if entrada.lower() == "fin":
        break
    try:
        num = int(entrada)
        print(f"Factorial de {num}: {calcular_factorial(num)}")
        contador += 1
    except ValueError:
        print("Error: Ingrese un número entero válido o 'fin' para terminar.")

print(f"\nCantidad total de números leídos: {contador}")

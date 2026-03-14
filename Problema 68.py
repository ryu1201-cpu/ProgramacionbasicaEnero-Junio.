#Problema 68:  Programa que identifica si un número es primo.

def es_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Ejemplo de uso
num = int(input("Ingrese un número para verificar si es primo: "))
print(f"{num} es primo: {es_primo(num)}")

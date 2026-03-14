#Problema 64:  Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

def EsMultiplo(num1, num2):
    if num2 == 0:
        print("Error: El segundo número no puede ser 0.")
        return False
    return num1 % num2 == 0

#Problema 63:  Escribir una función que reciba una lista y devuelva otra lista con sus cuadrados.

def lista_cuadrados(lista_numeros):
    lista_cuadrados = []
    for num in lista_numeros:
        lista_cuadrados.append(num ** 2)
    return lista_cuadrados

#Problema 60:  Crear la función promedio usando la función sumatoria.

def calcular_promedio(lista_numeros):
    if not lista_numeros:
        return 0
    suma = calcular_suma(lista_numeros)
    return suma / len(lista_numeros)

#Problema 67:  Crear la función ordena creciente una lista que recibe y la regresa Crear la función ordena decreciente una lista que recibe y la regresa Crear la función elimina por índice (pop) que recibe yregresa el valor eliminado Crear la dunción elimina por dato (remove) y regresa la lista Crear la funcion que calcula promedios, max y min y regresa los 3 valores Usar todas esas fuciones para crear un programa que pueda realizar todos esos cálculos.

# Funciones auxiliares
def ordena_creciente(lista):
    return sorted(lista)

def ordena_decreciente(lista):
    return sorted(lista, reverse=True)

def elimina_por_indice(lista, indice):
    if 0 <= indice < len(lista):
        return lista.pop(indice)
    else:
        print("Error: Índice fuera de rango.")
        return None

def elimina_por_dato(lista, dato):
    if dato in lista:
        lista.remove(dato)
    else:
        print("Error: Dato no encontrado en la lista.")
    return lista

def calcula_estadisticas(lista):
    if not lista:
        print("Error: La lista está vacía.")
        return (None, None, None)
    promedio = sum(lista) / len(lista)
    maximo = max(lista)
    minimo = min(lista)
    return (promedio, maximo, minimo)

# Programa principal
lista_datos = [15, 8, 22, 5, 12]
print("Lista original:", lista_datos)

print("Lista ordenada creciente:", ordena_creciente(lista_datos.copy()))
print("Lista ordenada decreciente:", ordena_decreciente(lista_datos.copy()))

print("Valor eliminado del índice 2:", elimina_por_indice(lista_datos, 2))
print("Lista después de eliminar por dato 8:", elimina_por_dato(lista_datos, 8))

prom, max_val, min_val = calcula_estadisticas(lista_datos)
print(f"Estadísticas - Promedio: {prom:.2f}, Máximo: {max_val}, Mínimo: {min_val}")

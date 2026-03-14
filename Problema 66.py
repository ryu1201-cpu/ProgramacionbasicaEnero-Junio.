#Problema 66:  De una lista de nombres y calificaciones separar los que tengan calificación reprobatoria y guardar los nombres en una nueva lista. La fucnión devuelve la lista de nombres reprobados.

def obtener_reprobados(lista_nombres, lista_calificaciones):
    if len(lista_nombres) != len(lista_calificaciones):
        print("Error: Las listas deben tener la misma longitud.")
        return []
    reprobados = []
    for nombre, calif in zip(lista_nombres, lista_calificaciones):
        if calif < 6:  # Calificación mínima aprobatoria = 6
            reprobados.append(nombre)
    return reprobados

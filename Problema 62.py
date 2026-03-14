#Problema 62:  Definir una función parametrizada que reciba las 3 calificaciones del semestre y devuelve la calificación final. La función regresa el promedio. Si es reprobatoria indica "te vas a extra".

def calcular_calificacion_final(calif1, calif2, calif3):
    promedio = (calif1 + calif2 + calif3) / 3
    if promedio < 6:  # Asumiendo que 6 es la calificación mínima aprobatoria
        return f"Promedio: {promedio:.2f} - te vas a extra"
    else:
        return f"Promedio final: {promedio:.2f}"

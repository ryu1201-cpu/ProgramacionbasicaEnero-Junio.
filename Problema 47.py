#Problema 47

n = int(input("Ingresa el número de materias: "))
for i in range(n):
    nombre = input(f"Ingresa el nombre de la materia {i+1}: ")
    m = int(input(f"Ingresa el número de calificaciones para {nombre}: "))
    suma = 0
    for j in range(m):
        cal = float(input(f"Ingresa la calificación {j+1}: "))
        suma += cal
    promedio = suma / m
    print(f"Materia: {nombre} | Promedio: {promedio:.2f}")

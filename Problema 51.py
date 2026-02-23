#Problema 51

n = int(input("Ingresa el número de trabajadores: "))
nombres = []
asistencias = []
for i in range(n):
    nombres.append(input(f"Nombre del trabajador {i+1}: "))
    asist = int(input(f"¿Asistió {nombres[-1]}? (0=no, 1=si): "))
    asistencias.append(asist)
for nom, asist in zip(nombres, asistencias):
    estado = "asistió" if asist == 1 else "no asistió"
    print(f"{nom} {estado} a trabajar")

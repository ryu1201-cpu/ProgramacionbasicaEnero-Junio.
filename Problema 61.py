#Problema 61:  Crear una función que recibe base y altura de rectángulo para calular perímetro y devolver su valor.

def calcular_perimetro_rectangulo(base, altura):
    if base <= 0 or altura <= 0:
        print("Error: Base y altura deben ser mayores a 0.")
        return None
    perimetro = 2 * (base + altura)
    return perimetro

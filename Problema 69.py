#Problema 69:  Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo.Una dirección se considerará válida si contiene el símbolo "@".

def validar_email(email):
    return "@" in email

# Programa principal
email_usuario = input("Ingrese su dirección de email: ")
if validar_email(email_usuario):
    print("La dirección de email es válida.")
else:
    print("La dirección de email no es válida (debe contener '@').")
